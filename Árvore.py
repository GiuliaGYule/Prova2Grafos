import networkx as nx

def eh_arvore(grafo):
    """
    Verifica se um grafo é uma árvore.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - True se o grafo for uma árvore, False caso contrário.
    """
    return nx.is_tree(grafo)

# Exemplo de uso:
grafo_arvore = nx.Graph([(1, 2), (2, 3), (2, 4)])
grafo_nao_arvore = nx.Graph([(1, 2), (2, 3), (3, 1), (4, 5)])

print("É uma árvore:", eh_arvore(grafo_arvore))
print("É uma árvore:", eh_arvore(grafo_nao_arvore))
