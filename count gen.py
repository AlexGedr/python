s = input()
i = 0
j = len(s)
t = 1
k = 1
s2 =[]
while k < j:
    if s[i] == s[k]:
        t += 1
        i += 1
        k += 1
    else:
        
        print(s[i]+str(t), end='')
        t = 1
        i += 1
        k += 1
print(s[i]+str(t), end='')

   


         




        
