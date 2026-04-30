#!/bin/bash
# PADI Sovereign Bureau - Bulk Validation Script
echo "Starting Sovereign Audit of Bureau Records..."
echo "------------------------------------------"

count=0
errors=0

for file in data/*.yaml; do
    echo -n "Checking $file... "
    # Determine target class based on filename or content
    if [[ $file == *"agent"* ]]; then CLASS="BureauAgent"; elif [[ $file == *"log"* ]]; then CLASS="OutreachLog";
        CLASS="BureauAgent"
    else
        CLASS="AuthorityRecord"
    fi

    if linkml-validate --target-class $CLASS --schema src/padi_schema.yaml "$file" > /dev/null 2>&1; then
        echo "VALID"
    else
        echo "INVALID"
        ((errors++))
    fi
    ((count++))
done

echo "------------------------------------------"
echo "Audit Complete: $count files checked, $errors errors found."

if [ $errors -gt 0 ]; then
    exit 1
fi
