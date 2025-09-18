# Função para verificar se uma string contem apenas letras e espaços
def is_alpha_space(text):
    if not text:
        return False
    for char in text:
        if not ('a' <= char.lower() <= 'z' or char == ' '):
            return False
    return True

# Outra função para verificar se uma string contém apenas números
def is_digit(text):
    if not text:
        return False
    for char in text:
        if not '0' <= char <= '9':
            return False
    return True

# Classe para o candidato
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

class NoCurso:
    def __init__(self, curso):
        self.curso = curso
        self.total_candidatos = 0
        self.lista_candidatos = None # Inicio da lista ligada de candidatos do curso
        self.proximo = None

# Lista ligada para gerenciar os candidatos
class ListaCandidatos:
    def __init__(self):
        self.inicio = None
        self.total = 0
        self.lista_cursos = None # Início da lista ligada de cursos

        # Popula a lista ligada de cursos
        curso_ia = NoCurso("Tecnologia em Inteligência Artificial")
        curso_esg = NoCurso("Gestão da Sustentabilidade Ambiental e Governança Corporativa (ESG)")

        self.lista_cursos = curso_ia
        curso_ia.proximo = curso_esg
    
    def adicionar_candidato_ao_curso(self, curso_nome, novo_candidato):
        atual_curso = self.lista_cursos
        while atual_curso:
            if atual_curso.curso == curso_nome:
                novo_no_candidato = No(novo_candidato)
                if not atual_curso.lista_candidatos:
                    atual_curso.lista_candidatos = novo_no_candidato
                else:
                    ultimo = atual_curso.lista_candidatos
                    while ultimo.proximo:
                        ultimo = ultimo.proximo
                    ultimo.proximo = novo_no_candidato
                atual_curso.total_candidatos += 1
                return
            atual_curso = atual_curso.proximo
        
    def adicionar_candidato(self):

        # Coletar os dados do usuário
        while True:
            nome = input("Entre com o nome do candidato: ").strip()
            if is_alpha_space(nome):
                break
            print("⚠️ Por favor, preencha o nome com apenas letras e espaços!")

        while True:
            cpf = input("Entre com o CPF do candidato (apenas números): ").strip()
            if len(cpf) == 11:
                break
            print("⚠️ O CPF deve ter exatamente 11 dígitos!")
            if is_digit(cpf):
                break
            print("⚠️ Por favor, preencha o CPF com apenas números!")

        while True:
            print("\nEscolha a opção de curso desejado: ")
            print("1 - Tecnologia em Inteligência Artificial")
            print("2 - Gestão da Sustentabilidade Ambiental e Governança Corporativa (ESG)")
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

        # Adiciona o candidato à lista ligada do curso correspondente
        self.adicionar_candidato_ao_curso(curso, novo_candidato)

        print(f"✅ Inscrição realizada com sucesso! Número da inscrição: {self.total}")

    def buscar_candidato(self, numero_inscricao):
        atual_curso = self.lista_cursos
        while atual_curso:
            atual_candidato = atual_curso.lista_candidatos
            while atual_candidato:
                if atual_candidato.candidato.numero_inscricao == numero_inscricao:
                    return atual_candidato.candidato
                atual_candidato = atual_candidato.proximo
            atual_curso = atual_curso.proximo
        return None
    
    def executar_edicao(self):
        try:
            numero = int(input("Digite o número da inscrição: "))
            candidato = self.buscar_candidato(numero)
            if not candidato:
                print("\nCandidato não encontrado.")
                return
            
            nome = input(f"Novo nome (atual: {candidato.nome}) - Deixe vazio para não alterar nada: ").strip()
            if nome and is_alpha_space(nome):
                print("⚠️ Nome inválido. Apenas letras e espaços são permitidos. Nenhuma alteração foi feita.")
                nome = None
            
            cpf = input(f"Novo CPF (atual: {candidato.cpf}) - Deixe vazio para não alterar: ").strip()
            if cpf and not is_digit(cpf):
                print("⚠️ CPF inválido. Apenas números são permitindo. Nenhuma alteração feita.")
                cpf = None

            curso_antigo = candidato.curso
            curso_novo = None
            while True:
                print("\nNovo curso (atual: {}).".format(curso_antigo))
                print("1 - Tecnologia em Inteligência Artificial")
                print("2 - Gestão da Sustentabilidade Ambiental e Governança Corporativa (ESG)")
                opcao_curso = input("Escolha (Deixe vazio para não alterar): ").strip()

                if not opcao_curso:
                    break
                elif opcao_curso == "1":
                    curso_novo = "Tecnologia em Inteligência Artificial"
                    break
                elif opcao_curso == "2":
                    curso_novo = "Gestão da Sustentabilidade Ambiental e Governança Corporativa (ESG)"
                    break
                else:
                    print("⚠️ Selecione uma opção válida (1 ou 2)!")
                    continue

            if nome or cpf or curso_novo:
                self.editar_candidato(numero, nome or None, cpf or None, curso_novo or None)

        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número de inscrição válido.")
    
    def editar_candidato(self, numero_inscricao, nome=None, cpf=None, curso=None):
        candidato = self.buscar_candidato(numero_inscricao)
        if candidato:
            if nome:
                candidato.nome = nome
            if cpf:
                candidato.cpf = cpf
            if curso and curso != candidato.curso:
                self.remover_candidato_do_curso(candidato.curso, candidato)
                candidato.curso = curso
                self.adicionar_candidato_ao_curso(curso, candidato)
            print(f"\nDados do candidato {numero_inscricao} atualizados com sucesso!")
        else:
            print("\nCandidato não encontrado.")

    def remover_candidato_do_curso(self, curso_nome, candidato_alvo):
        atual_curso = self.lista_cursos
        while atual_curso:
            if atual_curso.curso == curso_nome:
                atual_candidato = atual_curso.lista_candidatos
                anterior = None
                while atual_candidato:
                    if atual_candidato.candidato == candidato_alvo:
                        if anterior:
                            anterior.proximo = atual_candidato.proximo
                        else:
                            atual_curso.lista_candidatos = atual_candidato.proximo
                        atual_curso.total_candidatos -= 1
                        return True
                    anterior = atual_candidato
                    atual_candidato = atual_candidato.proximo
                atual_curso = atual_curso.proximo
            return False

    def executar_pagamento(self):
        try:
            numero = int(input("Digite o número de inscrição do candidato: "))
            self.efetivar_pagamento(numero)
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número de inscrição válido.")
    
    def efetivar_pagamento(self, numero_inscricao):
        candidato = self.buscar_candidato(numero_inscricao)
        if candidato:
            candidato.pago = True
            print(f"\nPagamento do candidato {numero_inscricao} registrado com sucesso!")
        else:
            print("\nCandidato não encontrado.")

    def _bubble_sort_list(self, head):
        if not head:
            return None

        swapped = True
        while swapped:
            swapped = False
            p = head
            while p and p.proximo:
                if p.candidato.nome.lower() > p.proximo.candidato.nome.lower():
                    # Trocar os dados dos nós
                    p.candidato, p.proximo.candidato = p.proximo.candidato, p.candidato
                    swapped = True
                p = p.proximo
            return head
    
    def listar_candidatos(self):
        if not self.lista_cursos:
            print("\nNenhum candidato inscrito.")
            return

        print("\n==== Lista de Candidatos ====")
        print("Unidade: Fatec Rio Claro")
        print("Vagas por curso: 40\n")

        atual_curso = self.lista_cursos
        while atual_curso:
            total_candidatos = atual_curso.total_candidatos
            vagas = 40
            relacao = total_candidatos / vagas if vagas > 0 else 0

            print(f"--- Curso: {atual_curso.curso} ---")
            print(f"Total de candidatos: {total_candidatos}")
            print(f"Relação candidato/vaga: {relacao:.1f}")

            # Ordenar a lista do curso
            atual_curso.lista_candidatos = self._bubble_sort_list(atual_curso.lista_candidatos)

            atual_candidato = atual_curso.lista_candidatos
            while atual_candidato:
                print(atual_candidato.candidato)
                atual_candidato = atual_candidato.proximo
            print("-" * 30)

            atual_curso = atual_curso.proximo

    def relacao_candidatos_efetivados(self):
        print("\n--- Relação Candidato/Vaga (apenas efetivados) ---")
        vagas = 40
        atual_curso = self.lista_cursos
        while atual_curso:
            total_efetivados = 0
            atual_candidato = atual_curso.lista_candidatos
            while atual_candidato:
                if atual_candidato.candidato.pago:
                    total_efetivados += 1
                atual_candidato = atual_candidato.proximo

            relacao_efetivados = total_efetivados / vagas if vagas > 0 else 0
            print(f"Curso: {atual_curso.curso}")
            print(f"Candidatos efetivados: {total_efetivados}")
            print(f"Relação candidato/vaga: {relacao_efetivados:.1f}")
            print("-" * 30)

            atual_curso = atual_curso.proximo

    def calcular_salas_necessarias(self):
        total_efetivados = 0
        atual_curso = self.lista_cursos
        while atual_curso:
            atual_candidato = atual_curso.lista_candidatos
            while atual_candidato:
                if atual_candidato.candidato.pago:
                    total_efetivados += 1
                atual_candidato = atual_candidato.proximo
            atual_curso = atual_curso.proximo
        
        salas = total_efetivados // 30
        if total_efetivados % 30 > 0:
            salas += 1

        print(f"\n--- Preparação para o Vestibular ---")
        print(f"Total de candidatos com inscrição efetivada: {total_efetivados}")
        print(f"Número de salas necessárias (capacidade 30): {salas}")
        return salas

    # Método para gerar lista efetivados
    def gerar_lista_efetivados(self):
        lista_efetivados = ListaEfetivados()
        atual_curso = self.lista_cursos
        while atual_curso:
            atual_candidato = atual_curso.lista_candidatos
            while atual_candidato:
                if atual_candidato.candidato.pago:
                    lista_efetivados.adicionar(atual_candidato.candidato)
                atual_candidato = atual_candidato.proximo
            atual_curso = atual_curso.proximo
        return lista_efetivados

    def gerenciar_aprovacao(self, lista_aprovados):
        print("\n--- Gerenciamento de Aprovação ---")
        candidatos_efetivados = self.gerar_lista_efetivados()
        if not candidatos_efetivados.inicio:
            print("Não há candidatos efetivados para o processo de aprovação.")
            return

        atual_candidato = candidatos_efetivados.inicio
        while atual_candidato:
            c = atual_candidato.candidato
            print(f"\nCandidato: {c.nome} | Inscrição: {c.numero_inscricao} | Curso: {c.curso}")
            aprovado = input("Aprovar este candidato? (s/n): ").lower()
            if aprovado == 's':
                lista_aprovados.adicionar_aprovado(c.nome, c.cpf, c.curso)
            atual_candidato = atual_candidato.proximo
    
