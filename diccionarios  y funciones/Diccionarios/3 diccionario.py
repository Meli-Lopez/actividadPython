# Agregar datos al diccionario despues de creado:
# Se asigna el valor 0 a la variable 'calificaciones'.
calificaciones = {}

#Tecnicas de iteracion: 
# El update es para modificar o agregar un nuevo dato al diccionario 
calificaciones.update({"Rosa": 3.7, "German": 4.8})
# Se crea un diccionario con claves 'nombre' y 'notafinal' con sus valores.
calificaciones = {
    'nombre': 'Sandra',
    'notafinal': 5.0
}
# Se crea otro diccionario con nombres como claves y calificaciones como valores.
calificaciones = {
    'Sandra': 5.0,
    'Adriana': 5.0,
    'Mauricio': 4.5,
    'Jose': 2.5
}
# Se crea un ciclo que itera a traves del diccionario 'calificaciones' para imprimir las claves (variable i)y sus valores (Variable j).
for i, j in calificaciones.items(): #La función items() se utiliza para obtener una vista de los pares clave y valor del diccionario.
    print(i, j) 


# Tecnicas de iterar los diccionarios:
print("Tecnicas por clave") # Imprime el mensaje "Tecnicas por clave" en la consola.
# Inicia un bucle for para iterar a traves de las claves del diccionario 'calificaciones'.
for i in calificaciones.keys(): #keys: claves
    print(i) # Imprime las claves del diccionario 'calificaciones'.


print("Iterar por valor") # Imprime el mensaje "Iterar por valor" en la consola.
# Inicia un bucle for para iterar a traves de los valores del diccionario 'calificaciones'.
for j in calificaciones.values(): #values: valores 
    print(j)# Imprime los valores del diccionario 'calificaciones'.