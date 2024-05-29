import customtkinter as ctk

funcao = ''
tempString = ''
numbers = []
potences = []
operations = []

bNumber = True
bPotence = False
bOperations = False

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
    global funcao, tempString
    print(funcao)   
    global numbers, potences, operations
    global bNumber, bPotence, bOperations
    
    isOperation = False
    
    if (txt == '+') or (txt == '-'): 
        isOperation = True 
    else:
        isOperation = False
    
    if (bNumber == True) and (txt != 'x') and (txt != '^'):
        tempString = tempString + str(txt)
    elif (txt == 'x') or (isOperation == True):
        numbers.append(tempString)
        tempString = ""
    else:
        bNumber = False
        
    #elif(bOperations)
        
        
        
    print(funcao)
    funcao = funcao + str(txt)
    label.configure(text=funcao)
    
    
    
    