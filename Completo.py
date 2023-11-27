import networkx as nx

def eh_grafo_completo(arestas):
    # Calcular o número máximo de vértices a partir das arestas fornecidas
    vertices = set()
    for u, v in arestas:
        vertices.add(u)
        vertices.add(v)
    
    numero_vertices = len(vertices)

    # Criar um grafo não direcionado
    grafo = nx.Graph(arestas)

    # Calcular o número máximo de arestas para um grafo completo
    numero_maximo_arestas = (numero_vertices * (numero_vertices - 1)) // 2

    # Verificar se o número de arestas no grafo é igual ao número máximo
    return grafo.number_of_edges() == numero_maximo_arestas

# Exemplo de lista de arestas para um grafo não direcionado
lista_arestas_exemplo = [(1, 2), (1, 3), (2, 3), (1, 4), (2, 4), (3, 4)]

# Verificar se o grafo é completo
if eh_grafo_completo(lista_arestas_exemplo):
    print("O grafo é completo.")
else:
    print("O grafo não é completo.")
