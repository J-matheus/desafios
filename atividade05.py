soma=0
notas=[]*4
for x in range(0,4):
    nota =float(input("Informe as notas do aluno: "))
    notas.append(nota)

soma = notas[0] + notas[1] + notas[2] + notas[3]
media = soma / 4
if media>=7:
    print(f"Com a nota {media}, O aluno está aprovado.")
elif media>=5 and media<=6:
    print(f"Com a nota {media}, o aluno está de recuperação.")
else:
    print(f"Com a nota {media}, o aluno está reprovado.")