total2 = 0
total3 = 0
for i in range(100):
    if i%2 == 0:
        print('{} multiplo de 2'.format(i))
        total2 +=1
    elif i%3 == 0:
        print('{} multiplo de 3'.format(i))
        total3 +=1
print('total de multiplos de 2={}'.format(total2))
print('total de multiplos de 3={}'.format(total3))
