import networkx as nx

def eh_grafo_simples(grafo):
    """
    Verifica se um grafo é simples.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - True se o grafo for simples, False caso contrário.
    """
    return nx.number_of_selfloops(grafo) == 0

# Exemplo de uso:
grafo_simples = nx.Graph([(1, 2), (2, 3), (3, 1)])
grafo_com_laco = nx.Graph([(1, 1), (2, 3), (3, 1)])

print("O grafo simples é simples?", eh_grafo_simples(grafo_simples))
print("O grafo com laço é simples?", eh_grafo_simples(grafo_com_laco))
