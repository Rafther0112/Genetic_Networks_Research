#%%
import numpy as np
import matplotlib.pyplot as plt
import csv
# %%
simulacion_FFL_I1 = np.load('diccionario_FFL_I1.npy', allow_pickle=True).item()
simulacion_FFL_I2 = np.load('diccionario_FFL_I2.npy', allow_pickle=True).item()
simulacion_FFL_I3 = np.load('diccionario_FFL_I3.npy', allow_pickle=True).item()
simulacion_FFL_I4 = np.load('diccionario_FFL_I4.npy', allow_pickle=True).item()
# %%
ARNm_estacionario_I1 = simulacion_FFL_I1["Estados_estacionarios_ARNm"]
proteina_estacionario_I1 = simulacion_FFL_I1["Estados_estacionarios_proteina"]

ARNm_estacionario_I2 = simulacion_FFL_I2["Estados_estacionarios_ARNm"]
proteina_estacionario_I2 = simulacion_FFL_I2["Estados_estacionarios_proteina"]

ARNm_estacionario_I3 = simulacion_FFL_I3["Estados_estacionarios_ARNm"]
proteina_estacionario_I3 = simulacion_FFL_I3["Estados_estacionarios_proteina"]

ARNm_estacionario_I4 = simulacion_FFL_I4["Estados_estacionarios_ARNm"]
proteina_estacionario_I4 = simulacion_FFL_I4["Estados_estacionarios_proteina"]
# %%
estado_estacionario_X_I1 = []
estado_estacionario_X_I2 = []
estado_estacionario_X_I3 = []
estado_estacionario_X_I4 = []

for i in range(len(simulacion_FFL_I1["Estados_estacionarios_proteina"])):
    estado_estacionario_X_I1.append(np.array([ARNm_estacionario_I1[i][0], proteina_estacionario_I1[i][0]]))
    estado_estacionario_X_I2.append(np.array([ARNm_estacionario_I2[i][0], proteina_estacionario_I2[i][0]]))
    estado_estacionario_X_I3.append(np.array([ARNm_estacionario_I3[i][0], proteina_estacionario_I3[i][0]]))
    estado_estacionario_X_I4.append(np.array([ARNm_estacionario_I4[i][0], proteina_estacionario_I4[i][0]]))

estado_estacionario_X_I1 = np.array(estado_estacionario_X_I1)
estado_estacionario_X_I2 = np.array(estado_estacionario_X_I2)
estado_estacionario_X_I3 = np.array(estado_estacionario_X_I3)
estado_estacionario_X_I4 = np.array(estado_estacionario_X_I4)
# %%
estado_estacionario_Y_I1 = []
estado_estacionario_Y_I2 = []
estado_estacionario_Y_I3 = []
estado_estacionario_Y_I4 = []

for i in range(len(simulacion_FFL_I1["Estados_estacionarios_proteina"])):
    estado_estacionario_Y_I1.append(np.array([ARNm_estacionario_I1[i][1], proteina_estacionario_I1[i][1]]))
    estado_estacionario_Y_I2.append(np.array([ARNm_estacionario_I2[i][1], proteina_estacionario_I2[i][1]]))
    estado_estacionario_Y_I3.append(np.array([ARNm_estacionario_I3[i][1], proteina_estacionario_I3[i][1]]))
    estado_estacionario_Y_I4.append(np.array([ARNm_estacionario_I4[i][1], proteina_estacionario_I4[i][1]]))

estado_estacionario_Y_I1 = np.array(estado_estacionario_Y_I1)
estado_estacionario_Y_I2 = np.array(estado_estacionario_Y_I2)
estado_estacionario_Y_I3 = np.array(estado_estacionario_Y_I3)
estado_estacionario_Y_I4 = np.array(estado_estacionario_Y_I4)
# %%
estado_estacionario_Z_I1 = []
estado_estacionario_Z_I2 = []
estado_estacionario_Z_I3 = []
estado_estacionario_Z_I4 = []

for i in range(len(simulacion_FFL_I1["Estados_estacionarios_proteina"])):
    estado_estacionario_Z_I1.append(np.array([ARNm_estacionario_I1[i][2], proteina_estacionario_I1[i][2]]))
    estado_estacionario_Z_I2.append(np.array([ARNm_estacionario_I2[i][2], proteina_estacionario_I2[i][2]]))
    estado_estacionario_Z_I3.append(np.array([ARNm_estacionario_I3[i][2], proteina_estacionario_I3[i][2]]))
    estado_estacionario_Z_I4.append(np.array([ARNm_estacionario_I4[i][2], proteina_estacionario_I4[i][2]]))

