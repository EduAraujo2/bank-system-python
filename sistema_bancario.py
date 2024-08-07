menu = """
----- MENU -----
1. Depósito
2. Saque
3. Extrato
4. Sair
-----------------
Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        try:
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Erro: Valor inválido para depósito.")
        except ValueError:
            print("Erro: Valor deve ser um número.")

    elif opcao == "2":
        try:
            valor = float(input("Digite o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITES_SAQUES

            if excedeu_saldo:
                print("Erro: Saldo insuficiente para saque.")
            elif excedeu_limite:
                print("Erro: Valor excede o limite permitido.")
            elif excedeu_saques:
                print("Erro: Limite de saques diário alcançado.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Erro: Valor inválido para saque.")
        except ValueError:
            print("Erro: Valor deve ser um número.")

    elif opcao == "3":
        print("\n----- Extrato -----")
        print("Nenhuma movimentação registrada." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("--------------------")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
