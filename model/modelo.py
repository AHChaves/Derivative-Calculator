import string

letras = string.ascii_lowercase
coeficientes = []
potencia = []
operadores = ["+","-","*","/"]
count = 0
print("coeficiente de a e b para ax^b")
while True:
    print(f'iteracao {count}', end="\n\n")
    a = input("valor do coeficiente a: ")
    b = input("valor da potencia b: ")
    if a != 's' or b != 's':  
        count += 1
        try:
            coeficientes.append(int(a))
            potencia.append(int(b))
            print("---------")
        except ValueError:
            print("Por favor, insira um número válido para 'a' e 'b'.")
    else:
        break

for a, b in zip(coeficientes, potencia):
    if a != 0 and b != 0:
        print(f'{b * a}x^{b - 1}', end="")
    else:
        print(f'{b * a}x^{b - 1}', end="")
