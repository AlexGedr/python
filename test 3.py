n = int(input())#размер матрицы
a = [[0]*n for i in range(n)]# создание матрицы
count = 0 # количество заполненных ячеек
for i in range(n): #заполнение 1 строки
    count += 1
    a[0][i] = count
j = 0
i = n - 1
n -= 1#устанавливаем размер 1 блока 1 витка
while len(a)**2 != count:
    for k in range(n):# движение вниз
        j += 1
        count += 1
        a[i][j] = count
    for k in range(n-1):# движение влево
        i -= 1
        count += 1
        a[i][j] = count
    for k in range(n-1):# движение вверх
        j -= 1
        count += 1
        a[i][j] = count
    for k in range(n-1):# движение вправо
        i += 1
        count += 1
        a[i][j] = count
    n -= 2 #обеспечение переход на внутренний виток
for i in range(len(a)): #вывод полученной матрицы
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
