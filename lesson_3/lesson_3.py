# coding=windows-1251

# Задание 1 
print("Введите вид вашего питомца:")
type = input()
print("Введите возраст питомца:")
age = int(input())
print("Введите кличку питомца:")
name = input()

remainder = age % 10
if remainder == 1:
    year = "год."
elif remainder >1 and remainder < 5:
    year = "года."
else:
    year = "лет."
print(f"Это {type} по кличке \"{name}\". Возраст: {age} {year}")


# Задание 2
# Австралопитек, Человек умелый, Человек прямоходящий, Неандерталец, Человек разумный (Homo sapiens)
print("Введите 5 стадий этапа развития человека (антропогенез), поочередно и нажимая enter")
for i in range(5):
    if i == 0:
        print("1 стадия")
        a = input()
    elif i == 1:
        print("2 стадия")
        b = input()
    elif i == 2:
        print("3 стадия")
        c = input()
    elif i == 3:
        print("4 стадия")
        d = input()
    elif i == 4:
        print("5 стадия")
        e = input()        
print(a, b, c, d, e, sep="=>")
