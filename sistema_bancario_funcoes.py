menu = """
[1] Depositar
[2] Sacar 
[3] Extrato
[4] Sair
escolha uma das opções acima : """

saldo = 0
limite = 500
extrato = ""
saques = 0
limite_saques = 3

def depositar(valor):   
    if valor > 0:

        global saldo
        global extrato

        saldo += valor
        extrato += (f"Deposito de : R$ {valor:.2f}\n")
        print(f"O deposito de R$ : {valor} foi realizado com sucesso")        
    else:
        print("A operação Falhou! o valor informado é invalido")

def sacar(valor):
            global saldo
            global limite
            global extrato
            global saques
            global limite_saques    

            exedeu_saldo = valor > saldo

            exedeu_limite = valor > limite

            exedeu_saques = saques >= limite_saques

            if exedeu_saldo:
                print("A operacao falhou! o saldo nao é suficiente")

            elif exedeu_limite:
                print("A operacao falhou! exedeu o limite por saque")

            elif exedeu_saques:
                print("A operacao falhou! exedeu a quantidade de saques")

            elif valor > 0:
                saldo -= valor
                extrato += (f"saque : R$ {valor:.2f}\n")
                saques += 1
                print(f"saque no valor de R$ {valor} realizado com sucesso")

            else:
                print("A operação falhou! insira um valor valido")


def extrato():
    print("\n===============  Extrato ===============")
    print("ão foram realizadas operações" if not extrato else extrato)
    print(f"\n saldo : R$ {saldo:.2f}\n")
    print("==========================================")



while True:

    op = input(menu)
        
    if op == '1':
        valor = float(input("digite o valor do deposito : "))
        depositar(valor)
    elif op == '2':
        valor = float(input("digite o valor do saque : "))
        sacar(valor)
    elif op == '3':
        extrato()
    elif op == '4':
        break
