# Programa que calcula el iva de productos
precio = float(input("ingrese el precio del producto "))
cantidad = int(input("ingrese la cantidad que va a comprar "))
iva = precio * cantidad
resultado = iva / 100 * 116
print("el iva total a pagar por el o los productos es: ", resultado, "pesos colombiano")