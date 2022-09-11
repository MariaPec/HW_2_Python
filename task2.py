# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

n = int(input("Введите число N "))


sum = 0

for i in range(1, n+1):
    sum = sum + i
    print(i)

print("") 
print(sum)    
