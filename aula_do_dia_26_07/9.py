# Eu tenho que falar? Sim, os números não são tratados.
metros = float(input("digite um valor. (em metros): "))
centimetros = int(metros*100)
# tiramos um pouco de dígitos assim e de quebra transformamos em int.
milimetros = centimetros*10
# eu sei que se eu digitar 0.01 metros vou ter 1 centímetros ao invés de 1 centímetro
print (f"{metros} metros equivalem a {centimetros} centímetros ou {milimetros} milímetros.")