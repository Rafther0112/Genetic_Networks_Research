#%%
import numpy as np
import matplotlib.pyplot as plt
import csv
#%%

with open('datos_FFL_C1.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    datos_FFL_C1 = list(lector)

with open('datos_FFL_C2.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    datos_FFL_C2 = list(lector)

with open('datos_FFL_C3.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    datos_FFL_C3 = list(lector)

with open('datos_FFL_C4.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    datos_FFL_C4 = list(lector)

with open('datos_FFL_I1.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    datos_FFL_I1 = list(lector)

with open('datos_FFL_I2.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    datos_FFL_I2 = list(lector)

with open('datos_FFL_I3.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    datos_FFL_I3 = list(lector)

with open('datos_FFL_I4.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    datos_FFL_I4 = list(lector)
# %%
simulacion_FFL_C1 = np.load('diccionario_FFL_C1.npy', allow_pickle=True).item()
simulacion_FFL_C2 = np.load('diccionario_FFL_C2.npy', allow_pickle=True).item()
simulacion_FFL_C3 = np.load('diccionario_FFL_C3.npy', allow_pickle=True).item()
simulacion_FFL_C4 = np.load('diccionario_FFL_C4.npy', allow_pickle=True).item()

simulacion_FFL_I1 = np.load('diccionario_FFL_I1.npy', allow_pickle=True).item()
simulacion_FFL_I2 = np.load('diccionario_FFL_I2.npy', allow_pickle=True).item()
simulacion_FFL_I3 = np.load('diccionario_FFL_I3.npy', allow_pickle=True).item()
simulacion_FFL_I4 = np.load('diccionario_FFL_I4.npy', allow_pickle=True).item()

# %%
datos_teoricos_FFL_C1 = []
for tipo in datos_FFL_C1:
    valores_tipo = []
    for valor in tipo:
        dato = float(valor)
        valores_tipo.append(dato)
    datos_teoricos_FFL_C1.append(valores_tipo)

datos_teoricos_FFL_C2 = []
for tipo in datos_FFL_C2:
    valores_tipo = []
    for valor in tipo:
        dato = float(valor)
        valores_tipo.append(dato)
    datos_teoricos_FFL_C2.append(valores_tipo)

datos_teoricos_FFL_C3 = []
for tipo in datos_FFL_C3:
    valores_tipo = []
    for valor in tipo:
        dato = float(valor)
        valores_tipo.append(dato)
    datos_teoricos_FFL_C3.append(valores_tipo)

datos_teoricos_FFL_C4 = []
for tipo in datos_FFL_C4:
    valores_tipo = []
    for valor in tipo:
        dato = float(valor)
        valores_tipo.append(dato)
    datos_teoricos_FFL_C4.append(valores_tipo)

datos_teoricos_FFL_I1 = []
for tipo in datos_FFL_I1:
    valores_tipo = []
    for valor in tipo:
        dato = float(valor)
        valores_tipo.append(dato)
    datos_teoricos_FFL_I1.append(valores_tipo)

datos_teoricos_FFL_I2 = []
for tipo in datos_FFL_I2:
    valores_tipo = []
    for valor in tipo:
        dato = float(valor)
        valores_tipo.append(dato)
    datos_teoricos_FFL_I2.append(valores_tipo)

datos_teoricos_FFL_I3 = []
for tipo in datos_FFL_I3:
    valores_tipo = []
    for valor in tipo:
        dato = float(valor)
        valores_tipo.append(dato)
    datos_teoricos_FFL_I3.append(valores_tipo)

datos_teoricos_FFL_I4 = []
for tipo in datos_FFL_I4:
    valores_tipo = []
    for valor in tipo:
        dato = float(valor)
        valores_tipo.append(dato)
    datos_teoricos_FFL_I4.append(valores_tipo)

# %%
print(simulacion_FFL_C1["InformacionYX"])
#%%
comportamiento , figuras = plt.subplots(2, 2)
comportamiento.suptitle("Análisis de información FFL C1",fontweight ="bold", fontsize = 16)
comportamiento.set_figheight(7)
comportamiento.set_figwidth(11)
figuras[0,0].set_title("Información mutua I(Y;X) en función de tasa Kx")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_C1[0][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(0,10), simulacion_FFL_C1["InformacionYX"], color = "red", label ="Simulacion Computacional", marker = "*")

figuras[0,0].set_ylabel("Información mutua", fontsize = 16)
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X) en función de tasa Kx")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_C1[1][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(0,10), simulacion_FFL_C1["InformacionZX"], color = "red", label ="Simulacion Computacional", marker = "*")

figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;Y) en función de tasa Kx")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_C1[2][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(0,10), simulacion_FFL_C1["InformacionZY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx", fontsize = 16)
figuras[1,0].set_ylabel("Información mutua", fontsize = 16)
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) en función de tasa Kx")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_C1[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(0,10), simulacion_FFL_C1["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")

figuras[1,1].set_xlabel("Tasa de sintesis Kx", fontsize = 16)
figuras[1,1].legend()
comportamiento.tight_layout()
#comportamiento.savefig("Informacion_FFL_C1.png", dpi = 500)
# %%
comportamiento , figuras = plt.subplots(2, 2)
comportamiento.suptitle("Análisis de información FFL C2",fontweight ="bold")
comportamiento.set_figheight(10)
comportamiento.set_figwidth(15)
figuras[0,0].set_title("Información mutua I(Y;X) en función de tasa Kx")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_C2[0][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(0,10), simulacion_FFL_C2["InformacionYX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,0].set_xlabel("Tasa de sintesis Kx")
figuras[0,0].set_ylabel("Información mutua")
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X) en función de tasa Kx")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_C2[1][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(0,10), simulacion_FFL_C2["InformacionZX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,1].set_xlabel("Tasa de sintesis Kx")
figuras[0,1].set_ylabel("Información mutua")
figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;Y) en función de tasa Kx")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_C2[2][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(0,10), simulacion_FFL_C2["InformacionZY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx")
figuras[1,0].set_ylabel("Información mutua")
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) en función de tasa Kx")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_C2[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(0,10), simulacion_FFL_C2["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,1].set_xlabel("Tasa de sintesis Kx")
figuras[1,1].set_ylabel("Información mutua")
figuras[1,1].legend()

#comportamiento.savefig("Informacion_FFL_C2.jpg", dpi = 500)

#%%
comportamiento , figuras = plt.subplots(2, 2)
comportamiento.suptitle("Análisis de información FFL C3",fontweight ="bold")
comportamiento.set_figheight(10)
comportamiento.set_figwidth(15)
figuras[0,0].set_title("Información mutua I(Y;X) en función de tasa Kx")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_C3[0][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(0,10), simulacion_FFL_C3["InformacionYX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,0].set_xlabel("Tasa de sintesis Kx")
figuras[0,0].set_ylabel("Información mutua")
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X) en función de tasa Kx")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_C3[1][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(0,10), simulacion_FFL_C3["InformacionZX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,1].set_xlabel("Tasa de sintesis Kx")
figuras[0,1].set_ylabel("Información mutua")
figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;Y) en función de tasa Kx")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_C3[2][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(0,10), simulacion_FFL_C3["InformacionZY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx")
figuras[1,0].set_ylabel("Información mutua")
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) en función de tasa Kx")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_C3[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(0,10), simulacion_FFL_C3["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,1].set_xlabel("Tasa de sintesis Kx")
figuras[1,1].set_ylabel("Información mutua")
figuras[1,1].legend()

