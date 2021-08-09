from datetime import date
from random import randrange
dia_str = date.today().strftime("%d%m%Y") # essa linha gera uma string com a data atual. Tentando manter sempre o mesmo número de dígitos.
banco = "341-7"
numero = str(randrange(1000, 10000))# essa linha gera um número aleatório de 1000 a 9999, desse modo todos os números de boletos terão 4 dígitos, criando um padrão.
valor = input("digite o valor do boleto. (no máximo 9999.99)") #o valor não é tratado, então se você digitar um valor acima de 9999, só vai quebrar o padrão de dígitos, mas deve funcionar normalmente.
valor = float(valor)
print(f"o código do seu boleto é: {banco+numero} {dia_str}00000000{valor:{0}{7}.{2}f}") # esse último bloco de chaves com vários aninhados é uma aplicação da Format Specification Mini-Language do python.