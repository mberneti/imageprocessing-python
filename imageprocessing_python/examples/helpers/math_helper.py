from numba import njit, prange
import numpy as np
from numba import njit, prange


@njit
def getMinMax(array):
    n = array.shape[0]
    min = max = array[0]

    for i in prange(n):
        if(array[i] > max):
            max = array[i]
        elif(array[i] < min):
            min = array[i]

    return min, max


@njit
def normalizeWithMinMax(x, min, max):
    if(min == max):
        return 1
    y = (x-min) / (max-min)
    return y
