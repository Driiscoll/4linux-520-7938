ano_nasc = int(input("Digite o ano do seu nascimento: "))

if ano_nasc <= 1964:
    print("Baby Boomer")

elif ano_nasc >= 1965 and ano_nasc <=1979:
    print("Geração: X")

elif ano_nasc >= 1980 and ano_nasc <= 1994:
    print("Geração: Y")

else:
    print("Geração: Z")