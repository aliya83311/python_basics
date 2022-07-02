class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print("The car goes.")

    def stop(self):
        print("The car stops.")

    def turn(self, direction):
        if direction == "left":
            print("The car turns left.")
        elif direction == "right":
            print("The car turns right.")
        else:
            print("Impossible to turn.")

    def show_speed(self):
        print(f"The car`s {self.name} speed is {self.speed}.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Speed is too high!")
        else:
            print(f"The car`s {self.name} speed is {self.speed}.")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Speed is too high!")
        else:
            print(f"The car`s {self.name} speed is {self.speed}.")


my_car = TownCar("Toyota", 65, "red", False)
print("-" * 60)
print(my_car.name)
print(my_car.color)
print(my_car.is_police)
my_car.go()
my_car.turn("left")
my_car.show_speed()
my_car.stop()

car_car = SportCar("Ferrari", 120, "black", False)
print("-" * 60)
print(car_car.name)
print(car_car.color)
print(car_car.is_police)
car_car.go()
car_car.turn("ךרןנו")
car_car.show_speed()
car_car.stop()

truck = WorkCar("Caterpillar", 45, "orange", False)
print("-" * 60)
print(truck.name)
print(truck.color)
print(truck.is_police)
truck.go()
truck.turn("right")
truck.show_speed()
truck.stop()

city_police = PoliceCar("Volvo", 90, "blue", True)
print("-" * 60)
print(city_police.name)
print(city_police.color)
print(city_police.is_police)
city_police.go()
city_police.turn("right")
city_police.show_speed()
city_police.stop()
