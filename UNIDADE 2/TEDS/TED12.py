import random

matriza = []

for c in range(10):
    matrizaa = []
    for y in range(10):
        matrizaa.append(random.randint(0, 100))
    
    matriza.append(matrizaa)

for v in matriza:
    print(v)

print('\n \n')

s = 0

for x in matriza:
    for h in x:
        s += h

print(f'A soma dos valores da matriz A é: {s}')

matrizb = []

for a in range (0, len(matriza)):

    matrizbb = []

    for b in range (0, len(matriza[a])):

        mult = matriza[a][b] * 3
        matrizbb.append(mult)

    matrizb.append(matrizbb)

print(matrizb)





