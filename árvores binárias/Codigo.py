# Classe para representar um nó da árvore
class No:
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.esquerda = None  # Filho esquerdo
        self.direita = None   # Filho direito

# Classe para a Árvore Binária de Busca (BST)
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # Inicializa a árvore vazia

    # Inserir um novo nó na árvore
    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if no is None:  # Se a posição está vazia, cria um novo nó
            return No(valor)
        if valor < no.valor:  # Se o valor for menor, vai para a esquerda
            no.esquerda = self._inserir_recursivo(no.esquerda, valor)
        else:  # Se o valor for maior, vai para a direita
            no.direita = self._inserir_recursivo(no.direita, valor)
        return no

    # Percorrer a árvore em ordem (Esquerda -> Raiz -> Direita)
    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)
        print()

    def _em_ordem_recursivo(self, no):
        if no:
            self._em_ordem_recursivo(no.esquerda)
            print(no.valor, end=" ")  # Visita o nó
            self._em_ordem_recursivo(no.direita)

# Criando a árvore e inserindo elementos
arvore = ArvoreBinaria()
valores = [10, 5, 15, 3, 7, 12, 18]  # Elementos a serem inseridos

for v in valores:
    arvore.inserir(v)

# Exibindo os valores em ordem crescente
print("Árvore em ordem:")
arvore.em_ordem()  # Saída: 3 5 7 10 12 15 18
