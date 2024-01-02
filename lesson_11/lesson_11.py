# coding=windows-1251

# Задание 1

def factorial(number):
    f = 1
    for i in range(2,number+1):
        f = f*i
    return f

print("Введите число и я посчитаю факториал его")
number = int(input())
my_list = []
for i in range(number, 0, -1):
    my_list.append(factorial(i))
print(my_list)


# Задание 2

pets = {}

def get_data():
    data = []
    data.append(input("Введите кличку вашего питомца: "))
    data.append(input("Введите вид вашего питомца: "))
    data.append(int(input("Введите возраст питомца: ")))
    data.append(input("Введите имя владельца: "))
    return data

def set_data(data, the_pet):
    name = data[0]
    the_pet[name] = {}
    the_pet[name]["Вид питомца"] = data[1]
    the_pet[name]["Возраст питомца"] = data[2]
    the_pet[name]["Имя владельца"] = data[3]

def create():
    data = get_data()
    the_pet = {}
    pets[len(pets)] = the_pet
    set_data(data, the_pet)
    
def read(index):
    if index >= len(pets):
        print("Нет записи с таким ключом")
        return
    name = list(pets[index].keys())[0]
    age = pets[index][name]["Возраст питомца"]
    year = get_suffix(age)
    print(f"Это {pets[index][name]['Вид питомца']} по кличке \"{name}\". Возраст питомца: {age} {year} Имя владельца: {pets[index][name]['Имя владельца']} ") 
    
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
        year = "год."
    elif remainder >1 and remainder < 5:
        year = "года."
    else:
        year = "лет."
    return year 

    
command = ""
while command != "stop":
    command = input("command_pets? ")
    if command == "create":
        create()
    elif command == "read":
        index = int(input("Введите индекс: "))
        read(index)
    elif command == "update":
        index = int(input("Введите индекс: "))
        update(index)
    elif command == "delete":
        index = int(input("Введите индекс: "))
        delete(index)
    elif command != "stop":
        print("Неизвестная команда: ", command)
