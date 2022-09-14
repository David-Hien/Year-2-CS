class timeTrial:
    def build():
        count = 1
        for z in range(3):
            print(f"\nz{z+1}")
            for _ in range(5):
                for _ in range(5):
                    print(count, end=" ")
                    count += 1

                print()

        return

timeTrial.build()