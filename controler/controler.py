import customtkinter as ctk
import sys

sys.path.insert(0, './model')
import calc as calc
sys.path.insert(0, './view')
import resultados as rst


def calculator(funcao):
    if funcao != "":
        funcaostring, derivada = calc.CalculaDerivada(funcao)
        rst.SetResults(funcaostring, derivada)

def ValorX(valor):
    if valor != "":
        # Encontra a variável na string da função
        variavel = next((char for char in valor if char.isalpha()), None)
        if variavel:
            result, resultDerivada, ponto = calc.ValorFuncional(valor, variavel)
            tangente = calc.RetaTangente(valor, variavel)
            rst.SetFuncional(result, resultDerivada, ponto, tangente)
        else:
            print("Nenhuma variável encontrada na função.")

