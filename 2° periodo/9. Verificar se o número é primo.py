n = int(input("Digite um número: "))

if n <= 1:
    print(f"{n} não é um número primo.")
elif n == 2:
    print(f"{n} é um número primo.")
elif n % 2 == 0:
    print(f"{n} não é um número primo.")
else:
    primo = True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            primo = False
            break
    
    if primo:
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")