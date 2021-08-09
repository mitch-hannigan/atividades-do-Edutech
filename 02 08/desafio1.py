# vou usar orientação a objétos para facilitar a minha vida. Vale destacar que eu dividiria em arquivos também, mas não estou fazendo isso aqui para simplificar.
from random import randrange
class Funcionario:
    def __init__(self):
        self._nome = input("digite o nome do funcionário.")
        self._salario = float(input(f"digite o salário do funcionário {self._nome}"))
    def almentar(self, percent):
        self._salario+=self._salario*percent
    def diminuir(self, percent):
        self._salario-=self._salario*percent
funcionarios = []
while(len(funcionarios)<10):
    funcionarios.append(Funcionario())
    if (len(funcionarios)%3==0):
        for i in funcionarios:
            i.almentar(0.05)
funcionarios[randrange(0, len(funcionarios))].almentar(0.1)
final = "nome, salário\n"
for i in funcionarios:
    final += f"{i._nome}, {i._salario:.{2}f}\n"
print (final)