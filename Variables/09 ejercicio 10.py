# Programa que determina el salario de persona
ganancia_diaria = int(input("ingrese la cantidad de dinero que ganas a diario: "))
dias_trabajados = int(input("ingrese los dias que trabajas: "))
dinero_dias = dias_trabajados * ganancia_diaria
pension = dinero_dias / 100 * 10
salud = dinero_dias / 100 * 15
pago_total = dinero_dias - pension - salud
print ("tu pago total mensual que te llega es: ", pago_total)
