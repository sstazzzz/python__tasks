# coding=windows-1251


class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} - {capacity} пассажиров"

# Задание 1        

autobus = Transport("Renault Logan", 180, 12)
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")


# Задание 2

class Autobus(Transport):
        
    def seating_capacity(self, capacity = 50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"
    
autobus2 = Autobus("Renault Logan", 180, 12)
print(autobus2.seating_capacity())
