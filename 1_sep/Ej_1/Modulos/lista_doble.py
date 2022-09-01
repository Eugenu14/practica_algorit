# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:27:18 2022

@author: alumno
"""
from Modulos.nodo import Nodo
class Lista_DE :
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        
    def esta_vacia(self):
        return self.tamanio == 0
        
    @property
    def cabeza(self):
        return self._cabeza
    
    @property
    def cola(self):
        return self._cola
    
    @property
    def tamanio (self):
        return self._tamanio
    
    @cabeza.setter
    def cabeza(self,dato):
        self._cabeza=dato
        
    @cola.setter
    def cola (self,dato):
        self._cola = dato
        
    @tamanio.setter
    def tamanio(self,dato):
        self._tamanio=dato
        
      
    def agregar(self,dato):
        nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nodo
            self.cola = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
            
        self.tamanio += 1
        
    def anexar (self,dato):
        nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nodo
            self.cola = nodo
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
            
        self.tamanio += 1
    
    def insertar (self,posicion,dato):
        temp = self.cabeza
        nodo = Nodo(dato)
        
        if posicion > 0 and not posicion== self.tamanio:            
            for i in range(posicion-1):
                temp = temp.siguiente
            nodo.siguiente = temp.siguiente
            temp.siguiente.anterior = nodo
            temp.siguiente = nodo
            nodo.anterior = temp
            self.tamanio += 1
            
        elif posicion == 0:
            self.agregar(dato)
        
        elif posicion == self.tamanio :
            self.anexar(dato)
        
        elif posicion == self.tamanio-1:
            self.cola.anterior.siguiente = nodo
            nodo.anterior = self.cola.anterior
            nodo.siguiente = self.cola
            self.cola.anterior = nodo
            self.tamanio +=1
        
        elif posicion < 0 or posicion > self.tamanio :
            print ("Fuera de rango")
            
            
        
            
            
            
        
        
        
        
        
    