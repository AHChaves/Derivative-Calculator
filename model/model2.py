import string
import sympy as sp

# Receber a expressão do usuário
fx = input("Digite a expressão f(x): ")

# Criar o símbolo 'x'
x = sp.symbols('x')

# Converter a expressão em uma expressão simbólica
expr = sp.sympify(fx)

# Calcular a derivada da expressão
derivada = sp.diff(expr, x)

# Imprimir a derivada
print("A derivada de f(x) é:", derivada)