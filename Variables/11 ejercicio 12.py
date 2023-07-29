# Programa que calcula la hipotenusa por ingreso de catetos
numero1 = int(input("ingrese el primer lado hipotenusa"))
numero2 = int(input("ingrese el segundo lado hipotenusa"))
catetoA = numero1 * numero1
catetoB = numero2 * numero2
hipotenusa = catetoA + catetoB
resultado = hipotenusa ** 0.5
print ("la hipotenusa de los lados ingresados es: ", resultado)