import networkx as nx

def grau_maximo_minimo(grafo):
    """
    Calcula o grau máximo e mínimo de um grafo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - Tuple contendo o grau máximo e o grau mínimo (in-degree e out-degree para grafos direcionados).
    """
    if grafo.is_directed():
        graus_entrada = dict(grafo.in_degree())
        graus_saida = dict(grafo.out_degree())
    else:
        graus = dict(grafo.degree())
        graus_entrada = graus
        graus_saida = graus

    if not graus_entrada:
        return (0, 0)  # Grafo vazio

    grau_maximo_entrada = max(graus_entrada.values())
    grau_minimo_entrada = min(graus_entrada.values())
    grau_maximo_saida = max(graus_saida.values())
    grau_minimo_saida = min(graus_saida.values())

    return (grau_maximo_entrada, grau_minimo_entrada, grau_maximo_saida, grau_minimo_saida)

# Exemplo de uso:
grafo_direcionado = nx.DiGraph([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])

grau_max_entrada, grau_min_entrada, grau_max_saida, grau_min_saida = grau_maximo_minimo(grafo_direcionado)
print("Grau máximo de entrada:", grau_max_entrada)
print("Grau mínimo de entrada:", grau_min_entrada)
print("Grau máximo de saída:", grau_max_saida)
print("Grau mínimo de saída:", grau_min_saida)
