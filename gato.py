#!/usr/bin/env python

from typing import cast
import random

class Tablero:
    dv = None       #diccionario de valores
    dc = None       #Diccionario de posiciones
    sc = None       #Set combinaciones ganadoras
    movimiento = None   #indica quien esta jugando
    lista_celdas = None #Lista de celdas en el tablero
    
    def __init__(self) -> None:
        self.dv = {}        
        self.lista_celdas = "ABCDEFGHI"
        self.sc = set(["ABC","DEF","GHI","ADG","BEH","AEI","CEG","CFI"]) # set de combinaciones
        self.movimiento = 1

    def limpia_tablero(self):
        self.dv={}
        self.movimiento= 1

    def jugar(self, celda):
        if celda not in self.dv: #Si no ha sido jugada esta celda
            if self.movimiento % 2 != 0:   #es impar el movimiento
                self.dv[celda]="X"
            else:
                self.dv[celda]="O"
            self.movimiento += 1
        ganador = self.revisa_si_hay_ganador() #llama al método del objeto Tablero
        diccionario = {}
        for c in self.lista_celdas:
            if c in self.dv:
                if self.dv[c] == "X":
                    diccionario[c] = "/static/images/cruz.png"
                else:
                    diccionario[c] = "/static/images/circulo.png"
            else:
                diccionario[c] = "/static/images/blanco.png"
        return diccionario,ganador

    def revisa_si_hay_ganador(self) -> str:
        set_combo = self.sc
        diccionario_valores = self.dv
        X =[]
        O =[]
        for keys in set_combo:
            lista_x = self.checa_simbolo_en_diccionario(keys,"X")
            lista_o = self.checa_simbolo_en_diccionario(keys,"O")
            X.append("".join(lista_x))
            O.append("".join(lista_o))
        print(X)
        print(O)
        for x in X:
            if x in set_combo:
                return "X"
        for o in O:
            if o in set_combo:
                return "O"
        return None     

    def checa_simbolo_en_diccionario(self, keys:str, simbolo:str) -> list:
        diccionario = self.dv #diccionario de valores interno del Tablero
        lista =[]
        for k in keys:
            if (k in diccionario):
                if (diccionario[k]==simbolo):
                    lista.append(k)
        return lista

    def jugar_computadora(self):
        movs_disponibles = []
        for a in self.lista_celdas:
            if a not in self.dv:
                movs_disponibles.append(a)
        celda = random.choice(movs_disponibles)
        diccionario, ganador = self.jugar(celda)
        return diccionario, ganador