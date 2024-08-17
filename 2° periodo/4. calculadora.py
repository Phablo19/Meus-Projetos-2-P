n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro numero: '))

opcoes = input('''
    [1] = adição
    [2] = multiplicação
    [3] = subtração 
    [4] = divisão 

=> ''')

if opcoes == "1":
    total = n1 + n2
    print(total)
elif opcoes == "2":
    total = n1 * n2
    print(total)
elif opcoes == "3":
    total = n1 - n2
    print(total)
elif opcoes == "4":
    total =  n1 / n2
    print(total)