# Programa que convierte segundos ingresados en horas y minutos
segundos = int(input("ingresa los segundos")) 
segundos1 = segundos if segundos >= 0 else -segundos
horas = segundos1 // 3600
minutos =(segundos1 % 3600) //60
segundos_restantes = segundos1 % 60
print("el resultado de los segundos en minutos es: ", horas, "hora(s)" "y en minutos es: ", minutos, "minuto(s)")