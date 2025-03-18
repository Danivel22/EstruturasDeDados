""" https://www.youtube.com/watch?v=RW0oD2L_tSg 
"""

# Classe que representa um nó da lista encadeada
class Node:
    def __init__(self, valor):
        self.valor = valor  # Armazena o valor do nó
        self.proximo = None  # Ponteiro para o próximo nó (inicialmente None)

# Classe que representa a lista encadeada
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Ponteiro para o primeiro nó da lista (inicialmente None)

    # Método para inserir um novo valor no final da lista
    def inserir_no_final(self, valor):
        novo_no = Node(valor)  # Cria um novo nó com o valor fornecido
        if not self.cabeca:  # Se a lista estiver vazia, define o novo nó como a cabeça
            self.cabeca = novo_no
            return
        atual = self.cabeca  # Começa pelo primeiro nó
        while atual.proximo:  # Percorre até encontrar o último nó
            atual = atual.proximo
        atual.proximo = novo_no  # Insere o novo nó no final

    # Método para exibir os valores da lista encadeada
    def exibir(self):
        atual = self.cabeca  # Começa pelo primeiro nó
        while atual:  # Percorre a lista até o fim
            print(atual.valor, end=" -> ")  # Imprime o valor do nó
            atual = atual.proximo  # Passa para o próximo nó
        print("None")  # Indica o final da lista

# Criando a lista encadeada e adicionando elementos dinamicamente
lista = ListaEncadeada()
for i in range(1, 6):  # Adicionando os valores de 1 a 5
    lista.inserir_no_final(i)

# Exibindo a lista
lista.exibir()  # Saída: 1 -> 2 -> 3 -> 4 -> 5 -> None
