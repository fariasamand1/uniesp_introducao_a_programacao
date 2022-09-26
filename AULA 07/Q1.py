compra = int(input("Quantas maçãs você quer comprar?"))

if compra >= 12:
    resultado = compra * 1.0
    print(f"Comprei {compra} maçãs por {resultado}!")

else:
    resultado = compra * 1.30
    print(f"Comprei {compra} maçãs por {resultado}")

    #oi