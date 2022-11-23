# Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um
# vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a
# mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário

times = []

for c in range (1, 11):
    times.append(str(input(f'Digite um nome para o time {c}')))
busca = (str(input('Qual time de futebol você deseja achar?')))
if busca in times:
    print('Achei')
else:
    print('Não achei')


# Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever
# quantas vezes esse número aparece no vetor.

num = []

for c in range (1, 4):
    num.append(int(input('Digite um núemro:')))
n = (int(input('Digite um número que você deseja pesquisar')))

if n in num:
    num.count(n)
    print(f'O numero aparece {num.count(n)} vezes')
else:
    print('O número não aparece nenhuma vez')
