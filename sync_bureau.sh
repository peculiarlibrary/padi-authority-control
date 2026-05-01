#!/bin/bash
echo "--- Initiating Sovereign Sync ---"
./sovereign_audit.sh
if [ $? -ne 0 ]; then
    echo "CRITICAL FAILURE: Audit failed. Sync aborted."
    exit 1
fi
echo "Audit PASSED. Synchronizing..."
git add .
git commit -m "chore: Bureau synchronization and automated ledger update"
git push
echo "--- Sync Complete ---"
