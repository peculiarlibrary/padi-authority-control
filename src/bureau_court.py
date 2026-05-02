import rdflib
import os
import glob

g = rdflib.Graph()
data_dir = "../data/"
jsonld_files = glob.glob(os.path.join(data_dir, "*.jsonld"))

print(f"--- [ BUREAU COURT: MASS AUDIT OPEN ] ---")

for file in jsonld_files:
    try:
        g.parse(file, format="json-ld")
        print(f"Evidence Loaded: {os.path.basename(file)}")
    except Exception as e:
        print(f"Failed to load {file}: {e}")

# The Law: Updated to match your @vocab: https://gitandu.com/padi/
audit_query = """
SELECT ?label ?source
WHERE {
    ?s <https://gitandu.com/padi/label> ?label .
    OPTIONAL { ?s <https://gitandu.com/padi/source> ?source }
}
"""

results = g.query(audit_query)
records = list(results)

print(f"\n[ JUDICIAL REVIEW: {len(records)} Assets Identified ]")

violations = 0
for row in records:
    # RULE-002: Provenance-Lock Enforcement
    status = "SETTLED" if row.source else "VIOLATION (No Source)"
    if not row.source: violations += 1
    print(f"Asset: {row.label} | Status: {status}")

print(f"\nVerdict: {len(records) - violations} Passed, {violations} Failed.")
print("--- [ FULL BUREAU AUDIT CLOSED ] ---")
