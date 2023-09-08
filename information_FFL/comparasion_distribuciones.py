#%%
import numpy as np
import matplotlib.pyplot as plt
import csv
# %%
simulacion_FFL_C1 = np.load('diccionario_FFL_C1_experimentos_distribuciones.npy', allow_pickle=True).item()
simulacion_FFL_C4 = np.load('diccionario_FFL_C4_experimentos_distribuciones.npy', allow_pickle=True).item()
# %%
simulacion_FFL_C1
# %%
import numpy as np
from scipy import stats


sample1 = stats.laplace.rvs(size=105, random_state=rng)
sample2 = stats.laplace.rvs(size=95, random_state=rng)
stats.kstest(sample1, sample2)

# %%
distribucion_estacionario_ARNmY_C1 = simulacion_FFL_C1["distribucion_estacionario_ARNmY"]
distribucion_estacionario_ARNmZ_C1 = simulacion_FFL_C1["distribucion_estacionario_ARNmZ"]

distribucion_estacionario_ARNmY_C4 = simulacion_FFL_C4["distribucion_estacionario_ARNmY"]
distribucion_estacionario_ARNmZ_C4 = simulacion_FFL_C4["distribucion_estacionario_ARNmZ"]
# %%
p_value_ARNmY_C1_C4 = stats.kstest(distribucion_estacionario_ARNmY_C1, distribucion_estacionario_ARNmY_C4)[1]
p_value_ARNmZ_C1_C4 = stats.kstest(distribucion_estacionario_ARNmZ_C1, distribucion_estacionario_ARNmZ_C4)[1]
# %%
p_value_ARNmY_C1_C4

# %%
p_value_ARNmZ_C1_C4
# %%
