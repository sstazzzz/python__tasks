# coding=windows-1251

# Задание 1

pets = {}

name = input("Введите кличку вашего питомца:")
pets[name] = {}
pets[name]["Вид питомца"] = input("Введите вид вашего питомца:")
pets[name]["Возраст питомца"] = int(input("Введите возраст питомца:"))
pets[name]["Имя владельца"] = input("Введите имя владельца:")

age = pets[name]["Возраст питомца"]
remainder = age % 10
if remainder == 1:
    year = "год."
elif remainder >1 and remainder < 5:
    year = "года."
else:
    year = "лет."

print(f"Это {pets[name]['Вид питомца']} по кличке \"{name}\". Возраст питомца: {age} {year} Имя владельца: {pets[name]['Имя владельца']} ")   


#Задание 2

print("Задание 2")
my_dict = {}
for i in range(10, -6, -1):
    my_dict[i] = i**i
print(my_dict)   