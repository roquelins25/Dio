vMENU = """
-------- Banco Roquelins --------
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [x] - Sair
=> """

vSALDO = 0
vLIMITE = 500
vEXTRATO = ""
vNUMERO_SAQUE = 0
vLIMITE_SAQUES = 3

while True:
    vOpcao = str(input(vMENU).lower())

    if vOpcao == "d":
        vDEPOSITO = float(input("Valor Deposito: "))
        if vDEPOSITO > 0:
            vSALDO += vDEPOSITO
            vEXTRATO += f"deposito de R$ { vDEPOSITO: .2f}\n"
        else:
            print("Operação invalida!")

    elif vOpcao == "s":
        vSAQUE = float(input("Valor do Saque: "))
        vExec_saque = vSAQUE > vSALDO
        vExec_limit = vSAQUE > vLIMITE
        vExec_limite_saque = vNUMERO_SAQUE >= vLIMITE_SAQUES

        if vExec_saque:
            print("Saldo insuficiente")
        elif vExec_limit:
            print("Limite Excedido")
        elif vExec_limite_saque:
            print("Numero maximo de saques exedido")
        elif vSAQUE > 0:
            vSALDO -= vSAQUE
            vEXTRATO += f"Saque de R$ {vSAQUE: .2f}\n"
            vNUMERO_SAQUE = + 1
        else:
            print("Operação Invalida")

    elif vOpcao == "e":
        print("\n------------------------------ EXTRATO ------------------------------")
        print("Não contém Movimentações." if not vEXTRATO else vEXTRATO)
        print(f"\nSaldo: R$ {vSALDO: .2f}")
        print("----------------------------------------------------------------------")
    elif vOpcao == "x":
        break
    else:
        print("Operação Inválida, Por Favor selecione novamente a operação Desejada")
