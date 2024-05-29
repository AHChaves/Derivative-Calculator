import re

monomios = []
operadores = []
coeficientes = []
expoentes = []
derivada = []

def separar_monomios_e_operadores(funcao):
    if funcao[0] not in '+-':
        funcao = '+' + funcao
    monomios = re.findall(r'[+-]?\d*x\^\d+|[+-]?\d*x|[+-]?\d+', funcao)
    operadores = re.findall(r'[+-]', funcao[1:])
    return monomios, operadores

string = input("Digite uma funcao para derivar: ").lower().replace(" ","")
monomios, operadores = separar_monomios_e_operadores(string)

contador = 0
d = ""

for x in monomios:
    pos = x.find("x")
    if pos != -1:
        coeficientes.append(int(x[:pos]))
        try:
            expoentes.append(int(x[pos+2:]))
        except ValueError:
            expoentes.append(int(1))
        temp = coeficientes[contador] * expoentes[contador]
        if expoentes[contador] == 1:
            derivada.append(str(temp))
        else:
            aux = expoentes[contador]-1
            derivada.append(str(temp)+"x^"+str(aux))            
    contador += 1

for y in derivada:
    
    if y[0] == '-':
        d += y
    else:
        d += "+"+y

print("Monômios:", monomios)
print("Operadores:", operadores)
print("Coeficientes:", coeficientes)
print("Expoentes:", expoentes)
print("Derivada:", derivada)
print("AAA:", d)