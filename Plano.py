import networkx as nx

def eh_planar(grafo):
    """
    Verifica se um grafo é planar usando a função check_planarity do NetworkX.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - True se o grafo for planar, False caso contrário.
    """
    return nx.check_planarity(grafo)[0]

# Exemplo de uso:
grafo_planar = nx.Graph([(1, 2), (2, 3), (3, 1), (2, 4)])
grafo_nao_planar = nx.complete_graph(5)  # K5

print("É planar:", eh_planar(grafo_planar))
print("É planar:", eh_planar(grafo_nao_planar))
