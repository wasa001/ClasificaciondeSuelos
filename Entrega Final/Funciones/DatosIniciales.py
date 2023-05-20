#Importando librerias 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

'-------------------------------------------------------------------------'

#Introduce valores iniciales
Ll = 15                        #Captura el valor del Limite Liquido
LP= 10                    #Captura el valor del Indice de Plasticidad
IP = Ll - LP 

'-------------------------------------------------------------------------'
#POR FAVOR MODIFIQUE SU GRANULOMETRIA
Pasa =pd.Series([
    100,   #Tamiz 1 1/2"
    100,  #Tamiz 1"
    98,  #Tamiz 3/4"
    95,   #Tamiz 3/8"
    80,  #Tamiz Nº 4
    60,   #Tamiz Nº 10
    42,  #Tamiz Nº 30
    28, #Tamiz Nº 40
    15,  #Tamiz Nº 50
    13,   #Tamiz Nº 100
    8,  #Tamiz Nº 200
])
Tamiz = pd.Series(['1 1/2"', '1"', '3/4"', '3/8"', 'Nº 4', 'Nº 10', 'Nº 30',  'Nº 40', 'Nº 50', 'Nº 100', 'Nº 200']) #Define la lista de tamises
Apertura =pd.Series([37.5, 25.4, 19.1, 9.5, 4.75, 1.9, 0.85, 0.425, 0.25, 0.15, 0.074]) #Define la lista de tamices en mm

Estructura = pd.DataFrame({'Tamiz':Tamiz, 'Apertura' : Apertura, 'Pasa' : Pasa})

# Imprime la granulometria.
print("--------------------------------------------------- ")
print(Estructura)  #Deveulve la tabla de datos para la granulometria
print("--------------------------------------------------- ")


'-------------------------------------------------------------------------'
#D60, D30, D10
f = interp1d(Pasa, Apertura) #Realiza la funcion para determinar los valores de X y Y

#valores de entrada
y1_coord = 60
y2_coord = 30
y3_coord = 10

#Realiza interpolación
x1_coord = f(y1_coord)
x2_coord = f(y2_coord)
x3_coord = f(y3_coord)

#Calculo del Cofeiciente de curvatura y del Coeficiente de uniformidad.
Cc= (x2_coord**2)/(x1_coord*x3_coord)       
Cu= (x1_coord)/(x3_coord)  
