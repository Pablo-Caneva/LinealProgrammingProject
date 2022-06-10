from menu import Principal
from transporte import resolucion
from asignacion import minimizacion
from asignacion import maximizacion
import os

control = True

while control:
    os.system('cls')
    Principal()
    ing=input("Ingrese una opcion: ")
    if ing=="1":
        resolucion()
    elif ing=="2":
        minimizacion()
    elif ing=="3":
        maximizacion()
    elif ing=="4":
        control=False
    else:
        print("El valor ingresado no es correcto.")cla