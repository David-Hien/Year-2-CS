# Adder class
from lib.stack import stack


class adder:
    def __init__(self, text):
        self.text = text
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def sum(self):
        total = 0
        while not self.text.isEmpty():
            char = self.text.pop().lower()
            if char in self.alphabet:
                total += self.alphabet.index(char) + 1

        return total

# Interface example


def stackify(text):
    stk = stack()
    for char in text:
        stk.push(char)

    return stk


test1 = adder(stackify("Math"))
test2 = adder(stackify("maTH"))
test3 = adder(stackify("Hello World"))
test4 = adder(stackify("Computer SCIENCE"))

print(test1.sum())
print(test2.sum())
print(test3.sum())
print(test4.sum())
