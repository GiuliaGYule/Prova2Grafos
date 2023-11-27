import networkx as nx

def eh_grafo_direcionado_completo(arestas):
    # Calcular o número máximo de vértices a partir das arestas fornecidas
    vertices = set()
    for u, v in arestas:
        vertices.add(u)
        vertices.add(v)

    numero_vertices = len(vertices)

    # Criar um grafo direcionado
    grafo = nx.DiGraph(arestas)

    # Calcular o número máximo de arestas para um grafo direcionado completo
    numero_maximo_arestas = numero_vertices * (numero_vertices - 1)

    # Verificar se o número de arestas no grafo é igual ao número máximo
    return grafo.number_of_edges() == numero_maximo_arestas

# Exemplo de lista de arestas para um grafo direcionado completo
lista_arestas_exemplo_direcionado = [(1, 2), (1, 3), (2, 3), (2, 1), (3, 1), (3, 2), (1, 4)]

# Verificar se o grafo direcionado é completo
if eh_grafo_direcionado_completo(lista_arestas_exemplo_direcionado):
    print("O grafo direcionado é completo.")
else:
    print("O grafo direcionado não é completo.")
