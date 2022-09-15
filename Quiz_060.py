class colorLog:
    def build(self):
        count = 0
        result = ""
        dict = {0:"\33[0;31m red", 1:"\33[0;34m blue", 2:"\33[0;32m green", 3:"\33[0;30m black"}
        for _ in range(5):
            row = ""

            for _ in range(5):
                row += f"{dict[count%4]} ".center(10)
                count += 1

            result += row.center(5) + "\n"
        
        return result

print(colorLog().build())