import customtkinter as ctk

funcao = ''
numbers = []
potences = []
operations = []

def calculator():
    print("test")

def clear(label):
    global funcao
    funcao = ""
    label.configure(text="")

def delete(label):
    global funcao
    tamanho = len(funcao)
    if tamanho > 0:
        funcao= funcao[:-1]
        label.configure(text=funcao)

def num(txt, label):
    
    global funcao
    
    funcao = funcao + str(txt)
    
    print(funcao)   
    label.configure(text=funcao)