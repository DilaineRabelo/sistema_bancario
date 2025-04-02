menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[p] Cadastrar Conta
[q] Sair

=> """

contas = []  
clientes = []  
id_conta = 1
id_cliente = 1
LIMITE_SAQUE = 500  
MAX_SAQUES_DIARIOS = 3  
historico_saques = {}  
extratos = {}  

def listar_contas():
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    
    print("\n📋 Contas cadastradas:")
    for conta in contas:
        cliente_nome = conta["Cliente"]["Nome"]
        print(f"ID: {conta['ID Conta']} | Conta: {conta['Número da Conta']} | Cliente: {cliente_nome} | Saldo: R$ {conta['Saldo']:.2f}")

def listar_clientes():
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return
    
    print("\n👤 Clientes cadastrados:")
    for cliente in clientes:
        print(f"ID: {cliente['ID Cliente']} | Nome: {cliente['Nome']} | CPF: {cliente['CPF']}")

def encontrar_cliente_por_id(id_cliente):
    return next((c for c in clientes if c["ID Cliente"] == id_cliente), None)

def encontrar_conta_por_id(id_conta):
    return next((c for c in contas if c["ID Conta"] == id_conta), None)

def obter_id_valido(mensagem):
    """Função para validar entrada do ID"""
    while True:
        try:
            id_digitado = int(input(mensagem))
            return id_digitado
        except ValueError:
            print("❌ Entrada inválida! Digite um número válido.")

while True:
    opcao = input(menu)

    if opcao == "c":  
        nome = input("\nNome do cliente: ")
        cpf = input("CPF do cliente: ")

        clientes.append({"ID Cliente": id_cliente, "Nome": nome, "CPF": cpf})
        print(f"✅ Cliente cadastrado com sucesso! ID: {id_cliente}")
        id_cliente += 1

    elif opcao == "p":  
        listar_clientes()
        if not clientes:
            continue

        id_cliente_escolhido = obter_id_valido("\nDigite o ID do cliente para criar a conta: ")
        cliente = encontrar_cliente_por_id(id_cliente_escolhido)

        if cliente:
            numero_conta = f"{id_conta:04d}"
            nova_conta = {
                "ID Conta": id_conta,
                "Número da Conta": numero_conta,
                "Saldo": 0.0,
                "Cliente": cliente
            }
            contas.append(nova_conta)
            historico_saques[id_conta] = 0  
            extratos[id_conta] = []  
            print(f"✅ Conta criada com sucesso! Número da Conta: {numero_conta}")
            id_conta += 1
        else:
            print("❌ Cliente não encontrado.")

    elif opcao == "d": 
        listar_contas()
        if not contas:
            continue

        id_conta_escolhida = obter_id_valido("\nDigite o ID da conta para depósito: ")
        conta = encontrar_conta_por_id(id_conta_escolhida)

        if conta:
            valor = float(input("Informe o valor do depósito: "))

            if valor <= 0:
                print("❌ O valor do depósito deve ser positivo.")
                continue

            conta["Saldo"] += valor
            extratos[id_conta_escolhida].append(f"+ R$ {valor:.2f}")  
            print(f"✅ Depósito realizado! Novo saldo: R$ {conta['Saldo']:.2f}")
        else:
            print("❌ Conta não encontrada.")

    elif opcao == "s":  
        listar_contas()
        if not contas:
            continue

        id_conta_escolhida = obter_id_valido("\nDigite o ID da conta para saque: ")
        conta = encontrar_conta_por_id(id_conta_escolhida)

        if conta:
            if historico_saques[id_conta_escolhida] >= MAX_SAQUES_DIARIOS:
                print(f"❌ Limite de {MAX_SAQUES_DIARIOS} saques diários atingido!")
                continue

            valor = float(input("Informe o valor do saque: "))

            if valor <= 0:
                print("❌ O valor do saque deve ser positivo.")
            elif valor > LIMITE_SAQUE:
                print(f"❌ O valor máximo por saque é R$ {LIMITE_SAQUE:.2f}.")
            elif valor > conta["Saldo"]:
                print("❌ Saldo insuficiente.")
            else:
                conta["Saldo"] -= valor
                historico_saques[id_conta_escolhida] += 1
                extratos[id_conta_escolhida].append(f"- R$ {valor:.2f}")  
                print(f"✅ Saque realizado! Novo saldo: R$ {conta['Saldo']:.2f}")
        else:
            print("❌ Conta não encontrada.")

    elif opcao == "e":  
        listar_contas()
        if not contas:
            continue

        id_conta_escolhida = obter_id_valido("\nDigite o ID da conta para extrato: ")
        conta = encontrar_conta_por_id(id_conta_escolhida)

        if conta:
            print(f"\n📄 Extrato da conta {conta['Número da Conta']}:")
            if extratos[id_conta_escolhida]:
                for transacao in extratos[id_conta_escolhida]:
                    print(transacao)
            else:
                print("Nenhuma movimentação.")
            
            print(f"\n💰 Saldo atual: R$ {conta['Saldo']:.2f}")
        else:
            print("❌ Conta não encontrada.")

    elif opcao == "q":
        print("🚪 Saindo do sistema bancário...")
        break

    else:
        print("❌ Operação inválida, tente novamente.")
