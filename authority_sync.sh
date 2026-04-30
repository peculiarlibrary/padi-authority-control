#!/bin/bash
SCHEMA="src/padi_schema.yaml"

echo "------------------------------------------------"
echo "PADI AUTHORITY CONTROL: SYNCHRONIZING ARTIFACTS"
echo "------------------------------------------------"

# 1. Logic Check (Schema verification)
if [ ! -f "$SCHEMA" ]; then
    echo "ERROR: Sovereign Schema not found at $SCHEMA"
    exit 1
fi

# 2. Enforce Truth (SHACL Generation)
python -m linkml.generators.shaclgen $SCHEMA > project/authority_shapes.ttl

# 3. Enable Interoperability (JSON-LD Context)
python -m linkml.generators.jsonldcontextgen $SCHEMA > project/authority_context.jsonld

# 4. Generate Registry Documentation
python -m linkml.generators.docgen $SCHEMA -d docs/

echo "STATUS: Authority Control Active. Repository is Deterministic."
