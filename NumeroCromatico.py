import networkx as nx

def numero_cromatico(grafo):
    """
    Calcula o número cromático de um grafo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - Número cromático do grafo.
    """
    coloracao = nx.coloring.greedy_color(grafo, strategy="largest_first")
    return max(coloracao.values()) + 1

# Exemplo de uso:
grafo = nx.Graph([(1, 2), (2, 3), (3, 1), (2, 4)])
numero_crom = numero_cromatico(grafo)

print("Número cromático:", numero_crom)
