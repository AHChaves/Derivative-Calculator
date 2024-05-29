import customtkinter as ctk

funcao = ''
numbers = []
potences = []
operations = []

def calculator():
    print("test")




def num(text, label):
    
    global funcao
    
    funcao = funcao + str(text)
    
    print(funcao)
    label.set(funcao)