#!/bin/bash
echo "Starting Sovereign Audit of Bureau Records..."
echo "------------------------------------------"
FILES_CHECKED=0
ERRORS=0

for file in data/*.yaml; do
    FILES_CHECKED=$((FILES_CHECKED + 1))
    
    if [[ $file == *"data/log_"* ]]; then
        CLASS="OutreachLog"
    elif [[ $file == *"agent"* ]]; then
        CLASS="BureauAgent"
    else
        CLASS="AuthorityRecord"
    fi

    linkml-validate --schema src/padi_schema.yaml --target-class $CLASS "$file"
    
    if [ $? -eq 0 ]; then
        echo "Checking $file... VALID"
    else
        echo "Checking $file... INVALID"
        ERRORS=$((ERRORS + 1))
    fi
done

echo "------------------------------------------"
echo "Audit Complete: $FILES_CHECKED files checked, $ERRORS errors found."
[ $ERRORS -eq 0 ] || exit 1
