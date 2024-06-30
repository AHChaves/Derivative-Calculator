import re


# Inicializa as listas para armazenar os monômios, coeficientes, expoentes e derivadas
monomios = []
coeficientes = []
expoentes = []
derivadas = []
raizes_refinadas = []

#Calculando funções

def CalculandoFuncaoParaEnesima(n, k, x0):
    return x0 ** n - k

def CalculandoDerivadaParaEnesima(n, x0):
    return n * (x0**(n-1))

#Manipulação da string

def separar_monomios(string_do_usuario):
    monomios.clear()
    coeficientes.clear()
    expoentes.clear()
    derivadas.clear()
    raizes_refinadas.clear()
    if string_do_usuario[0] not in '+-':
        string_do_usuario = '+' + string_do_usuario

    mon = re.findall(r'[+-]?\d*x\^\d+|[+-]?\d*x|[+-]?\d+', string_do_usuario)

    for x in mon:
        monomios.append(x)

    return mon

def separando_coeficiente_expoente_e_derivada(array_dos_monomios):
   contador = 0
   for x in array_dos_monomios:
    pos = x.find("x")

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
                derivadas.append(str(temp)+"x")
            else:
                aux = expoentes[contador]-1
                derivadas.append(str(temp)+"x^"+str(aux))            
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
                derivadas.append(str(temp)+"x")
            else:
                aux = expoentes[contador]-1
                derivadas.append(str(temp)+"x^"+str(aux))            
            contador += 1

def fazendoFuncaoDerivada(array_da_derivada):
    first_term = True
    funcao_derivada = ""
    for y in array_da_derivada:
        if y[0] != '-' and first_term == False:
            funcao_derivada += "+"+y
        else:
            funcao_derivada += y
        first_term = False
    return funcao_derivada

def calcularFuncao(array, numero):
    somaFuncao = 0
    first_term = True
    for x in array:
        if array[0] == x and first_term == True and x[0] == '+':
            x = x.replace("+", "")
        if first_term == True and x[0] == '-' and x[1] == 'x':
           x = x.replace('x', f'({numero})')
           x = x.replace('^', '**')
           somaFuncao += eval(x)
        elif x[0] == '+' and x[1] == 'x':
            x = x.replace('x', f'({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        elif x[0] == '-' and x[1] == 'x':
            x = x.replace('x', f'({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        elif x[0] == 'x':
            x = x.replace('x', f'({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        else:
            x = x.replace('x', f'*({numero})')
            x = x.replace('^', '**')
            somaFuncao += eval(x)
        first_term = False
    return somaFuncao

def EncontrarIntervalos(monomio):
    intervalos_encontrados = []
    intervalos = (-10, 10)
    passo = 0.1
    x = intervalos[0]
    while x < intervalos[1]:
        proximo_x = x + passo
        resultado_com_x = calcularFuncao(monomio, x)
        resultado_com_proximo_x = calcularFuncao(monomio, proximo_x)

        if resultado_com_x * resultado_com_proximo_x < 0:
            aux1 = f"{x:.1f}"
            aux2 = f"{proximo_x:.1f}"
            intervalos_encontrados.append((float(aux1), float(aux2)))
        elif resultado_com_x == 0:
            aux1 = f"{x:.1f}"
            intervalos_encontrados.append((float(aux1), float(aux1)))
        elif resultado_com_proximo_x == 0:
            aux2 = f"{proximo_x:.1f}"
            intervalos_encontrados.append((float(aux2), float(aux2)))
        x = proximo_x
    return intervalos_encontrados

def CalcularRaizEnesima(n, k, x0, tol=1e-18, max_iter=100):
    for i in range(max_iter):
        funcao_x0 = CalculandoFuncaoParaEnesima(n, k, x0)
        funcao_derivada_x0 = CalculandoDerivadaParaEnesima(n, x0)

        if funcao_derivada_x0 == 0:
            return None
        
        x1 = x0 - funcao_x0 / funcao_derivada_x0

        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

def CalcularRaizesRefinadas(funcao, derivada, x0, tol=1e-18, max_iter=100):
    for i in range(max_iter):
        funcao_x0 = calcularFuncao(funcao, x0)
        funcao_derivada_x0 = calcularFuncao(derivada, x0)
        if funcao_derivada_x0 == 0:
            return None
        
        x1 = x0 - funcao_x0 / funcao_derivada_x0
        print("x1 = " + str(x1))
        if abs(x1 - x0) < tol or abs(funcao_x0) < tol:
            return x1
        
        x0 = x1
    return round(x0, 9)

def MetodoNewtonEnesima(n, k):
    x0 = 1
    raiz = CalcularRaizEnesima(n, k, x0)
    if raiz is not None:
        return raiz

def MetodoNewton(intervalos):
    for(x0, x1) in intervalos:
        x_inicial = (x0 + x1) / 2
        raiz = CalcularRaizesRefinadas(monomios, derivadas, x_inicial)
        if raiz is not None:
            aux = f"{raiz:.9f}"
            aux = aux[:-1]
            raizes_refinadas.append(aux)

    return raizes_refinadas

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
        return "y = {0}".format(b.replace("+",""))
    else:
        return "y = {0}x{1}".format(valor_funcional_derivada, b)

def ValorFuncional(num):
    valor_funcional_funcao = calcularFuncao(monomios, num)
    valor_funcional_derivada = calcularFuncao(derivadas, num)
    return "f({0}) = {1}".format(num, valor_funcional_funcao), "f'({0}) = {1}".format(num, valor_funcional_derivada), "P({0}, {1})".format(num, valor_funcional_funcao)

def CalculaDerivada(funcao):
    monomio = separar_monomios(funcao)
    for x in monomio:
        monomios.append(x)

    separando_coeficiente_expoente_e_derivada(monomios)
    funcao_derivada = fazendoFuncaoDerivada(derivadas)

    if len(funcao_derivada) == 0:
        funcao_derivada = '0'

    count = 0

    for x in monomio:
        if x[0] == '+' and monomio[0] == x:
            x.replace("+", "")

        if x.find('x') != -1:
            count += 1
    if count == 0:
        funcao = str(eval(funcao))

    return "f(x) = " + funcao, "f'(x) = " + funcao_derivada
