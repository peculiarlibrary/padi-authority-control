import rdflib
import os
import glob

def generate_integrity_report(target_nodes=31):
    g = rdflib.Graph()
    # Explicitly look in the 'data' folder of the current repository root
    data_dir = "data"
    
    if not os.path.exists(data_dir):
        print(f"[ ERROR ]: Data directory not found at {os.path.abspath(data_dir)}")
        return

    jsonld_files = glob.glob(os.path.join(data_dir, "*.jsonld"))
    if not jsonld_files:
        print(f"[ WARNING ]: No .jsonld files found in {data_dir}")

    for file in jsonld_files:
        try:
            g.parse(file, format="json-ld")
        except Exception as e:
            print(f"[ ERROR ]: Failed to parse {file}: {e}")

    # Calculate unique node count (Subjects + Objects)
    nodes = set(g.subjects()) | set(g.objects())
    node_count = len(nodes)
    
    report_path = "docs/graph_integrity_report_2026-05-02.md"
    os.makedirs("docs", exist_ok=True)
    
    with open(report_path, "w") as f:
        f.write(f"# PADI Graph Integrity Report\n\n")
        f.write(f"- **Lead Architect**: Samuel Muriithi Gitandu\n")
        f.write(f"- **Actual Nodes**: {node_count}\n")
        f.write(f"- **Status**: {'VERIFIED' if node_count >= target_nodes else 'INCOMPLETE'}\n")
    
    print(f"\n[ LIAISON AGENT ]: Report generated with {node_count} nodes.")

if __name__ == "__main__":
    generate_integrity_report(31)
