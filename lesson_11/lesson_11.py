# coding=windows-1251

# ������� 1

def factorial(number):
    f = 1
    for i in range(2,number+1):
        f = f*i
    return f

print("������� ����� � � �������� ��������� ���")
number = int(input())
my_list = []
for i in range(number, 0, -1):
    my_list.append(factorial(i))
print(my_list)


# ������� 2

pets = {}

def get_data():
    data = []
    data.append(input("������� ������ ������ �������: "))
    data.append(input("������� ��� ������ �������: "))
    data.append(int(input("������� ������� �������: ")))
    data.append(input("������� ��� ���������: "))
    return data

def set_data(data, the_pet):
    name = data[0]
    the_pet[name] = {}
    the_pet[name]["��� �������"] = data[1]
    the_pet[name]["������� �������"] = data[2]
    the_pet[name]["��� ���������"] = data[3]

def create():
    data = get_data()
    the_pet = {}
    pets[len(pets)] = the_pet
    set_data(data, the_pet)
    
def read(index):
    if index >= len(pets):
        print("��� ������ � ����� ������")
        return
    name = list(pets[index].keys())[0]
    age = pets[index][name]["������� �������"]
    year = get_suffix(age)
    print(f"��� {pets[index][name]['��� �������']} �� ������ \"{name}\". ������� �������: {age} {year} ��� ���������: {pets[index][name]['��� ���������']} ") 
    
def update(index):
    data = get_data()
    the_pet = pets[index]
    name = list(the_pet.keys())[0]
    if name != data[0]:
        del the_pet[name]
    set_data(data, the_pet) 
    
def delete(index):
    pets.pop(index, None)
    
def get_suffix(age):
    remainder = age % 10
    if remainder == 1:
        year = "���."
    elif remainder >1 and remainder < 5:
        year = "����."
    else:
        year = "���."
    return year 

    
command = ""
while command != "stop":
    command = input("command_pets? ")
    if command == "create":
        create()
    elif command == "read":
        index = int(input("������� ������: "))
        read(index)
    elif command == "update":
        index = int(input("������� ������: "))
        update(index)
    elif command == "delete":
        index = int(input("������� ������: "))
        delete(index)
    elif command != "stop":
        print("����������� �������: ", command)
