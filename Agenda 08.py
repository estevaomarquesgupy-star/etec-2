nome = input ("Boas Vindas cidadão, por gentileza informe o seu nome: ")
print("Olá,", nome, "! Seja bem-vindo à Pesquisa de satisfação.")

idade = int(input("Por favor, informe a sua idade: "))

Opiniao = int(input("Por Gentileza qual sua satisfação com nosso serviço (1-Excelente, 2-Bom, 3-Ruim): "))

if Opiniao == 1 or Opiniao == 2:
    print("Agradecemos seu retorno, sua opinião é muito importante para nós!")

elif Opiniao == 3:
    resposta = int(input("Pedimos desculpas pelo transtorno, estaremos trabalhando para melhorar nosso serviço, gostaria de um brinde para compensar? (1-Sim, 2-Não): "))

    if resposta == 1:
        print("Ótimo! Você receberá um brinde em breve em sua residência.")

        if resposta == 2:
            print("Agradecemos seu retorno, iremos trabalhar para melhorar nosso atendimento, tenha um bom dia")

            

    


        