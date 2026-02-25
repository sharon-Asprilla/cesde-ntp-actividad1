# Tema: Input y Casting (Conversión de tipos)

# Ejercicio 1: Pide al usuario que ingrese su nombre usando input() y luego imprime un saludo 
# personalizado que incluya su nombre.
# Escribe tu código debajo de esta línea:

nombre = input("Por favor, ingresa tu nombre: ")
print("¡Hola", nombre + "!", "Bienvenid@ a este mundo bello :)")


# Ejercicio 2: Pide al usuario que ingrese su edad como texto (input siempre devuelve texto).
# Convierte esa edad a un número entero (casting) y luego calcula y muestra cuántos años tendrá 
# en el año 2050 (puedes asumir que el año actual es 2024 para el cálculo, o restarle su año de nacimiento).
# Simplificado: asume que sumarle 26 años le da su edad en 2050.
# Escribe tu código debajo de esta línea:

edad_texto = input("Por favor, ingresa tu edad: ")  
edad = int(edad_texto)  
edad_2= edad + 26   
print("En el año 2050 tendrás", edad_2, "años.")



# Ejercicio 3: Pide al usuario que ingrese el precio de un producto. Convierte el valor ingresado 
# a un número decimal (float). Luego, calcula y muestra el precio con un 20% de descuento.
# Escribe tu código debajo de esta línea:
precio = input ("ingrese el precio de su producto ")
precio = float(precio)
precio2 = precio * 0.20
precio_descuento = precio2- precio 
print("el precio del producto es ",precio,"el descuento es de ",precio2,"el precio final es ","el precio total es ",precio_descuento)

