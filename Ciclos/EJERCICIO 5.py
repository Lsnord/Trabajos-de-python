numero_usuario = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero_usuario * i
    print(f"{numero_usuario} x {i} = {resultado}")