#comportamiento.savefig("Informacion_FFL_C3.jpg", dpi = 500)

# %%
comportamiento , figuras = plt.subplots(2, 2)
comportamiento.suptitle("Análisis de información FFL C4",fontweight ="bold")
comportamiento.set_figheight(10)
comportamiento.set_figwidth(15)
figuras[0,0].set_title("Información mutua I(Y;X) en función de tasa Kx")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_C4[0][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(1,10), simulacion_FFL_C4["InformacionYX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,0].set_xlabel("Tasa de sintesis Kx")
figuras[0,0].set_ylabel("Información mutua")
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X) en función de tasa Kx")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_C4[1][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(1,10), simulacion_FFL_C4["InformacionZX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,1].set_xlabel("Tasa de sintesis Kx")
figuras[0,1].set_ylabel("Información mutua")
figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;Y) en función de tasa Kx")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_C4[2][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(1,10), simulacion_FFL_C4["InformacionZY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx")
figuras[1,0].set_ylabel("Información mutua")
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) en función de tasa Kx")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_C4[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(1,10), simulacion_FFL_C4["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,1].set_xlabel("Tasa de sintesis Kx")
figuras[1,1].set_ylabel("Información mutua")
figuras[1,1].legend()

#comportamiento.savefig("Informacion_FFL_C4.jpg", dpi = 500)

