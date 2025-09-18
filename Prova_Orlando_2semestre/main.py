from Estrutura_de_dados.classes import *
from Estrutura_de_dados.aplicadores import *

lista_candidatos = ListaCandidatos()
lista_aplicadores = ListaAplicadores()
lista_aprovados = ListaAprovados()

print("")
print("  ███████            ███████      █      ███████ ███████ ███████ ███████ ███████      █      ███████ ███████")
print("██         ██████  ██             █      ██      ██   ██   ██    ██      ██           █      ██      ██   ██")
print("██       ██      ██  █████        █      ████    ███████   ██    ████    ██           █      ███████ ███████")
print("  ██████████     ██       ██      █      ██      ██   ██   ██    ██      ██           █           ██ ██     ")
print("         ██ ██████████████        █      ██      ██   ██   ██    ███████ ███████      █      ███████ ██     ")
print("         ██                       █                                                   █                     ")
print("         ██                       █                                                   █  By Marvin Cristhian")
print("")
print("------------------------------------------------------------------------------------------------------------")

while True:
    print("\nBem vindo(a) ao Sistema Gerenciador de Vestibular FATEC 2026 1° Semestre!              ")
    print("Selecione a opção que deseja realizar:                                                   ")
    print("                                                                                         ")
    print("1 - Inscrever candidato(a)                   |   7 - Visualizar salas necessárias        ")
    print("2 - Editar informações do(a) candidato(a)    |   8 - Listar candidatos por sala          ")
    print("3 - Confirmar pagamento do(a) candidato(a)   |   9 - Relação candidatos/vaga (efetivados)")
    print("4 - Visualizar lista de candidatos           |   10 - Gerenciar aprovações               ")
    print("5 - Cadastrar funcionário(a)                 |   11 - Listar aprovados                   ")
    print("6 - Visualizar lista de funcionários(as)     |   0 - Sair do sistema                     ")
    print("                                                                                         ")

    escolha = input("Escolha: ")

    if escolha == "1":
        lista_candidatos.adicionar_candidato()
    elif escolha == "2":
        lista_candidatos.executar_edicao()
    elif escolha == "3":
        lista_candidatos.executar_pagamento()
    elif escolha == "4":
        lista_candidatos.listar_candidatos()
    elif escolha == "5":
        nome_aplicador = input("Nome do(a) funcionário(a): ").strip()
        print("\n Selecione o cargo:                                                                 ")
        print("                                                                                      ")
        print("1 - Aplicador(a) de prova                 |    4 - Fiscal de banheiros                ")
        print("2 - Fiscal de sala                        |    5 - Segurança                          ")
        print("3 - Fiscal de corredor                    |    6 - Porteiro(a)                        ")
        print("                                                                                      ")
        opcao = input("Selecione: ")
        if opcao == "1":
            cargo_aplicador = "Aplicador(a) de prova"
        elif opcao == "2":
            cargo_aplicador = "Fiscal de sala"
        elif opcao == "3":
            cargo_aplicador = "Fiscal de corredor"
        elif opcao == "4":
            cargo_aplicador = "Fiscal de banheiros"
        elif opcao == "5":
            cargo_aplicador = "Segurança"
        elif opcao == "6":
            cargo_aplicador = "Porteiro(a)"
        else:
            print("⚠️ Opção inválida!")
        lista_aplicadores.adicionar_aplicador(nome_aplicador, cargo_aplicador)
    elif escolha == "6":
        lista_aplicadores.listar_aplicadores()
    elif escolha == "7":
        lista_candidatos.calcular_salas_necessarias()
    elif escolha == "8":
        lista_candidatos.gerar_lista_efetivados().listar_por_sala()
    elif escolha == "9":
        lista_candidatos.relacao_candidatos_efetivados()
    elif escolha == "10":
        lista_candidatos.gerenciar_aprovacao(lista_aprovados)
    elif escolha == "11":
        lista_aprovados.listar_aprovados()
    elif escolha == "0":
        print("\nSaindo do sistema...")
        break
    else:
        print("⚠️ Opção inválida!")
