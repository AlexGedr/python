a = int(input())
b = a % 1000
c = a // 1000
x1 = b % 10
x2 = b % 100 // 10
x3 = b // 100
x4 = c % 10
x5 = c % 100 // 10
x6 = c // 100
if (x1 + x2 + x3) == (x4 + x5 + x6):
    print('Счастливый')
else:
    print ('Обычный')
