habilitado = input("Você é habilitado? ").lower()

if habilitado.lower().startswith('s') == 'sim':
    print("Você pode dirigir!")

elif habilitado.lower().startswith('n'):
    print("Você não deve dirifigir")
