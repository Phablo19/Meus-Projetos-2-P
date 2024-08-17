import random
cara_coroa = ['cara', 'coroa']
moeda = input('''
    [1] = Cara
    [2] = Coroa
              
=> ''')

resultado = random.choice(cara_coroa)

print(resultado)