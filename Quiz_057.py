class converter:
    def __init__(self, decimal, base):
        self.decimal = decimal
        self.base = base

    def symbols(self, number):
        if number > 9:
            return chr(number + 55)

    def build(self):
        result = ""
        while self.decimal > 0:
            result = str(self.symbols(self.decimal % self.base)) + result
            self.decimal = self.decimal // self.base

        return result

test1 = converter(10, 16).build()
test2 = converter(10987, 20).build()
test3 = converter(10987, 36).build()

print(test1)
print(test2)
print(test3)