estado_estacionario_Z_I1 = np.array(estado_estacionario_Z_I1)
estado_estacionario_Z_I2 = np.array(estado_estacionario_Z_I2)
estado_estacionario_Z_I3 = np.array(estado_estacionario_Z_I3)
estado_estacionario_Z_I4 = np.array(estado_estacionario_Z_I4)
# %%
posiciones = np.arange(0,10)

plt.figure(figsize=(10,6))
plt.title("Comparación ARNm X estacionaria")
plt.scatter(posiciones,estado_estacionario_X_I1[0:,0], label = "FFL I1")
plt.scatter(posiciones,estado_estacionario_X_I2[0:,0], label = "FFL I2")
plt.scatter(posiciones,estado_estacionario_X_I3[0:,0], label = "FFL I3")
plt.scatter(posiciones,estado_estacionario_X_I4[0:,0], label = "FFL I4")
plt.legend()
plt.ylabel("Valor estacionario de ARNm Z")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
#%%
plt.figure(figsize=(10,6))
plt.title("Comparación ARNm Y estacionaria")
plt.scatter(posiciones,estado_estacionario_Y_I1[0:,0], label = "FFL I1")
plt.scatter(posiciones,estado_estacionario_Y_I2[0:,0], label = "FFL I2")
plt.scatter(posiciones,estado_estacionario_Y_I3[0:,0], label = "FFL I3")
plt.scatter(posiciones,estado_estacionario_Y_I4[0:,0], label = "FFL I4")
plt.legend()
plt.ylabel("Valor estacionario de ARNm Z")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
# %%
plt.figure(figsize=(10,6))
plt.title("Comparación ARNm Z estacionaria")
plt.scatter(posiciones,estado_estacionario_Z_I1[0:,0], label = "FFL I1")
plt.scatter(posiciones,estado_estacionario_Z_I2[0:,0], label = "FFL I2")
plt.scatter(posiciones,estado_estacionario_Z_I3[0:,0], label = "FFL I3")
plt.scatter(posiciones,estado_estacionario_Z_I4[0:,0], label = "FFL I4")
plt.legend()
plt.ylabel("Valor estacionario de ARNm Z")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
# %%
plt.figure(figsize=(10,6))
plt.title("Comparación Proteina Y estacionaria")
plt.scatter(posiciones,estado_estacionario_Y_I1[0:,1], label = "FFL I1", color = "red")
plt.scatter(posiciones,estado_estacionario_Y_I2[0:,1], label = "FFL I2", color = "blue")
plt.scatter(posiciones,estado_estacionario_Y_I3[0:,1], label = "FFL I3", color = "red")
plt.scatter(posiciones,estado_estacionario_Y_I4[0:,1], label = "FFL I4", color = "blue")
plt.legend()
plt.ylabel("Valor estacionario de proteina Y")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
plt.savefig("proteina_Y_estacionario_incoherentes.jpg", dpi = 500)
# %%
plt.figure(figsize=(10,6))
plt.title("Comparación Proteina Z estacionaria")
plt.scatter(posiciones,estado_estacionario_Z_I1[0:,1], label = "FFL I1", color = "red")
plt.scatter(posiciones,estado_estacionario_Z_I2[0:,1], label = "FFL I2", color = "blue")
plt.scatter(posiciones,estado_estacionario_Z_I3[0:,1], label = "FFL I3", color = "red")
plt.scatter(posiciones,estado_estacionario_Z_I4[0:,1], label = "FFL I4", color = 'blue')
plt.legend()
plt.ylabel("Valor estacionario de proteina Z")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
plt.savefig("proteina_Z_estacionario_incoherentes.jpg", dpi = 500)
# %%
plt.figure(figsize=(8,6))
plt.title("Comportamiento proteinas Y+Z estacionaria coherentes")
plt.scatter(posiciones,np.array(estado_estacionario_Y_I1)[0:,1] + np.array(estado_estacionario_Z_I1)[0:,1], label = "FFL I1", color = "red")
plt.scatter(posiciones, np.array(estado_estacionario_Y_I2)[0:,1] + np.array(estado_estacionario_Z_I2)[0:,1], label = "FFL I2", color = "blue")
plt.scatter(posiciones,np.array(estado_estacionario_Y_I3)[0:,1] + np.array(estado_estacionario_Z_I3)[0:,1], label = "FFL I3", color = "green")
plt.scatter(posiciones,np.array(estado_estacionario_Y_I4)[0:,1] + np.array(estado_estacionario_Z_I4)[0:,1], label = "FFL I4", color = "orange")
plt.legend()
plt.xlabel(r"Valor de $K_x$")
plt.ylabel(r"Proteina Y en estacionario")
plt.savefig("Proteina_ZY_FFL_incoherentes.jpg", dpi = 500)
# %%
np.array(estado_estacionario_Y_I1) + np.array(estado_estacionario_Z_I1)
# %%
