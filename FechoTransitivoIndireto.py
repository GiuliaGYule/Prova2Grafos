import networkx as nx

def fecho_transitivo_indireto(grafo, vertice):
    """
    Encontra o fecho transitivo indireto de um vértice em um grafo direcionado.

    Parâmetros:
    - grafo: Grafo direcionado representado por um objeto NetworkX.
    - vertice: Vértice para o qual se deseja encontrar o fecho transitivo indireto.

    Retorna:
    - Conjunto de vértices no fecho transitivo indireto do vértice especificado.
    """
    return set(nx.ancestors(grafo, vertice))

# Exemplo de uso:
grafo_direcionado = nx.DiGraph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3)])
vertice_inicial = 1
fecho_transitivo = fecho_transitivo_indireto(grafo_direcionado, vertice_inicial)
print(f"Fecho transitivo indireto do vértice {vertice_inicial}: {fecho_transitivo}")
