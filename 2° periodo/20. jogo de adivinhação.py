import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)

    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 10.")

    while True:
        palpite = int(input("Faça sua adivinhação: "))

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou!!")
            break

resultado = jogo_adivinhacao()
print(resultado)