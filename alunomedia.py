nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
nota3 = float(input("digite a terceira nota"))

media = (nota1 + nota2 + nota3)/3

if media > 6:
    print("Aluno aprovado")

elif media >= 4:
    print("aluno ficará em recuperação")

elif media < 4:
    print("aluno reprovado")