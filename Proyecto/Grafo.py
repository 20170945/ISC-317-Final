from collections import defaultdict, deque
from PQ import PriorityQueue


# Este algoritmo fue implementado a base del siguiente video
# https://youtu.be/pSqmAO-m7Lk
def dijkstra(grafo, inicio, fin):
    distance = defaultdict(lambda: float('inf'))
    past = defaultdict(lambda: None)
    visited = set()
    pq = PriorityQueue()
    distance[inicio] = 0
    pq.push(0, inicio)
    while not pq.is_empty():
        peso, nodo = pq.pop()
        visited.add(nodo)
        if distance[nodo] < peso:
            continue
        for adj, value in grafo[nodo].items():
            if adj in visited:
                continue
            next_distance = peso + value
            if next_distance < distance[adj]:
                distance[adj] = next_distance
                past[adj] = nodo
                pq.push(next_distance, adj)
    next = fin
    path = deque()
    while next!=None:
        path.appendleft(next)
        next=past[next]
    return (list(path) if len(path)>1 else None, distance[fin])