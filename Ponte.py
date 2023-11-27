import networkx as nx

def eh_ponte_alternativa(grafo, aresta):
    """
    Verifica se uma aresta é uma ponte em um grafo (alternativa).

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.
    - aresta: Tupla representando a aresta (u, v).

    Retorna:
    - True se a aresta for uma ponte, False caso contrário.
    """
    grafo_temp = grafo.copy()
    grafo_temp.remove_edge(*aresta)
    return not nx.is_connected(grafo_temp)

# Exemplo de uso:
grafo = nx.Graph([(1, 2), (2, 3), (3, 1), (2, 4)])
aresta_ponte = (3, 1)

print(f"A aresta {aresta_ponte} é uma ponte (alternativa): {eh_ponte_alternativa(grafo, aresta_ponte)}")
