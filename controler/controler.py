import customtkinter as ctk
import sys

sys.path.insert(0, './model')
import calc as calc
sys.path.insert(0, './view')
import resultados as rst

func = ""

def calculator(funcao):

    global func
    func = funcao

    if funcao != "":
        funcaostring, derivada = calc.CalculaDerivada(funcao)
        rst.SetResults(funcaostring, derivada)

    result = "f(x) = "
    resultDerivada = "f'(x) = "
    ponto = "P(x,f(x))"
    tangente = "y = "

    rst.SetFuncional(result, resultDerivada, ponto, tangente)

    

def ValorX(valor):

    if ('x' or 'X') in func:
        if valor != "":
            result, resultDerivada, ponto = calc.ValorFuncional(valor)
            tangente = calc.RetaTangente(valor)
            rst.SetFuncional(result, resultDerivada, ponto, tangente)


