nota1 = int(input("Coloque sua nota 1:"))
nota2 = int(input("Coloque sua nota 2:"))
nota3 = int(input("Coloque sua nota 3:"))
nota4 = int(input("Coloque sua nota 4:"))

resultado = (nota1 + nota2 + nota3 + nota4) / 4

if resultado < 5:
    print("Reprovado")
elif 7>= resultado >= 5:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")