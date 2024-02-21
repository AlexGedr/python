n = int(input())
a= []
c = 1
for i in range(n):
    b = [c]*c
    c += 1
    a.extend(b)
print(*a[0:n])


    
