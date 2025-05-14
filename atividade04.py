soma=0
cont = 0
while True:
    nota =float(input("Informe as notas do aluno: "))
    soma += nota
    cont+=1
    if cont==4:
        break
media=soma/4
if media>=7 and media<=10:
    print(f"Com a nota {media}, O aluno está aprovado.")
elif media>=5 and media<=6:
    print(f"Com a nota {media}, o aluno está de recuperação.")
else:
    print(f"Com a nota {media}, o aluno está reprovado.")