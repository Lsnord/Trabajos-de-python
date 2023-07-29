print("Este programa calculará la suma y el promedio de 10 números.")

numeros = []
for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

suma = sum(numeros)
promedio = suma / len(numeros)

print("\nResultados:")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")