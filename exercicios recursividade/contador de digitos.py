def tamanhoDoNumero(i):
    if i:
        return tamanhoDoNumero(i//10) + 1
    return 0
    
digito = int(input('Informe o valor do digito: '))
resultado = tamanhoDoNumero(digito)
print(resultado)