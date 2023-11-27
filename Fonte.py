import networkx as nx
from Graph import construir_grafo

def encontrar_vertice_fonte(grafo):
    if not grafo.is_directed():
        print("O grafo não é direcionado. Não há vértice fonte.")
        return None

    fontes = [node for node, in_degree in grafo.in_degree() if in_degree == 0]

    if not fontes:
        print("Não há vértice fonte no grafo.")
        return None

    if len(fontes) == 1:
        print(f"O vértice fonte é: {fontes[0]}")
        return fontes[0]
    else:
        print("O grafo tem múltiplos vértices fonte.")
        return fontes

# Exemplo de lista de arestas para um grafo direcionado
lista_arestas_exemplo_direcionado = [(1, 2), (2, 3), (3, 1), (3, 4)]

# Construir o grafo direcionado
grafo_direcionado = construir_grafo(lista_arestas_exemplo_direcionado, direcionado=True)

# Encontrar o vértice fonte
vertice_fonte = encontrar_vertice_fonte(grafo_direcionado)