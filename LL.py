import random

# Estrutura para armazenar contas
contas = {}

# Função para criar uma nova conta
def criar_conta():
    print("\n--- Criar Conta ---")
    nome = input("Digite o nome do cliente: ")
    numero_conta = str(random.randint(1000, 9999))
    while numero_conta in contas:
        numero_conta = str(random.randint(1000, 9999))
    saldo_inicial = float(input("Digite o saldo inicial: R$ "))
    contas[numero_conta] = {"nome": nome, "saldo": saldo_inicial, "historico": []}
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

# Função para consultar saldo
def consultar_saldo():
    print("\n--- Consultar Saldo ---")
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        conta = contas[numero_conta]
        print(f"Titular: {conta['nome']}")
        print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

# Função para realizar depósito
def depositar():
    print("\n--- Depositar ---")
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input("Digite o valor do depósito: R$ "))
        if valor > 0:
            contas[numero_conta]["saldo"] += valor
            contas[numero_conta]["historico"].append(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito realizado! Novo saldo: R$ {contas[numero_conta]['saldo']:.2f}")
        else:
            print("Valor inválido.")
    else:
        print("Conta não encontrada.")

# Função para realizar saque
def sacar():
    print("\n--- Sacar ---")
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input("Digite o valor do saque: R$ "))
        if valor > 0 and contas[numero_conta]["saldo"] >= valor:
            contas[numero_conta]["saldo"] -= valor
            contas[numero_conta]["historico"].append(f"Saque de R$ {valor:.2f}")
            print(f"Saque realizado! Novo saldo: R$ {contas[numero_conta]['saldo']:.2f}")
        elif valor > contas[numero_conta]["saldo"]:
            print("Saldo insuficiente.")
        else:
            print("Valor inválido.")
    else:
        print("Conta não encontrada.")

# Função para encerrar conta
def encerrar_conta():
    print("\n--- Encerrar Conta ---")
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        if contas[numero_conta]["saldo"] == 0:
            del contas[numero_conta]
            print("Conta encerrada com sucesso.")
        else:
            print("A conta não pode ser encerrada. Saldo ainda não zerado.")
    else:
        print("Conta não encontrada.")

# Função para exibir histórico de transações
def exibir_historico():
    print("\n--- Histórico de Transações ---")
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        historico = contas[numero_conta]["historico"]
        if historico:
            print(f"Histórico de transações para a conta {numero_conta}:")
            for transacao in historico:
                print(f"- {transacao}")
        else:
            print("Nenhuma transação registrada.")
    else:
        print("Conta não encontrada.")

# Menu principal
def main():
    print("Bem-vindo ao Banco Arcanjo Finance!")
    while True:
        print("\nEscolha uma operação:")
        print("1. Criar Conta")
        print("2. Consultar Saldo")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Encerrar Conta")
        print("6. Exibir Histórico de Transações")
        print("7. Sair")
        opcao = input("Digite o número da operação: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            consultar_saldo()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            encerrar_conta()
        elif opcao == "6":
            exibir_historico()
        elif opcao == "7":
            print("Obrigado por usar o Banco Arcanjo Finance. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
