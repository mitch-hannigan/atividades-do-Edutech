# Os valores não são verificados antes da converção.
altura = float(input("digite a altura da parede. (em metros)"))
largura = float(input("digite a largura da parede. (em metros)"))
area = largura*altura
print(f"Você vai precisar no mínimo {area/2} litros de tinta.")