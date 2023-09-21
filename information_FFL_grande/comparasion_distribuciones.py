#%%
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import stats
# %%
simulacion_FFL_C1 = np.load('Simulacion_FFL_I1_AND_Hill_3.npy', allow_pickle=True).item()
simulacion_FFL_C2 = np.load('Simulacion_FFL_I2_AND_Hill_3.npy', allow_pickle=True).item()
simulacion_FFL_C3 = np.load('Simulacion_FFL_I3_AND_Hill_3.npy', allow_pickle=True).item()
simulacion_FFL_C4 = np.load('Simulacion_FFL_I4_AND_Hill_3.npy', allow_pickle=True).item()
#%%
estado_estacionario_Z_C1 = []
estado_estacionario_Z_C2 = []
estado_estacionario_Z_C3 = []
estado_estacionario_Z_C4 = []

for i in range(len(simulacion_FFL_C1["Estados_estacionarios_proteina"])):
    estado_estacionario_Z_C1.append(simulacion_FFL_C1["Estados_estacionarios_proteina"][i][-1])
    estado_estacionario_Z_C2.append(simulacion_FFL_C2["Estados_estacionarios_proteina"][i][-1])
    estado_estacionario_Z_C3.append(simulacion_FFL_C3["Estados_estacionarios_proteina"][i][-1])
    estado_estacionario_Z_C4.append(simulacion_FFL_C4["Estados_estacionarios_proteina"][i][-1])

#%%
simulacion_FFL_C1
#%%
estado_estacionario_Z_C1
#%%
posiciones = np.arange(1,11)
#%%
plt.title("Comportamiento proteina Z estacionaria")
plt.scatter(posiciones,estado_estacionario_Z_C1, label = "FFL C1")
plt.scatter(posiciones,estado_estacionario_Z_C2, label = "FFL C2")
plt.scatter(posiciones,estado_estacionario_Z_C3, label = "FFL C3")
plt.scatter(posiciones,estado_estacionario_Z_C4, label = "FFL C4")
plt.legend()

#%%
datos_0 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][0]
datos_1 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][1]
datos_2 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][2]

datos_3 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][3]
datos_4 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][4]
datos_5 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][5]
datos_6 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][6]
datos_7 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][7]
datos_8 = simulacion_FFL_C1["distribucion_estacionario_proteinaZ"][8]

datos_00 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][0]
datos_10 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][1]
datos_20 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][2]

datos_30 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][3]
datos_40 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][4]
datos_50 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][5]
datos_60 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][6]
datos_70 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][7]
datos_80 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][8]

plt.plot(1.2*np.ones(len(datos_00)), datos_00, color = "red")
plt.plot(2.2*np.ones(len(datos_10)), datos_10, color = "red", alpha = 1)
plt.plot(3.2*np.ones(len(datos_20)), datos_20, color = "red", alpha = 1)
plt.plot(4.2*np.ones(len(datos_30)), datos_30, color = "red", alpha = 1)
plt.plot(5.2*np.ones(len(datos_40)), datos_40, color = "red", alpha = 1)
plt.plot(6.2*np.ones(len(datos_50)), datos_50, color = "red", alpha = 1)
plt.plot(7.2*np.ones(len(datos_60)), datos_60, color = "red", alpha = 1)
plt.plot(8.2*np.ones(len(datos_70)), datos_70, color = "red", alpha = 1)
plt.plot(9.2*np.ones(len(datos_80)), datos_80, color = "red", alpha = 1)

plt.plot(np.ones(len(datos_0)), datos_0, color = "blue")
plt.plot(2*np.ones(len(datos_1)), datos_1, color = "blue")
plt.plot(3*np.ones(len(datos_2)), datos_2, color = "blue")
plt.plot(4*np.ones(len(datos_3)), datos_3, color = "blue")
plt.plot(5*np.ones(len(datos_4)), datos_4, color = "blue")
plt.plot(6*np.ones(len(datos_5)), datos_5, color = "blue")
plt.plot(7*np.ones(len(datos_6)), datos_6, color = "blue")
plt.plot(8*np.ones(len(datos_7)), datos_7, color = "blue")
plt.plot(9*np.ones(len(datos_8)), datos_8, color = "blue")
plt.ylim(20000, 150000)
#%%
datos_00 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][0]
datos_10 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][1]
datos_20 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][2]

