from Estrutura_de_dados.classes import *

lista_candidatos = ListaCandidatos()

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
    print("\nBem vindo(a) ao Sistema Gerenciador de Vestibular FATEC 2026 1° Semestre!          ")
    print("Selecione a opção que deseja realizar:                                               ")
    print("                                                                                     ")
    print("1 - Inscrever candidato(a)                   |   1 - Inscrever funcionário(a)        ")
    print("2 - Editar informações do(a) candidato(a)    |   1 - Inscrever funcionário(a)        ")
    print("3 - Confirmar pagamento do(a) candidato(a)   |   1 - Inscrever funcionário(a)        ")
    print("4 - Visualizar lista de candidatos           |   1 - Visualizar lista de funcionários")
    print("0 - Sair                                     |                                       ")
    print("                                                                                     ")

    escolha = input("Escolha: ")

    if escolha == "1":
        lista_candidatos.adicionar_candidato()
    elif escolha == "2":
        lista_candidatos.executar_edicao()
    elif escolha == "3":
        lista_candidatos.executar_pagamento()
    elif escolha == "4":
        lista_candidatos.listar_candidatos()
    elif escolha == "0":
        print("\nSaindo do sistema...")
        break
    else:
        print("⚠️ Opção inválida!")
