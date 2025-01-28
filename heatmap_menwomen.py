import networkx as nx
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the graph
graph_path = "filename.graphml"  # Replace with your GraphML file
G = nx.read_graphml(graph_path)

# Ensure the 'gender' attribute exists
if "gender" not in list(G.nodes(data=True))[0][1]:
    raise ValueError("The graph does not have a 'gender' attribute for nodes.")

# Separate nodes by gender and calculate degrees
degrees = dict(G.degree())
male_nodes = [node for node, data in G.nodes(data=True) if data.get("gender") == "male"]
female_nodes = [node for node, data in G.nodes(data=True) if data.get("gender") == "female"]

# Create degree bins (adjust bin size as needed)
bin_size = 2  # Degrees per bin
male_bins = range(0, max(degrees[node] for node in male_nodes) + bin_size, bin_size)
female_bins = range(0, max(degrees[node] for node in female_nodes) + bin_size, bin_size)
print(male_bins)
print(female_bins)

# Create a dictionary to store the heatmap values
heatmap_data = np.zeros((len(male_bins), len(female_bins)))

# Iterate over edges to count inter-cluster connections
for u, v in G.edges():
    if u in male_nodes and v in female_nodes:
        male_degree = degrees[u]
        female_degree = degrees[v]
    elif u in female_nodes and v in male_nodes:
        male_degree = degrees[v]
        female_degree = degrees[u]
    else:
        continue  # Skip intra-cluster edges

    # Determine the bins for the male and female nodes
    male_bin = max(i for i, b in enumerate(male_bins) if male_degree >= b)
    female_bin = max(i for i, b in enumerate(female_bins) if female_degree >= b)

    # for i, b in enumerate(male_bins):

    # Increment the corresponding heatmap cell
    heatmap_data[male_bin, female_bin] += 1

# Convert to DataFrame for better visualization
# heatmap_df = pd.DataFrame(
#     heatmap_data,
#     index=[f"Male ({b}-{b+bin_size-1})" for b in male_bins],
#     columns=[f"Female ({b}-{b+bin_size-1})" for b in female_bins],
# )
heatmap_df = pd.DataFrame(
    heatmap_data,
    index=[f"Male ({b}-{b+bin_size-1})" for b in male_bins],
    columns=[f"Male ({b}-{b+bin_size-1})" for b in male_bins],
)

# Print or save the heatmap dataset
print(heatmap_df)



plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_df, annot=True, fmt=".0f", cmap="Blues", cbar=True)
plt.title("Heatmap of Inter-Gender Connections by Degree Bins", fontsize=16)
plt.xlabel("Female Degree Bins", fontsize=12)
plt.ylabel("Male Degree Bins", fontsize=12)
plt.show()
