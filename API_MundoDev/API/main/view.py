from tkinter import *

class App:
    def __init__(self, master=None):
        """esta função constroi os containers e widgets para fazer a GUI(Graphic User Interface)"""
        try:
            self.cont2_1.destroy()
            self.cont2_2.destroy()
            self.cont3_1.destroy()
            self.cont3_2.destroy()
        except AttributeError:
            pass

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
        self.cont4['pady'] = 10
        self.cont4.pack()

        self.cont2_1 = Frame(master)
        self.cont2_1['padx'] = 110
        self.cont2_1['pady'] = 10

        self.cont2_2 = Frame(master)
        self.cont2_2['padx'] = 110
        self.cont2_2['pady'] = 10

        self.cont3_1 = Frame(master)
        self.cont3_1['padx'] = 110

        self.cont3_2 = Frame(master)
        self.cont3_2['padx'] = 110

        self.titulo = Label(self.cont1, text='API MUNDO DEV')
        self.titulo['font'] = 'Arial Black', 30
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
        self.msg_verificacao.pack(side=TOP)

        self.apagar = Button(self.cont3, height=1, width=14, text="Apagar Dados", font='Arial')
        self.apagar['command'] = self.apagar_data
        self.apagar.pack(side=TOP)

        self.dados_salvos = Button(self.cont4, height=1, width=14, text="Lista de dados", font='Arial')
        self.dados_salvos['command'] = self.pagina_2
        self.dados_salvos.pack(side=LEFT)

    def executar(self):
        """está função é a parte principal é ela que busca o IP com a IPI API
        e depois salva os dados em uma planilha excel"""
        from main import API
        ip = self.ip.get()
        dados = API.buscar_dados(ip)

        if dados['status'] == 'fail':
            self.msg_verificacao['text'] = f'O IP {ip} é invalido. {dados["message"]}'
        else:
            self.msg_verificacao['text'] = f'O IP {ip} foi salvo com sucesso'
            API.salvar_dados(ip, dados, "database.xlsx")

    def apagar_data(self):
        """Está função apaga a planilha excel"""
        try:
            from main import API
            API.del_data("database.xlsx")
        except FileNotFoundError:
            pass

    def pagina_2(self):
        """Está função mostra a pagina onde estão todos os IPs ja pesquisados e salvos"""
        import pandas as pd
        from functools import partial
        try:
            read = pd.read_excel('database.xlsx')
        except FileNotFoundError:
            pass
        self.cont1.destroy()
        self.cont2.destroy()
        self.cont3.destroy()
        self.cont4.destroy()

        self.cont2_1.pack()
        self.cont2_2.pack()

        self.voltar = Button(self.cont2_1, text='Voltar')
        self.voltar['command'] = self.__init__
        self.voltar.pack()

        try:
            self.butaoip = list(range(0, len(read)))
            for n, ip in enumerate(read['IP']):

                self.butaoip[n] = Button(self.cont2_2, text=f'{ip}')
                self.butaoip[n]['command'] = partial(self.pagina_3, n)
                self.butaoip[n].pack()
        except UnboundLocalError:
            pass

    def pagina_3(self, i):
        """Está função mostra a pagina onde estão os dados de cada IP"""
        import pandas as pd
        from ast import literal_eval
        read = pd.read_excel('database.xlsx')
        try:
            self.cont2_1.destroy()
            self.cont2_2.destroy()
        except AttributeError:
            pass

        self.cont3_1.pack()
        self.cont3_2.pack()

        self.voltar1 = Button(self.cont3_1, text='Voltar')
        self.voltar1['command'] = self.__init__
        self.voltar1.pack()

        dados0 = read['Dados'].tolist()
        dados = literal_eval(dados0[i])
        for c, d in dados.items():
            self.dados = Label(self.cont3_2, text=f'{c}: {d}')
            self.dados['font'] = 'Arial Black', 12
            self.dados.pack()


root = Tk()
root.title('API MUNDO DEV - By Douglas FJ')
#root.iconbitmap('icone.ico')
App(root)
root.mainloop()
