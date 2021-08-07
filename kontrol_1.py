number = input("Введите номер карты: ")

x = 0
n = ''
print("Вывод на экран:")
for i in number:
    x+=1
    if x <= len(number)-4:
        n = n+"*"
    if x > len(number)-4:
        n = n+i

print(n)

