class quiz067:
    def __init__(self, n):
        self.n = n

    def build(self):
        for i in range(self.n):
            print("+" * self.n)


test1 = quiz067(5)
test1.build()