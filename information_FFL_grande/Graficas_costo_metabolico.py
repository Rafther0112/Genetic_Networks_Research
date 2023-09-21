#%%
import numpy as np
import matplotlib.pyplot as plt
import csv
# %%
simulacion_FFL_C1 = np.load('diccionario_FFL_C1.npy', allow_pickle=True).item()
simulacion_FFL_C2 = np.load('diccionario_FFL_C2.npy', allow_pickle=True).item()
simulacion_FFL_C3 = np.load('diccionario_FFL_C3.npy', allow_pickle=True).item()
simulacion_FFL_C4 = np.load('diccionario_FFL_C4.npy', allow_pickle=True).item()
# %%
simulacion_FFL_C1["Estados_estacionarios_ARNm"]
# %%
simulacion_FFL_C4["Estados_estacionarios_ARNm"]

# %%
simulacion_FFL_C1["Estados_estacionarios_proteina"][0]
simulacion_FFL_C4["Estados_estacionarios_proteina"]
# %%
plt.figure(figsize=(12,7))
plt.scatter([1],simulacion_FFL_C1["Estados_estacionarios_proteina"][-1][0], label = ["Proteina X", "Proteina Y", "Proteina Z"])
plt.scatter([1],simulacion_FFL_C2["Estados_estacionarios_proteina"][-1][0], label = ["Proteina X", "Proteina Y", "Proteina Z"])
plt.scatter([1],simulacion_FFL_C3["Estados_estacionarios_proteina"][-1][0], label = ["Proteina X", "Proteina Y", "Proteina Z"])
plt.scatter([1],simulacion_FFL_C4["Estados_estacionarios_proteina"][-1][0], label = ["Proteina X", "Proteina Y", "Proteina Z"])
plt.legend()
# %%
plt.figure(figsize=(12,7))
plt.plot(simulacion_FFL_C1["Estados_estacionarios_ARNm"], label = ["ARNm X", "ARNm Y", "ARNm Z"])
#plt.plot(simulacion_FFL_C2["Estados_estacionarios_ARNm"], label = ["ARNm X", "ARNm Y", "ARNm Z"])
#plt.plot(simulacion_FFL_C3["Estados_estacionarios_ARNm"], label = ["ARNm X", "ARNm Y", "ARNm Z"])
plt.plot(simulacion_FFL_C4["Estados_estacionarios_ARNm"], label = ["ARNm X", "ARNm Y", "ARNm Z"])
plt.legend()
# %%
plt.scatter([1,2,3],simulacion_FFL_C1["Estados_estacionarios_proteina"][-1], label = ["Proteina X", "Proteina Y", "Proteina Z"])

# %%
estado_estacionario_Z_C1 = []
estado_estacionario_Z_C2 = []
estado_estacionario_Z_C3 = []
estado_estacionario_Z_C4 = []

for i in range(len(simulacion_FFL_C1["Estados_estacionarios_proteina"])):
    estado_estacionario_Z_C1.append(simulacion_FFL_C1["Estados_estacionarios_proteina"][i][-1])
    estado_estacionario_Z_C2.append(simulacion_FFL_C2["Estados_estacionarios_proteina"][i][-1])
    estado_estacionario_Z_C3.append(simulacion_FFL_C3["Estados_estacionarios_proteina"][i][-1])
    estado_estacionario_Z_C4.append(simulacion_FFL_C4["Estados_estacionarios_proteina"][i][-1])

# %%
estado_estacionario_X_C1 = []
estado_estacionario_X_C2 = []
estado_estacionario_X_C3 = []
estado_estacionario_X_C4 = []

for i in range(len(simulacion_FFL_C1["Estados_estacionarios_proteina"])):
    estado_estacionario_X_C1.append(simulacion_FFL_C1["Estados_estacionarios_proteina"][i][0])
    estado_estacionario_X_C2.append(simulacion_FFL_C2["Estados_estacionarios_proteina"][i][0])
    estado_estacionario_X_C3.append(simulacion_FFL_C3["Estados_estacionarios_proteina"][i][0])
    estado_estacionario_X_C4.append(simulacion_FFL_C4["Estados_estacionarios_proteina"][i][0])

# %%
estado_estacionario_Y_C1 = []
estado_estacionario_Y_C2 = []
estado_estacionario_Y_C3 = []
estado_estacionario_Y_C4 = []

