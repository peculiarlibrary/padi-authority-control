import rdflib
import os
import glob

# Initialize the Graph
g = rdflib.Graph()

# Define the data directory path
data_dir = "../data/"
jsonld_files = glob.glob(os.path.join(data_dir, "*.jsonld"))

if not jsonld_files:
    print(f"Error: No .jsonld files found in {data_dir}.")
    exit(1)

print(f"--- [ BUREAU COURT: MASS AUDIT OPEN ({len(jsonld_files)} Assets) ] ---")

# Load all assets into the collective reasoning graph
for file in jsonld_files:
    try:
        g.parse(file, format="json-ld")
        print(f"Evidence Loaded: {os.path.basename(file)}")
    except Exception as e:
        print(f"ERROR: Could not parse {file} - {e}")

# 1. Global Provenance Interrogation (RULE-002)
print("\n[ JUDICIAL REVIEW: Global Provenance Check ]")
provenance_query = """
PREFIX padi: <https://peculiarlibrarian.github.io/padi-authority-control/>
SELECT ?label ?source
WHERE {
    ?subject a padi:AuthorityRecord .
    ?subject padi:label ?label .
    OPTIONAL { ?subject padi:source ?source }
}
"""

results = g.query(provenance_query)
compliance_count = 0
violations = []

for row in results:
    if row.source:
        compliance_count += 1
    else:
        violations.append(row.label)

print(f"Verdict: {compliance_count} records SETTLED. {len(violations)} violations found.")
if violations:
    for v in violations:
        print(f"  - VIOLATION: '{v}' lacks a Provenance-Lock.")

# 2. Global Dependency Mapping (Structural Integrity)
print("\n[ JUDICIAL REVIEW: Multi-Node Dependencies ]")
dep_query = """
PREFIX padi: <https://peculiarlibrarian.github.io/padi-authority-control/>
SELECT ?child_label ?parent_label
WHERE {
    ?child padi:label ?child_label .
    ?child padi:derived_from ?parent .
    ?parent padi:label ?parent_label .
}
"""

dep_results = g.query(dep_query)
if len(dep_results) == 0:
    print("Status: No inter-node dependencies detected across the Bureau.")
else:
    for row in dep_results:
        print(f"Relationship: {row.child_label} -> Anchored to -> {row.parent_label}")

print("\n--- [ FULL BUREAU AUDIT CLOSED ] ---")
