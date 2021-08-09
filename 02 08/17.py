from random import randrange
alunos = []
for i in range(0, 4):
    alunos.append(input(f"digite o nome do {i+1}º aluno."))
print(f"o aluno sorteado foi: {alunos[randrange(0, len(alunos))]}")