# %%
# %%
comportamiento , figuras = plt.subplots(2, 2)
comportamiento.suptitle("Análisis de información FFL I1",fontweight ="bold")
comportamiento.set_figheight(10)
comportamiento.set_figwidth(15)
figuras[0,0].set_title("Información mutua I(Y;X) en función de tasa Kx")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_I1[0][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(1,10), simulacion_FFL_I1["InformacionYX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,0].set_xlabel("Tasa de sintesis Kx")
figuras[0,0].set_ylabel("Información mutua")
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X) en función de tasa Kx")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_I1[1][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(1,10), simulacion_FFL_I1["InformacionZX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,1].set_xlabel("Tasa de sintesis Kx")
figuras[0,1].set_ylabel("Información mutua")
figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;Y) en función de tasa Kx")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_I1[2][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(1,10), simulacion_FFL_I1["InformacionZY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx")
figuras[1,0].set_ylabel("Información mutua")
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) en función de tasa Kx")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_I1[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(1,10), simulacion_FFL_I1["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,1].set_xlabel("Tasa de sintesis Kx")
figuras[1,1].set_ylabel("Información mutua")
figuras[1,1].legend()

comportamiento.savefig("Informacion_FFL_I1.jpg", dpi = 500)
# %%

comportamiento , figuras = plt.subplots(2, 2)
comportamiento.suptitle("Análisis de información FFL I2",fontweight ="bold")
comportamiento.set_figheight(10)
comportamiento.set_figwidth(15)
figuras[0,0].set_title("Información mutua I(Y;X) en función de tasa Kx")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_I2[0][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(1,9), simulacion_FFL_I2["InformacionYX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,0].set_xlabel("Tasa de sintesis Kx")
figuras[0,0].set_ylabel("Información mutua")
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X) en función de tasa Kx")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_I2[1][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(1,9), simulacion_FFL_I2["InformacionZX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,1].set_xlabel("Tasa de sintesis Kx")
figuras[0,1].set_ylabel("Información mutua")
figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;Y) en función de tasa Kx")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_I2[2][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(1,9), simulacion_FFL_I2["InformacionZY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx")
figuras[1,0].set_ylabel("Información mutua")
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) en función de tasa Kx")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_I2[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(1,9), simulacion_FFL_I2["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,1].set_xlabel("Tasa de sintesis Kx")
figuras[1,1].set_ylabel("Información mutua")
figuras[1,1].legend()

comportamiento.savefig("Informacion_FFL_I2.jpg", dpi = 500)

# %%
comportamiento , figuras = plt.subplots(2, 2)
comportamiento.suptitle("Análisis de información FFL I3",fontweight ="bold")
comportamiento.set_figheight(10)
comportamiento.set_figwidth(15)
figuras[0,0].set_title("Información mutua I(Y;X) en función de tasa Kx")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_I3[0][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(1,9), simulacion_FFL_I3["InformacionYX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,0].set_xlabel("Tasa de sintesis Kx")
figuras[0,0].set_ylabel("Información mutua")
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X) en función de tasa Kx")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_I3[1][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(1,9), simulacion_FFL_I3["InformacionZX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,1].set_xlabel("Tasa de sintesis Kx")
figuras[0,1].set_ylabel("Información mutua")
figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;Y) en función de tasa Kx")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_I3[2][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(1,9), simulacion_FFL_I3["InformacionZY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx")
figuras[1,0].set_ylabel("Información mutua")
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) en función de tasa Kx")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_I3[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(1,9), simulacion_FFL_I3["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,1].set_xlabel("Tasa de sintesis Kx")
figuras[1,1].set_ylabel("Información mutua")
figuras[1,1].legend()

comportamiento.savefig("Informacion_FFL_I3.jpg", dpi = 500)

