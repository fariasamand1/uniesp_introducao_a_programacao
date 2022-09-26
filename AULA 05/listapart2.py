# ESTRUTURAS DE SELEÇÃO

#Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

numero = int(input("Digite um número, por favor"))

if numero > 10:
    print("Este número é maio que 10")

elif numero == 10:
    print("Esté núemro não é maior e menor que 10")

else:
    print("Este número é menor que 10")

# Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor zero como positivo).

num = float(input("Digite um número, por favor"))

if numero >= 0:
    print(f"Este número {num} é positivo")

else:
    print(f"Este número {num} é negativo")
   

# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

macas = int(input("Quantas maçãs você quer?"))

if macas >= 12:
    resultado = macas * 1
    print(f"Comprei {macas} por R${resultado}")

else:
    resultado = macas * 1,30
    print(f"Comprei {macas} por R${resultado}")



