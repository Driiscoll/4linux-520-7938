dados = ('Fabricio', 29, '4Linux')

print(dados[0])
print(dados[1])
print(dados[2])

for dado in dados:
    print("dado é", dado)

(nome, idade, trabalho) = dados
print("nome: ",nome)
print("idade: ",idade)
print("trabalho: ",trabalho)

(cidade, estado, pais) = ('Ubatuba', 'São Paulo', 'Brasil')
print(cidade, estado, pais)

print(dados.count(29))
print(dados.index('4Linux'))

turma = (520, 7938, ['luciano'])
turma[2].append('Saulo')
print(turma)
