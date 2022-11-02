class quiz068:
    def __init__(self, distance, time, velocity, fuel, fuel_consumption):
        self.distance = distance
        self.time = time
        self.velocity = velocity
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def check_fuel(self):   # check if the fuel is enough
        result = "Failure, "    # default result

        if self.distance < self.time * self.velocity:
            result += "Not enough time."
        elif self.fuel < self.distance / self.fuel_consumption:
            result += "Not enough fuel."
        else:
            result = "Welcome to Mars"

        return result


test1 = quiz068(100, 10, 10, 10, 10)
print(test1.check_fuel())