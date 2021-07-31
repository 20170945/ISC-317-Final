#Este es un código que hize para la clase de Estructura de Datos para el periodo 2 del 2020-2021
#Fue hecho en Python 2.7, pero lo transforme a Python 3
class PriorityQueue:
    def __init__(self, ini=7):
        self.heap = [None] * (1 << ini)
        self.current = ini
        self.data_dict = {}

    def push(self, priority, data):
        if self.heap[0] is None:
            self.heap[0] = [priority, data]
            self.data_dict[data] = [0, 0]
        if data in self.data_dict:
            # print("Start",priority, data)
            # print(data, self.data_dict[data], self.heap[self.data_dict[data][0]])
            index = self.data_dict[data][0]
            if self.heap[index][0] > priority:
                self.heap[index][0] = priority
                if index > 0:
                    padre = (index - 1) // 2
                    while self.heap[padre][0] > priority or (self.heap[padre][0] == priority and self.heap[padre][1] > data):
                        self.data_dict[self.heap[padre][1]], self.data_dict[data] = self.data_dict[data], self.data_dict[self.heap[padre][1]]
                        self.heap[padre], self.heap[index] = self.heap[index], self.heap[padre]
                        # print(index, padre)
                        index = padre
                        padre = (index - 1) // 2
                        # print(index, padre)
                        if (padre < 0):
                            break
            # print(data, self.data_dict[data], self.heap[self.data_dict[data][0]])
            # print(self.heap)
            # print(self.data_dict)
            # print("End")


        else:
            index = 0
            while True:
                left = 2 * index + 1
                right = 2 * (index + 1)
                postright = 2 * (right + 1)
                # print(right >= len(self.heap), len(self.heap), )
                while postright >= len(self.heap):
                    self.heap.extend([None] * (1 << self.current))
                    self.current += 1
                    # print(len(self.heap))
                if (self.heap[index][0] > priority) or (self.heap[index][0] == priority and self.heap[index][1] > data):
                    self.data_dict[data] = self.data_dict[self.heap[index][1]]
                    self.heap[index][0], priority = priority, self.heap[index][0]
                    self.heap[index][1], data = data, self.heap[index][1]

                self.data_dict[self.heap[index][1]][1] += 1
                if self.heap[left] is None:
                    self.heap[left] = [priority, data]
                    self.data_dict[data] = [left, 0]
                    break
                elif self.heap[right] is None:
                    self.heap[right] = [priority, data]
                    self.data_dict[data] = [right, 0]
                    break
                elif self.data_dict[self.heap[left][1]][1] <= self.data_dict[self.heap[right][1]][1]:
                    index = left
                else:
                    index = right

    def pop(self):
        resultado = self.heap[0]
        index = 0
        if resultado is not None:
            lastweight = self.data_dict[resultado[1]][1]
            while self.heap[index] is not None:
                left = 2 * index + 1
                right = 2 * (index + 1)
                if self.heap[left] is None:
                    if self.heap[right] is None:
                        self.heap[index] = None
                    else:
                        self.heap[index] = self.heap[right]
                        temp = self.data_dict[self.heap[right][1]][1]
                        self.data_dict[self.heap[index][1]] = [index, lastweight - 1]
                        lastweight = temp
                        index = right
                elif self.heap[right] is None or self.heap[left][0] < self.heap[right][0] or (
                        self.heap[left][0] == self.heap[right][0] and self.heap[left][1] < self.heap[right][1]):
                    self.heap[index] = self.heap[left]
                    temp = self.data_dict[self.heap[left][1]][1]
                    self.data_dict[self.heap[index][1]] = [index, lastweight - 1]
                    lastweight = temp
                    index = left
                else:
                    self.heap[index] = self.heap[right]
                    temp = self.data_dict[self.heap[right][1]][1]
                    self.data_dict[self.heap[index][1]] = [index, lastweight - 1]
                    lastweight = temp
                    index = right

            self.data_dict.pop(resultado[1])
            return tuple(resultado)
        return None

    def peek(self):
        return self.heap[0]

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return self.data_dict.__len__()

    def is_empty(self):
        return self.__len__() == 0
