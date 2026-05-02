import rdflib
import os
import glob

# Initialize the Liaison's local reasoning capacity
liaison_graph = rdflib.Graph()

def check_authority(asset_label):
    """
    The Liaison Agent requests a settlement check from the Bureau Court.
    This ensures the 'Agent-to-User' (A2UI) interface remains deterministic.
    """
    print(f"\n[ LIAISON AGENT ]: Requesting verification for '{asset_label}'...")
    
    # Load all bureau evidence into the Liaison's temporary graph
    data_dir = "../data/"
    jsonld_files = glob.glob(os.path.join(data_dir, "*.jsonld"))
    
    for file in jsonld_files:
        try:
            liaison_graph.parse(file, format="json-ld")
        except Exception as e:
            pass # Silent failure for malformed files during liaison phase

    # SPARQL Interrogation: Querying gitandu.com/padi/ namespace
    query = f"""
    SELECT ?source
    WHERE {{
        ?s <https://gitandu.com/padi/label> "{asset_label}" .
        ?s <https://gitandu.com/padi/source> ?source .
    }}
    """
    
    results = liaison_graph.query(query)
    
    if len(results) > 0:
        for row in results:
            print(f"--- [ VERIFIED ]: Asset anchored to source: {row.source}")
            return True
    else:
        print(f"--- [ REJECTED ]: Asset '{asset_label}' lacks a verified Provenance-Lock.")
        return False

# --- Execution for McKinsey Forward Milestone ---
if __name__ == "__main__":
    print("--- [ BUREAU AGENT ORCHESTRATION START ] ---")
    
    # Target: The recently settled McKinsey record
    target = "McKinsey Forward Program (Core Skills Level) - 2026 Cohort"
    
    if check_authority(target):
        print("Liaison Agent Status: Authorized to proceed with McKinsey Milestone Tracking.")
    else:
        print("Liaison Agent Status: Halted. Insufficient Authority.")
        
    print("\n--- [ ORCHESTRATION COMPLETE ] ---")