class CandidatosEfetivados:
    def __init__(self, candidato):
        self.candidato = candidato
        self.proximo = None
        
class ListaEfetivados:
    def __init__(self):
        self.inicio = None

    def adicionar(self, candidato):
        novo_no = CandidatosEfetivados(candidato)
        if not self.inicio:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def listar_por_sala(self):
        if not self.inicio:
            print("\nNenhum candidato com inscrição efetivada para alocar em salas.")
            return

        print("\n--- Alocação de Candidatos por Sala ---")
        sala_numero = 1
        contador_sala = 0
        atual = self.inicio

        while atual:
            if contador_sala == 0:
                print(f"\nSala {sala_numero}:")

            print(f" - {atual.candidato.nome} (Inscrição: {atual.candidato.numero_inscricao})")

            contador_sala += 1
            if contador_sala == 30:
                sala_numero += 1
                contador_sala = 0

            atual = atual.proximo

class AlunoAprovado:
    def __init__(self, nome, cpf, curso):
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.proximo = None

class ListaAprovados:
    def __init__(self):
        self.inicio = None
        self.total_aprovados_ia = 0
        self.total_aprovados_esg = 0

    def adicionar_aprovado(self, nome, cpf, curso):
        if curso == "Tecnologia em Inteligência Artificial" and self.total_aprovados_ia >= 40:
            print(f"⚠️ Limite de 40 vagas para Inteligência Artificial atingido. {nome} não pode ser aprovado(a).")
            return
        if curso == "Gestão da Sustentabilidade Ambiental e Governança Corporativa (ESG)" and self.total_aprovados_esg >= 40:
            print(f"⚠️ Limite de 40 vagas para Gestão ESG atingido. {nome} não pode ser aprovado(a).")

        novo_aprovado = AlunoAprovado(nome, cpf, curso)
        if not self.inicio:
            self.inicio = novo_aprovado
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_aprovado

        if curso == "Tecnologia em Inteligência Artificial":
            self.total_aprovados_ia += 1
        else:
            self.total_aprovados_esg += 1
        print("✅ {nome} aprovado(a) no curso de {curso}!")

    def listar_aprovados(self):
        if not self.inicio:
            print("\Nenhum aluno aprovado.")
            return

        print("\n--- Lista de Alunos Aprovados ---")
        atual = self.inicio
        while atual:
            print(f"- Nome: {atual.nome} | CPF: {atual.cpf} | Curso: {atual.curso}")
            atual = atual.proximo
