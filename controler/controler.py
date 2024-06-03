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

    if ('x' or 'X') not in funcao:
        y = funcaostring.split('=')
        tangente = "y = {0}".format(y[1])

    rst.SetFuncional(result, resultDerivada, ponto, tangente)

    
def ValorX(valor):

    if ('x' or 'X') in func and valor != "":
        result, resultDerivada, ponto = calc.ValorFuncional(valor)
        tangente = calc.RetaTangente(valor)
        rst.SetFuncional(result, resultDerivada, ponto, tangente)