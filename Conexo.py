import networkx as nx

def grafo_conexo(grafo):
    """
    Verifica se um grafo (direcionado ou não) é conexo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - True se o grafo for conexo (fortemente conexo para grafos direcionados), False caso contrário.
    """
    if isinstance(grafo, nx.DiGraph):
        return nx.is_strongly_connected(grafo)
    else:
        return nx.is_connected(grafo)

# Exemplo de uso:
grafo_direcionado = nx.DiGraph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3), (6, 6)])
grafo_nao_direcionado = nx.Graph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3)])

conexo_direcionado = grafo_conexo(grafo_direcionado)
conexo_nao_direcionado = grafo_conexo(grafo_nao_direcionado)

print("O grafo direcionado é conexo:", conexo_direcionado)
print("O grafo não direcionado é conexo:", conexo_nao_direcionado)
