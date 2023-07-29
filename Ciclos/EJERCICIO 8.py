num_filas = 4
numero = 1

for i in range(1, num_filas + 1):
    for _ in range(num_filas - i):
        print(" ", end="")
    for j in range(i):
        print(numero, end=" ")
        numero += 1
    print()