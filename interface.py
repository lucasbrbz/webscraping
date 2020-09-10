from tkinter import *
from tkinter.filedialog import askopenfilename
from backend import *

class Interface():
    window = Tk()
    window.wm_title("Web Scraping")
    txtChave = StringVar()
    lblChave = Label(window, text="Chave")
    entChave = Entry(window, textvariable=txtChave)
    listResult = Listbox(window)
    scrollResult = Scrollbar(window)

    def setLista(self):
        for entrada in Backend.lista:
            self.listResult.insert(entrada)

    def buscarChave():
        Backend.chave = Interface.entChave.get()
        Backend.flag = 1
        #após rodar o programa inteiro

    def carregar():
        arquivo = askopenfilename()
        return arquivo

    btnBuscar = Button(window, text="Buscar", command=buscarChave)
    btnCarregar = Button(window, text="Carregar arquivos", command=carregar)
    lblChave.grid(row=0, column=0)
    entChave.grid(row=0, column=1, padx=50, pady=50)
    listResult.grid(row=0, column=2, rowspan=10)
    scrollResult.grid(row=0, column=6, rowspan=10)
    btnBuscar.grid(row=4, column=0, columnspan=2)
    btnCarregar.grid(row=5, column=0, columnspan=2)
    listResult.configure(yscrollcommand=scrollResult.set)
    scrollResult.configure(command=listResult.yview)
    x_pad = 5
    y_pad = 3
    width_entry = 30
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Interface.window.mainloop()