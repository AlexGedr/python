a = [int(i) for i in input().split()]
b = len(a)
i = 1
while i <= b:
    if b == 1:
        print(a[0])
        break
    if i == 1:        
        print(a[1]+a[-1])
        i+=1
    while 1<i<b:
        print(a[i-2]+a[i])
        i+=1
    else:
        print(a[i-2]+a[0])
        break

     
   
