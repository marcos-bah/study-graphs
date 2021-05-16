from heap import *

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

    def mostra_matriz(self):
        print("A matriz de adjacencias é:")
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo_vem = [[-1,0] for i in range(self.vertices)]
        custo_vem[origem - 1] = [0, origem]
        h = Heap(isMax=False)
        h.adiciona_no(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist+self.grafo[v-1][i]:
                        custo_vem[i] = [dist + self.grafo[v-1][i], v]
                        h.adiciona_no(dist + self.grafo[v-1][i], i+1)
        return custo_vem

"""
grafo = Grafo(7)
grafo.adiciona_aresta(1,2,5)
grafo.adiciona_aresta(1,3,6)
grafo.adiciona_aresta(1,4,10)
grafo.adiciona_aresta(2,5,13)
grafo.adiciona_aresta(3,4,3)
grafo.adiciona_aresta(3,5,11)
grafo.adiciona_aresta(3,6,6)
grafo.adiciona_aresta(4,5,6)
grafo.adiciona_aresta(4,6,4)
grafo.adiciona_aresta(5,7,3)
grafo.adiciona_aresta(6,7,8)

grafo.mostra_matriz()

print(grafo.dijkstra(1))
"""