from datetime import datetime

# Pedir la fecha de nacimiento en formato DD/MM/AAAA
fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato DD/MM/AAAA: ")

# Convertir la fecha de nacimiento a un objeto datetime
nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

# Obtener la fecha actual
hoy = datetime.now()

# Calcular la diferencia en días
dias_de_edad = (hoy - nacimiento).days

# Mostrar el resultado
print(f"Tienes {dias_de_edad} días de edad.")

