digito =  int(input('Deseja ver qual tabuada?: '))
mutiplicador = 0
print('=============')
while True:
    
    if mutiplicador >= 10:
        break
    mutiplicador =  mutiplicador + 1
    total = digito * mutiplicador

    print(f'{digito} x {mutiplicador} = {total}')
print('=============')
print('     fim')