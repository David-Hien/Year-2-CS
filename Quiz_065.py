class quiz065:
    def __init__(self, n, water):
        self.n = n
        self.water = water

    def build(self):
        for i in range(self.n):
            print(" " * i + self.water)


test1 = quiz065(5, "-")
test1.build()