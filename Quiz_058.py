class neighbor:
    def __init__(self, n, lst):
        self.n = n
        self.lst = lst
        self.result = [[] for _ in range(n)]

    def __call__(self):
        for nodes in self.lst:
            a, b = nodes[0], nodes[1]

            if a >= self.n or b >= self.n:
                return "Error"

            self.result[a].append(b)
            self.result[b].append(a)

        return self.result

test1 = neighbor(4, [[0, 1], [0, 2], [2, 3], [2, 1]])
print(test1())