import math
import random


class open_doors:
    def __init__(self, num_student):
        self.num_student = num_student
        self.doors = [False] * num_student
        
    def count_open(self):   # count the number of open doors with math
        return math.floor(math.sqrt(self.num_student))

    def count_open_loop(self):  # count the number of open doors with loop
        for i in range(1, self.num_student + 1):
            for j in range(i - 1, self.num_student, i):
                self.doors[j] = not self.doors[j]
        return self.doors.count(True)

    def __repr__(self) -> str:  # string representation
        output = ""
        border_length = 0

        for item in self.doors: # generate the color stack
            output += self.color(item) + " | "
            border_length += len(str(item)) + 3

        border = "-" * (border_length + 1)

        return f"{border} \n| {output}\n{border}"

    def color(self, item):  # color the stack
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return "\x1b[38;2;{r};{g};{b};243m".format(r=r, g=g, b=b)  + str(item) + "\x1b[0m"


# Test
test1 = open_doors(num_student=10)
test2 = open_doors(num_student=100)
test3 = open_doors(num_student=200)
test4 = open_doors(num_student=5678)

print(test1.count_open_loop())
print(test2.count_open_loop())
print(test3.count_open_loop())
print(test4.count_open_loop())

print(test1)
print(test2)
print(test3)
print(test4)