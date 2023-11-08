# Se crean dos listas, 'nombres' y 'edades', que contienen nombres y edades correspondientes.
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']
# Se utiliza un bucle 'for' para iterar a traves de los elementos de 'nombres' y 'edades' al mismo tiempo.
for n, e in zip(nombres, edades): # En cada iteracion, 'n' es un nombre y 'e'una edad.
# La funcion 'zip' combina elementos de ambas listas en pares ordenados.
    print('Tu nombre es {0} y tu edad {1}.'.format(n, e)) #Format se utiliza para formatear cadenas de texto y para la inserción de valores en lugares especificos dentro de la cadena
# Itera a traves de dos listas ('nombres' y 'edades') utilizando zip para combinarlas y luego imprime un mensaje formateado con los valores.

# Crea un diccionario utilizando un diccionario por comprension con claves siendo valores al cuadrado para los elementos en el rango (2, 4, 6).
dicaleatorio = {x: x**2 for x in (2, 4, 6)}
print(dicaleatorio) 