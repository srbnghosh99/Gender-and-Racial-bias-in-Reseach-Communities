import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import combinations
import networkx as nx
import math

# Step 1: Define races
races = ['nh_white', 'asian', 'hispanic', 'nh_black','unknown']
race_pairs = [(r1, r2) for r1, r2 in combinations(races, 2)] + [(r, r) for r in races]

# Step 2: Initialize race-pair counts
race_heatmap_data = pd.DataFrame(0, index=races, columns=races)

# Step 3: Iterate through edges and classify by race
G = nx.read_graphml("filename.graphml")

for u, v in G.edges():
    race_u = G.nodes[u].get('race')
    race_v = G.nodes[v].get('race')
    # print(u,v,race_u,race_v)
    # if race_v == 'nan' or race_u =='nan':
    #     continue
    if race_u and race_v:
        race_heatmap_data.loc[race_u, race_v] += 1
        if race_u != race_v:
            race_heatmap_data.loc[race_v, race_u] += 1

# Step 4: Normalize counts by total edges to get percentages
total_edges = race_heatmap_data.values.sum()
race_heatmap_data_percentage = (race_heatmap_data / total_edges) * 100

# Step 5: Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    race_heatmap_data_percentage,
    annot=True,
    fmt=".2f",
    cmap="YlGnBu",
    cbar_kws={'label': 'Percentage (%)'}
)
plt.title("Human Computer Interaction Inter and Intra-Racial Collaborations Heatmap")
plt.xlabel("Race of Node A")
plt.ylabel("Race of Node B")
plt.tight_layout()
plt.show()
