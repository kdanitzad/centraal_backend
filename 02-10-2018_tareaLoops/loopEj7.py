lista = []
while True:
    word = input()
    if(word == 'detente'):
        break
    print('ingresa una palabra:')
    lista.append(word)
    print(lista)
    print('lista tiene: {} items'.format(len(lista)))
