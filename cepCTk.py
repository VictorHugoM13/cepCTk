import customtkinter
import requests

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("300x400")

textVariable = customtkinter.StringVar()

def getCep():
    if len(entryCep.get()) != 9:
        textVariable.set('Digite o um CEP válido!')
    else:
        entryCep.get().replace("-", "")
        request = requests.get(f'https://viacep.com.br/ws/{entryCep.get()}/json/')
        adress_data = request.json()
        if 'code' not in adress_data:
            city = adress_data['localidade']
            states = adress_data['uf']
            textVariable.set(f'Cidade {city} no Estado de {states}')     
        else:
            textVariable.set('CEP não encontrado')
            
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=12, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Digite o CEP", font=("Roboto", 24))
label.pack(pady=30, padx=10)

entryCep = customtkinter.CTkEntry(master=frame, placeholder_text="00000-000", width=200)
entryCep.pack(pady=30, padx=10)

button = customtkinter.CTkButton(master=frame, text="BUSCAR", command=getCep, width=150)
button.pack(pady=30, padx=10)

labelResponse = customtkinter.CTkLabel(master=frame, textvariable=textVariable, font=("Roboto", 13, "bold"))
labelResponse.pack(pady=25, padx=15)


root.mainloop()
