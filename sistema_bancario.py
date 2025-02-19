menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            print(f"Depósito realizado com sucesso! Novo saldo: R$ " + str(valor))
            saldo += float(valor)
            extrato += f"Depósito de R$ {valor}\n"
        else:
            print("Digite um valor válido")
    
    elif opcao == "s":
        if numero_saques <= LIMITE_SAQUES: 
            saque = float(input("Informe o valor do saque: "))
            if saque < limite:
                if saque <= float(saldo):
                    print(f"Saque de R$ {saque} realizado com sucesso.")
                    numero_saques += 1
                    saldo -= float(saque)
                    extrato += f"Saque de R$ -{saque}\n"
                else:
                    print(f"Saldo insuficiente.")
            else:
                print("O limite por saque é de R$ 500")
        else: 
            print("Limite de saques excedido")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if extrato == '' else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}") 
        print("==========================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        

    