datos_30 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][3]
datos_40 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][4]
datos_50 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][5]
datos_60 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][6]
datos_70 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][7]
datos_80 = simulacion_FFL_C4["distribucion_estacionario_proteinaZ"][8]


plt.scatter(np.ones(len(datos_00)), datos_00)
plt.scatter(2*np.ones(len(datos_10)), datos_10)
plt.scatter(3*np.ones(len(datos_20)), datos_20)
plt.scatter(4*np.ones(len(datos_30)), datos_30)
plt.scatter(5*np.ones(len(datos_40)), datos_40)
plt.scatter(6*np.ones(len(datos_50)), datos_50)
plt.scatter(7*np.ones(len(datos_60)), datos_60)
plt.scatter(8*np.ones(len(datos_70)), datos_70)
plt.scatter(9*np.ones(len(datos_80)), datos_80)
plt.ylim(30000, 150000)
# %%
valores_p_distribuciones_ARNmY_C1C4 = []
valores_p_distribuciones_ARNmZ_C1C4 = []

valores_p_distribuciones_proteinaY_C1C4 = []
valores_p_distribuciones_proteinaZ_C1C4 = []
for i in range(0,10):
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

plt.scatter(np.arange(0,10), valores_p_distribuciones_proteinaZ_C1C4)
# %%
valores_p_distribuciones_proteinaY_C1C4
# %%
plt.hist(simulacion_FFL_C1["distribucion_estacionario_proteinaY"][5], bins = 20, histtype="step")
plt.hist(simulacion_FFL_C4["distribucion_estacionario_proteinaY"][5], bins = 20, histtype="step")
# %%
valores_p_distribuciones_ARNmY_C2C3 = []
valores_p_distribuciones_ARNmZ_C2C3 = []

valores_p_distribuciones_proteinaY_C2C3 = []
valores_p_distribuciones_proteinaZ_C2C3 = []
for i in range(0,10):
    distribucion_C2_ARNmY = simulacion_FFL_C2["distribucion_estacionario_ARNmY"][i]
    distribucion_C3_ARNmY = simulacion_FFL_C3["distribucion_estacionario_ARNmY"][i]

    distribucion_C2_ARNmZ = simulacion_FFL_C2["distribucion_estacionario_ARNmZ"][i]
    distribucion_C3_ARNmZ = simulacion_FFL_C3["distribucion_estacionario_ARNmZ"][i]

    distribucion_C2_proteinaY = simulacion_FFL_C2["distribucion_estacionario_proteinaY"][i]
    distribucion_C3_proteinaY = simulacion_FFL_C3["distribucion_estacionario_proteinaY"][i]
    
    distribucion_C2_proteinaZ = simulacion_FFL_C2["distribucion_estacionario_proteinaZ"][i]
    distribucion_C3_proteinaZ = simulacion_FFL_C3["distribucion_estacionario_proteinaZ"][i]


    p_value_ARNmY_C2_C3 = stats.kstest(distribucion_C2_ARNmY, distribucion_C3_ARNmY)[1]
    p_value_ARNmZ_C2_C3 = stats.kstest(distribucion_C2_ARNmZ, distribucion_C3_ARNmZ)[1]

    p_value_proteinaY_C2_C3 = stats.kstest(distribucion_C2_proteinaY, distribucion_C3_proteinaY)[1]
    p_value_proteinaZ_C2_C3 = stats.kstest(distribucion_C2_proteinaZ, distribucion_C3_proteinaZ)[1]

    valores_p_distribuciones_ARNmY_C2C3.append(p_value_ARNmY_C2_C3)
    valores_p_distribuciones_ARNmZ_C2C3.append(p_value_ARNmZ_C2_C3)

    valores_p_distribuciones_proteinaY_C2C3.append(p_value_proteinaY_C2_C3)
    valores_p_distribuciones_proteinaZ_C2C3.append(p_value_proteinaZ_C2_C3)
# %%

plt.scatter(np.arange(0,10), valores_p_distribuciones_proteinaZ_C2C3)
# %%
valores_p_distribuciones_proteinaY_C2C3
