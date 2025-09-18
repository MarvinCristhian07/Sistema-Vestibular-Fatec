from Estrutura_de_dados.classes import *
from Estrutura_de_dados.aplicadores import *

lista_candidatos = ListaCandidatos()
lista_aplicadores = ListaAplicadores()

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
    print("1 - Inscrever candidato(a)                   |   5 - Cadastrar funcionário(a)            ")
    print("2 - Editar informações do(a) candidato(a)    |   6 - Visualizar lista de funcionários(as)")
    print("3 - Confirmar pagamento do(a) candidato(a)   |   7 - .                                   ")
    print("4 - Visualizar lista de candidatos           |   8 - .                                   ")
    print("0 - Sair                                     |                                           ")
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
    elif escolha == "0":
        print("\nSaindo do sistema...")
        break
    else:
        print("⚠️ Opção inválida!")
