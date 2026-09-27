#Compra de um tenis

nome = input("Boas vindas consumidor, por gentileza me diga seu nome: ")
print("Olá consumidor,", nome, ", boas vindas a nossa loja, em que posso ajudar? ")

#pagamento

valor = float(input("Qual o valor do tenis que deseja comprar? "))
if valor >= 200:
    print("Parabéns, você recebeu um desconto de 10%!")
    valor = valor * 0.9
    print("O valor final do tenis é: R$", valor)
else:
    print("O valor final do tenis é: R$", valor)

    if valor < 200:
        print(("infelizmente você não recebeu nenhum desconto, mas não se preocupe, temos outros produtos que podem te interessar!"))

if valor > 300:
        if valor > 350:
            print("Parabéns, você recebeu um desconto de 15%!")
            valor = valor * 0.85
print("Compra no valor de R$", valor, "realizada com sucesso!")



#finalizando a compra

print("Obrigado por comprar conosco,", nome, ", volte sempre")