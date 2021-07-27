# programa que soma 2 números digitados pelo usuário. Verificações numéricas não são efetuadas antes da conversão, por causa disso, um erro ocorrerá em caso de ser digitado valores não numéricos.
valor1 = float(input("digite o primeiro número. Pode ser um valor negativo ou positivo, com ou sem casas decimais."))
valor2 = float(input("digite o segundo número. Pode ser um valor negativo ou positivo, com ou sem casas decimais."))
print (f"a soma dos valores {valor1} e {valor2} resulta {valor1+valor2}")