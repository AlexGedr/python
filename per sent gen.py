gen = input()
s = len(gen)
gen = gen.upper()
a = gen.upper().count('G') + gen.upper().count('C')
print(a*100/s)
    
