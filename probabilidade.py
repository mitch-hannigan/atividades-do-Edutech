# esse programa mostra quantas vezes você deve matar um inimigo em um jogo para ter uma certa chanse de ganhar um item.
# algumas coisas importantes, o resultado não é matematicamente perfeito, afinal, quem vai matar 1.5 inimigos?
# eu também fiz o arredondamento da porcentagem, isso foi uma escolha minha, e pode ser desfeito a qualquer momento.
from math import ceil
def calcula_chanse(vezes, total, vezes_matou):
    valor=vezes*vezes_matou
    # não quero porcentagens com casas decimais. Algum problema?
    return int((valor/total)*100)
def calcula_kills(vezes, total, porcentagem):
    # não se pode matar um inimigo e meio, ou pode?
    return ceil(((porcentagem/100)*total)/vezes)
def cria_tabela(vezes, total, porcentagens):
    final="porcentagem, número de kills"
    for i in porcentagens:
        final+=f"\n{i}%, {calcula_kills(vezes, total, i)}"
    return final
chanse = input("digite qual é a chanse de obter o item. (escreva no formato de frações.)")
matou = int(input("quantas vezes você matou esse inimigo?"))
vezes, total = chanse.split("/")
vezes, total=int(vezes), int(total)
# eu não preciso mais da variável chanse, então ela será substituída mas por uma boa causa.
chanse=calcula_chanse(vezes, total, matou)
print(f"você matou {matou} inimigos, isso te da uma chanse de {chanse}% de obter o item.")
# muito bem, agora vem a parte legal, fazer uma tabela repleta de números.
# ha ha, a função criadora de tabelas está no topo do código.
print(cria_tabela(vezes, total, [40, 50, 60, 70, 80, 90, 95, 97]))