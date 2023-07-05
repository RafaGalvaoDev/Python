saldo = saque = saque_Diario = 0
extrato = []
while True:
    print("Bem-Vindo ao Banco DI0")
    print("""Escolha a operação do dia! 
    1- Deposito
    2- Saque
    3- Extrato
    0- Sair""")
    operacao = int(input("Digite a operação: "))
    if operacao == 1:
        deposito_Valor = float(input("Digite o valor do Deposito: "))
        saldo += deposito_Valor
        print(f"O valor depositado foi R${saldo:.2f}")
    elif operacao == 2:
        saque_Valor = float(input("Digite o valor do saque: "))
        if saque_Diario >= 3:
            print("Saques diarios estrapolados, volte amanhã")
            print(f"Saldo atual R${saldo:.2f}")
        elif saque_Valor > 500:
            print("Você só pode sacar 500R$ por dia")
            print(f"Saldo atual R${saldo:.2f}")
        elif saque_Valor > saldo:
            print("Valor inválido, você não tem dinheiro suficiente")
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            saldo -= saque_Valor
            saque_Diario += 1
            extrato.append(f"Saque: R${saque_Valor:.2f}")
            print(f"Saldo atual R${saldo:.2f}")
    elif operacao == 3:
        for valor in extrato:
            print(valor)
        print(f"Seu saldo atual é {saldo}")


    deseja_Continuar = input("Sim/Não: ").strip().upper()[0]
    if deseja_Continuar == "N":
        print("Volte sempre, Até mais.")
        break
