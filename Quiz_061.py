class vowels:   # Class name
    def __init__(self, msg):    # Constructor
        self.msg = msg
        self.vowels = {"a":1, "i":2, "u":3, "e":4, "o":5}
        self.result = ""

    def extract(self):  # Change vowels into numbers
        for char in self.msg:
            if char in self.vowels:
                self.result += str(self.vowels[char])
            else:
                self.result += char

        return self.result

print(vowels("Hello World").extract())
print(vowels("anime").extract())