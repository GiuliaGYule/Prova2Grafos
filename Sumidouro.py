import networkx as nx
from Graph import construir_grafo

def encontrar_vertice_sumidouro(grafo):
    if not grafo.is_directed():
        print("O grafo não é direcionado. Não há vértice sumidouro.")
        return None

    sumidouros = [node for node, out_degree in grafo.out_degree() if out_degree == 0]

    if not sumidouros:
        print("Não há vértice sumidouro no grafo.")
        return None

    if len(sumidouros) == 1:
        print(f"O vértice sumidouro é: {sumidouros[0]}")
        return sumidouros[0]
    else:
        print("O grafo tem múltiplos vértices sumidouros.")
        return sumidouros

# Exemplo de lista de arestas para um grafo direcionado
lista_arestas_exemplo_direcionado = [(1, 2), (2, 3), (3, 1), (3, 4)]

# Construir o grafo direcionado
grafo_direcionado = construir_grafo(lista_arestas_exemplo_direcionado, direcionado=True)

# Encontrar o vértice sumidouro
vertice_sumidouro = encontrar_vertice_sumidouro(grafo_direcionado)