for i in range(len(simulacion_FFL_C1["Estados_estacionarios_proteina"])):
    estado_estacionario_Y_C1.append(simulacion_FFL_C1["Estados_estacionarios_proteina"][i][1])
    estado_estacionario_Y_C2.append(simulacion_FFL_C2["Estados_estacionarios_proteina"][i][1])
    estado_estacionario_Y_C3.append(simulacion_FFL_C3["Estados_estacionarios_proteina"][i][1])
    estado_estacionario_Y_C4.append(simulacion_FFL_C4["Estados_estacionarios_proteina"][i][1])

#%%
posiciones = np.arange(0,10)
# %%
plt.title("Comportamiento proteina X estacionaria")
plt.scatter(posiciones,estado_estacionario_X_C1, label = "FFL C1")
plt.scatter(posiciones,estado_estacionario_X_C2, label = "FFL C2")
plt.scatter(posiciones,estado_estacionario_X_C3, label = "FFL C3")
plt.scatter(posiciones,estado_estacionario_X_C4, label = "FFL C4")
plt.legend()
# %%
plt.title("Comportamiento proteina Y estacionaria")
plt.scatter(posiciones,estado_estacionario_Y_C1, label = "FFL C1")
plt.scatter(posiciones,estado_estacionario_Y_C2, label = "FFL C2")
plt.scatter(posiciones,estado_estacionario_Y_C3, label = "FFL C3")
plt.scatter(posiciones,estado_estacionario_Y_C4, label = "FFL C4")
plt.legend()
#%%
plt.title("Comportamiento proteina Z estacionaria")
plt.scatter(posiciones,estado_estacionario_Z_C1, label = "FFL C1")
plt.scatter(posiciones,estado_estacionario_Z_C2, label = "FFL C2")
plt.scatter(posiciones,estado_estacionario_Z_C3, label = "FFL C3")
plt.scatter(posiciones,estado_estacionario_Z_C4, label = "FFL C4")
plt.legend()
# %%
estado_estacionario_ARNm_Z_C1 = []
estado_estacionario_ARNm_Z_C2 = []
estado_estacionario_ARNm_Z_C3 = []
estado_estacionario_ARNm_Z_C4 = []

for i in range(len(simulacion_FFL_C1["Estados_estacionarios_proteina"])):
    estado_estacionario_ARNm_Z_C1.append(simulacion_FFL_C1["Estados_estacionarios_ARNm"][i][-1])
    estado_estacionario_ARNm_Z_C2.append(simulacion_FFL_C2["Estados_estacionarios_ARNm"][i][-1])
    estado_estacionario_ARNm_Z_C3.append(simulacion_FFL_C3["Estados_estacionarios_ARNm"][i][-1])
    estado_estacionario_ARNm_Z_C4.append(simulacion_FFL_C4["Estados_estacionarios_ARNm"][i][-1])

estado_estacionario_ARNm_X_C1 = []
estado_estacionario_ARNm_X_C2 = []
estado_estacionario_ARNm_X_C3 = []
estado_estacionario_ARNm_X_C4 = []

for i in range(len(simulacion_FFL_C1["Estados_estacionarios_proteina"])):
    estado_estacionario_ARNm_X_C1.append(simulacion_FFL_C1["Estados_estacionarios_ARNm"][i][0])
    estado_estacionario_ARNm_X_C2.append(simulacion_FFL_C2["Estados_estacionarios_ARNm"][i][0])
    estado_estacionario_ARNm_X_C3.append(simulacion_FFL_C3["Estados_estacionarios_ARNm"][i][0])
    estado_estacionario_ARNm_X_C4.append(simulacion_FFL_C4["Estados_estacionarios_ARNm"][i][0])

estado_estacionario_ARNm_Y_C1 = []
estado_estacionario_ARNm_Y_C2 = []
estado_estacionario_ARNm_Y_C3 = []
estado_estacionario_ARNm_Y_C4 = []

for i in range(len(simulacion_FFL_C1["Estados_estacionarios_proteina"])):
    estado_estacionario_ARNm_Y_C1.append(simulacion_FFL_C1["Estados_estacionarios_ARNm"][i][1])
    estado_estacionario_ARNm_Y_C2.append(simulacion_FFL_C2["Estados_estacionarios_ARNm"][i][1])
    estado_estacionario_ARNm_Y_C3.append(simulacion_FFL_C3["Estados_estacionarios_ARNm"][i][1])
    estado_estacionario_ARNm_Y_C4.append(simulacion_FFL_C4["Estados_estacionarios_ARNm"][i][1])
