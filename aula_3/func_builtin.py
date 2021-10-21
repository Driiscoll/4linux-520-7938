print(1, 2, 4,8 , 16, 32, sep =", ", end=". \n\n\n")

#print(input("digite: "))

frutas = 'Banana Melancia Morango Uva Caju Pera Maçã'.split()
print(frutas)

for (i, fruta) in enumerate(frutas, start=10):
    print(i, fruta, sep=': ')