#!/bin/bash
# PADI Bureau Synchronization Engine

echo "Starting Local Build for PADI Authority Control..."

# 1. Generate SHACL (The Validation Firewall)
python -m linkml.generators.shaclgen src/padi_schema.yaml > project/padi_constraints.ttl

# 2. Generate JSON-LD (The Interoperability Bridge)
python -m linkml.generators.jsonldcontextgen src/padi_schema.yaml > project/padi_context.jsonld

# 3. Generate Documentation (The Librarian's Audit)
python -m linkml.generators.docgen src/padi_schema.yaml -d docs/

echo "------------------------------------------------"
echo "LOCAL ARTIFACTS GENERATED SUCCESSFULLY."
echo "Check /project for the SHACL shapes."
echo "------------------------------------------------"
