# Estrutura para o aplicador da prova
class Aplicador:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
        self.proximo = None

# Lista ligada para gerenciar os aplicadores
class ListaAplicadores:
    def __init__(self):
        self.inicio = None

    def adicionar_aplicador(self, nome, cargo):
        novo_aplicador = Aplicador(nome, cargo)
        if not self.inicio:
            self.inicio = novo_aplicador
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_aplicador
        print(f"✅ Aplicador(a) {nome} cadastrado(a) com sucesso!")

    def listar_aplicadores(self):
        if not self.inicio:
            print("Nenhum aplicador cadastrado.")
            return

        print("\n==== Lista de Funcionários ====")
        atual = self.inicio
        while atual:
            print(f"- Nome: {atual.nome} | Cargo: {atual.cargo}")
            atual = atual.proximo
