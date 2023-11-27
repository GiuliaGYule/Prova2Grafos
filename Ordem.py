from Graph import construir_grafo
import networkx as nx

def ordem_do_grafo(grafo):
    return grafo.order()

# Exemplo de lista de arestas
lista_arestas_exemplo = [(1, 2), (2, 3), (3, 1), (3, 4)]

# Construir o grafo
#grafo = construir_grafo(lista_arestas_exemplo, direcionado=False)

# Calcular a ordem do grafo
#ordem = ordem_do_grafo(grafo)

#print(f'A ordem do grafo é: {ordem}')