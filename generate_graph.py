import os
import yaml
import networkx as nx
import matplotlib.pyplot as plt

def generate_padi_graph():
    G = nx.DiGraph()
    data_dir = 'data/'
    
    color_map = {
        'skill_': '#3498db',     # Blue: Skills
        'log_': '#e74c3c',       # Red: Logs
        'agent_': '#2ecc71',     # Green: Agents
        'ontology_': '#f1c40f',  # Yellow: Ontologies
        'default': '#95a5a6'
    }

    if not os.path.exists(data_dir):
        print(f"Error: {data_dir} not found.")
        return

    for filename in os.listdir(data_dir):
        if filename.endswith('.yaml'):
            with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
                try:
                    content = yaml.safe_load(f)
                    node_id = filename.replace('.yaml', '')
                    
                    color = color_map['default']
                    for prefix, c in color_map.items():
                        if filename.startswith(prefix):
                            color = c
                            break
                    
                    G.add_node(node_id, color=color)
                    
                    # Logic for PADI edges
                    if content and isinstance(content, dict):
                        if 'target_node' in content:
                            G.add_edge(node_id, content['target_node'])
                        if 'source' in content:
                            G.add_edge(node_id, content['source'])
                except Exception as e:
                    print(f"Skip {filename}: {e}")

    plt.figure(figsize=(12, 10), facecolor='#1a1a1a')
    pos = nx.spring_layout(G, seed=42)
    colors = [nx.get_node_attributes(G, 'color').get(node, '#95a5a6') for node in G.nodes()]
    
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1800, 
            font_size=7, font_color='white', edge_color='gray', arrows=True)
    
    plt.title("Sovereign Bureau: PADI Knowledge Graph", color='white')
    os.makedirs('docs', exist_ok=True)
    plt.savefig('docs/graph_snapshot.png', facecolor='#1a1a1a')
    print("Graph artifact generated at docs/graph_snapshot.png")

if __name__ == "__main__":
    generate_padi_graph()