# %%
comportamiento , figuras = plt.subplots(2, 2)
comportamiento.suptitle("Análisis de información FFL I4",fontweight ="bold")
comportamiento.set_figheight(10)
comportamiento.set_figwidth(15)
figuras[0,0].set_title("Información mutua I(Y;X) en función de tasa Kx")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_I4[0][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(1,9), simulacion_FFL_I4["InformacionYX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,0].set_xlabel("Tasa de sintesis Kx")
figuras[0,0].set_ylabel("Información mutua")
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X) en función de tasa Kx")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_I4[1][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(1,9), simulacion_FFL_I4["InformacionZX"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,1].set_xlabel("Tasa de sintesis Kx")
figuras[0,1].set_ylabel("Información mutua")
figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;Y) en función de tasa Kx")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_I4[2][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(1,9), simulacion_FFL_I4["InformacionZY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx")
figuras[1,0].set_ylabel("Información mutua")
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) en función de tasa Kx")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_I4[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(1,9), simulacion_FFL_I4["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,1].set_xlabel("Tasa de sintesis Kx")
figuras[1,1].set_ylabel("Información mutua")
figuras[1,1].legend()

comportamiento.savefig("Informacion_FFL_I4.jpg", dpi = 500)

# %%
comportamiento , figuras = plt.subplots(4, 2)
comportamiento.suptitle("Análisis de información mutua I(Z;X,Y) FFL",fontweight ="bold")
comportamiento.set_figheight(15)
comportamiento.set_figwidth(15)
figuras[0,0].set_title("Información mutua I(Z;X,Y) FFL_C1")
figuras[0,0].plot(np.arange(0,20), datos_teoricos_FFL_C1[3][0:20], label = "Solucion teorica")
figuras[0,0].scatter(np.arange(0,10), simulacion_FFL_C1["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,0].set_xlabel("Tasa de sintesis Kx")
figuras[0,0].set_ylabel("Información mutua")
figuras[0,0].legend()

figuras[0,1].set_title("Información mutua I(Z;X,Y) FFL_C4")
figuras[0,1].plot(np.arange(0,20), datos_teoricos_FFL_C4[3][0:20], label = "Solucion teorica")
figuras[0,1].scatter(np.arange(0,10), simulacion_FFL_C4["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[0,1].set_xlabel("Tasa de sintesis Kx")
figuras[0,1].set_ylabel("Información mutua")
figuras[0,1].legend()


figuras[1,0].set_title("Información mutua I(Z;X,Y) FFL_C2")
figuras[1,0].plot(np.arange(0,20), datos_teoricos_FFL_C2[3][0:20], label = "Solucion teorica")
figuras[1,0].scatter(np.arange(0,10), simulacion_FFL_C2["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,0].set_xlabel("Tasa de sintesis Kx")
figuras[1,0].set_ylabel("Información mutua")
figuras[1,0].legend()

figuras[1,1].set_title("Información mutua I(Z;X,Y) FFL_C3")
figuras[1,1].plot(np.arange(0,20), datos_teoricos_FFL_C3[3][0:20], label = "Solucion teorica")
figuras[1,1].scatter(np.arange(0,10), simulacion_FFL_C3["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[1,1].set_xlabel("Tasa de sintesis Kx")
figuras[1,1].set_ylabel("Información mutua")
figuras[1,1].legend()

figuras[2,0].set_title("Información mutua I(Z;X,Y) FFL_I1")
figuras[2,0].plot(np.arange(0,20), datos_teoricos_FFL_I1[3][0:20], label = "Solucion teorica")
figuras[2,0].scatter(np.arange(0,10), simulacion_FFL_I1["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[2,0].set_xlabel("Tasa de sintesis Kx")
figuras[2,0].set_ylabel("Información mutua")
figuras[2,0].legend()

figuras[2,1].set_title("Información mutua I(Z;X,Y) FFL_I2")
figuras[2,1].plot(np.arange(0,20), datos_teoricos_FFL_I2[3][0:20], label = "Solucion teorica")
figuras[2,1].scatter(np.arange(0,10), simulacion_FFL_I2["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[2,1].set_xlabel("Tasa de sintesis Kx")
figuras[2,1].set_ylabel("Información mutua")
figuras[2,1].legend()

figuras[3,0].set_title("Información mutua I(Z;X,Y) FFL_I3")
figuras[3,0].plot(np.arange(0,20), datos_teoricos_FFL_I3[3][0:20], label = "Solucion teorica")
#figuras[3,0].scatter(np.arange(1,9), simulacion_FFL_I3["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[3,0].set_xlabel("Tasa de sintesis Kx")
figuras[3,0].set_ylabel("Información mutua")
figuras[3,0].legend()

figuras[3,1].set_title("Información mutua I(Z;X,Y) FFL_I3")
figuras[3,1].plot(np.arange(0,20), datos_teoricos_FFL_I3[3][0:20], label = "Solucion teorica")
#figuras[3,1].scatter(np.arange(1,9), simulacion_FFL_I3["InformacionZXY"], color = "red", label ="Simulacion Computacional", marker = "*")
figuras[3,1].set_xlabel("Tasa de sintesis Kx")
figuras[3,1].set_ylabel("Información mutua")
figuras[3,1].legend()

comportamiento.tight_layout()
#comportamiento.savefig("Informacion_FFL_ZXY.jpg", dpi = 1000)
# %%
len(simulacion_FFL_I3["InformacionZXY"])
# %%
comportamiento , figuras = plt.subplots(1,2)
comportamiento.suptitle("Análisis de información FFL n = 2",fontweight ="bold")
comportamiento.set_figheight(3)
comportamiento.set_figwidth(11)
figuras[0].set_title("Información mutua I(Z;Y,X) en función de tasa Kx FFL C")

figuras[0].plot(np.arange(0,35), datos_teoricos_FFL_C1[3][0:35],"-.." ,label = "FFL C1", color = "red")
figuras[0].scatter(np.arange(1,len(simulacion_FFL_C1["InformacionZXY"])+1), simulacion_FFL_C1["InformacionZXY"], color = "red", marker = "v", alpha = 0.4)

figuras[0].plot(np.arange(0,35), datos_teoricos_FFL_C4[3][0:35],"--", label = "FFL C4", color = "blue")
figuras[0].scatter(np.arange(1,len(simulacion_FFL_C4["InformacionZXY"])+1), simulacion_FFL_C4["InformacionZXY"], color = "blue", marker = "^", alpha = 0.4)


figuras[0].plot(np.arange(0,35), datos_teoricos_FFL_C2[3][0:35],"-..", label = "FFL C2", color ="tomato")
figuras[0].scatter(np.arange(1,len(simulacion_FFL_C2["InformacionZXY"])+1), simulacion_FFL_C2["InformacionZXY"], color = "tomato", marker = "v", alpha = 0.4)

figuras[0].plot(np.arange(0,35), datos_teoricos_FFL_C3[3][0:35],"--",  label = "FFL C3", color = "green")
figuras[0].scatter(np.arange(1,len(simulacion_FFL_C3["InformacionZXY"])+1), simulacion_FFL_C3["InformacionZXY"], color = "green", marker = "^", alpha = 0.4)


figuras[1].set_title("Información mutua I(Z;Y,X) en función de tasa Kx FFL I")

figuras[1].plot(np.arange(0,35), datos_teoricos_FFL_I1[3][0:35],"-.." ,label = "FFL I1", color = "red")
figuras[1].scatter(np.arange(1,len(simulacion_FFL_I1["InformacionZXY"])+1), simulacion_FFL_I1["InformacionZXY"], color = "red", marker = "v", alpha = 0.4)

figuras[1].plot(np.arange(0,35), datos_teoricos_FFL_I2[3][0:35],"-..", label = "FFL I2", color ="blue")
figuras[1].scatter(np.arange(1,len(simulacion_FFL_I2["InformacionZXY"])+1), simulacion_FFL_I2["InformacionZXY"], color = "blue", marker = "v", alpha = 0.4)


figuras[1].plot(np.arange(0,35), datos_teoricos_FFL_I4[3][0:35],"--", label = "FFL I4", color = "tomato")
figuras[1].scatter(np.arange(1,len(simulacion_FFL_I4["InformacionZXY"])+1), simulacion_FFL_I4["InformacionZXY"], color = "tomato", marker = "^", alpha = 0.4)

figuras[1].plot(np.arange(0,35), datos_teoricos_FFL_I3[3][0:35],"--",  label = "FFL I3", color = "green")
figuras[1].scatter(np.arange(1,len(simulacion_FFL_I3["InformacionZXY"])+1), simulacion_FFL_I3["InformacionZXY"], color = "green", marker = "^", alpha = 0.4)
figuras[1].legend()

figuras[0].set_xlabel("Tasa de sintesis Kx", fontsize = 16)
figuras[0].set_ylabel("Información mutua", fontsize = 14)

figuras[1].set_xlabel("Tasa de sintesis Kx", fontsize = 16)


figuras[1].axis(ymin=0.0,ymax=0.35)
figuras[0].legend()
figuras[1].legend()
comportamiento.tight_layout()
#comportamiento.savefig("FFL_information_ZXY_hill2_pequeñas.png", dpi = 500)

# %%
