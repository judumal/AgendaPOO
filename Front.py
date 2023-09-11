from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from PIL import *
from Agenda import Agenda
from Pessoa import Pessoa

# Cores
white = "#FFFFFF"
amarelinho = "#FFFFE0"
verdinho = "#a3ffac"
roxinho = "#dfcae1"
rosinha = "#fabfb7"
azulzinho = "#b2e2f2"
laranjinha = "#ffda9e"

class Interface:
    def __init__(self):
        # Criando uma instância da classe Agenda
        self.minha_agenda = Agenda()

        # Criando a janela
        janela = Tk()
        janela.title("MINHA AGENDA")
        janela.geometry('600x600')
        janela.configure(background=amarelinho)
        janela.resizable(width=FALSE, height=FALSE)
        #janela.iconbitmap("icon.ico")

        # Frames
        frame_cima = Frame(janela, width=600, height=60, bg=laranjinha, relief="flat")
        frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        frame_baixo = Frame(janela, width=600, height=150, bg=amarelinho, relief="flat")
        frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        frame_tabela = Frame(janela, width=600, height=248, bg=white, relief="flat")
        frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, sticky=NSEW)

        title = Label(frame_cima, text='CONTATOS', anchor=NE, font=('candara 25 bold'), bg=laranjinha, fg="#fa8072")
        title.place(x=230, y=7)

        # Campos de entrada
        name = Label(frame_baixo, text="NOME: ", font="Calibri 10 bold", bg=amarelinho)
        name.place(x=1, y=10)
        self.nomeContato = Entry(frame_baixo, width=30, font=('roboto', 10))
        self.nomeContato.place(x=65, y=10)

        sex = Label(frame_baixo, text="SEXO: ", font="Calibri 10 bold", bg=amarelinho)
        sex.place(x=300, y=10)
        self.sexoContato = Entry(frame_baixo, width=30, font=('roboto', 10))
        self.sexoContato.place(x=350, y=10)

        fone = Label(frame_baixo, text="TELEFONE: ", font="Calibri 10 bold", bg=amarelinho)
        fone.place(x=1, y=40)
        self.telefoneContato = Entry(frame_baixo, width=30, font=('roboto', 10))
        self.telefoneContato.place(x=65, y=40)

        mail = Label(frame_baixo, text="EMAIL: ", font="Calibri 10 bold", bg=amarelinho)
        mail.place(x=300, y=40)
        self.emailContato = Entry(frame_baixo, width=30, font=('roboto', 10))
        self.emailContato.place(x=350, y=40)

        # Campo de busca
        Label(frame_baixo, text='BUSCAR POR NOME:', font=('Calibri 10 bold'), bg=amarelinho, fg='black').place(x=80, y=70)
        self.nomeBusca = Entry(frame_baixo, width=30, font=('roboto', 10))
        self.nomeBusca.place(x=210, y=70)

        # Botões
        Button(frame_baixo, text='ADICIONAR', font=('roboto 10 bold'), bg=verdinho, fg='black', relief=RAISED,
               overrelief=GROOVE, command=self.adicionar_contato).place(x=60, y=105)
        Button(frame_baixo, text='BUSCAR', font=('roboto 10 bold'), bg=roxinho, fg='black', relief=RAISED,
               overrelief=GROOVE, command=self.buscar_contato).place(x=180, y=105)
        Button(frame_baixo, text='EDITAR', font=('roboto 10 bold'), bg=laranjinha, fg='black', relief=RAISED,
               overrelief=GROOVE, command=self.editar_contato).place(x=275, y=105)
        Button(frame_baixo, text='EXCLUIR', font=('roboto 10 bold'), bg=rosinha, fg='black', relief=RAISED,
               overrelief=GROOVE, command=self.excluir_contato).place(x=370, y=105)
        Button(frame_baixo, text='LISTAR', font=('roboto 10 bold'), bg=azulzinho, fg='black', relief=RAISED,
               overrelief=GROOVE, command=self.listar_contatos).place(x=470, y=105)

        # Tabela
        list_header = ['NOME', 'SEXO', 'TELEFONE', 'E-MAIL']
        self.tree = ttk.Treeview(frame_tabela, columns=list_header, show="headings")
        rolaVertical = ttk.Scrollbar(frame_tabela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=rolaVertical.set)

        self.tree.grid(column=0, row=0, sticky='nsew')
        rolaVertical.grid(column=1, row=0, sticky='ns')

        self.tree.heading(0, text="NOME", anchor=CENTER)
        self.tree.heading(1, text="SEXO", anchor=CENTER)
        self.tree.heading(2, text="TELEFONE", anchor=CENTER)
        self.tree.heading(3, text="EMAIL", anchor=CENTER)
        self.tree.column(0, width=220, anchor='nw')
        self.tree.column(1, width=100, anchor='nw')
        self.tree.column(2, width=120, anchor='nw')
        self.tree.column(3, width=120, anchor='nw')

        #imgcontatos = PhotoImage(file="contatos.png")
        #painel = Label(janela, image=imgcontatos, bg=amarelinho)
        #painel.place(x=250, y=470)

        janela.mainloop()

    # Função para atualizar a tabela
    def atualizar_treeview(self, contatos=None):
        self.tree.delete(*self.tree.get_children())
        contatos_list = contatos if contatos else self.minha_agenda.contatos
        for contato in contatos_list:
            self.tree.insert("", "end", values=(contato.nome, contato.sexo, contato.telefone, contato.email))

    # Função para limpar campos
    def limpar_campos(self):
        self.nomeContato.delete(0, END)
        self.sexoContato.delete(0,END)
        self.telefoneContato.delete(0, END)
        self.emailContato.delete(0, END)
        self.nomeBusca.delete(0, END)

    # Função para adicionar contato
    def adicionar_contato(self):
        nome = self.nomeContato.get()
        sexo = self.sexoContato.get()
        telefone = self.telefoneContato.get()
        email = self.emailContato.get()

        novo_contato = Pessoa(nome, sexo, telefone, email)
        self.minha_agenda.adicionar_contato(novo_contato)

        self.limpar_campos()

    # Função para buscar contato
    def buscar_contato(self):
        nome = self.nomeBusca.get()
        resultados = self.minha_agenda.buscar_contato(nome)
        self.atualizar_treeview(resultados)

    # Função para excluir contato
    def excluir_contato(self):
        item_selecionado = self.tree.selection()
        if item_selecionado:
            nome_contato_selecionado = self.tree.item(item_selecionado)["values"][0]
            contato_selecionado = None
            for contato in self.minha_agenda.contatos:
                if contato.nome == nome_contato_selecionado:
                    contato_selecionado = contato
                    break
            if contato_selecionado:
                self.minha_agenda.excluir_contato(contato_selecionado)
                self.atualizar_treeview()
                self.limpar_campos()

    # Função para editar contato
    def editar_contato(self):
        item_selecionado = self.tree.selection()
        if item_selecionado:
            nome_contato_selecionado = self.tree.item(item_selecionado)["values"][0]
            contato_selecionado = None
            for contato in self.minha_agenda.contatos:
                if contato.nome == nome_contato_selecionado:
                    contato_selecionado = contato
                    break
            if contato_selecionado:
                # Abra uma nova janela para editar o contato
                editar_janela = Toplevel()
                editar_janela.title("Editar Contato")

                Label(editar_janela, text="EDITAR DADOS: ", font=('roboto 10 bold')).pack()

                nomeEditar = Entry(editar_janela, width=30, font=('roboto', 10))
                nomeEditar.insert(0, contato_selecionado.nome)
                nomeEditar.pack()

                sexoEditar = Entry(editar_janela, width=28, font=('roboto', 10))
                sexoEditar.insert(0, contato_selecionado.nome)
                sexoEditar.pack()

                telefoneEditar = Entry(editar_janela, width=30, font=('roboto', 10))
                telefoneEditar.insert(0, contato_selecionado.telefone)
                telefoneEditar.pack()

                emailEditar = Entry(editar_janela, width=30, font=('roboto', 10))
                emailEditar.insert(0, contato_selecionado.email)
                emailEditar.pack()

                def salvar_edicao():
                    contato_selecionado.nome = nomeEditar.get()
                    contato_selecionado.sexo = sexoEditar.get()
                    contato_selecionado.telefone = telefoneEditar.get()
                    contato_selecionado.email = emailEditar.get()

                    self.atualizar_treeview()
                    editar_janela.destroy()

                Button(editar_janela, text='SALVAR', font=('roboto 10 bold'), bg=verdinho, fg='black',
                       relief=RAISED, overrelief=GROOVE, command=salvar_edicao).pack()

    # Função para listar contatos
    def listar_contatos(self):
        self.atualizar_treeview(self.minha_agenda.contatos)



# Iniciar a interface
if __name__ == "__main__":
    app = Interface()
