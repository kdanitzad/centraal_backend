print('dame un numero y te dare los multiplos de 3:')
num = int(input())
for i in range(num+1):
    if i%3 == 0 and i != 0:
        print(i)
