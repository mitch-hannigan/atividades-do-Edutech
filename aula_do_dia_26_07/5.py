# programa cheio dos infames if. Não seria ifames, ele vai dizer qual o tipo de valor que você digitou.
# desculpe pela piada acima, falta do que fazer faz isso.
valor = input("digite alguma coisa, eu vou falar que tipo de coisa você digitou.")
if (valor==""):
    print ("você digitou minha vida! Já que ela também é um nada absoluto.")
elif (valor.isalpha()):
    print("você digitou letras, aka alfa, ou alpha. EU JÁ FALEI QUE NÃO É IMPORTANTE!!!! Calma Calma Calma, não bate em mim não pleaseeeeeeeeeeeeeee")
# estou usando aspas nas linhas abaixo já que eu teria duas opções, converter a variável, ou usar strings diretamente.
elif (valor=="1" or valor=="2" or valor=="3"):
    print (f"a lei da robótica número {valor} diz que: calma, calma, calma, eu sei que você não quer saber a lei número {valor} da robótica.")
elif (valor=="42"):
    print ("gostei de você, você sabe a resposta final!")
elif (valor.isdigit()):
    print ("você digitou números, valores numéricos, digitos da linha acima da linha das letras qwertyuiop, coisas muito usadas no dia dia, algo que não é texto... Ele terminou, já entendi que o que eu digitei é um número. Mas eu os chamo de mine matemáticos. Mine matemáticos, isso é sério? Não, chamo eles de senha de 6 dígitos. Elas geralmente são numéricas.")
elif (valor.isalnum()):
    print ("você digitou um valor que tem letras e números, eu falaria o nome disso, mas não sei escrever, algo do tipo alfa numérico. Eu acho que é isso. Ou seria alpha numeric, não é importante!")
else:
    print ("Eu não sei o que você digitou. Talvês eu seja meio burro.")