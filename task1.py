# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

n = int(input("Введите кол-во монеток "))

from random import randint
count = 0
count1 = 0

for i in range(n):
    a = randint(0,1)
    print(a)

    if a == 0:
        count = count + 1
    else:
        count1 = count1 + 1

print(" ")
if count > count1:
    print(f"Нужно перевернуть {count1} монеты")
else:
    print(f"Нужно перевернуть {count} монеты")    

 
