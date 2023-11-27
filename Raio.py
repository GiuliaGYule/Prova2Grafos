import networkx as nx

def calcular_raio(grafo):
    """
    Calcula o raio de um grafo.

    Parâmetros:
    - grafo: Grafo representado por um objeto NetworkX.

    Retorna:
    - O raio do grafo.
    """
    excentricidades = nx.eccentricity(grafo)
    raio = min(excentricidades.values())
    return raio

# Exemplo de uso:
grafo_exemplo = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1), (4, 2)])

raio_grafo = calcular_raio(grafo_exemplo)

print(f"O raio do grafo é: {raio_grafo}")
