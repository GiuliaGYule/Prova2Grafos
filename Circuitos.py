import networkx as nx

def encontrar_circuitos_direcionados(grafo):
    """
    Encontra todos os circuitos em um grafo direcionado.

    Parâmetros:
    - grafo: Grafo direcionado representado por um objeto NetworkX.

    Retorna:
    - Lista de listas, onde cada lista é um circuito no grafo direcionado.
    """
    ciclos = nx.simple_cycles(grafo)
    return [ciclo for ciclo in ciclos]

# Exemplo de uso:
grafo_direcionado = nx.DiGraph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3)])
circuitos_direcionados = encontrar_circuitos_direcionados(grafo_direcionado)
print("Circuitos no grafo direcionado:", circuitos_direcionados)
