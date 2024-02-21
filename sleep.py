A = int(input('рекомендуется спать  '))
B = int(input('не рекомендуется спать  '))
H = int(input('Аня спит  '))
if H < A:
    print ('Недосып')
elif A <= H <= B:
    print ('Это нормально')
elif H > B:
    print ('Пересып')
