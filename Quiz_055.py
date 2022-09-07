class Converter():
    def __init__(self, number):
        self.number = number

    def binirize(self):
        result = ""

        while self.number > 0:
            result = str(self.number % 2) + result
            self.number = self.number // 2

        return result

test1 = Converter(number=125)
print(test1.binirize())
