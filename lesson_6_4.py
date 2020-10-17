class Car:
    is_police = False

    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        else:
            print(self.speed)


class PoliceCar(Car):
    is_police = True


car = Car('KIA', 50, 'yellow')
town_car = TownCar('Volvo', 70, 'black')
sport_car = SportCar('Lamb', 100, 'red')
work_car = WorkCar('Man', 50, 'white')
police_car = PoliceCar('Ford', 60, 'black')

print(car.color)
print(car.is_police)
print(town_car.name)
print(sport_car.speed)
print(work_car.color)
print(police_car.is_police)
car.go()
town_car.show_speed()
sport_car.stop()
work_car.show_speed()
police_car.turn('направо')
