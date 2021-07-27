# programa que soma 2 números digitados pelo usuário  e mostra o antecessor e o sucessor. Verificações numéricas não são efetuadas antes da conversão, por causa disso, um erro ocorrerá em caso de ser digitado valores não numéricos.
valor1 = int(input("digite o primeiro número. Pode ser um valor negativo ou positivo, sem casas decimais."))
valor2 = int(input("digite o segundo número. Pode ser um valor negativo ou positivo, sem casas decimais."))
resultado = valor1+valor2
print(f"A soma dos valores {valor1} com {valor2} resulta {resultado}, o antecessor desse número é: {resultado-1} e o sucessor desse número é: {resultado+1}")