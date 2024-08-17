string = input('Digite uma palavra: ')
inversao = string[::-1]

if inversao == string.lower():
    print('É polidromo')
else:
    print('Não é um polidromo')