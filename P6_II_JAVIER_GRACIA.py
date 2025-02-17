# Entrada de la presión en psi
presion = float(input("¿Qué presión lee el sensor en psi?"))

# Determina la velocidad del motor según la presión
if presion < 20:
    velocidad = 30
elif 20 <= presion <= 50:
    velocidad = 60
else:
    velocidad = 100

# Escribe la velocidad a la que debe ir el motor
print(f"El motor girará a {velocidad}% de velocidad.")

#-----------------------------------------------------------------------------------------------------------

# Entrada de pulsos positivos y negativos
pulsos_positivos = int(input("Ingresa la cantidad de pulsos positivos: "))
pulsos_negativos = int(input("Ingresa la cantidad de pulsos negativos: "))

# Determinar la dirección del giro
if pulsos_positivos > pulsos_negativos:
    direccion = "Horario"
elif pulsos_negativos > pulsos_positivos:
    direccion = "Antihorario"
else:
    direccion = "Detenido"

# Escribe el sentido de giro del motor
print("La dirección del giro es:", direccion)