class quiz070:
    def build(self):
        print("The quiz is trivial")    # is it "not BC" or "notB C" or not "notC B"?
        print("| A | B | C | AB + not B + not CB |")

        for i in range(8):
            A = i // 4
            B = (i // 2) % 2
            C = i % 2
            res = (A and B) or (not B) or (not C and B)

            print(f"| {A} | {B} | {C} | {int(res)} |")
            


test1 = quiz070()
test1.build()