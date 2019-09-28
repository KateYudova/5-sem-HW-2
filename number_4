"""
Home Work 2, exercise 4.
"""
class Graph:
    """
    Example : graph [[1],[0]], num, visit [True, False], level [0, 1]
    """
    def __init__(self, k):
        self.pair = []
        i = 0
        while i < len(k):
            while len(self.pair) <= k[i][0] or len(self.pair) <= k[i][1]:
                self.pair.append([])
            i += 1
        self.num = len(self.pair)
        self.visit = [False]*self.num
        self.level = [-1]*self.num
        i = 0
        while i < len(k):
            self.pair[k[i][0]].append(k[i][1])
            self.pair[k[i][1]].append(k[i][0])
            i += 1
    def dfs(self, l):
        """
        deep, start - l
        """
        print (l)
        self.visit[l] = True
        for j in self.pair[l]:
            if not self.visit[j]:
                self.dfs(j)
    def bfs(self, r):
        """
        breadth, start - r
        """
        print("bfs:")
        self.level[r] = 0
        queue = [r]
        while queue:
            w = queue.pop(0)
            print(w)
            for j in self.pair[w]:
                if self.level[j] == -1:
                    queue.append(j)
                    self.level[j] = self.level[w] + 1
