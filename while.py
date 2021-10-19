valor = 10

while valor > 0:
    valor -= 1
    if valor % 2!=0:
        continue

    if valor == 0:
        break

    print("Valor: ", valor)

else:
    print("fim do loop")


print("Fora do loop!")

