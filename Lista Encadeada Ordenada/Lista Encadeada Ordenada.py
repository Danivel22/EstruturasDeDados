# Classe que representa um nó da lista encadeada
class Node:
    def __init__(self, valor):
        self.valor = valor  # Armazena o valor do nó
        self.proximo = None  # Ponteiro para o próximo nó (inicialmente None)

# Classe para uma lista encadeada ordenada
class ListaEncadeadaOrdenada:
    def __init__(self):
        self.cabeca = None  # Ponteiro para o primeiro nó da lista (inicialmente None)

    # Método para inserir um valor na lista mantendo a ordem crescente
    def inserir_ordenado(self, valor):
        novo_no = Node(valor)  # Cria um novo nó com o valor fornecido
        # Se a lista estiver vazia ou o novo valor for menor que a cabeça, insere no início
        if not self.cabeca or valor < self.cabeca.valor:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            return

        atual = self.cabeca  # Começa pelo primeiro nó
        # Percorre a lista até encontrar a posição correta para inserção
        while atual.proximo and atual.proximo.valor < valor:
            atual = atual.proximo
        
        # Insere o novo nó na posição correta
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

    # Método para exibir os valores da lista encadeada
    def exibir(self):
        atual = self.cabeca  # Começa pelo primeiro nó
        while atual:  # Percorre a lista até o fim
            print(atual.valor, end=" -> ")  # Imprime o valor do nó
            atual = atual.proximo  # Passa para o próximo nó
        print("None")  # Indica o final da lista

# Criando a lista encadeada ordenada e adicionando elementos fora de ordem
lista = ListaEncadeadaOrdenada()
valores = [3, 1, 4, 5, 2]  # Lista de valores fora de ordem
for v in valores:
    lista.inserir_ordenado(v)

# Exibindo a lista ordenada
lista.exibir()  # Saída: 1 -> 2 -> 3 -> 4 -> 5 -> None
