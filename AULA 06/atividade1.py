# Exemplo while
abacate = 1

while abacate <= 10:
    print(abacate)
    abacate += 1

# Exemplo for
for abacaxi in range (1,11, 1):
    print(abacaxi)

# Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando dividivos por 11, produzam o resto igual a 5

for num in range(1000, 2001):
    if (num % 11) == 5:
        print(num)

# Faça um programa que mostre as tabuadas dos números de 1 a 10
for num in range(1,11):
    print(f"Tabuada de {num}")

    for num2 in range(1,11):
        resultado = num * num2
        print(f"{num} x {num2} = {resultado}")

# Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada pessoa acessando cada elemento da lista um de cada vez.
list_friends = ["Amanda", "Talita", "Joana", "Symone", "Isabelly"]
for nome in list_friends:
    print(f"Obrigada por vir a aula, {nome}")

# Faça um programa que receba um número e que calcule e mostre a tabuada desse número
numero = int(input("Digite um numero"))

for num in range(1,11):
    resultado = (num)*(numero)
    print(f"{num} x {numero} = {resultado}")

# Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.

list_friends = ["Amanda", "Talita", "Joana", "Symone", "Isabelly"]
for name in list_friends:
    print(f"Olá, {name}! Como você está?")

#Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
#Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
#Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
#Modifique sua lista, substitua os desistentes por novos convidados.
#Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados = [
    "Coringa", "Thor", "Jesus", "Naruto", "Loki"
]

# Convite
for nome in convidados:
    mensagem = f"Bora pra balada, {nome.upper()}!"
    print(mensagem)

# Quem não poderá ir
print("Jesus: Infelizmente não \
    posso estar no mesmo ambiente que o Loki!")

print("Coringa: Infelizmente não \
    posso estar no mesmo ambiente que o Naruto!")

# Modifique sua lista, substitua os
# desistentes por novos convidados.
convidados[2] = "Madre Tereza"
convidados[0] = "Pinguim"

# Convite
for nome in convidados:
    mensagem = f"Bora pra balada, {nome.upper()}!"
    print(mensagem)

# Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora

print("Olá! Realize o seu cadastro!")

nome = input("Informe o seu nome")
idade = int(input("Informe a sua idade"))
email = input("Informe o seu e-mail")

print("Seu cadastro foi realizado!")

   