# %%
plt.figure(figsize=(10,6))
plt.title("Comportamiento ARNm X estacionaria")
plt.scatter(posiciones,estado_estacionario_ARNm_X_C1, label = "FFL C1")
plt.scatter(posiciones,estado_estacionario_ARNm_X_C2, label = "FFL C2")
plt.scatter(posiciones,estado_estacionario_ARNm_X_C3, label = "FFL C3")
plt.scatter(posiciones,estado_estacionario_ARNm_X_C4, label = "FFL C4")
plt.ylabel("Valor estacionario de ARNm X")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
#plt.savefig("Comparación_ARNm_X_C1C4.jpg", dpi = 500)
# %%
plt.figure(figsize=(10,6))
plt.title("Comportamiento ARNm Y estacionaria")
plt.scatter(posiciones,estado_estacionario_ARNm_Y_C1, label = "FFL C1")
plt.scatter(posiciones,estado_estacionario_ARNm_Y_C2, label = "FFL C2")
plt.scatter(posiciones,estado_estacionario_ARNm_Y_C3, label = "FFL C3")
plt.scatter(posiciones,estado_estacionario_ARNm_Y_C4, label = "FFL C4")
plt.legend()
plt.ylabel("Valor estacionario de ARNm Y")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
#plt.savefig("Comparación_ARNm_Y_C1C4.jpg", dpi = 500)
# %%
plt.figure(figsize=(8,6))
plt.title("Comportamiento ARNm Z estacionaria")
plt.scatter(posiciones,estado_estacionario_ARNm_Z_C1, label = "FFL C1", color = "red", marker = "*")
plt.scatter(posiciones,estado_estacionario_ARNm_Z_C2, label = "FFL C2", color = "red")
plt.scatter(posiciones,estado_estacionario_ARNm_Z_C3, label = "FFL C3", color = "green", marker = "*")
plt.scatter(posiciones,estado_estacionario_ARNm_Z_C4, label = "FFL C4", color = "green")
plt.legend()
plt.ylabel("Valor estacionario de ARNm Z")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
#plt.savefig("Comparación_ARNm_Z_C1C4.jpg", dpi = 500)

