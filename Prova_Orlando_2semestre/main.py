from Estrutura_de_dados.classes import *

lista_candidatoa = ListaCandidatos()

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
    print("\nBem vindo(a) ao Sistema Gerenciador de Vestibular FATEC 2026 1° Semestre!")
    print("Selecione a opção que deseja realizar:")
    print("")
    print("1 - Inscrever candidato(a)                   |   1 - Inscrever funcionário(a)")
    print("2 - Editar informações do(a) candidato(a)    |   1 - Inscrever funcionário(a)")
    print("3 - Confirmar pagamento do(a) candidato(a)   |   1 - Inscrever funcionário(a)")
    print("4 - Visualizar lista de candidatos           |   1 - Visualizar lista de funcionários")
    print("")

    escolha = input("Escolha: ")

    if escolha == "1":
        lista_candidatoa.adicionar_candidato()
    elif escolha == "2":
        numero = int(input("Digite o número da inscrição: "))
        nome = input("Novo nome (Deixe vazio para não alterar): ").strip()
        cpf = input("Novo CPF (deixe vazio para não alterar): ").strip()
        curso = input("Novo curso (deixe vazio para não alterar): ").strip()
        lista_candidatoa.editar_candidato(numero, nome or None, cpf or None, curso or None)
    elif escolha == "3":
        numero = int(input("Digite o numero da inscrição: "))
        lista_candidatoa.efetivar_pagamento(numero)
    elif escolha == "4":
        lista_candidatoa.listar_candidatos()
    elif escolha == "0":
        break
    else:
        print("⚠️ Opção inválida!")