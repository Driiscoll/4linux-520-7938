cesta = {

}

quitanda = {
    'Banana': 3.50,
    'Melancia': 7.50,
    'Morango': 5.00
}

while True:
    print()
    print("-" *10)
    print("Bem-vindo à quintada Pynthera")
    print("1: Ver Cesta")
    print("2: Adicionar Frutas")
    print("3: Checkout")
    print("4: Sair")

    entrada = int(input('Digite a opção desejada: '))

    if  entrada == 1:
        print(cesta)
    
    elif entrada == 2:
        quitanda_ks = list(quitanda.keys())
        while True:
            for (i, fruta) in enumerate(quitanda):
                print(f"{i}: {fruta}")
            print('-1: Sair')

            entrada = int(input("Digite a fruta/opção desejada: "))            

            if entrada == -1:
                break
            
            elif 0 <= entrada < len(quitanda_ks):
                fruta = quitanda_ks[entrada]
                cesta[fruta] = cesta.get(fruta, 0) + 1

            else:
                print("digite uma opção valida.")

    elif entrada ==3:
        print("cesta: ", cesta)

        total = 0
        for(fruta, quantidade) in cesta.items():
            total += quantidade * quitanda[fruta]
        
        print(f"Total: R$ {total}")

    elif entrada == 4:
        print("até Logo!")
        break