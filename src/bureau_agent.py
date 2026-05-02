import rdflib
import os
import glob
from rdflib import URIRef, Literal, Namespace

def generate_integrity_report(target_nodes=31):
    g = rdflib.Graph()
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)

    jsonld_files = glob.glob(os.path.join(data_dir, "*.jsonld"))
    for file in jsonld_files:
        try:
            g.parse(file, format="json-ld")
        except Exception as e:
            print(f"[ ERROR ]: Failed to parse {file}: {e}")

    nodes = set(g.subjects()) | set(g.objects())
    node_count = len(nodes)
    report_path = "docs/graph_integrity_report_2026-05-02.md"
    os.makedirs("docs", exist_ok=True)
    
    with open(report_path, "w") as f:
        f.write(f"# PADI Graph Integrity Report\n\n")
        f.write(f"- **Lead Architect**: Samuel Muriithi Gitandu\n")
        f.write(f"- **Actual Nodes**: {node_count}\n")
        f.write(f"- **Status**: {'VERIFIED' if node_count >= target_nodes else 'INCOMPLETE'}\n")
    
    print(f"\n[ LIAISON AGENT ]: Report updated with {node_count} nodes.")

def register_milestone(module_name, status="Completed"):
    PADI = Namespace("https://gitandu.com/padi/")
    g = rdflib.Graph()
    data_file = "data/mckinsey_milestones.jsonld"
    
    if os.path.exists(data_file):
        g.parse(data_file, format="json-ld")

    milestone_uri = URIRef(f"https://gitandu.com/padi/milestone/{module_name.replace(' ', '_')}")
    g.add((milestone_uri, PADI.label, Literal(module_name)))
    g.add((milestone_uri, PADI.status, Literal(status)))
    g.add((milestone_uri, PADI.source, URIRef("https://www.mckinsey.com/forward")))
    
    g.serialize(destination=data_file, format="json-ld")
    print(f"[ LIAISON AGENT ]: Milestone '{module_name}' registered.")
    generate_integrity_report()

if __name__ == "__main__":
    generate_integrity_report(31)
