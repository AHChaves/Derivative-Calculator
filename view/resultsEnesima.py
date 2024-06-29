import customtkinter as ctk

Rst_function = ctk.CTkLabel
Intervalos = []
raizes = []
Frame_Intervalos = ctk.CTkFrame
Frame_Raizes = ctk.CTkFrame
fontepadrao = ctk.CTkFont

def Cria_Resultados(frame, fraizes):

    global Rst_functions, Frame_Intervalos, fontepadrao, Frame_Raizes

    fontepadrao = ctk.CTkFont(family="Roboto", size=16) 
    Frame_Intervalos = frame
    Frame_Raizes = fraizes


    lIntervalos = ctk.CTkLabel(master=frame, text="Intervalos", font=("Roboto", 18))
    lIntervalos.pack(pady=10, padx=5)


    Rst_function = ctk.CTkLabel(master=frame, text="f(x) =", font=fontepadrao)
    Rst_function.pack(pady=2, padx=10, anchor='w')


def Adiciona_Intervalos(vet):
    
    global Intervalos
    i = 0 

    for x in vet:
        Intervalos.append(ctk.CTkLabel(master=Frame_Intervalos, text=x, font=fontepadrao))
        Intervalos[i].pack(pady=2, padx=10)
        i+1

def Adiciona_Raizes(vet):
    global raizes
    i = 0 

    for x in vet:
        raizes.append(ctk.CTkLabel(master=Frame_Raizes, text=x, font=fontepadrao))
        raizes[i].pack(pady=2, padx=10)
        i+1