#!/usr/bin/env python3
# Created by AI Assistant on 2026-01-27

"""
Fetch notice details from Chinese government standards website.
This script reads notice IDs from notices.json and fetches detailed information
from the detail page for each notice, saving the results to individual files.
"""

import json
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from typing import List, Dict, Any


class NoticeDetailFetcher:
    """Fetches and parses notice details based on schema configuration."""
    
    def __init__(self, schema_path: str, notices_path: str, meta_path: str, output_dir: str = "."):
        """
        Initialize the fetcher.
        
        Args:
            schema_path: Path to cn-gov-std-notice-schema.json
            notices_path: Path to notices.json
            meta_path: Path to std-meta-info.json
            output_dir: Directory to save output files
        """
        self.schema_path = Path(schema_path)
        self.notices_path = Path(notices_path)
        self.meta_path = Path(meta_path)
        self.output_dir = Path(output_dir)
        
        # Load configuration
        self.schema = self._load_json(self.schema_path)
        self.notices = self._load_json(self.notices_path)
        self.meta_info = self._load_json(self.meta_path)
        
        # Extract configuration
        self.notice_detail_source_url = self.schema.get("noticeDetailSourceUrl", "")
        self.notice_detail_item_schema = self.schema.get("noticeDetailItem", {})
        
    def _load_json(self, path: Path) -> Dict[str, Any]:
        """Load JSON file."""
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _save_json(self, path: Path, data: Dict[str, Any]):
        """Save JSON file."""
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def _get_notice_id_list(self) -> List[str]:
        """
        Get sorted notice ID list from notices.json.
        
        Returns:
            List of notice IDs sorted as numbers from small to big.
        """
        # Extract all IDs
        ids = [notice.get("id", "") for notice in self.notices]
        
        # Filter out empty strings and convert to integers for sorting
        valid_ids = []
        for notice_id in ids:
            if notice_id and notice_id.strip():
                try:
                    valid_ids.append((int(notice_id), notice_id))
                except ValueError:
                    print(f"Warning: Invalid ID '{notice_id}' - skipping")
        
        # Sort by integer value
        valid_ids.sort(key=lambda x: x[0])
        
        # Return only the string IDs in sorted order
        return [item[1] for item in valid_ids]
    
    def _get_notice_no_cursor(self) -> str:
        """
        Get current noticeNoCursor from meta info.

        Returns:
            Current noticeNoCursor value (empty string if not set)
        """
        return self.meta_info.get("noticeNoCursor", "")

    def _update_notice_no_cursor(self, notice_no: str):
        """
        Update noticeNoCursor in meta info and save to file.

        Args:
            notice_no: New notice number to set as cursor
        """
        self.meta_info["noticeNoCursor"] = notice_no
        self._save_json(self.meta_path, self.meta_info)

    def _get_already_fetched_list(self) -> set:
        """
        Get the list of already fetched notice numbers.

        Returns:
            Set of notice numbers that have been fetched
        """
        fetched_list_str = self.meta_info.get("noticeNoAlreadyFetchedList", "")
        if not fetched_list_str:
            return set()
        # Parse comma-separated list
        return set(item.strip() for item in fetched_list_str.split(',') if item.strip())

    def _get_ignore_list(self) -> set:
        """
        Get the list of notice numbers to ignore.

        Returns:
            Set of notice numbers to ignore
        """
        ignore_list_str = self.meta_info.get("noticeNoIgnoreList", "")
        if not ignore_list_str:
            return set()
        # Parse comma-separated list
        return set(item.strip() for item in ignore_list_str.split(',') if item.strip())

    def _append_to_fetched_list(self, notice_no: str):
        """
        Append a notice number to the already fetched list.

        Args:
            notice_no: Notice number to add to the list
        """
        current_list = self.meta_info.get("noticeNoAlreadyFetchedList", "")
        if current_list and not current_list.endswith(','):
            current_list += ','
        current_list += f"{notice_no},"
        self.meta_info["noticeNoAlreadyFetchedList"] = current_list
        self._save_json(self.meta_path, self.meta_info)
    
    def _fetch_content(self, url: str) -> str:
        """
        Fetch content from URL with retry logic.

        Args:
            url: URL to fetch

        Returns:
            HTML content as string
        """
        import time

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        max_retries = 3
        retry_delay = 10

        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=headers, timeout=30)
                response.raise_for_status()
                response.encoding = 'utf-8'
                return response.text
            except requests.RequestException as e:
                if attempt < max_retries - 1:
                    print(f"Error fetching {url}: {e}. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                else:
                    print(f"Error fetching {url}: {e}. Max retries ({max_retries}) exceeded.")
                    return ""
        return ""
    
    def _extract_field_value(self, element, field_schema: Dict[str, Any]) -> Any:
        """
        Extract field value from HTML element based on schema.
        
        Args:
            element: BeautifulSoup element
            field_schema: Field configuration from schema
            
        Returns:
            Extracted value
        """
        extract_from = field_schema.get("extractFrom", "")
        pattern = field_schema.get("pattern", "")
        field_type = field_schema.get("type", "string")
        date_format = field_schema.get("format", "YYYY-MM-DD")
        
        try:
            if extract_from == "text":
                text = element.get_text(strip=True)
                if pattern:
                    match = re.search(pattern, text)
                    if match:
                        value = match.group(1) if match.lastindex else match.group(0)
                    else:
                        value = None
                else:
                    value = text
                    
            elif extract_from == "href":
                href = element.get("href", "")
                if pattern:
                    match = re.search(pattern, href)
                    if match:
                        value = match.group(1) if match.lastindex else match.group(0)
                    else:
                        value = None
                else:
                    value = href
                    
            elif extract_from == "span":
                # Handle special case with style attribute
                attribute = field_schema.get("attribute", "")
                text_pattern = field_schema.get("textPattern", "")
                
                if attribute:
                    attr_value = element.get(attribute, "")
                    if text_pattern:
                        match = re.search(text_pattern, attr_value)
                        if match:
                            value = match.group(1) if match.lastindex else match.group(0)
                        else:
                            value = None
                    else:
                        value = attr_value
                else:
                    value = None
                    
            else:
                value = None
            
            # Convert to specified type
            if value and field_type == "date":
                # Date format conversion if needed
                if date_format == "YYYY-MM-DD":
                    # Assume date is already in correct format or close to it
                    value = value.split()[0] if value else ""
                    
            return value
            
        except Exception as e:
            print(f"Error extracting field: {e}")
            return None
    
    def _parse_notice_detail(self, html_content: str, notice_no: str) -> List[Dict[str, Any]]:
        """
        Parse notice detail HTML content based on schema.

        Args:
            html_content: HTML content string

        Returns:
            List of notice detail items
        """
        soup = BeautifulSoup(html_content, 'html.parser')

        selector = self.notice_detail_item_schema.get("selector", "")
        fields = self.notice_detail_item_schema.get("fields", {})

        items = []

        # Find the content div and get the table
        content_div = soup.find('div', class_='content')
        if not content_div:
            print("Warning: No content div found")
            return items

        table = content_div.find('table')
        if not table:
            print("Warning: No table found in content div")
            return items

        # Find all table rows
        rows = table.find_all('tr')

        # Skip header row (first row) and process data rows
        for row in rows[1:]:
            cells = row.find_all('td')

            # Skip if not enough cells (malformed row)
            if len(cells) < 3:
                continue

            item = {}

            item["noticeNo"] = notice_no
            # Cell 0: noticeNo (序号)
            item["id"] = cells[0].get_text(strip=True)

            # Determine row type based on cell count and content
            if len(cells) == 3:
                # Type 2: 3 cells - simple format (id, stdCode with link, stdNameCn)
                # Cell 1: stdCode and stdHeaderUrl
                link = cells[1].find('a')
                if link:
                    item["stdHeaderUrl"] = link.get('href', '')
                    item["stdCode"] = link.get_text(strip=True)
                else:
                    item["stdCode"] = cells[1].get_text(strip=True)

                # Cell 2: stdNameCn
                item["stdNameCn"] = cells[2].get_text(strip=True)

            elif len(cells) == 4:
                # Type 3: 4 cells - previous standard code format
                # Cell 1: stdCode (text only, no link)
                item["previousStdCode"] = cells[1].get_text(strip=True)

                # Cell 2: stdNameCn
                item["stdNameCn"] = cells[2].get_text(strip=True)

                # Cell 3: previousStdCode (with link)
                link = cells[3].find('a')
                if link:
                    item["stdCode"] = link.get_text(strip=True)

            elif len(cells) >= 5:
                # Type 1: 5+ cells - full format with dates
                # Cell 1: stdCode and stdHeaderUrl
                link = cells[1].find('a')
                if link:
                    item["stdHeaderUrl"] = link.get('href', '')
                    item["stdCode"] = link.get_text(strip=True)
                else:
                    item["stdCode"] = cells[1].get_text(strip=True)

                # Cell 2: stdNameCn
                item["stdNameCn"] = cells[2].get_text(strip=True)

                # Cell 3: stdReleaseDate (optional)
                cell3_text = cells[3].get_text(strip=True)
                if cell3_text:
                    item["stdReleaseDate"] = cell3_text

                # Cell 4: stdActivatedDate (optional)
                cell4_text = cells[4].get_text(strip=True)
                if cell4_text:
                    item["stdActivatedDate"] = cell4_text

            # Only add non-empty items
            if item:
                items.append(item)

        return items
    
    def process_notices(self, max_per_run: int = 50):
        """
        Main processing loop:
        1. Get notice ID list sorted by number
        2. Get current cursor from meta info
        3. Process each notice starting from cursor (up to max_per_run)
        4. Save details to individual files

        Args:
            max_per_run: Maximum number of notices to process per run
        """
        # Step 1: Get sorted notice ID list
        notice_no_list = self._get_notice_id_list()
        print(f"Found {len(notice_no_list)} notices to process")

        # Get current cursor
        notice_no_cursor = self._get_notice_no_cursor()
        print(f"Current cursor: {notice_no_cursor if notice_no_cursor else '(none)'}")

        # Get already fetched list
        already_fetched = self._get_already_fetched_list()
        print(f"Already fetched {len(already_fetched)} notices")

        # Get ignore list
        ignore_list = self._get_ignore_list()
        print(f"Ignore list contains {len(ignore_list)} notices")

        # Find starting point
        start_processing = not notice_no_cursor  # Start from beginning if no cursor

        processed_count = 0

        for notice_no in notice_no_list:
            # Check if we've processed enough notices for this run
            if processed_count >= max_per_run:
                print(f"\nProcessed {processed_count} notices (limit: {max_per_run})")
                print("Next run will continue from cursor")
                break

            # Check if already fetched
            if notice_no in already_fetched:
                print(f"\nSkipping notice {notice_no} (already fetched)")
                continue

            # Check if in ignore list
            if notice_no in ignore_list:
                print(f"\nSkipping notice {notice_no} (in ignore list)")
                continue

            # Step 1: Skip until we find notice greater than cursor
            # if not start_processing:
            #     if notice_no >= notice_no_cursor:
            #         start_processing = True
            #     else:
            #         continue

            print(f"\nProcessing notice: {notice_no}")

            # Step 2: Update cursor
            self._update_notice_no_cursor(notice_no)

            # Step 3: Fetch content
            url = self.notice_detail_source_url + notice_no
            print(f"Fetching: {url}")
            html_content = self._fetch_content(url)

            if not html_content:
                print(f"Failed to fetch content for notice {notice_no}")
                continue

            # Parse notice detail
            notice_details = self._parse_notice_detail(html_content,notice_no)

            if not notice_details:
                print(f"No details found for notice {notice_no}")
                continue

            # If less than 5 items, add URL to tocheck.txt
            if len(notice_details) < 5:
                print(f"Warning: Only {len(notice_details)} items found (< 5), adding to tocheck.txt")
                tocheck_file = self.output_dir / "tocheck.txt"
                with open(tocheck_file, 'a', encoding='utf-8') as f:
                    f.write(f"{url}\n")

            print(f"Found {len(notice_details)} detail items")

            # Step 4: Save to notice-details.json (prepend new content)
            output_file = self.output_dir / "notice-details.json"

            # Load existing content if file exists
            existing_details = []
            if output_file.exists():
                try:
                    existing_details = self._load_json(output_file)
                    if not isinstance(existing_details, list):
                        existing_details = []
                except Exception as e:
                    print(f"Warning: Could not load existing details: {e}")
                    existing_details = []

            # Prepend new details to existing ones
            all_details = notice_details + existing_details

            # Save all details
            self._save_json(output_file, all_details)
            print(f"Saved to: {output_file} ({len(notice_details)} new items, {len(all_details)} total)")

            # Append to already fetched list
            self._append_to_fetched_list(notice_no)

            processed_count += 1

            # Wait 10 seconds before processing next notice
            import time
            time.sleep(10)

        print(f"\nRun complete. Processed {processed_count} notices.")


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    
    fetcher = NoticeDetailFetcher(
        schema_path=script_dir / "cn-gov-std-notice-schema.json",
        notices_path=script_dir / "notices.json",
        meta_path=script_dir / "std-meta-info.json",
        output_dir=script_dir
    )
    
    fetcher.process_notices()
    print("\nProcessing complete!")


if __name__ == "__main__":
    main()
