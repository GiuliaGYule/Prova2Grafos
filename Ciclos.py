import networkx as nx

def encontrar_ciclos_unicos(grafo):
    """
    Encontra todos os ciclos únicos em um grafo direcionado, omitindo ciclos que contenham combinações de vértices de outros ciclos.

    Parâmetros:
    - grafo: Grafo direcionado representado por um objeto NetworkX.

    Retorna:
    - Lista de listas, onde cada lista é um ciclo único no grafo.
    """
    ciclos = nx.simple_cycles(grafo)

    # Filtrar ciclos
    ciclos_unicos = []
    for ciclo in ciclos:
        is_subset = False
        for ciclo_existente in ciclos_unicos:
            if set(ciclo).issubset(ciclo_existente):
                is_subset = True
                break
        if not is_subset:
            ciclos_unicos.append(ciclo)

    return ciclos_unicos

# Exemplo de uso:
grafo_direcionado = nx.DiGraph([(1, 2), (1, 3), (2, 3)])
resultado = encontrar_ciclos_unicos(grafo_direcionado)
print("Ciclos únicos no grafo direcionado:", resultado)
