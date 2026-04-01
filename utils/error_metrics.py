import numpy as np

def mse(original, interpolated):
    return np.sum((original - interpolated) ** 2) / np.sum(original ** 2)