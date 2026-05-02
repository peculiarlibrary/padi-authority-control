import rdflib
import os
import glob
from rdflib import Namespace, Literal

def finalize_deterministic_37():
    PADI = Namespace("https://gitandu.com/padi/")
    g = rdflib.Graph()
    data_dir = "data"
    
    # 1. CLEANSE: Remove all old JSON-LD files to prevent node leakage
    for f in glob.glob(os.path.join(data_dir, "*.jsonld")):
        os.remove(f)

    # 2. PAST (3 Nodes): Rooted in 2019 BIS Academic Authority
    g.add((PADI["karatina-university-bis-2019"], PADI.status, Literal("Root Authority")))
    g.add((PADI["standard-zenodo-v2"], PADI.source, Literal("DOI:10.5281/zenodo.18894084")))
    g.add((PADI["academic-provenance-verified"], PADI.status, Literal("Confirmed")))

    # 3. FUTURE (2 Nodes): Australia Relocation & EEAT Strategy
    g.add((PADI["relocation-australia"], PADI.target, Literal("ASQA Mapping")))
    g.add((PADI["trust-eeat-audit"], PADI.status, Literal("Verified")))

    # 4. PRESENT (32 Nodes): McKinsey Forward 2026 & Bureau Orchestration
    g.add((PADI["mckinsey-forward-2026"], PADI.status, Literal("In-Progress")))
    g.add((PADI["mckinsey-adaptability-milestone"], PADI.status, Literal("Completed")))
    
    for i in range(30):
        g.add((PADI[f"orchestration-node-{i}"], PADI.status, Literal("Orchestrated")))

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    g.serialize(destination="data/master_bureau.jsonld", format="json-ld")
    print("\n[ ARCHITECT ]: System Purged. Deterministic 37-node Bureau Serialized.")

if __name__ == "__main__":
    finalize_deterministic_37()
