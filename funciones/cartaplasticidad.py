#Importando librerias 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Se grafica la carta de plasticidad en las siguientes lineas
def cartaDePlasticidad():
    # Linea Limite liquido = 50%
    x = [50,50]
    y = [0,60]

    #Se grafica la Linea A
    Linea_A = pd.DataFrame({'LL': (20,100),'LP': (0,58.4)})  #IP = 0.73(LL-20)

    #Se grafica la Linea u
    Linea_u = pd.DataFrame({'LL': (8,85.78),'LP': (0,70)})  #IP = 0.9(LL-8)

    #Se grafica la Linea Horizontal Superior
    Linea_h_Superior = pd.DataFrame({'LL': (7,29.6),'LP': (7,7)})

    #Se grafica la Linea Horizontal Inferior
    Linea_h_Inferior = pd.DataFrame({'LL': (4,25.5),'LP': (4,4)})
    # Se imprimen todas las lineas en una grafica "plot lines"

    print("--------------------------------------------------- ")
    plt.plot(x, y, label = "LL = 50%", color='red')  #Linea LL=50%
    #plt.plot(Ll, LP, marker='o')   #Grafica el punto ingresado por el usuario
    plt.plot('LL', 'LP', data=Linea_h_Superior, linestyle='--', label = "CL-ML") #Grafica la linea horizontal superior
    plt.plot('LL', 'LP', data=Linea_h_Inferior, linestyle='--', label = "CL-ML") #Grafica la linea horizontal inferior
    plt.plot('LL', 'LP', data=Linea_A, linestyle='-', label = "Linea A", color='red') #Grafica la linea A 
    plt.plot('LL', 'LP', data=Linea_u, linestyle=':', label = "Linea U", color='gray') #Grafica la linea U
    '''plt.plot('LL', 'LP', data=Linea_B, linestyle='-.', label = "Linea B", color='darkblue') #Grafica la linea B'''
    plt.legend() 
    plt.grid(color='darkblue', ls = ':', lw = 0.6)   #Define caracteristicas de la grilla
    plt.title("CARTA DE PLASTICIDAD",fontsize=15)    #Define caracteristicas del titulo
    plt.xlabel("Limite liquido LL",fontsize=10)      #Define caracteristicas del eje x
    plt.ylabel("Limite Plastico LP",fontsize=10)      #Define caracteristicas del eje y
    plt.show()