# %%
plt.figure(figsize=(8,6))
plt.title("Comportamiento proteina Z estacionaria coherentes")
plt.scatter(posiciones,np.array(estado_estacionario_Z_C1), label = "FFL C1", color = "red", marker = "*")
plt.scatter(posiciones,np.array(estado_estacionario_Z_C2), label = "FFL C2", color = "red")
plt.scatter(posiciones,np.array(estado_estacionario_Z_C3), label = "FFL C3", color = "green", marker = "*")
plt.scatter(posiciones,np.array(estado_estacionario_Z_C4), label = "FFL C4", color = "green")
plt.legend()
plt.xlabel(r"Valor de $K_x$")
plt.ylabel(r"Proteina Z en estacionario$")
plt.savefig("Proteina_Z_FFL_coherentes.jpg", dpi = 500)
#%%
plt.figure(figsize=(8,6))
plt.title("Comportamiento proteina Y estacionaria coherentes")
plt.scatter(posiciones,np.array(estado_estacionario_Y_C1), label = "FFL C1", color = "red", marker = "*")
plt.scatter(posiciones,np.array(estado_estacionario_Y_C3), label = "FFL C3", color = "red")
plt.scatter(posiciones,np.array(estado_estacionario_Y_C2), label = "FFL C2", color = "green")
plt.scatter(posiciones,np.array(estado_estacionario_Y_C4), label = "FFL C4", color = "green", marker = "*")
plt.legend()
plt.xlabel(r"Valor de $K_x$")
plt.ylabel(r"Proteina Y en estacionario")
plt.savefig("Proteina_Y_FFL_coherentes.jpg", dpi = 500)
#%%
plt.figure(figsize=(8,6))
plt.title("Comportamiento proteinas Y+Z estacionaria coherentes")
plt.scatter(posiciones,np.array(estado_estacionario_Y_C1) + np.array(estado_estacionario_Z_C1), label = "FFL C1", color = "red")
plt.scatter(posiciones, np.array(estado_estacionario_Y_C2) + np.array(estado_estacionario_Z_C2), label = "FFL C2", color = "orange")
plt.scatter(posiciones,np.array(estado_estacionario_Y_C3) + np.array(estado_estacionario_Z_C3), label = "FFL C3", color = "green")
plt.scatter(posiciones,np.array(estado_estacionario_Y_C4) + np.array(estado_estacionario_Z_C4), label = "FFL C4", color = "blue")
plt.legend()
plt.xlabel(r"Valor de $K_x$")
plt.ylabel(r"Proteina Y en estacionario")
plt.savefig("Proteina_ZY_FFL_coherentes.jpg", dpi = 500)
# %%
plt.figure(figsize=(8,5))
plt.title("Comparacion C1 y C4 fraccion Z estacionaria")
plt.scatter(posiciones,(np.array(estado_estacionario_ARNm_Z_C1) +np.array(estado_estacionario_Z_C1))/(np.array(estado_estacionario_ARNm_Z_C4) +np.array(estado_estacionario_Z_C4)))
plt.ylim(0.85,1.1)
plt.axhline(y = 1, color = "red")
plt.legend()
plt.ylabel(r"Fraccion $\frac{[C1]}{[C4]}$")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
plt.savefig("Comparación_fraccion_proteina_ARNM_C1C4.jpg", dpi = 500)
# %%
plt.figure(figsize=(8,5))
plt.title("Comparacion C2 y C3 fraccion Z estacionaria")
plt.scatter(posiciones,(np.array(estado_estacionario_ARNm_Z_C2) +np.array(estado_estacionario_Z_C2))/(np.array(estado_estacionario_ARNm_Z_C3) +np.array(estado_estacionario_Z_C3)))
plt.ylim(0.85,1.1)
plt.axhline(y = 1, color = "red")
plt.legend()
plt.ylabel(r"Fraccion $\frac{[C2]}{[C3]}$")
plt.xlabel(r"Valor de $K_x$")
plt.legend()
plt.savefig("Comparación_fraccion_proteina_ARNM_C2C3.jpg", dpi = 500)
# %%
total_proteina_C1 = np.array(estado_estacionario_Y_C1) + np.array(estado_estacionario_Z_C1)
total_proteina_C2 = np.array(estado_estacionario_Y_C2) + np.array(estado_estacionario_Z_C2)
total_proteina_C3 = np.array(estado_estacionario_Y_C3) + np.array(estado_estacionario_Z_C3)
total_proteina_C4 = np.array(estado_estacionario_Y_C4) + np.array(estado_estacionario_Z_C4)
# %%
plt.title("Comportamiento proteina Y estacionaria")
plt.scatter(posiciones,total_proteina_C1, label = "FFL C1")
#plt.scatter(posiciones,total_proteina_C2, label = "FFL C2")
#plt.scatter(posiciones,total_proteina_C3, label = "FFL C3")
plt.scatter(posiciones,total_proteina_C4, label = "FFL C4")
plt.legend()
#%%
plt.title("Comportamiento proteina Y estacionaria")
#plt.scatter(posiciones,total_proteina_C1, label = "FFL C1")
plt.scatter(posiciones,total_proteina_C2, label = "FFL C2")
plt.scatter(posiciones,total_proteina_C3, label = "FFL C3")
#plt.scatter(posiciones,total_proteina_C4, label = "FFL C4")
plt.legend()
# %%
total_proteina_C1
# %%
fraccion = total_proteina_C4/total_proteina_C1
# %%
plt.scatter(posiciones, fraccion)

# %%
plt.scatter(posiciones, fraccion-1)
plt.axhline(y=0, color = "red")
# %%
total_proteina_C1 = np.array(estado_estacionario_Y_C1) + np.array(estado_estacionario_Z_C1)
informacion_final_C1 = np.array(simulacion_FFL_C1["InformacionZXY"])
costo_informacion_C1 = informacion_final_C1*total_proteina_C1
# %%
total_proteina_C4 = np.array(estado_estacionario_Y_C4) + np.array(estado_estacionario_Z_C4)
informacion_final_C4 = np.array(simulacion_FFL_C4["InformacionZXY"])
costo_informacion_C4 = informacion_final_C4*total_proteina_C4

# %%
plt.title("Comportamiento fraccion Z estacionaria")
plt.scatter(posiciones,costo_informacion_C1, label = "FFL C1")
plt.scatter(posiciones,costo_informacion_C4, label = "FFL C4")
plt.legend()
# %%
informacion_final_C1
# %%
informacion_final_C4
# %%
total_proteina_C1
# %%
total_proteina_C4
# %%
plt.title("Comportamiento fraccion Z estacionaria")
plt.scatter(posiciones,informacion_final_C1, label = "FFL C1")
plt.scatter(posiciones,informacion_final_C4, label = "FFL C4")
plt.legend()
# %%
