# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:56:23 2022

@author: alumno
"""


# def busqueda_binaria (lista,item):
#     encontrado= False
#     primero = 0
#     ultimo = len(lista)-1
    
#     while primero<=ultimo and not encontrado: 
#         punto_medio = (primero + ultimo)//2
#         if lista[punto_medio] == item:
#             encontrado == True
#         elif lista[punto_medio] < item:
#             primero = punto_medio+1
#         else:
#             ultimo = punto_medio -1
    
#     return encontrado

""" Implemente una función recursiva que retorne la suma de los dígitos de un
número entero positivo. ( ayuda: puede obtener los dígitos del número, 
haciendo divisiones sucesivas por 10) """

def suma_digitos (numero):
   if numero==0:
    return 0
   else:
    return suma_digitos(numero//10)+ numero%10
print(suma_digitos(3))
    
    
