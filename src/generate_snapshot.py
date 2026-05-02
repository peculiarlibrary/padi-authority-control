import rdflib
import networkx as nx
import matplotlib.pyplot as plt
import os

def update_graph_snapshot():
    # Load the graph
    g = rdflib.Graph()
    g.parse("data/master_bureau.jsonld", format="json-ld")
    
    # Convert RDFLib graph to NetworkX for visualization
    nx_graph = nx.DiGraph()
    for s, p, o in g:
        # Use only the local name for clarity in the image
        s_label = str(s).split('/')[-1]
        o_label = str(o).split('/')[-1]
        nx_graph.add_edge(s_label, o_label, label=str(p).split('/')[-1])

    # Visualization Setup
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(nx_graph, seed=42)
    
    # Draw nodes and edges
    nx.draw(nx_graph, pos, with_labels=True, node_color='skyblue', 
            node_size=2000, font_size=8, font_weight='bold', 
            arrows=True, edge_color='gray')
            
    plt.title("Sovereign Bureau: 37-Node Baseline Snapshot (2026-05-02)")
    
    # Ensure docs directory exists
    if not os.path.exists('docs'):
        os.makedirs('docs')
        
    plt.savefig("docs/graph_snapshot.png", format="PNG", dpi=300)
    print("\n[ ARCHITECT ]: Snapshot updated at docs/graph_snapshot.png")

if __name__ == "__main__":
    update_graph_snapshot()
