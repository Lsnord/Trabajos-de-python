n = int(input("ingrese un numero: "))
numN = [i for i in range (1, n+1)]
numNS = sum (i for i in range(1, n+1))
print(f"\nLos primeros {n} terminos naturales son: ")
print(numNS)
print("la suma del numero {n} es: ", (numNS))