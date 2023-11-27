import networkx as nx

def eh_multigrafo(grafo):
    """
    Verifica se um grafo é um multigrafo.

    Parâmetros:
    - grafo: Grafo a ser verificado.

    Retorna:
    - True se o grafo é um multigrafo, False caso contrário.
    """
    return isinstance(grafo, nx.MultiGraph)

# Exemplo de uso:
grafo_nao_direcionado = nx.Graph([(1, 2), (2, 3), (3, 1)])
grafo_direcionado = nx.DiGraph([(1, 2), (2, 3), (3, 1)])

print("Grafo não direcionado é multigrafo:", eh_multigrafo(grafo_nao_direcionado))
print("Grafo direcionado é multigrafo:", eh_multigrafo(grafo_direcionado))
