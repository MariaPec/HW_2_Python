# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1

n = int(input("Введите число N "))

a = 2

while a <= n:

    if n % a == 0:
        print(a)
        break
    else:
        a = a + 1
      
   

