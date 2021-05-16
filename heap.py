import math

class Heap:

    def __init__(self, isMax = True):
        self.isMax = isMax
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        filho = self.nos
        while True:
            if filho == 1: #está na raiz? topo?
                break
            pai = filho // 2 #valor truncado
            verifica = self.heap[pai-1][0] >= self.heap[filho-1][0] if self.isMax else self.heap[pai-1][0] <= self.heap[filho-1][0]
            if verifica: #se quiser o heap min, use <=. Usa -1 pois o array inicia em 0
                break
            else:
                self.heap[pai-1], self.heap[filho-1] = self.heap[filho-1] , self.heap[pai-1] #troca de posição
                filho = pai

    def mostra_heap(self):
        print(self.heap)
        print("A estrutura heap é a seguinte:")
        nivel = int(math.log(self.nos,2))
        aux = 0
        for i in range(nivel):
            for j in range(2**i):
                print(f"{self.heap[aux]}", end=" ")
                aux += 1
            print("")
        for i in range(self.nos - aux):
            print(f"{self.heap[aux]}", end=" ")
            aux += 1
        print("")

    def remove_no(self):
        aux = self.heap[0]
        self.heap[0] = self.heap[self.nos-1]
        self.heap.pop()
        self.nos -= 1
        pai = 1
        while True:
            filho = 2 * pai #formula para obter a pos do filho
            if filho > self.nos: 
                break
            if filho + 1 <= self.nos: #filho a direita existe?
                verifica = self.heap[filho+1-1][0] > self.heap[filho-1][0] if self.isMax else self.heap[filho+1-1][0] < self.heap[filho-1][0]
                if verifica: #filho a direita é maior que filho a esquerda? < se for HeapMin
                    filho += 1
            verifica = self.heap[pai-1][0] >= self.heap[filho-1][0] if self.isMax else self.heap[pai-1][0] <= self.heap[filho-1][0]
            if verifica: #<=heapmin
                break
            else:
                self.heap[filho-1], self.heap[pai-1] = self.heap[pai-1], self.heap[filho-1] #troca de posição
                pai = filho
        return aux
    
    def tamanho(self):
        return self.nos
    
    def maior_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return "Arvore vazia"

    def filho_esquerda(self, i):
        if self.nos >= 2*i:
            return self.heap[2*i-1]
        return "Esse nó não tem filho"

    def filho_direita(self, i):
        if self.nos >= 2*i+1:
            return self.heap[2*i]
        return "Esse nó não tem filho ah direita"

    def pai(self, i):
        if self.nos != 0:
            return self.heap[i//2-1]
        else:
            return "Heap vazio, sem pai"



"""
h = Heap(isMax=True)
h.adiciona_no(17,1)  
h.adiciona_no(36,2)
h.adiciona_no(25,3)
h.adiciona_no(7,4)
h.adiciona_no(3,5)
h.adiciona_no(100,6)
h.adiciona_no(1,7)
h.adiciona_no(2,7)
h.adiciona_no(19,8)

h.mostra_heap()

max = h.remove_no()
print(f"elemento max: {max}\n")
h.mostra_heap()

print(f"Tamanho: {h.tamanho()}")
print(f"filho_esquerda 25: {h.filho_esquerda(3)}")
print(f"filho_direita 25: {h.filho_direita(3)}")
print(f"pai 25: {h.pai(3)}")"""