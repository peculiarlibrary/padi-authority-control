#!/bin/bash
echo "--- Specific Isolation Test: Ontology Record ---"
FILE="data/ontology_engineering_padi.yaml"
CLASS="AuthorityRecord"
SCHEMA="src/padi_schema.yaml"

# Run validation with visible output
linkml-validate --schema $SCHEMA --target-class $CLASS "$FILE"

if [ $? -eq 0 ]; then
    echo "RESULT: $FILE is technically VALID."
    echo "ACTION: The error is in the sovereign_audit.sh loop logic."
else
    echo "RESULT: $FILE is technically INVALID."
    echo "ACTION: The error is in the YAML structure."
fi
