# coding=windows-1251


class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"����������� ������ �������� {self.name} - {capacity} ����������"

# ������� 1        

autobus = Transport("Renault Logan", 180, 12)
print(f"�������� ����������: {autobus.name} ��������: {autobus.max_speed} ������: {autobus.mileage}")


# ������� 2

class Autobus(Transport):
        
    def seating_capacity(self, capacity = 50):
        return f"����������� ������ �������� {self.name}: {capacity} ����������"
    
autobus2 = Autobus("Renault Logan", 180, 12)
print(autobus2.seating_capacity())
