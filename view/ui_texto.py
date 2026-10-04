from controller.controller import Controller


def menu():
    ctrl = Controller()

    while True:
        print("\n--- Sistema de Estacionamento ---")
        print("1. Estacionar veículo")
        print("2. Retirar veículo")
        print("3. Relatório")
        print("4. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            tipo = input("Tipo (carro/moto/caminhao): ").lower()
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            vaga = int(input("Número da vaga: "))
            try:
                ctrl.estacionar_veiculo(tipo, placa, modelo, vaga)
                print(f"Veículo {placa} estacionado na vaga {vaga}.")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            vaga = int(input("Número da vaga: "))
            horas = int(input("Horas estacionado: "))
            try:
                tarifa = ctrl.retirar_veiculo(vaga, horas)
                print(f"Veículo retirado. Tarifa: R$ {tarifa}")
            except ValueError as e:
                print(e)

        elif opcao == "3":
            rel = ctrl.relatorio()
            print(f"Vagas ocupadas: {rel['ocupadas']}, Vagas livres: {rel['livres']}")

        elif opcao == "4":
            ctrl.salvar()
            print("Saindo... Histórico salvo.")
            break
        else:
            print("Opção inválida.")
