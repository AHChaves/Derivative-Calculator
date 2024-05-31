import sys
import customtkinter as ctk
import re

sys.path.insert(0, './controler')
import controler as ctr

# Variável global para armazenar a variável da função
variavel = None

# Inicializa as listas para armazenar os monômios, coeficientes, expoentes e derivadas
monomios = []
coeficientes = []
expoentes = []
derivadas = []

def separar_monomios(string_do_usuario):
    global variavel
    monomios.clear()
    coeficientes.clear()
    expoentes.clear()
    derivadas.clear()
    if string_do_usuario[0] not in '+-':
        string_do_usuario = '+' + string_do_usuario
    mon = re.findall(r'[+-]?\d*[a-z]?\^\d+|[+-]?\d*[a-z]|[+-]?\d+', string_do_usuario)
    # Identifica a variável na string da função
    variavel = next((char for char in string_do_usuario if char.isalpha()), None)
    return mon

# Função para separar os coeficientes, expoentes e derivadas dos monômios
def separando_coeficiente_expoente_e_derivada(array_dos_monomios):
   contador = 0
   for x in array_dos_monomios:
    pos = x.find(variavel)
    if pos != -1:
        try:
            coeficientes.append(int(x[:pos]))
            try:
                expoentes.append(int(x[pos+2:]))
            except ValueError:
                expoentes.append(int(1))
            temp = coeficientes[contador] * expoentes[contador]
            if expoentes[contador] == 1:
                derivadas.append(str(temp))
            elif expoentes[contador] == 2:
                derivadas.append(str(temp) + variavel)
            else:
                aux = expoentes[contador] - 1
                derivadas.append(str(temp) + variavel + '^' + str(aux))            
            contador += 1
        except ValueError:
            if x[0] == '-':
                coeficientes.append(-1)
            else:
                coeficientes.append(1)
            try:
                expoentes.append(int(x[pos+2:]))
            except ValueError:
                expoentes.append(int(1))
            temp = coeficientes[contador] * expoentes[contador]
            if expoentes[contador] == 1:
                derivadas.append(str(temp))
            elif expoentes[contador] == 2:
                derivadas.append(str(temp) + variavel)
            else:
                aux = expoentes[contador] - 1
                derivadas.append(str(temp) + variavel + '^' + str(aux))            
            contador += 1

# Função para criar a derivada da função
def fazendoFuncaoDerivada(array_da_derivada):
    first_term = True
    funcao_derivada = ""
    for y in array_da_derivada:
        if y[0] != '-' and first_term == False:
            funcao_derivada += "+" + y
        else:
            funcao_derivada += y
        first_term = False
    return funcao_derivada

# Função para calcular a função em um determinado número
def calcularFuncao(array, numero):
    somaFuncao = 0
    first_term = True
    for x in array:
        if array[0] == x and first_term == True and x[0] == '+':
            x = x.replace("+", "")
        if x == f'+{variavel}' or x == f'-{variavel}':
            x = x.replace(variavel, f'{numero}')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        elif x[0] == variavel:
            x = x.replace(variavel, f'{numero}')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        else:
            x = x.replace(variavel, f'({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        first_term = False

    return somaFuncao

# Função para calcular a reta tangente em um determinado número
def RetaTangente(num):
    valor_funcional_funcao = calcularFuncao(monomios, num)
    valor_funcional_derivada = calcularFuncao(derivadas, num)
    b = valor_funcional_funcao - valor_funcional_derivada * float(num)
    if b > 0:
        aux = "+"
        aux += str(b)
        b = str(aux)
    elif b == 0:
        b = ""
    else:
        str(b)
    if valor_funcional_derivada == 1:
        return "y = x{0}".format(b)
    elif valor_funcional_derivada == -1:
        return "y = -x{0}".format(b)
    elif valor_funcional_derivada == 0 and len(str(b)) == 0:
        return "y = {0}{1}".format(valor_funcional_derivada, b)
    elif valor_funcional_derivada == 0 and len(str(b)) != 0:
        return "y = {0}".format(int(b))
    else:
        return "y = {0}x{1}".format(valor_funcional_derivada, b)


# Função para calcular o valor funcional e a derivada em um determinado número
def ValorFuncional(num):
    valor_funcional_funcao = calcularFuncao(monomios, num)
    valor_funcional_derivada = calcularFuncao(derivadas, num)

    return "f({0}) = {1}".format(num, valor_funcional_funcao), "f'({0}) = {1}".format(num, valor_funcional_derivada), "P({0}, {1})".format(num, valor_funcional_funcao)

# Função para calcular a derivada da função
def CalculaDerivada(funcao):
    monomio = separar_monomios(funcao)
    for x in monomio:
        monomios.append(x)
    separando_coeficiente_expoente_e_derivada(monomios)
    funcao_derivada = fazendoFuncaoDerivada(derivadas)

    return "f({0}) = ".format(variavel) + funcao, "f'({0}) = ".format(variavel) + funcao_derivada
