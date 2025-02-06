# 2D Hippocampus Voxel Coordinate Visualization

This python application aims to:
- Visualize successive slices contained in a *.XYZ file 
- Edit/modify the slices by adding or deleting the points.

Input: XYZ file.
Output: XYZ file 

This project is built using the Streamlit library.
An example of application of this project is for visualizing and modifying rat 3D hippocampus voxel coordinates.
The test file provided (TEST_FILE.xyz) corresponds to the granule cell layer in the dentate gyrus region as described here:  https://krasnow1.gmu.edu/cn3/hippocampus3d/. 
The original dataset containing voxel coordinates for various hippocampal regions in a .txt format was converted into an .xyz file.

<img width="845" alt="Image" src="https://github.com/user-attachments/assets/1af0e403-0d7b-4f14-9dd0-6f50a6e9019c">

###### Image Source: Hippocampus. (n.d.). Radiopaedia. https://radiopaedia.org/articles/hippocampus

The primary goal of this project is to generate 2D visualizations by slicing the point cloud along a constant z-axis value, resulting in x-y coordinate plots. These plots represent the centers of voxels within the granule cell layer, providing insights into the spatial distribution of this region.

![image](https://github.com/user-attachments/assets/6de98499-05ca-42fe-8a1f-3a034f1ca754)

## Usage
From the command line (e.g., an anaconda command line), run the program using `streamlit run Final_code.py`
This should open a web app in your default web browser.

<br />
The project supports 3 operations.
- Adding points: simply click on areas where you would like to add points
- Deleting points: after selecting the 'delete points' option, click on an existing point to remove it from the dataset. To remove multiple points, you may use Box or Lasso within the Plotly tools. 
- Gridding points: shifts points into the nearest bin separated by units of 16µm

  

You can find the source data using in TEST_FILE.xyz here: https://krasnow1.gmu.edu/cn3/hippocampus3d/.

## Requirements
- streamlit
- protobuf
- plotly  (`conda install plotly`)
- streamlit_plotly_events (`pip install streamlit-plotly-events`)
- sqlalchemy  (`conda install sqlalchemy`)



## Important notes: 

As of Feb. 2025, protobuf requires python<=3.10.x, so you must use python 3.10.x
In addition, there is a problem with streamlit and protobuf (streamlit requires protobuf version <=3.20.x )
=> run:  `conda install protobuf==3.20.1`




