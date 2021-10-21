

def somar (*valores):
    soma = 0
    # tupla sendo somada em um 'for'
    for num in valores:
        soma += num

    return soma

#def subtrair(a, b):
 #   return a - b


def montar_nome(*nomes, **opcoes):

    return opcoes.get('sep', ' ').join(nomes)
