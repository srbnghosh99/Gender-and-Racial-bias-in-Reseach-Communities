# Four Fields, One Problem: Bias and Disparities in CS Research Communities


### The preprint version is shared here, still on going reseach on this.
https://www.researchgate.net/publication/388327694_Four_Fields_One_Problem_Bias_and_Disparities_in_Computer_Science_Research_Communities



## Overview
This repository contains scripts and notebooks for processing data and generating various visualizations, including graphs and heatmaps. Below is a brief description of each file, its inputs, and its outputs.

## Files and Their Descriptions

### 1. `create_graph.ipynb`
**Description**: This notebook is used to generate a graph representation from processed data.
- **Input**: Processed data (CSV, JSON, or other structured formats)
- **Output**: Graph object (NetworkX, visualization plots, or saved graph files)

### 2. `preprocessing.ipynb`
**Description**: This notebook handles data preprocessing tasks, including cleaning, transformation, and feature extraction.
- **Input**: Raw data files (CSV, JSON, etc.)
- **Output**: Preprocessed data saved for further analysis

### 3. `heatmap_menwomen.py`
**Description**: Generates a heatmap comparing different aspects between men and women.
- **Input**: Processed dataset with gender information
- **Output**: Heatmap visualization (PNG, JPG, or interactive plot)

### 4. `inter_cluster_heatmap.py`
**Description**: Generates an inter-cluster heatmap to show relationships between different clusters.
- **Input**: Clustered data
- **Output**: Heatmap visualization

### 5. `inter_race_heatmap.py`
**Description**: Generates a heatmap analyzing relationships between different racial groups.
- **Input**: Dataset containing racial information
- **Output**: Heatmap visualization

### 6. `intra_cluster_heatmap.py`
**Description**: Generates an intra-cluster heatmap to analyze patterns within individual clusters.
- **Input**: Clustered data
- **Output**: Heatmap visualization

## Usage
Run each script or notebook as required:

For Python scripts:
```bash
python heatmap_menwomen.py
python inter_cluster_heatmap.py
python inter_race_heatmap.py
python intra_cluster_heatmap.py
```

For Jupyter notebooks, open and execute them in Jupyter Notebook or Jupyter Lab:
```bash
jupyter notebook create_graph.ipynb
jupyter notebook preprocessing.ipynb
```

## Dependencies
- Python 3.x
- Required libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `networkx` (if applicable)

## Notes
- Ensure that the input data files are correctly formatted before running the scripts.
- Modify visualization parameters in the scripts if needed to customize the output.

---


