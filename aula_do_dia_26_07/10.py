# números não tratados!
valor = int(input("Digite um número inteiro. (positivo pelo amor dos números): "))
tab = ""
for x in range(1,11):
    tab += f"{valor}*{x}={valor*x}\n"
# estou usando input pra fazer o script parar com os resultados na tela, deve ter alguma função pra isso, mas eu não sei qual.
input (tab)