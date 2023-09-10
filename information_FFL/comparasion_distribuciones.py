#%%
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import stats
# %%
simulacion_FFL_C1 = np.load('Simulacion_FFL_C1_AND_Hill.npy', allow_pickle=True).item()
simulacion_FFL_C4 = np.load('diccionario_FFL_C4_experimentos_distribuciones.npy', allow_pickle=True).item()
#%%
print(len(simulacion_FFL_C1))
# %%
valores_p_distribuciones_ARNmY_C1C4 = []
valores_p_distribuciones_ARNmZ_C1C4 = []

valores_p_distribuciones_proteinaY_C1C4 = []
valores_p_distribuciones_proteinaZ_C1C4 = []
for i in range(0,6):
    distribucion_C1_ARNmY = simulacion_FFL_C1["distribucion_estacionario_ARNmY"][i]
    distribucion_C4_ARNmY = simulacion_FFL_C4["distribucion_estacionario_ARNmY"][i]

    distribucion_C1_ARNmZ = simulacion_FFL_C1["distribucion_estacionario_ARNmZ"][i]
    distribucion_C4_ARNmZ = simulacion_FFL_C4["distribucion_estacionario_ARNmZ"][i]

    distribucion_C1_proteinaY = simulacion_FFL_C1["distribucion_estacionario_proteinaY"][i]
    distribucion_C4_proteinaY = simulacion_FFL_C4["distribucion_estacionario_proteinaY"][i]
    
    distribucion_C1_proteinaZ = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][i]
    distribucion_C4_proteinaZ = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][i]


    p_value_ARNmY_C1_C4 = stats.kstest(distribucion_C1_ARNmY, distribucion_C4_ARNmY)[1]
    p_value_ARNmZ_C1_C4 = stats.kstest(distribucion_C1_ARNmZ, distribucion_C4_ARNmZ)[1]

    p_value_proteinaY_C1_C4 = stats.kstest(distribucion_C1_proteinaY, distribucion_C4_proteinaY)[1]
    p_value_proteinaZ_C1_C4 = stats.kstest(distribucion_C1_proteinaZ, distribucion_C4_proteinaZ)[1]

    valores_p_distribuciones_ARNmY_C1C4.append(p_value_ARNmY_C1_C4)
    valores_p_distribuciones_ARNmZ_C1C4.append(p_value_ARNmZ_C1_C4)

    valores_p_distribuciones_proteinaY_C1C4.append(p_value_proteinaY_C1_C4)
    valores_p_distribuciones_proteinaZ_C1C4.append(p_value_proteinaZ_C1_C4)
# %%

plt.scatter(np.arange(0,6), valores_p_distribuciones_proteinaZ_C1C4)
# %%
valores_p_distribuciones_proteinaY_C1C4
# %%
plt.hist(simulacion_FFL_C1["distribucion_estacionario_proteinaY"][5], bins = 20, histtype="step")
plt.hist(simulacion_FFL_C4["distribucion_estacionario_proteinaY"][5], bins = 20, histtype="step")
# %%
