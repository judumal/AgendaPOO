from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Classe Agenda
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, pessoa):
        self.contatos.append(pessoa)

    def buscar_contato(self, nome):
        resultados = []
        for contato in self.contatos:
            if nome.lower() in contato.nome.lower():
                resultados.append(contato)
        return resultados

    def excluir_contato(self, contato):
        if contato in self.contatos:
            self.contatos.remove(contato)



