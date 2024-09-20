def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente -1)
res = potencia(3,3)
print(res)