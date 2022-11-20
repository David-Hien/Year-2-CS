class quiz072:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2
    
    def hexToBin(self, text):    # Convert hex to binary
        short_bin = bin(int(text, 16))[2:]
        return "".join(["0" for _ in range(len(text) * 4 - len(short_bin))]) + short_bin

    def binToHex(self, text):   # Convert binary to hex
        return hex(int(text, 2))[2:]

    def xor(self, a, b):    # XOR two binary strings
        return "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])

    def build(self):
        return self.binToHex(self.xor(self.hexToBin(self.text1), self.hexToBin(self.text2)))

test1 = quiz072("3b101c091d53320c000910", "071d154502010a04000419")
print(test1.build())
