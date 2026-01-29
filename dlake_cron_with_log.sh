#!/bin/bash

# Created by AI Assistant on 2026-01-29
# Wrapper script with logging for cron execution

LOG_FILE="/workspace/dlake_cron.log"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting dlake update..." >> "$LOG_FILE"

/workspace/update_dlake.sh >> "$LOG_FILE" 2>&1

if [ $? -eq 0 ]; then
    echo "[$DATE] dlake update completed successfully." >> "$LOG_FILE"
else
    echo "[$DATE] dlake update failed with exit code $?" >> "$LOG_FILE"
fi

echo "----------------------------------------" >> "$LOG_FILE"
