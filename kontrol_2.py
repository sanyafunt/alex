word = input("Введите палиндром: " )
print(word[::-1])
if word == word[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")