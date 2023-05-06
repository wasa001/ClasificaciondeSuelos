#Importando librerias 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def Granulometria(): #Se grafica la Granulometria en las siguientes lineas

    pasa = [100,100,88.70,75.65,65.22,60,51.30,42.61,24.78,20.43,3.04]  #Datos para el limite superior
    tamiz = [37.5,25,19,9.5,4.75,2,0.85,0.425,0.25,0.15 ,0.075] #Datos para el limite superior



    print("--------------------------------------------------- ")
    #plt.plot(Estructura['Apertura'],Estructura['Pasa'], label="Su muestra", color='lightgreen') #Grafica la granulometria ingresada
    #plt.scatter(Estructura['Apertura'],Estructura['Pasa'], color='green') #Grafica los puntos de la granulometria ingresada
    plt.scatter(tamiz,pasa, color='orange')      #Grafica los puntos de la linea superior
    plt.plot(tamiz,pasa, label="Linea Superior", color='red')  #Grafica la linea superior de la granulometria
    plt.grid(color='darkblue', ls = ':', lw = 0.6) #Define caracteristicas de la grilla
    plt.xscale("log",base=10)  #Cambia la escala del eje x
    plt.gca().invert_xaxis()  #Modifica el sentido del eje x
    plt.title("GRANULOMETRIA",fontsize=15)    #Define caracteristicas del titulo
    plt.xlabel("% Tamiz en Escala Logarítmica",fontsize=10)      #Define caracteristicas del eje x
    plt.ylabel("% Pasa en Escala Normal",fontsize=10)      #Define caracteristicas del eje
    plt.show()

def GranulometriaFina():
    #valores de entrada
    nombre = [
        "No. 4",
        "No. 10",
        "No. 20",
        "No. 40",
        "No. 60",
        "No. 140",
        "No. 200"
        ]
    abertura = np.array([
        4.750, #No. 4
        2, #No. 10      
        0.850, #No. 20
        0.425,  #No. 40
        0.250, #No. 60
        0.106, #No. 140
        0.075 #No. 200
        ]) 
    pasa = np.array([
        95, #No. 4
        80, #No. 10
        51, #No. 20
        33, #No. 40
        13, #No. 60
        6,  #No. 140
        3 #No. 200
        ]) 

    #Se grafica la línea de la granulometría
    plt.figure(figsize=(14, 4)) 
    plt.plot(abertura,pasa,linestyle='-', marker='o', color='k', fillstyle='none',label='Data') 
    #f = interp1d(pasa, abertura)

    # # #Calcular D60 D50 D30 D10
    # # #valores de entrada
    # y1_coord = 60
    # y2_coord = 30
    # y3_coord = 10
    # # #Realiza interpolación
    # x1_coord = f(y1_coord)
    # x2_coord = f(y2_coord)
    # x3_coord = f(y3_coord)
    # # #Solo toma dos decimales
    # x1_formatted = '{:.2f}'.format(x1_coord)
    # x2_formatted = '{:.2f}'.format(x2_coord)
    # x3_formatted = '{:.2f}'.format(x3_coord)
    # # #Los ubica en el plano
    # plt.scatter(x1_coord, y1_coord, marker='s', s=50, color='k', label='D60='+x1_formatted)
    # plt.scatter(x2_coord, y2_coord, marker='<', s=50, color='k', label='D50='+x2_formatted)
    # plt.scatter(x3_coord, y3_coord, marker='>', s=50, color='k', label='D30='+x3_formatted)

    #Grafica
    plt.title("",fontsize=10)
    plt.xlabel('Diámetro (mm)')
    plt.ylabel('Porcentaje pasa acumulado (%)')
    plt.title('Curva granulométrica')
    plt.legend() 
    plt.xscale("log")
    plt.xlim(0.075,4.75)
    plt.ylim(0,100) 
    plt.grid(color='k',lw='0.1',ls='-')

    #se agregan más grillas
    ax1 = plt.gca()
    ax1.invert_xaxis()

    # Agregar el segundo eje x para los nombres de los tamices
    ax2 = ax1.twiny()
    ax2.set_xscale('log')
    ax2.set_xticks(abertura)
    ax2.set_xticklabels(nombre, rotation=90, fontsize=8)

    # Agregar linas de los tamices
    ax2.set_xlabel('Tamices')
    ax2.set_xlim(0.075,4.75)
    ax2.invert_xaxis()

    #agregamos nombre lineas verticales
    L_No10 = ([4.75,4.75]) 
    L_No20 = ([2,2]) 
    L_No40 = ([0.850,0.850]) 
    L_No60 = ([0.425,0.425])
    L_No140 = ([0.106,0.106])  
    L_rango = ([0,100])

    #se indicca en el plot la ubicación de estas líneas
    plt.plot(L_No10, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No20, L_rango, color='grey', lw='0.8', ls='--') 
    plt.plot(L_No40, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No60, L_rango, color='grey', lw='0.8', ls='--')
    plt.plot(L_No140, L_rango, color='grey', lw='0.8', ls='--')

    #se agrega textos
    plt.text(4.75, 2, 'Grava(Fina)', fontsize=8, rotation=90)
    plt.text(1.95, 2, 'Arena(Gruesa)', fontsize=8, rotation=90)
    plt.text(0.415, 2, 'Arena(Mediana)', fontsize=8, rotation=90)
    plt.text(0.075, 2, 'Arena(Fina)', fontsize=8, rotation=90)

    x_values = [4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08]
    for x in x_values:
        plt.axvline(x=x, color='grey', ls='-', lw='0.3')

    plt.show()