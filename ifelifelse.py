habilitado = input("Você é habilitado? ").lower().strip()

if habilitado.lower().startswith('s') == 'sim':
    print("Você pode dirigir!")

elif habilitado.lower().startswith('n'):
    print("Você não deve dirifigir")

elif habilitado.find('s') != -1:
    print("Acho que você pode dirigir...")

else:
    print("não entendi")