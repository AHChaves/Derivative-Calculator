import string

letras = string.ascii_lowercase
coeficientes = []
potencia = []
count = 0
print("coeficiente de a e b para ax^b")
while True:
    print(f'iteracao {count}',end="\n\n")
    a = input("valor do coeficiente a: ")
    b = input("valor da potencia b: ")
    if a != 's' or  b != 's':
        count +=1
        coeficientes.append(int(a))
        potencia.append(int(b))  

        print("---------")  
    else:
        break
    
for a,b in zip(coeficientes, potencia):
    print(f'{b*a}x^{b-1}', end="")