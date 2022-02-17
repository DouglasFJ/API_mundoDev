from tkinter import *

class app:
    def __init__(self, master=None):
        self.cont1 = Frame(master)
        self.cont1['padx'] = 110
        self.cont1['pady'] = 10
        self.cont1.pack()

        self.cont2 = Frame(master)
        self.cont2['padx'] = 110
        self.cont2['pady'] = 20
        self.cont2.pack()

        self.cont3 = Frame(master)
        self.cont3['padx'] = 110
        self.cont3['pady'] = 10
        self.cont3.pack()

        self.cont4 = Frame(master)
        self.cont4['padx'] = 110
        self.cont4['pady'] = 100
        self.cont4.pack()

        self.titulo = Label(self.cont1, text='API MUNDO DEV')
        self.titulo['font'] = 'Arial', 30
        self.titulo.pack(side=LEFT)

        self.txt = Label(self.cont2, text='IP:')
        self.txt['font'] = 'Arial', 14
        self.txt.pack(side=LEFT)

        self.ip = Entry(self.cont2)
        self.ip['width'] = 40
        self.ip['font'] = 'Arial', 14
        self.ip.pack(side=LEFT)

        self.button = Button(self.cont2)
        self.button['text'] = 'Enter'
        self.button['command'] = self.executar
        self.button.pack(side=RIGHT)

        self.msg_verificacao = Label(self.cont3, text="")
        self.msg_verificacao['font'] = 'Arial', 14
        self.msg_verificacao.pack(side=BOTTOM)

        self.dados_salvos = Button(self.cont4, height=1, width=14, text="Lista de dados", font='Arial')
        self.dados_salvos.pack(side=LEFT)

        self.espaço = Label(self.cont4, text="                         ")
        self.espaço.pack(side=LEFT)

        self.sair = Button(self.cont4, height=1, width=10, text="SAIR", font='Arial')
        self.sair.pack(side=RIGHT)

    def executar(self):
        from main import API
        ip = self.ip.get()
        dados = API.buscar_dados(ip)
        print(dados)

        if dados['status'] == 'fail':
            self.msg_verificacao['text'] = f'O IP {ip} é invalido. {dados["message"]}'
        else:
            self.msg_verificacao['text'] = f'O IP {ip} foi salvo com sucesso'


root = Tk()
app(root)
root.mainloop()
