'''-----------------------------------------------'''
#Importando librerias 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from funciones.Inputs import DatosIniciales
from funciones.cartaplasticidad import CPlasticidad

'''-----------------------------------------------'''

#Funcion para definir si es CL o ML
def inorganico_2(): 
  if IP > 7  or 0.9*(Ll-8) > IP > 0.73*(Ll-20):
    print("El suelo es un CL: Arcilla de baja plasticidad")       #da como resultado el tipo de suelo
  elif IP < 4 or IP < 0.73*(Ll-20):
    print("El suelo es un ML: Limo de baja plasticidad.")         #da como resulta el tipo de suelo
  else:
    print("Hay algo raro")                                        #Es necesario verificar el error.

'''-----------------------------------------------'''

 #Funcion para definir si es CH o MH
def inorganico1():    
  if IP > 7 or 0.9*(Ll-8) > IP > 0.73*(Ll-20):
    print("El suelo es un CH: Arcilla de alta plasticidad")      #da como resultado el tipo de suelo
  elif IP < 4 or IP < 0.73*(Ll-20):
    print("El suelo es un MH: Limo de alta plasticidad.")        #da como resultado el tipo de suelo
  else:
    print("Hay algo raro")                                       #Es necesario verificar el error.

'''-----------------------------------------------'''

#Funcion para definir que tipo de fino es el suelo
def fino(): 
  if Ll > 50:   
    print("Suelo inorganico")     #Devuelve el tipo de suelo
    inorganico1()                 #Llama la funcion para definir si es CH o MH

  elif Ll < 50:
    print("Suelo inorganico")     #Devuelve el tipo de suelo
    inorganico_2()                #Llama la funcion para definir si es CL o ML

  else:
    print("Hay algo raro en el Limite liquido")     #Es necesario verificar el error  

'''-----------------------------------------------'''

#Funcion para definir que tipo de Arena es el suelo. esta es la que es Arena limpia
def Alimpia():    
  print("------------------------------------------------------")
  Cu= int(input("Digite el Coeficiente de uniformidad "))                #Captura el valor del Coeficiente de Uniformidad
  Cc= int(input("Digite el coeficiente de curvatura "))                  #Captura el valor del Coeficiente de Curvatura
  print("------------------------------------------------------")
  if Cu >= 6 and 1<= Cc <= 3:
    print("Es un suelo SW: Arena bien gradada")     #Devuelve el tipo de suelo SW
  elif Cu<6 and (Cc < 1 or Cc > 3):
    print("Es un suelo SP: Arena mal gradada")      #Devuelve el tipo de suelo SP
  else:
    print("Hay algo raro con el Cc o el Cu")        #Es necesario verificar el error

'''-----------------------------------------------'''

#Funcion para definir que tipo de Arena es el suelo. esta es la que tiene Arena con finos.
def Afinos(): 
  if IP < 4 or IP < 0.73*(Ll-20):
    print("El suelo es un SM: Arena limosa")             #Devuelve el tipo de suelo SM
  elif IP > 7 or 0.9*(Ll-8) > IP > 0.73*(Ll-20):  
    print("El suelo es un SC: Arena arcillosa.")         #Devuelve el tipo de suelo SC
  else:
    print("Hay algo raro")                               #Es necesario verificar el error

'''-----------------------------------------------'''

 #Funcion para definir que tipo de Arena es el suelo. esta es la que tiene Arena con finos y es limpia.
def limpiayfinos():
  print("------------------------------------------------------")
  Cu= int(input("Digite el Coeficiente de uniformidad "))                #Captura el valor del Coeficiente de Uniformidad
  Cc= int(input("Digite el coeficiente de curvatura "))                  #Captura el valor del Coeficiente de Curvatura
  print("------------------------------------------------------")    
  if IP > 7 and Cu >= 6 and 1<= Cc <= 3 or 0.9*(Ll-8) > IP > 0.73*(Ll-20):
    print("El suelo es un SW-SC: Arena bien gradada con arcilla")             #Devuelve el tipo de suelo
  elif IP > 7 and Cu<6 and (Cc < 1 or Cc > 3) or 0.9*(Ll-8) > IP > 0.73*(Ll-20):
    print("El suelo es un SP-SC: Arena mal gradada con arcilla")              #Devuelve el tipo de suelo
  elif IP < 4 and Cu >= 6 and 1<= Cc <= 3 or IP < 0.73*(Ll-20):
    print("El suelo es un SP-SC: Arena mal gradada con arcilla")              #Devuelve el tipo de suelo
    print("El suelo es un SW-SM: Arena bien gradada con limo")             
  elif IP < 4 and Cu<6 and (Cc < 1 or Cc > 3) or IP < 0.73*(Ll-20):
    print("El suelo es un SP-SC: Arena mal gradada con arcilla")              #Devuelve el tipo de suelo
    print("El suelo es un SP-SM: Arena mal gradada con limo ")                
  else:
    print("Hay un error")             #Es necesario verificar el error

'''-----------------------------------------------'''
#Funcion para definir que tipo de Arena es el suelo. y llama las funciones correspondientes
def arena():  
  if Estructura['Pasa'][10] < 5:
    print("El suelo es una Arena limpia")              #Devuelve el tipo de suelo
    Alimpia()                                          #Llama la funcion para Arenas Limpias
  
  elif Estructura['Pasa'][10] >12:
    print("El suelo es una Arena con finos")           #Devuelve el tipo de suelo
    Afinos()                                           #Llama la funcion para Arena con finos
  
  else:
    print("El suelo es una Arena limpia y con finos")       #Devuelve el tipo de suelo
    limpiayfinos()

