Here's how to set up a cronjob to run the script every 30 minutes:

## Step 1: Make the script executable
```bash
chmod +x /workspace/update_dlake.sh
```

## Step 2: Edit the crontab
```bash
crontab -e
```

## Step 3: Add this line
```cron
*/30 * * * * /workspace/update_dlake.sh
```

## Step 4: Save and exit (depends on editor)
- For nano: `Ctrl+O`, `Enter`, then `Ctrl+X`
- For vi/vim: `:wq`

---

## Verification

Check if the cronjob was added:
```bash
crontab -l
```

---

## Optional: Add logging to troubleshoot

If you want to log output, create a logging wrapper:
I've created a logging wrapper at `/workspace/dlake_cron_with_log.sh`. 

If you want to use logging instead, add this to your crontab:
```cron
*/30 * * * * /workspace/dlake_cron_with_log.sh
```

Then make it executable:
```bash
chmod +x /workspace/dlake_cron_with_log.sh
```

You can check the logs at `/workspace/dlake_cron.log` to see if the script ran successfully.



---
---

**check status**

```
systemctl status cron 2>/dev/null || service cron status 2>/dev/null || echo "Cron service status check failed"
```
