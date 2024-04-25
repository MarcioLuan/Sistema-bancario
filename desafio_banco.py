menu = """
###### MENU ######
Selecione uma das alternativas:
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair    """

saldo=0
extrato=""
deposito=0
quantidade_saque=0
quantidade_saque_limite=3
valor_saque_limite=500


while True:
    print (menu)
    opcao = int (input ("Informe a operação selecionada: "))

    if opcao ==1:
        deposito = float (input ("Informe o valor do depósito: "))
        if deposito > 0:         
            saldo = saldo + deposito
            extrato = extrato + f"Depósito de R$ {deposito:.2f}\n"
        else:
            print ("O valor de deposito informado não é válido")

    elif opcao == 2:
        saque = float (input("Informe o valor desejado para saque: "))

        excedeu_saldo = saque>saldo

        excedeu_limite = saque>valor_saque_limite

        excedeu_saques = quantidade_saque>=quantidade_saque_limite

        if excedeu_saldo:
            print ("Não foi possível completar o saque! Saldo insuficiente.")

        elif excedeu_saques:
            print ("Não foi possível completar o saque! Você excedeu o limite de 3 saques diários.")

        elif excedeu_limite:
            print ("Não foi possível completar o saque! Você excedeu o limite de R$500.00")

        else:
            saldo = saldo - saque
            extrato = extrato + f"Saque de R$ {saque:.2f}\n"
            quantidade_saque = quantidade_saque + 1

    elif opcao == 3:
        if extrato == "":
            print (f"######EXTRATO######\n{extrato}")
            print ("Não houve movimentações nessa conta")
        else:
            print (f"###EXTRATO###\n {extrato}")
            print (f"O saldo é de R$ {saldo:.2f}")

    elif opcao ==4:
        break
