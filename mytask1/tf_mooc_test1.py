import os
import numpy as np

def create_bin_file(index):
    with open('binary_file_%d'%index, 'wb') as f:
        f.write(np.full((100), index))
