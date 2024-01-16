import xarray as xr
import xroms
import numpy as np
import matplotlib.pyplot as plt
import cmocean.cm as cmo
import pandas as pd
import xgcm

filename = 'last10yrAVERAGE_LGM400.nc'
chunks = {'ocean_time': 1}

dataset = xr.open_dataset(filename)

print(dataset)