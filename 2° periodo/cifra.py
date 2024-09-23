import string, random

maiuscula = (string.ascii_uppercase)
minuscula = (string.ascii_lowercase)
digitos = (string.digits)

senha = []
nova_senha = []
quantidade = 8

qnt_maiuscula = random.randint(1, (quantidade - 2))
qnt_numeros = random.randint(1, (quantidade - qnt_maiuscula - 1))
qnt_minuscula = quantidade - qnt_numeros - qnt_maiuscula

for i in range(qnt_maiuscula):
    senha.append(random.choice(maiuscula))
for i in range(qnt_numeros):
    senha.append(random.choice(digitos))
for i in range(qnt_minuscula):
    senha.append(random.choice(minuscula))
random.shuffle(senha)

def cifraCesar(senha):
    if len(senha) == 0:
        return nova_senha
    
    if senha[0] in digitos:
        posicao = digitos.index(senha[0])
        if (posicao + 3) >= len(digitos):
            posicao = (posicao + 3) - len(digitos)
            nova_senha.append(digitos[posicao])
        else:
            nova_senha.append(digitos[posicao + 3])

    elif senha[0] in maiuscula:
        posicao = maiuscula.index(senha[0])
        if (posicao + 3) >= len(maiuscula):
            posicao = (posicao + 3) - len(maiuscula)
            nova_senha.append(maiuscula[posicao])
        else:
            nova_senha.append(maiuscula[posicao + 3])

    elif senha[0] in minuscula:
        posicao = minuscula.index(senha[0])
        if (posicao + 3) >= len(minuscula):
            posicao = (posicao + 3) - len(minuscula)
            nova_senha.append(minuscula[posicao])
        else:
            nova_senha.append(minuscula[posicao + 3])

    return cifraCesar(senha[1:])

print(''.join(senha))

resultado = cifraCesar(senha)
print(''.join(resultado))