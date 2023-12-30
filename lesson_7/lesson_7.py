# coding=windows-1251
# Задание 1
print("Введите строку без пробелов")
s = input()
if s == s[::-1]:
    print("yes")
else:
    print("no")

#Задание 2
print("Введите строку")
s = input()
start_str = 0 
end_str = 0
new_str = ""
is_space = s[0]==' '
while start_str < len(s):
    while end_str < len(s) and ((is_space and s[end_str] == ' ') or (not is_space and s[end_str] != ' ')):
        end_str += 1
    if is_space:
        new_str = new_str + " " 
    else:
        new_str = new_str + s[start_str:end_str]
    start_str = end_str            
    is_space = not is_space    
print(new_str)
