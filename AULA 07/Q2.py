ano = int(input("Em que ano você nasceu?"))

resultado = 2022 - ano

if resultado >= 16:
    print(f"Você tem {resultado} anos. Logo, você pode votar neste ano!")
else:
    print(f"Você tem {resultado} anos. Logo, você não pode votar neste ano!")