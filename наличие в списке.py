a = [int(i) for i in input().split()]
b = int(input())
c = []
i = 0
p = str('Отcутствует')
while i < len(a):
    if b not in a:
        print(p, end='')
        break
    elif a[i] == b:
        c.append(i)
    i += 1        
print(*c)


        
        
            
  
        
