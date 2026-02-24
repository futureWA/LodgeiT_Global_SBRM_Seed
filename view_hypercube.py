import os
import yaml

def render_hypercube():
    ontology_path = './01_Ontology'
    hypercube = {}

    print("\n=== LODGEIT GLOBAL: SBRM HYPERCUBE VIEW ===")
    
    # Iterate through all fact nodes
    for filename in os.listdir(ontology_path):
        if filename.endswith(".md"):
            with open(os.path.join(ontology_path, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                # Split YAML from Body
                parts = content.split('---')
                if len(parts) >= 3:
                    try:
                        metadata = yaml.safe_load(parts[1])
                        # We look for the classification in the body or tags
                        # For the Uplifted facts, we'll parse the 'Classification' line
                        body = parts[2]
                        classification = "Unclassified"
                        
                        for line in body.split('\n'):
                            if "Classification:" in line:
                                classification = line.split(":")[1].strip()
                        
                        if classification not in hypercube:
                            hypercube[classification] = []
                            
                        hypercube[classification].append({
                            "name": filename.replace('.md', ''),
                            "id": metadata.get('@id', 'No ID')
                        })
                    except Exception as e:
                        continue

    # Print the nested structure
    for dimension, nodes in sorted(hypercube.items()):
        print(f"\n[Dimension: {dimension}]")
        for node in nodes:
            print(f"  └── Fact: {node['name']}")
            print(f"      ID: {node['id']}")

    print("\n=== End of Cube ===")

if __name__ == "__main__":
    render_hypercube()