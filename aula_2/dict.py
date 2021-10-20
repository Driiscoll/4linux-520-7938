telefones = {
    'Fabricio': '123456789',
    'Luciano': '987654321',
    'Leonardo': '231654987'
}

print (telefones)

for nome in telefones:
    print(nome, telefones[nome])

print(telefones['Luciano'])
print(telefones.get('Diego'))
print(telefones.get('Fabricio'))

telefones['Veronica'] = '85165476'

for (nome, telefone) in telefones.items():
    print(telefone, " é o nomero do", nome)

print(telefones.setdefault('Gustavo', '7451594765'))
print(telefones)
print(telefones.setdefault('Veronica', '85165476'))
telefones.update({
    'Marcus': '121654432165',
    'Edilson': None
})