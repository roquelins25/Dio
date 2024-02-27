def menu():
    menu = """\n
    ================ MENU ================
    [a]\t Acessar
    [b]\t Novo usuário
    [x]\t Sair
    => """
    return input(menu)


def menu_1():
    menu_1 = """
-------- Banco Central --------
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [x] - Sair
=> """
    return input(menu_1)


def vCRIAR_USUARIO(usuarios):
    vCPF = input("Informar CPF(Somente Numeros): ")

    vNOME = input("Nome Completo: ")
    vDATA_NASC = input("Data Nascimento(dd-mm-yyyy): ")
    vUF = input("UF: ")
    vCIDADE = input("Cidade: ")
    vLOGRADOURO = input("Rua : ")
    vNUMERO = input("Numero: ")

    usuarios.append({"nome": vNOME, "data_nascimento": vDATA_NASC, "cpf": vCPF,
                    "UF": vUF, "cidade": vCIDADE, "Rua": vLOGRADOURO, "numero": vNUMERO})
    print(f"Usuario {vNOME} criado com sucesso!!!")


def vFiLTRAR_USUARIO(vCPF, usuarios):
    vUSUARIOS_FILTRADOS = [
        vUSUARIO for vUSUARIO in usuarios if vUSUARIO["cpf"] == vCPF]
    return vUSUARIOS_FILTRADOS[0] if vUSUARIOS_FILTRADOS else None


def vdepositar(saldo, vVALOR, extrato, /):
    if vVALOR > 0:
        saldo += vVALOR
        extrato += f"deposito:\tR$ { vVALOR: .2f}\n"
        print(f"Valor: R${vVALOR} Depositado com sucesso!")
    else:
        print("Operação invalida!")
    return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = valor_saque > saldo
    limite_excedido = valor_saque > limite
    saques_execidos = numero_saques >= limite_saques

    if saldo_excedido:
        print(f"Saldo insuficiente!!")

    elif limite_excedido:
        print(f'Limite de Saques excedido')

    elif saques_execidos:
        print(f'Número maximo de saques excedido')

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: \t\t R$ {valor_saque :.2f}\n"
        numero_saques + 1
        print(f'Valor de {valor_saque} Realizado com sucesso')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "a":
            vCPF = input("Digite CPF(somente numeros): ")
            vfiltro = vFiLTRAR_USUARIO(vCPF, usuarios)
            if vfiltro:
                break
                menu_1()
            else:
                print("Usuários não cadastrado")

        elif opcao == "b":
            vCPF = input("Digite CPF(somente numeros): ")
            vfiltro = vFiLTRAR_USUARIO(vCPF, usuarios)
            if vfiltro:
                print("Usuario Já Cadastrado!!!")
            else:
                vCRIAR_USUARIO(usuarios)

        elif opcao == "x":
            print(f'Obrigado por Utilizar nossos serviços')
            break
        else:
            print("Operação Invalida!")


main()


def main_1():
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        vopcao_1 = menu_1()

        if vopcao_1 == "d":
            vVALOR = float(input("Digite o Valor de Deposito: "))

            saldo, extrato = vdepositar(saldo, vVALOR, extrato)

        elif vopcao_1 == "s":
            valor_saque = float(input("Informe o Valor do Saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif vopcao_1 == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif vopcao_1 == "x":
            print(f'Obrigado por Utilizar nossos serviços')
            break
        else:
            print("Operação invalida!")


main_1()
