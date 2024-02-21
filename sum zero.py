a = []
while True:
    c = int(input())
    a.append(c)
    if sum(a) == 0:
            b = [ i*i for i in a]
            print(sum(b))
            break
 
