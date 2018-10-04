i=1
totalI=0
totalP=0
while i <= 100:
    if i%2 == 0:
        totalP += i
    else:
        totalI += i
    i+=1
print('suma de pares: {}'.format(totalP))
print('suma de impares: {}'.format(totalI))
