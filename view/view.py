import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Derivative Calculator")

def calculator():
    print("test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=30, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Derivative Calculator", font=("Roboto", 24))
label.pack(pady=12, padx=10)

function_entry = customtkinter.CTkEntry(master=frame, placeholder_text="F(x)=")
function_entry.pack(pady=12, padx=20, fill="x")

button = customtkinter.CTkButton(master=frame, text="Derivate", command=calculator)
button.pack(pady=12, padx=10)

root.mainloop()
