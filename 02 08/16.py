# valores não verificados.
dias = int(input("quantos dias você ficou com o carro?"))
km_rodado = int(input("quantos km você andou com o carro?"))
print(f"você terá de pagar r${dias*60.0+km_rodado*0.15:.{2}f}")