from collections import defaultdict, deque

class GrafoResidual:
    def __init__(self, grafo):
        self.grafo = grafo
        self.residual = defaultdict(dict)

    def adicionar_aresta_residual(self, u, v, capacidade):
        self.residual[u][v] = capacidade
        self.residual[v][u] = 0

def edmonds_karp(grafo, fonte, destino):
    def bfs(grafo_residual, pai, fonte, destino):
        visitado = set()
        fila = deque()
        fila.append(fonte)
        visitado.add(fonte)
        pai[fonte] = None

        while fila:
            u = fila.popleft()
            for v, capacidade in grafo_residual.residual[u].items():
                if v not in visitado and capacidade > 0:
                    fila.append(v)
                    visitado.add(v)
                    pai[v] = u
        return destino in visitado

    grafo_residual = GrafoResidual(grafo)
    pai = {}

    fluxo_maximo = 0

    while bfs(grafo_residual, pai, fonte, destino):
        caminho_fluxo_minimo = float('inf')
        v = destino

        while v != fonte:
            u = pai[v]
            caminho_fluxo_minimo = min(caminho_fluxo_minimo, grafo_residual.residual[u][v])
            v = u

        v = destino
        while v != fonte:
            u = pai[v]
            grafo_residual.residual[u][v] -= caminho_fluxo_minimo
            grafo_residual.residual[v][u] += caminho_fluxo_minimo
            v = u

        fluxo_maximo += caminho_fluxo_minimo

    return fluxo_maximo

# Exemplo de uso:
grafo = {
    'A': {'B': 10, 'C': 5},
    'B': {'A': 0, 'C': 15},
    'C': {'A': 0, 'B': 0}
}

fonte = 'A'
destino = 'C'

fluxo_maximo = edmonds_karp(grafo, fonte, destino)
print(f"Fluxo Máximo de {fonte} para {destino}: {fluxo_maximo}")
