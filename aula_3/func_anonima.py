def eh_par(numero):
    return numero % 2 == 0

eh_impar = lambda numero: numero % 2 != 0


valores = [1,2,3,4,5,6,7,8,9,]

pares = list(filter(eh_par, valores))
impares = list(filter(lambda numero: numero % 2 != 0 , valores))

print(pares)
print(impares)

def somar(a):
    return lambda b: a + b

somar2 = somar(2)
print(somar2(3))
print(somar(13)(7))