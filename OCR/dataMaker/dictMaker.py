import math
from textwrap import indent


class Heap():
    def __init__(self, priority=0, mode=0) -> None:
        self.heap = []
        self.priority = priority
        self.mode = mode
    
    def __len__(self):
        return len(self.heap)
    
    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def checkUp(self, index):
        father = (index-1)//2
        if self.mode == 0:
            #小根堆
            if self.heap[index][self.priority] < self.heap[father][self.priority]:
                self.swap(index, father)
                self.checkUp(father)
            else:
                return
        else:
            if self.heap[index][self.priority] > self.heap[father][self.priority]:
                self.swap(index, father)
                self.checkUp(father)
            else:
                return

    def checkDown(self, index):
        c1 = index * 2 + 1
        c2 = index * 2 + 2
        if c1 >= len(self) or c2 >= len(self):
            self.swap(index, len(self)-1)
            return self.heap.pop()
        if self.mode == 0:
            #小根堆
            if self.heap[c1][self.priority] < self.heap[c2][self.priority]:
                self.swap(index, c1)
                self.checkUp(c1)
            else:
                self.swap(index, c2)
                self.checkUp(c2)
        else:
            if self.heap[c1][self.priority] > self.heap[c2][self.priority]:
                self.swap(index, c1)
                self.checkUp(c1)
            else:
                self.swap(index, c2)
                self.checkUp(c2)

    def insert(self, item):
        self.heap.append(item)
        self.checkUp(self.__len__()-1)

    def remove(self):
        return self.checkDown(0)

def make(path_list, otp_path):
    characters = {}
    cnt = 0
    for path in path_list:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                for c in line:
                    if characters.has_key(c):
                        characters[c] += 1
                    else:
                        characters[c] = 1
                    cnt += 1
    
    with open(otp_path, 'w', encoding='utf-8') as otp:
        heap = Heap(1, 1)
        for k, v in characters.items():
            heap.insert([k, v])
        while len(heap) > 0 :
            k, v = heap.remove()
            otp.write(k + '\t' + v/cnt + '\n')
