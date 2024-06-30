import customtkinter as ctk
import sys

sys.path.insert(0, '../model')
import calc as calc
sys.path.insert(0, '../view')
import resultados as rst
import resultsNewton as rstN
import resultsEnesima as rstE

func = ""
monomios = []
intervalos = []

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

def Achar_Enesima(n, k):
    if n != "" and k != "":

        frame = rstE.GetFrame()
        
        for x in frame.winfo_children():
            x.destroy()

        raiz = calc.MetodoNewtonEnesima(float(n), float(k))

        rstE.Resultado(n, k, raiz)


def Achar_Intervalos(funcao):

    global func, monomios, intervalos
    func = funcao

    FI, FR = rstN.GetFrames()
    
    for x in FI.winfo_children():
        x.destroy()
    
    for x in FR.winfo_children():
        x.destroy()
    rstN.Cria_Resultados(FI, FR)

    if funcao != "":
        calc.separar_monomios(funcao)
        calc.separando_coeficiente_expoente_e_derivada(calc.monomios)
        intervalo = calc.EncontrarIntervalos(calc.monomios)
        if len(intervalo) != 0:
            for x in intervalo:
                rstN.Adiciona_Intervalos(x)
            raiz = calc.MetodoNewton(intervalo)
            for x in raiz:
                rstN.Adiciona_Raizes(x)
        elif len(intervalo) == 0:
            rstN.Funcao_sem_intervalos()