import customtkinter as ctk
import sys

sys.path.insert(0, './model')
import calc as calc
import resultados as rst


def calculator(funcao):
    if funcao != "":
        funcaostring, derivada = calc.CalculaDerivada(funcao)
        rst.SetResults(funcaostring, derivada)

def ValorX(valor):
    if valor != "":
        result, resultDerivada, ponto= calc.ValorFuncional(valor)
        tangente = calc.RetaTangente(valor)

        rst.SetFuncional(result, resultDerivada, ponto, tangente)
