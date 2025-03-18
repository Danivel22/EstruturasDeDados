# Classe que representa um nó da lista duplamente encadeada
class Node:
    def __init__(self, valor):
        self.valor = valor  # Armazena o valor do nó
        self.proximo = None  # Ponteiro para o próximo nó
        self.anterior = None  # Ponteiro para o nó anterior

# Classe para a Lista Duplamente Encadeada
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None  # Ponteiro para o primeiro nó da lista
        self.cauda = None   # Ponteiro para o último nó da lista

    # Método para inserir um valor no final da lista
    def inserir_no_final(self, valor):
        novo_no = Node(valor)  # Cria um novo nó com o valor fornecido
        if not self.cabeca:  # Se a lista estiver vazia
            self.cabeca = self.cauda = novo_no  # O novo nó é tanto a cabeça quanto a cauda
        else:
            self.cauda.proximo = novo_no  # O último nó aponta para o novo nó
            novo_no.anterior = self.cauda  # O novo nó aponta de volta para o último nó
            self.cauda = novo_no  # Atualiza a cauda para o novo nó

    # Método para exibir os valores da lista na ordem normal
    def exibir(self):
        atual = self.cabeca  # Começa pelo primeiro nó
        while atual:
            print(atual.valor, end=" <-> ")  # Imprime o valor do nó
            atual = atual.proximo  # Passa para o próximo nó
        print("None")  # Indica o final da lista

    # Método para exibir os valores da lista na ordem reversa
    def exibir_reverso(self):
        atual = self.cauda  # Começa pelo último nó
        while atual:
            print(atual.valor, end=" <-> ")  # Imprime o valor do nó
            atual = atual.anterior  # Passa para o nó anterior
        print("None")  # Indica o final da lista

# Criando a lista duplamente encadeada e adicionando elementos
lista = ListaDuplamenteEncadeada()
valores = [1, 2, 3, 4, 5]
for v in valores:
    lista.inserir_no_final(v)

# Exibindo a lista na ordem normal
print("Lista na ordem normal:")
lista.exibir()  # Saída: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None

# Exibindo a lista na ordem reversa
print("Lista na ordem reversa:")
lista.exibir_reverso()  # Saída: 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> None
