
from ast import parse
import queue


class Node:
    def __init__(self, c, w, l=None, r=None):
        self.l = l
        self.r = r
        self.w = w
        self.c = c
        self.dir = ''
    
    def __str__(self):
        return self.c
    
    def __lt__(self, other):
        return self.w < other.w
    


def read_file(file):
    N = 0
    with open(file, 'r') as f:
        lines = f.readlines()
        data = []
        
        for line in lines:
            c = line.strip().split(' ')
            print(c)
            if len(c) == 2:
                t = (c[0], int(c[1]))
                data.append(t)
            else:
                N = int(c[0])

    return data, N


def print_codes(node, code=''): 
    newCode = code + str(node.dir) 
  
    if(node.l): 
        print_codes(node.l, newCode) 
    if(node.r): 
        print_codes(node.r, newCode) 
 
    if(not node.l and not node.r): 
        print(f"{node.c} {newCode}") 
        

data, N= read_file('E:/PJATK/NAI/MP/MP7/MP7/data.txt')
print(data)
data.sort(key = lambda x: x[1])

pq = queue.PriorityQueue()

for i in range(N):
    pq.put(Node(data[i][0], data[i][1]))
    

while pq.qsize() > 1:
    l = pq.get()
    l.dir = 0
    r = pq.get()
    r.dir = 1
    
    node = Node(l.c+r.c, l.w+r.w, l, r)
    pq.put(node)
    
print_codes(pq.queue[0])
    


