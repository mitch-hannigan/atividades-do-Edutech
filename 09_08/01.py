#randomiza um número de 1 a 100, e pede para o usuário tentar adivinhar, dando a ele 5 tentativas.
from random import randrange
numero = randrange(1, 100)
tentativa_atual = 1
max_tentativas = 7
while (tentativa_atual<=max_tentativas):
    chute = input("digite um número, de 1 a 99")
    if (chute.isdigit()):
        chuteint = int(chute)
    else:
        print("erro, valor inválido")
        continue
    if(numero>chuteint):
        print("o número é maior")
    elif (numero<chuteint):
        print("o número é menor")
    else:
        print("parabéns! Você acertou!")
        break
    tentativa_atual+=1