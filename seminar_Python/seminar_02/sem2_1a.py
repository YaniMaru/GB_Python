n = int(input("Введите натуральное число n "))
result = "1, "
res = 1
for i in range(1, n):
    res *= (-3)
    result += str(res)
    result += ", "
print(result[0:(len(result) - 2)])
