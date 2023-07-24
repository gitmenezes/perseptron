# -*- coding: utf-8 -*-
"""
@author: Alexandre Menezes Ferreira
"""
import pandas as pd
import numpy as np
import matplotlib as plt
from time import sleep as sl


entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,0,0,1])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.0001

def stepFunction(soma):#StepFunction ou função escada retorna "zero" ou "um"
    if(soma >=1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos) #produto escalar - realiza multiplicação e soma
    return stepFunction(s)


def treinar(epic=0):
    """
    epic = calcula as épocas realizadas  para encontrar o melhor resultado
    
    """
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal=0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j]+(taxaAprendizagem * entradas[i][j]*erro)
                print("peso Atualizado:" +str(pesos[j]))
            print("Total de erros: " + str(erroTotal))
        epic = epic + 1            
        # sl(0.5)
    print("Épocas: "+ str(epic))
    
treinar()#executa a função

print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))
