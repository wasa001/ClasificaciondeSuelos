#Importando librerias 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from funciones.Input import DatosIniciales

def CPlasticidad():
  #Se grafica la carta de plasticidad en las siguientes lineas

  # # Se establecen los limites de los ejes x,y.
  plt.xlim(0,100)
  plt.ylim(0,60)

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

  # # # Divide la gráfica cuando el limite liquido es igual a 50 para diferenciar si el suelo es de plasticidad alta o baja
  plt.vlines(50,0,60,'g')

  # # # Estas lineas permiten que se muestren en la gráfica las etiquetas de las diferentes zonas.
  plt.annotate('CL-ML', (15,5))
  plt.annotate('MH', (80,20))
  plt.annotate('CL', (30,15))
  plt.annotate('CH', (62,40))
  plt.annotate('ML', (35,5))
  plt.annotate('NO EXISTE', (15,35))

  # Estas lineas mejoran la estetica de la gráfica, hacen que se sombreen las diferentes zonas de la carta de plasticidad
  # Dentro de las variables de la d a la m se guardan las coordenadas que delimitan cada zona.
  d=[50,50,100,100]
  e=[0,22,58,0]
  plt.fill(d,e,'pink')
  f=[25.5,12.4,8,20,50,50]
  g=[4,4,0,0,0,22]
  plt.fill(f,g,'lightgray')
  h=[50,100,100,75,50]
  i=[22,58,60,60,38]
  plt.fill(h,i,'lightgreen')
  j=[29.5,15.7,12.4,25.5]
  k=[7,7,4,4]
  plt.fill(j,k,'m')
  l=[15.7,29.5,50,50]
  m=[7,7,22,38]
  plt.fill(l,m,'bisque')

  print("--------------------------------------------------- ")
  plt.plot(x, y, label = "LL = 50%", color='red')  #Linea LL=50%
  plt.plot(Ll, LP, marker='o')   #Grafica el punto ingresado por el usuario
  plt.plot('LL', 'LP', data=Linea_h_Superior, linestyle='--', label = '--' ) #Grafica la linea horizontal superior
  plt.plot('LL', 'LP', data=Linea_h_Inferior, linestyle='--', label = '--' ) #Grafica la linea horizontal inferior
  plt.plot('LL', 'LP', data=Linea_A, linestyle='-', label = "Linea A", color='darkblue') #Grafica la linea A 
  plt.plot('LL', 'LP', data=Linea_u, linestyle=':', label = "Linea U", color='gray') #Grafica la linea U
  plt.legend() 
  plt.grid(color='darkblue', ls = ':', lw = 0.6)   #Define caracteristicas de la grilla
  plt.title("CARTA DE PLASTICIDAD",fontsize=15)    #Define caracteristicas del titulo
  plt.xlabel("Limite liquido LL",fontsize=10)      #Define caracteristicas del eje x
  plt.ylabel("Limite Plastico LP",fontsize=10)      #Define caracteristicas del eje y
  plt.show()
