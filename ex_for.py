string = input("> ")

for i in string:
    if i.lower():
        print(i, " é um caracter minusculo")
    elif i.upper():
        print(i, " é um caracter maisculo")
    elif i.numeric():
        print(i, " é um numero")
    else:
        print(i, " é um simbolo ou acento")