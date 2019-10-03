"""
Home Work 2, exercise 5.
"""
class Graph:
    """
    Example : graph [[[1,55]], [[0,55]]], done [True, False], num
    """
    def __init__(self, k):
        self.pair = []
        i = 0
        while i < len(k):
            while len(self.pair) <= k[i][0] or len(self.pair) <= k[i][1]:
                self.pair.append([])
            i += 1
        self.num = len(self.pair)
        self.done = [False]*self.num
        i = 0
        while i < self.num:
            j = 0
            while j < self.num:
                self.pair[i].append([j, 1000000000])
                j += 1
            i += 1
        i = 0
        while i < len(k):
            self.pair[k[i][0]][k[i][1]][1] = k[i][2]
            self.pair[k[i][1]][k[i][0]][1] = k[i][2]
            i += 1
    def way(self, node_start, node_end):
        """
        like Deiksra's algoritm
        """
        p = []
        d = []
        n = len(self.pair)
        for i in range(len(self.pair)):
            p.append(0)
            d.append(1000000000)
        d[node_start] = 0
        i = 0
        for i in range(n):
            v = -1
            j = 0
            for j in range(n):
                if not self.done[j] and (v == -1 or d[j] < d[v]):
                    v = j
            if d[v] == 1000000000:
                break
            self.done[v] = True
            j = 0
            for j in range(len(self.pair[v])):
                t = self.pair[v][j][0]
                length = self.pair[v][j][1]
                if d[v] + length < d[t]:
                    d[t] = d[v] + length
                    p[t] = v
        v = node_end
        path = []
        while v != node_start:
            path.append(v)
            v = p[v]
        path.append(node_start)
        print( *reversed(path))
