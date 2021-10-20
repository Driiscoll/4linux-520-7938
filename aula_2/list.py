nomes = [
    'Italo',
    'Vinicius',
    'Edson',
    'Dalton',
    'Paulo',
    'Marcelo',
    'Nincao'
]

nomes_copia = nomes.copy()
nomes_copia.clear()

print('nomes', nomes_copia)
print('index do Edson', nomes.index('Edson'))
nomes.insert(3, 'Fabio')
print("pos insert", nomes)
print('lista popada: ', nomes.pop())
print('pos pop: ',nomes)
print('lista popada (index 2): ', nomes.pop(2))
print('pos pop(index 2): ',nomes)
nomes.remove('Italo')
print('pos remove Italo', nomes)
nomes.reverse()
print('pos reverse: ', nomes)
nomes.sort()
print('pos sort: ',nomes)
nomes.sort(reverse=True)
print('pos sort and reverse: ',nomes)

print("\nSobreviventes")
for nome in nomes:
    print(nome)