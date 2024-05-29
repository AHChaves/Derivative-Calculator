import re

monomios = []
operadores = []


def separar_monomios_e_operadores(funcao):
    if funcao[0] not in '+-':
        funcao = '+' + funcao
    funcao = funcao.lower().replace(" ", "")
    monomios = re.findall(r'[+-]?\d*x\^\d+|[+-]?\d*x|[+-]?\d+', funcao)
    operadores = re.findall(r'[+-]', funcao[1:])
    return monomios, operadores

string = input("Digite uma funcao para derivar: ").lower().replace(" ","")
monomios, operadores = separar_monomios_e_operadores(string)

for x in monomios:
    print(x.find("^"))

print("Monômios:", monomios)
print("Operadores:", operadores)