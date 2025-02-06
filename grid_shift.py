"""
This file implements a function that takes a numpy array and shifts all the points onto a grid set by multiples of 16.
Returns a numpy array.
Updates: 
    2025.02.06: Shifts X and Y for all points on a grid that is truly a multiple of 16 
    (1st version did not offset point 0 and only shifted the X coordinate)

Author: Abhishek K, JM Bouteiller

"""

import numpy as np
from numpy.typing import NDArray

def load_xyz(file):
    data = np.loadtxt(file)
    return data

def grid_shift_strict(data: NDArray[np.float64]) -> NDArray[np.float64]:
    '''
    This function shifts X and Y coordinates of all the points onto a grid set by multiples of 16 without using an anchor point.
    It also removes potential duplicates

    Parameters
    ----------
    data : NDArray[np.float64]
        Initial points.

    Returns
    -------
    gridded_data : TYPE
        Points on the grid.

    '''
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
    
    print(" ")
    
    # Going through every layer and all points in all layers
    for zkey, points in z_layers.items():
        print("Working on z-layer: " + str(zkey))
        for point in points:
            
            #rel_x = (point[0] - anchor_pt_x)
            newX = ( round(point[0]/16.0)  ) * 16 # nearest grid line for X
            newY = ( round(point[1]/16.0)  ) * 16 # nearest grid line for Y
            #print ('zkey = ' , zkey , 'old x =' , point [0] , 'and new x =' , newX, 'old Y =' , point [1] , 'and new Y =' , newY)
            # Move the point's x and y to nearest grid line
            point[0] = newX
            point[1] = newY

    # Parsing back to numpy array
    gridded_data = []
    for zkey, points in z_layers.items():
        gridded_data.extend(points)

    gridded_data = np.array(gridded_data, dtype=np.float64)

    print("Removing potential duplicates...")
    # Use numpy's unique function to retrieve unique rows only and the inded for the points removed 
    unique_gridded_data, indices = np.unique(gridded_data, axis=0, return_index=True)
    
    
    # Check if duplicates were removed
    if len(unique_gridded_data) < len(gridded_data):
        print(f"Removed {len(gridded_data) - len(unique_gridded_data)} duplicate points.")
    else:
        print("No duplicate points were found.")    
        
    
    return unique_gridded_data



def grid_shift(data: NDArray[np.float64]) -> NDArray[np.float64]:
    '''
    This function shifts the X coordinate of all the points onto a grid set by multiples of 16 using the first point as an anchor point.
    i.e., this anchor is the reference; the X coordinate of all other points will be shifted by 16 compared to this one.

    Parameters
    ----------
    data : NDArray[np.float64]
        Initial points.

    Returns
    -------
    gridded_data : TYPE
        Points on the grid.
    '''
    
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
    
    #count = 0

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
    gridded_data = grid_shift_strict(data)
    print(gridded_data)
    print("done")
    