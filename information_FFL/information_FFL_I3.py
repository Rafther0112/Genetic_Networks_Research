import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from numba import jit,njit,float64,int32
import numba as nb
import pandas as pd

Kpx = 200            #Tasa de creacion de proteina X
Kpy = 300            #Tasa de creacion de proteina Y
Kpz = 100            #Tasa de creacion de proteina Z

Hill = 2            #Coeficiente de Hill

gammamx = 1/5        #Tasa de degradacion de ARNmX
gammamy = 1/7        #Tasa de degradacion de ARNmY
gammamz = 1/10        #Tasa de degradacion de ARNmZ

muX     =1/20            #Tasa de degradacion de proteina X
muY     =1/40            #Tasa de degradacion de proteina Y
muZ     =1/30            #Tasa de degradacion de proteina Z

My = 10
Mz = 25

matrices_covarianza_XYZ = []

variacion_informacion_YX = []
variacion_informacion_ZX = []
variacion_informacion_ZY = []
variacion_informacion_ZXY = []

estado_estacionario_ARNm = []
estado_estacionario_proteina = []

for Kx in [1,2,3,4,5,6,7,8,9,10]:
    
    Mx = Kx/gammamx
    valor_X_estacionario = (Kpx/muX)*Mx

    valor_Y_estacionario = (Kpy/muY)*My
    valor_Z_estacionario = (Kpz/muZ)*Mz


    Kxy  = valor_X_estacionario        #Coeficiente de interaccion proteina X con ARNmY
    Kxz  = valor_X_estacionario         #Coeficiente de interaccion proteina X con ARNmZ
    Kyz  = 2*valor_Y_estacionario         #Coeficiente de interaccion proteina Y con ARNmZ

    Ky = (My*gammamy)*(((valor_X_estacionario**Hill) + (Kxy**Hill))/(valor_X_estacionario**Hill))
    Kz = (Mz*gammamz)*( (((valor_Y_estacionario**Hill) + (Kyz**Hill))*((valor_X_estacionario**Hill) + (Kxz **Hill))     )   /  ((valor_Y_estacionario**Hill)*(Kxz**Hill))   )

    @njit
    def funcion_creacion_ARNmX():
        return Kx

    @njit
    def funcion_creacion_ARNmY(cantidad_X):
        return Ky*((cantidad_X**Hill)/(cantidad_X**Hill + Kxy**Hill))

    @njit
    def funcion_creacion_ARNmZ(cantidad_X, cantidad_Y):
        creacion_ARNmZ = Kz*((Kxz**Hill)/(cantidad_X**Hill + Kxz**Hill))*((cantidad_Y**Hill)/(cantidad_Y**Hill + Kyz**Hill))
        return creacion_ARNmZ

    @njit
    def funcion_creacion_X(cantidad_mX):
        return Kpx*cantidad_mX

    @njit
    def funcion_creacion_Y(cantidad_mY):
        return Kpy*cantidad_mY

    @njit
    def funcion_creacion_Z(cantidad_mZ):
        return Kpz*cantidad_mZ

    @njit
    def funcion_degradacion_ARNmX(cantidad_mX):
        return gammamx*cantidad_mX

    @njit
    def funcion_degradacion_ARNmY(cantidad_mY):
        return gammamy*cantidad_mY

    @njit
    def funcion_degradacion_ARNmZ(cantidad_mZ):
        return gammamz*cantidad_mZ

    @njit
    def funcion_degradacion_X(cantidad_X):
        return muX * cantidad_X 

    @njit
    def funcion_degradacion_Y(cantidad_Y):
        return muY * cantidad_Y 

    @njit
    def funcion_degradacion_Z(cantidad_Z):
        return muZ * cantidad_Z 
    
    @njit
    def modelo_constitutivo(cantidad_mX, cantidad_mY, cantidad_mZ, cantidad_X, cantidad_Y,cantidad_Z):

        propensidad_creacion_ARNmX = funcion_creacion_ARNmX()
        propensidad_creacion_ARNmY = funcion_creacion_ARNmY(cantidad_X)
        propensidad_creacion_ARNmZ = funcion_creacion_ARNmZ(cantidad_X, cantidad_Y)

        propensidad_creacion_proteinaX = funcion_creacion_X(cantidad_mX)
        propensidad_creacion_proteinaY = funcion_creacion_Y(cantidad_mY)
        propensidad_creacion_proteinaZ = funcion_creacion_Z(cantidad_mZ)

        propensidad_degradacion_ARNmX = funcion_degradacion_ARNmX(cantidad_mX)
        propensidad_degradacion_ARNmY = funcion_degradacion_ARNmY(cantidad_mY)
        propensidad_degradacion_ARNmZ = funcion_degradacion_ARNmZ(cantidad_mZ)

        propensidad_degradacion_proteinaX = funcion_degradacion_X(cantidad_X)
        propensidad_degradacion_proteinaY = funcion_degradacion_Y(cantidad_Y)
        propensidad_degradacion_proteinaZ = funcion_degradacion_Z(cantidad_Z)

        return propensidad_creacion_ARNmX, propensidad_creacion_ARNmY, propensidad_creacion_ARNmZ, propensidad_creacion_proteinaX, propensidad_creacion_proteinaY, propensidad_creacion_proteinaZ, propensidad_degradacion_ARNmX, propensidad_degradacion_ARNmY, propensidad_degradacion_ARNmZ, propensidad_degradacion_proteinaX, propensidad_degradacion_proteinaY, propensidad_degradacion_proteinaZ
    
    @njit('f8[:](f8[:],f8)')
    def Gillespie(trp0,tmax):

        t,ARNmX, ARNmY, ARNmZ, proteinaX, proteinaY, proteinaZ =trp0 

        while t < tmax:
            s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8, s_9, s_10, s_11, s_12 = modelo_constitutivo(ARNmX, ARNmY, ARNmZ, proteinaX, proteinaY, proteinaZ)
            S_T = s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8 + s_9 + s_10 + s_11 + s_12

            τ = (-1/S_T)*np.log(np.random.rand())
            x = np.random.rand()

            if x <= (s_1)/S_T:
                ARNmX += 1

            elif x<= (s_1 + s_2)/S_T:
                ARNmY += 1
            
            elif x <= (s_1 + s_2 + s_3)/S_T :
                ARNmZ+=1
            
            elif x <= (s_1 + s_2 + s_3 + s_4)/S_T :
                proteinaX+=1
            
            elif x <= (s_1 + s_2 + s_3 + s_4 + s_5)/S_T :
                proteinaY+= 1

            elif x <= (s_1 + s_2 + s_3 + s_4 + s_5 + s_6)/S_T :
                proteinaZ += 1
            
            elif x <= (s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7)/S_T :
                ARNmX-= 1
            
            elif x <= (s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8)/S_T :
                ARNmY-=1

            elif x <= (s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8 + s_9)/S_T :
            
                ARNmZ-= 1

            elif x <= (s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8 + s_9 + s_10)/S_T :

                proteinaX-=1

            elif x <= (s_1 + s_2 + s_3 + s_4 + s_5 + s_6 + s_7 + s_8 + s_9 + s_10 + s_11)/S_T :
                proteinaY-=1

            else: 
                proteinaZ-=1

            t+=τ
        return np.array([t,ARNmX, ARNmY, ARNmZ, proteinaX, proteinaY, proteinaZ]) 
    
    @njit('f8[:,:](f8[:],f8[:])')
    def Estado_celula(X0,tiempos):

        
        X = np.zeros((len(tiempos),len(X0)))
        X[0] = X0
        
        for i in range(1,len(tiempos)):
            X[i] = Gillespie(X[i-1],tiempos[i])
        
        return X
    
    x0 = np.array([0., 0., 0., 0., 0., 0., 0.])

    num_cel = 2000 #número de células 
    celulas = np.array([Estado_celula(x0,np.arange(0.,700.,2.)) for i in tqdm(range(num_cel))])

    celulas_prom = np.mean(celulas,axis=0) #axis = 0 saca el promedio componente a componente de cada célula.
    
    sampling = -200
    ARNmX_estacionario = celulas[:,sampling:,1].flatten()
    ARNmY_estacionario = celulas[:,sampling:,2].flatten()
    ARNmZ_estacionario = celulas[:,sampling:,3].flatten()

    X_estacionario = celulas[:,sampling:,4].flatten()
    Y_estacionario = celulas[:,sampling:,5].flatten()
    Z_estacionario = celulas[:,sampling:,6].flatten()

    estado_estacionario_ARNm.append([np.mean(ARNmX_estacionario), np.mean(ARNmY_estacionario), np.mean(ARNmZ_estacionario)])
    estado_estacionario_proteina.append([np.mean(X_estacionario), np.mean(Y_estacionario), np.mean(Z_estacionario)])

    data = {'X': X_estacionario,
        'Y': Y_estacionario,
        'Z': Z_estacionario}

    df = pd.DataFrame(data)

    cov_matrix = pd.DataFrame.cov(df)
    cov_matrix = np.array(cov_matrix)

    Informacion_Y_X = (1/2)*np.log2((cov_matrix[0][0]* cov_matrix[1][1])/(cov_matrix[0][0]* cov_matrix[1][1] - (cov_matrix[0][1])**2))
    Informacion_Z_X = (1/2)*np.log2((cov_matrix[0][0]* cov_matrix[2][2])/(cov_matrix[0][0]* cov_matrix[2][2] - (cov_matrix[0][2])**2))
    Informacion_Z_Y = (1/2)*np.log2((cov_matrix[1][1]* cov_matrix[2][2])/(cov_matrix[1][1]* cov_matrix[2][2] - (cov_matrix[1][2])**2))
    Informacion_Z_X_Y = (1/2)*np.log2((cov_matrix[0][0]*cov_matrix[1][1]* cov_matrix[2][2] - cov_matrix[0][1]**2)/(np.linalg.det(cov_matrix)))


    matrices_covarianza_XYZ.append(cov_matrix)

    variacion_informacion_YX.append(Informacion_Y_X)
    variacion_informacion_ZX.append(Informacion_Z_X)
    variacion_informacion_ZY.append(Informacion_Z_Y)
    variacion_informacion_ZXY.append(Informacion_Z_X_Y)

    diccionario_respuestas = {"matrices":matrices_covarianza_XYZ, "Estados_estacionarios_ARNm" :estado_estacionario_ARNm, "Estados_estacionarios_proteina" : estado_estacionario_proteina,  "InformacionYX":variacion_informacion_YX, "InformacionZX":variacion_informacion_ZX, "InformacionZY": variacion_informacion_ZY, "InformacionZXY":variacion_informacion_ZXY}
    np.save('diccionario_FFL_I3.npy', diccionario_respuestas)