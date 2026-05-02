import rdflib
import os

# Initialize the Graph
g = rdflib.Graph()

# Path to your settled JSON-LD
data_path = "../data/librarian_tech.jsonld"

if not os.path.exists(data_path):
    print(f"Error: {data_path} not found. Ensure you have run your serialization script.")
    exit(1)

# Load the data
g.parse(data_path, format="json-ld")

print("--- [ BUREAU COURT: SESSION OPEN ] ---")

# 1. Query for Provenance Violations (The Integrity Check)
print("\n[ JUDICIAL REVIEW: Provenance Check ]")
provenance_query = """
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX padi: <https://peculiarlibrarian.github.io/padi-authority-control/>

SELECT ?subject ?label
WHERE {
    ?subject a <https://peculiarlibrarian.github.io/padi-authority-control/AuthorityRecord> .
    ?subject <https://peculiarlibrarian.github.io/padi-authority-control/label> ?label .
    FILTER NOT EXISTS { ?subject <https://peculiarlibrarian.github.io/padi-authority-control/source> ?source }
}
"""

results = g.query(provenance_query)
if len(results) == 0:
    print("Verdict: All records comply with Provenance-Lock (RULE-002).")
else:
    for row in results:
        print(f"VIOLATION: Record '{row.label}' lacks a documented source.")

# 2. Query for Dependency Chains (The Reasoning Check)
print("\n[ JUDICIAL REVIEW: Dependency Chains ]")
# Note: This assumes 'derived_from' or similar linkage exists in your PADI model
dep_query = """
PREFIX padi: <https://peculiarlibrarian.github.io/padi-authority-control/>
SELECT ?child_label ?parent_label
WHERE {
    ?child <https://peculiarlibrarian.github.io/padi-authority-control/label> ?child_label .
    ?child <https://peculiarlibrarian.github.io/padi-authority-control/derived_from> ?parent .
    ?parent <https://peculiarlibrarian.github.io/padi-authority-control/label> ?parent_label .
}
"""

dep_results = g.query(dep_query)
if len(dep_results) == 0:
    print("Status: No inter-node dependencies currently mapped.")
else:
    for row in dep_results:
        print(f"Relationship: {row.child_label} -> Depends on -> {row.parent_label}")

print("\n--- [ SESSION CLOSED ] ---")
