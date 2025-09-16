class Candidato:
    def __init__(self, numero_inscricao, nome, cpf, curso, pago=False):
        self.numero_inscricao = numero_inscricao
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.pago = pago

    def __str__(self):
        status = "Efetivado" if self.pago else "Pendente"
        return (f"[{self.numero_inscricao}] {self.nome} | CPF: {self.cpf} | " 
                f"Curso: {self.curso} | Pagamento: {status}")
    
# Classe Nó para a lista ligada
class No:
    def __init__(self, candidato):
        self.candidato = candidato
        self.proximo = None

# Lista ligada para gerenciar os candidatos
class ListaCandidatos:
    def __init__(self):
        self.inicio = None
        self.total = 0
        
    def adicionar_candidato(self):

        # Coletar os dados do usuário
        while True:
            nome = input("Entre com o nome do candidato: ").strip()
            if nome != "":
                break
            print("⚠️ Por favor, preencha o nome para dar continuidade no processo!")

        while True:
            cpf = input("Entre com o CPF do candidato: ").strip()
            if cpf != "":
                break
            print("⚠️ Por favor, preencha o CPF para dar continuidade no processo!")

        while True:
            print("\nEscolha a opção de curso desejado: ")
            print("1 - Tecnologia em Inteligência Artificial\n2 - Gestão da Sustentabilidade Ambiental e Governança Corporativa (ESG)\n")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                curso = "Tecnologia em Inteligência Artificial"
                break
            elif opcao == "2":
                curso = "Gestão da Sustentabilidade Ambiental e Governança Corporativa (ESG)"
                break
            else:
                print("⚠️ Selecione uma opção válida (1 ou 2)!")
                break

        self.total += 1
        novo_candidato = Candidato(self.total, nome, cpf, curso, pago=False)
        novo_no = No(novo_candidato)

        # Inserir na lista ligada
        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

        print(f"\n✅ Inscrição realizada com sucesso! Número: {self.total}")

    def buscar_candidato(self, numero_inscricao):
        atual = self.inicio
        while atual:
            if atual.candidato.numero_inscricao == numero_inscricao:
                return atual.candidato
            atual = atual.proximo
        return None
    
    def editar_candidato(self, numero_inscricao, nome=None, cpf=None, curso=None):
        candidato = self.buscar_candidato(numero_inscricao)
        if candidato:
            if nome:
                candidato.nome = nome
            if cpf:
                candidato.cpf = cpf
            if curso:
                candidato.curso = curso
            print(f"\nDados do candidato {numero_inscricao} atualizados com sucesso!")
        else:
            print("\nCandidato não encontrado.")
    
    def efetivar_pagamento(self, numero_inscricao):
        candidato = self.buscar_candidato(numero_inscricao)
        if candidato:
            candidato.pago = True
            print(f"\nPagamento do candidato {numero_inscricao} registrado com sucesso!")
        else:
            print("\nCandidato não encontrado.")
    
    def listar_candidatos(self):
        if not self.inicio:
            print(f"\nNenhum candidato inscrito.")
            return
        atual = self.inicio
        print("\n==== Lista de Candidatos ====")
        while atual:
            print(atual.candidato)
            atual = atual.proximo