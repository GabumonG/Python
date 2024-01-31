""" PRIMEIRO EXEMPLO
nome = input ("Digite seu nome: ")
idade = int(input ("Digite sua idade: "))
peso = float(input ("Digite seu peso: "))

print (nome)
print (type(idade))
print (type(peso))
"""
"""OPERADORES
soma = 1 + 1
multiplicacao = 3 * 3
divisao = 30 / 3
potencia = 7 ** 2

print ("Soma", soma)
print ("Multiplicação", multiplicacao)
print ("Divisão", divisao)
print ("Potencia", potencia)
"""
"""CONDIÇÕES
#idade = int(input("Digite sua idade:"))
#
#if idade >= 18:
#    print("Liberado!")
#else:
#    print("Bloqueado!")

salario = float(input("Digite seu salario: "))

if salario <= 3000:
    print("Programador Junior!")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno!")
elif salario > 6000 and salario <= 15000:
    print("Programador Senior!")
else:
    print("Gerente de Projetos!")
"""
"""LISTA
lista = [0, 1, 2]

lista [0] = 5

print (lista[0])
print (lista[1])
print (lista[2])
"""
"""DESAFIO 1:
def media (nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

while True:
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    nota3 = float(input("Digite a terceira nota:"))

    resultado_media = media(nota1, nota2, nota3)
    print("Média = ", resultado_media)

    if resultado_media < 4:
        print("Reprovado!")
    elif resultado_media >= 4 and resultado_media < 6:
        print("Recuperação!")
    else:
        print ("Aprovado!")
"""
"""DESAFIO 2
import math

def soma (valor1, valor2):
    return valor1 + valor2

def subtracao (valor1, valor2):
    return valor1 - valor2

def multiplicacao (valor1, valor2):
    return valor1 * valor2

def divisao (valor1, valor2):
    return valor1 / valor2

def potenciacao (valor1, valor2):
    return valor1 ** valor2

def radiciacao (valor1):
    return math.sqrt(valor1)

mensagem = ""Escolha uma opção:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potenciação
6 - Radiciação
"" //ocultado aspas duplas para que o comentário fosse possível, se for executar, adicionar uma aspas duplas no começo e fim da mensagem
opcao = int(input(mensagem))

valor1 = float(input("Digite um valor: "))

if opcao != 6:
    valor2 = float(input("Digite outro valor: "))

if opcao == 1:
    resultado = soma(valor1, valor2)
    print ("Resultado = ", resultado)
elif opcao == 2:
    resultado = subtracao(valor1, valor2)
    print ("Resultado = ", resultado)
elif opcao == 3:
    resultado = multiplicacao(valor1, valor2)
    print ("Resultado = ", resultado)
elif opcao == 4:
    resultado = divisao(valor1, valor2)
    print ("Resultado = ", resultado)
elif opcao == 5:
    resultado = potenciacao(valor1, valor2)
    print ("Resultado = ", resultado)
else:
    resultado = radiciacao(valor1)
    print ("Resultado = ", resultado)
"""

import os

nome_arquivo = input("Antes de tudo, crie um arquivo e dê um nome a ele: ")
with open(nome_arquivo, 'w') as arquivo:
    conteudo = arquivo.write(input("O que quer escrever nele? Digite algo: "))

mensagem = """O que quer fazer com esse arquivo criado:
1 - Read
2 - Update
3 - Delete
"""
opcao = int(input(mensagem))

if opcao == 1:
    with open(nome_arquivo, 'r') as leitura:
        print(conteudo)

elif opcao == 2:
    with open(nome_arquivo, 'a') as atualizar:
        conteudo = atualizar.write(input("Digite o que quer atualizar no arquivo: "))
        print(conteudo)
elif opcao == 3:
    try:
        os.remove(nome_arquivo)
        print(f'O arquivo {nome_arquivo} foi removido com sucesso!')
    except FileNotFoundError:
        print(f'O arquivo "{nome_arquivo}" não foi encontrado.')
    except PermissionError:
        print(f'Não foi possível excluir o arquivo "{nome_arquivo}". Permissão negada.')
    except Exception as e:
        print(f'Ocorreu um erro ao excluir o arquivo: {e}')
