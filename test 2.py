a = [int(i) for i in input().split()]
b = int(input())
p = str('Отcутствует')
if b not in a:
    print(p, end='')
for index, item in enumerate(a):
    if item == b:        
        print(index, end=' ')