'''-----------------------------------------------'''
#Funcion para definir que tipo de Grava es el suelo. esta es Grava limpia
def Glimpia():
  print("------------------------------------------------------")
  Cu= int(input("Digite el Coeficiente de uniformidad "))                #Captura el valor del Coeficiente de Uniformidad
  Cc= int(input("Digite el coeficiente de curvatura "))                  #Captura el valor del Coeficiente de Curvatura
  print("------------------------------------------------------") 
  if Cu >= 4 and 1<= Cc <= 3:
    print("Es un suelo GW: Grava bien gradada")      #Devuelve el tipo de suelo
  elif Cu<4 and (Cc < 1 or Cc > 3):
    print("Es un suelo GP: Grava mal gradada")       #Devuelve el tipo de suelo
  else:
    print("Hay algo raro con el Cc o el Cu")         #Es necesario verificar el error

'''-----------------------------------------------'''
#Funcion para definir que tipo de Grava es el suelo. esta es la que tiene Grava con finos.
def Gfinos(): 
  if IP < 4 or IP < 0.73*(Ll-20):
    print("El suelo es un GM: Grava limosa")       #Devuelve el tipo de suelo
  elif IP > 7 or 0.9*(Ll-8) > IP > 0.73*(Ll-20):
    print("El suelo es un GC: Grava arcillosa.")   #Devuelve el tipo de suelo
  else:
    print("Hay algo raro")                         #Es necesario verificar el error

'''-----------------------------------------------'''
#Funcion para definir que tipo de Grava es el suelo. esta es la que tiene Grava con finos y es limpia.
def Glimpiayfinos():
  print("------------------------------------------------------")
  Cu= int(input("Digite el Coeficiente de uniformidad "))                #Captura el valor del Coeficiente de Uniformidad
  Cc= int(input("Digite el coeficiente de curvatura "))                  #Captura el valor del Coeficiente de Curvatura
  print("------------------------------------------------------") 
  if IP > 7 and Cu >= 6 and 1<= Cc <= 3 or 0.9*(Ll-8) > IP > 0.73*(Ll-20):
    print("El suelo es un GW-GC: Grava bien gradada con arcilla")      #Devuelve el tipo de suelo
  elif IP > 7 and Cu<6 and (Cc < 1 or Cc > 3) or 0.9*(Ll-8) > IP > 0.73*(Ll-20):
    print("El suelo es un GP-GC: Grava mal gradada con arcilla")       #Devuelve el tipo de suelo
  elif IP < 4 and Cu >= 6 and 1<= Cc <= 3 or IP < 0.73*(Ll-20):
    print("El suelo es un GW-GM: Grava bien gradada con limo")         #Devuelve el tipo de suelo
  elif IP < 4 and Cu<6 and (Cc < 1 or Cc > 3) or IP < 0.73*(Ll-20):
    print("El suelo es un GP-GM: Grava mal gradada con limo ")         #Devuelve el tipo de suelo
  else:
    print("Hay un error")         #Es necesario verificar el error

'''-----------------------------------------------'''
#Funcion para definir que tipo de Grava es el suelo. Llama las funciones necesarias para este tipo de suelo.
def grava(): 
  if Estructura['Pasa'][10] < 5:
    print("El suelo es una Grava limpia")                   #Devuelve el tipo de suelo
    Glimpia()                                               #Llama a la funcion de Gravas limpias
  
  elif Estructura['Pasa'][10] >12:
    print("El suelo es una Grava con finos")                #Devuelve el tipo de suelo
    Gfinos()                                                #Llama a la funcion de Gravas con finos
  
  else:
    print("El suelo es una Grava limpia y con finos")       #Devuelve el tipo de suelo
    Glimpiayfinos()                                         #Llama a la funcion de Gravas limpias y con finos

'''-----------------------------------------------'''
#Funcion para definir que tipo suelo es el grueso. si es Arena o Grava, y llama sus respectivas funciones
def grueso():   
  if Estructura['Pasa'][4] >= 50:
    print("El suelo es una Arena")     #Devuelve el tipo de suelo
    arena()                            #Llama a la funcion de Arenas
                        
  elif Estructura['Pasa'][4] < 50:
    print("El suelo es una Grava")     #Devuelve el tipo de suelo
    grava()                            #Llama a la funcion de Gravas

  else:
    print("Hay algo raro")             #Es necesario verificar el error
    
'''-----------------------------------------------'''
#Funcion para definir que tipo de Suelo es la muestra, si es un Fino o un Grueso
def clasificacion():
 if Estructura['Pasa'][10] >= 50:
    
    print("El suelo es un Fino")       #Devuelve el tipo de suelo
    fino()                             #Llama a la funcion de Suelos Finos
        
 elif Estructura['Pasa'][10] < 50:
    print("El suelo es un Grueso")     #Devuelve el tipo de suelo
    grueso()                           #Llama a la funcion de Suelos Gruesos
        
 else:
    print("Hay un error")              #Es necesario verificar el error

clasificacion()

'''-----------------------------------------------'''
