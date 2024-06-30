import customtkinter as ctk

def SetFrame(frame):
    global Frame 
    Frame = frame
    
def GetFrame():
    return Frame

def Resultado(expoente, num, raiz):
    
    global Result
    
    string = "A raiz {0}ª de {1} é {2}".format(expoente, num, raiz)

    Result = ctk.CTkLabel(master=Frame, text=string, font=("Roboto", 16))
    Result.grid(row=4, column=0)