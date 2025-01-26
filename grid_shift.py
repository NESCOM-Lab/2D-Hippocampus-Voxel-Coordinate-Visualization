"""
This file implements a function that takes a numpy array and shifts all the points onto a grid set by multiples of 16.
Returns a numpy array.
Author: Abhishek K
"""

import numpy as np
from numpy.typing import NDArray

def load_xyz(file):
    data = np.loadtxt(file)
    return data

def grid_shift(data: NDArray[np.float64]) -> NDArray[np.float64]:
    # print(data)
    z_layers = {}

    for line in data:
        x, y, z = line[0], line[1], line[2]
        # Additional properties of each point (i.e. Longitudinal position)
        # a, b, c, d, e, f = line[3], line[4], line[5], line[6], line[7], line[8] 

        # Add all points to their corresponding z layer
        if z not in z_layers:
            z_layers[z] = []
        # z_layers[z].append([x,y,z,a,b,c,d,e,f])
        z_layers[z].append([x,y,z])
    
    count = 0

    # Anchor point to base off the grid
    anchor_pt_x = data[0][0]
    print("Anchor point")
    print(anchor_pt_x)
    print(" ")
    for zkey, points in z_layers.items():
        print("Working on z-layer: " + str(zkey))
        for point in points:
            rel_x = (point[0] - anchor_pt_x)
            n = round(rel_x/16)
            g = anchor_pt_x + (n * 16) # nearest grid line
            
            # Move the point's x to nearest grid line
            point[0] = g

    # Parsing back to numpy array
    gridded_data = []
    for zkey, points in z_layers.items():
        gridded_data.extend(points)

    gridded_data = np.array(gridded_data, dtype=np.float64)

    return gridded_data

if __name__=="__main__":
    print("hi")
    data = load_xyz("TEST_FILE.xyz")
    gridded_data = grid_shift(data)
    print(gridded_data)
    print("done")
    