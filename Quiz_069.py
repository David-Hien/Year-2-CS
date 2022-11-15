class quiz069:
    def __init__(self, text):
        self.text = text

    def build(self):    # Swap two words
        return self.text.split(" ")[1] + " " + self.text.split(" ")[0]


test1 = quiz069("Hello World!!")
print(test1.build())