import networkx as nx
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the graph
graph_path = "/Users/shrabanighosh/My work/UNCC/Fall 2024/CHI2025/authors_names/author_info/hci_gender_race.graphml"  # Replace with your GraphML file
G = nx.read_graphml(graph_path)

# Ensure the 'gender' attribute exists
if "gender" not in list(G.nodes(data=True))[0][1]:
    raise ValueError("The graph does not have a 'gender' attribute for nodes.")

# Separate nodes by gender and calculate degrees
degrees = dict(G.degree())
male_nodes = [node for node, data in G.nodes(data=True) if data.get("gender") == "male"]
female_nodes = [node for node, data in G.nodes(data=True) if data.get("gender") == "female"]

# Create degree bins (adjust bin size as needed)
bin_size = 5  # Degrees per bin
male_bins = range(0, max(degrees[node] for node in male_nodes) + bin_size, bin_size)
female_bins = range(0, max(degrees[node] for node in female_nodes) + bin_size, bin_size)

# Create dictionaries to store heatmap values
male_heatmap_data = np.zeros((len(male_bins), len(male_bins)))
female_heatmap_data = np.zeros((len(female_bins), len(female_bins)))

# Function to find the bin for a given degree
def get_bin(degree, bins):
    return max(i for i, b in enumerate(bins) if degree >= b)

# Iterate over edges to count intra-cluster connections
for u, v in G.edges():
    if u in male_nodes and v in male_nodes:  # Intra-male cluster
        male_degree_u = degrees[u]
        male_degree_v = degrees[v]
        male_bin_u = get_bin(male_degree_u, male_bins)
        male_bin_v = get_bin(male_degree_v, male_bins)
        male_heatmap_data[male_bin_u, male_bin_v] += 1
        if male_bin_u != male_bin_v:
            male_heatmap_data[male_bin_v, male_bin_u] += 1  # Symmetric count
    elif u in female_nodes and v in female_nodes:  # Intra-female cluster
        female_degree_u = degrees[u]
        female_degree_v = degrees[v]
        female_bin_u = get_bin(female_degree_u, female_bins)
        female_bin_v = get_bin(female_degree_v, female_bins)
        female_heatmap_data[female_bin_u, female_bin_v] += 1
        if female_bin_u != female_bin_v:
            female_heatmap_data[female_bin_v, female_bin_u] += 1  # Symmetric count

male_heatmap_data = (male_heatmap_data / len(male_nodes)) * 100
female_heatmap_data = (female_heatmap_data / len(female_nodes)) * 100


# Convert to DataFrame for visualization
male_heatmap_df = pd.DataFrame(
    male_heatmap_data,
    index=[f"Male ({b}-{b+bin_size-1})" for b in male_bins],
    columns=[f"Male ({b}-{b+bin_size-1})" for b in male_bins],
)
female_heatmap_df = pd.DataFrame(
    female_heatmap_data,
    index=[f"Female ({b}-{b+bin_size-1})" for b in female_bins],
    columns=[f"Female ({b}-{b+bin_size-1})" for b in female_bins],
)

# Plot the heatmaps
plt.figure(figsize=(16, 6))

# Male Intra-Cluster Heatmap
plt.subplot(1, 2, 1)
# sns.heatmap(male_heatmap_df, annot=True, fmt=".0f", cmap="Blues", cbar=True)
sns.heatmap(male_heatmap_df, annot=True, fmt=".1f", cmap="Blues",cbar_kws={'format': '%.0f%%'})
plt.title("Human Computer Interaction Intra-Male Cluster Connections", fontsize=16)
plt.xlabel("Male Degree Bins", fontsize=12)
plt.ylabel("Male Degree Bins", fontsize=12)

# Female Intra-Cluster Heatmap
plt.subplot(1, 2, 2)
sns.heatmap(female_heatmap_df, annot=True, fmt=".1f", cmap="Reds",cbar_kws={'format': '%.0f%%'})
plt.title("Human Computer Interaction Intra-Female Cluster Connections", fontsize=16)
plt.xlabel("Female Degree Bins", fontsize=12)
plt.ylabel("Female Degree Bins", fontsize=12)

plt.tight_layout()
plt.show()
