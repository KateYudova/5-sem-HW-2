"""
Home Work 2, exercise 6.
"""
class Graph:
    """
    Example : graph [[[1,55]], [[0,-10000000000]]], done [True, False], num
    """
    def __init__(self, k, q):
        self.pair = []
        i = 0
        for i in range(q+1):
            self.pair.append([])
        self.num = len(self.pair)
        self.done = [False]*self.num
        i = 0
        while i < self.num:
            j = 0
            while j < self.num:
                if i == 0:
                    self.pair[i].append([j, 0])
                else:
                    self.pair[i].append([j, -1*10000000000])
                j += 1
            i += 1
        i = 0
        while i < len(k):
            self.pair[k[i][0]][k[i][1]][1] = k[i][2]
            i += 1
    def way(self, node_start):
        """
        like Deiksra's algoritm
        """
        p = []
        d = []
        n = len(self.pair)
        for i in range(len(self.pair)):
            p.append(-1)
            d.append(-1*10000000000)
        d[node_start] = 0
        i = 0
        for i in range(n):
            v = -1
            j = 0
            for j in range(n):
                if not self.done[j] and (v == -1 or d[j] > d[v]):
                    v = j
            if d[v] == -1*10000000000:
                break
            self.done[v] = True
            j = 0
            for j in range(len(self.pair[v])):
                t = self.pair[v][j][0]
                length = self.pair[v][j][1]
                if d[v] + length > d[t] and self.pair[v][j][1] != -10000000000:
                    d[t] = d[v] + length
                    p[t] = v
        for z in range(len(self.pair)):
            if p[z] == -1 and z != 0 and z != node_start:
                print("-1")
                return
        maxi = 0
        for y in range(1, len(self.pair)):
            if d[y] > maxi:
                maxi = d[y]
        print(maxi)
times = eval(input("Times = "))
N = eval(input("N = "))
X = eval(input("X = "))
m = Graph(times, N)
m.way(X)
