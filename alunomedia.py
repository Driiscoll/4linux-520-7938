nota1 = int(input("digite a primeira nota"))
nota2 = int(input("digite a segunda nota"))
nota3 = int(input("digite a terceira nota"))

media = (nota1 + nota2 + nota3)/3

if media >= 6:
    print("Aluno aprovado")

elif media >= 4:
    print("aluno ficará em recuperação")

elif media < 4 and media > 0:
    print("aluno reprovado")