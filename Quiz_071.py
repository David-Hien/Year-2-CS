class quiz071:
    def __init__(self, text):
        self.text = text
    
    def build(self):    # Convert hex to ascii
        return "".join([chr(int("".join(c), 16)) for c in zip(self.text[0::2], self.text[1::2])])


test1 = quiz071("48656c6c6f20576f726c64")
print(test1.build())