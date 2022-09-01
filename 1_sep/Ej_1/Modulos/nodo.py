# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:58:34 2022

@author: alumno
"""

class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
      
    
    @property
    def dato(self):
        return self._dato
    @property
    def siguiente(self):
        return self._siguiente
    
    @dato.setter
    def dato(self,nuevodato):
        self._dato = nuevodato
        
    @siguiente.setter
    def siguiente(self,nuevosiguiente):
        self._siguiente = nuevosiguiente
        
    @property
    def anterior(self):
         return self._anterior

    @anterior.setter
    def anterior(self,nuevo):
        self._anterior = nuevo
        

        
    