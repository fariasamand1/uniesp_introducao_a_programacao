# 1
a = int(input("Valor de a"))
b = int(input("Valor de b"))
c = int(input("Valor de c"))

delta =b ** 2 - 4 * a * c
print(delta)

if delta > 0:
    x1 = (-b +  delta**0.5) / (2*a)
    x2 = (-b -  delta**0.5) / (2*a)

    print(f"x1 -> {x1:.2f}")
    print(f"x12 -> {x2:.2f}")

else:
    print("Reduza os valores de A e C")

# 2

x1 = int(input("Valor de x1"))
x2 = int(input("Valor de x2"))
y1 = int(input("Valor de y1"))
y2 = int(input("Valor de y2"))

pontos = (x2 - x1)**2 + (y2 - y1)**2

d = pontos**0.5

print(f"A distância é:{d}")

# 3

num1 = int(input("Digite um número inteiro"))
num2 = int(input("Digite outro número inteiro"))

Adicao = num1 + num2
Subtracao = num1 - num2
Multiplicacao = num1 * num2
Divisao = num1 / num2
Potenciacao = num1 ** num2

print(f"O resultado das operaçãos com o números foram: Adição = {Adicao}, Subtração = {Subtracao}, Multiplicação = {Multiplicacao}, Divisão = {Divisao}, Potenciação = {Potenciacao}")

# 4
peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))

imc = peso/altura**2

if imc <= 18.5:
    print("Você está abaixo do peso")

elif imc >= 18.5 and imc <= 25:
    print("Peso normal")

elif imc >= 25 and imc <= 30:
    print("Você está acima do peso")

else:
    print("Você está obeso")


# 5

n = int(input("Quantos números?: "))
i = 0
a = 0
b = 0
c = 0
d = 0

while i < n: 
    numero = int(input("Insira um número: "))
    i = i + 1
    print(i)
    if numero < 0: 
        break
    if numero >= 0 and numero <= 25: 
        a = a + 1
    if numero >= 26 and numero <= 50: 
        b = b + 1
    if numero >= 51 and numero <= 75: 
        c = c + 1
    if numero >= 76 and numero <= 100: 
        d = d + 1
print
("Intervalo1: ",a)
print
("Intervalo2: ",b)
print
("Intervalo3: ",c)
print
("Intervalo4: ",d)


# 6
numero = int(input("Digite um número para calcular o seu fatorial"))
contador = numero
fatorial = 1

while contador > 0:
    print(f"{contador}" , end=" ")
    print("x" if contador > 1 else " = ", end=" ")
    fatorial *= contador
    contador -= 1

print(f"{fatorial}")





