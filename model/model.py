import string

print("quantos elementos serão")
elementos = int(input())
letras = string.ascii_lowercase
coeficientes = []
potencia = []
count = 0
while (count != elementos):
    print("coeficiente numero " + str(count+1) + " de a e b para ax^b: ")
    a = input("valor de a: ")
    b = input("valor de b: ")
    coeficientes.append(int(a))
    potencia.append(int(b))
    count = count+1

print(coeficientes)
print(potencia)

for a,b in zip(coeficientes, potencia):
    print(f'{b*a}x^{b-1}', end=" + ")