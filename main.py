import tkinter as tk
from tkinter import ttk

from calculadora import Calculadora


class Calculadora:
    @staticmethod
    def somar(num1, num2):
        return num1 + num2

    @staticmethod
    def maiorNumero(num1, num2):
        if num1 == num2:
            return 'Os dois números são iguais'
        if num1 > num2:
            return f'O maior número é {num1}'
        else:
            return f'O maior número é {num2}'

    @staticmethod
    def diferenca(numero1, numero2):
        return abs(numero1 - numero2)

def calcular():
    texto_maior_numero = Calculadora.maiorNumero(int(numero1.get()), int(numero2.get()))
    resultado_maior_label.config(text=texto_maior_numero)

    soma = Calculadora.somar(int(numero1.get()), int(numero2.get()))
    resultado_soma_label.config(text=f'A soma dos dois números é: {soma}')

    diferenca = Calculadora.diferenca(int(numero1.get()), int(numero2.get()))
    resultado_diferenca_label.config(text=f'A diferença entre os dois números é: {diferenca}')

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry('800x400')

# Criando as caixas de entrada
numero1 = ttk.Entry(janela)
numero1.pack()
numero2 = ttk.Entry(janela)
numero2.pack()

# Criando o botão
botao_calcular = ttk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack()

# Criando um label para mostrar o maior número
resultado_maior_label = ttk.Label(janela, text="")
resultado_maior_label.pack()

# Criando um label para mostrar o resultado da soma
resultado_soma_label = ttk.Label(janela, text="")
resultado_soma_label.pack()

# Criando um label para mostrar a diferença entre os dois números
resultado_diferenca_label = ttk.Label(janela, text="")
resultado_diferenca_label.pack()

# Iniciando a aplicação
janela.mainloop()
