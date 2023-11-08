#Ejemplo 2 funcion Lambda, es una funcion de una sola sentencia y hace un operacion o actividad en particular 

# Define una funcion (lambda) llamada "operadorand" que toma dos argumentos, "x" y "y" y realiza una operación AND en ellos
operadorAnd = lambda x, y: x & y
# Inicia un bucle externo para i en el rango de 0 a 1, es decir que el bucle realiza 2 iteraciones
for i in range(2):
    # Inicia un bucle interno para j en el rango de 0 a 1 (2 iteraciones) 
    for j in range(2):
        # Imprime una cadena que muestra los valores de i y j, asi como el resultado de la operacion AND
        print(f"{i} & {j} = {operadorAnd(i, j)}") 
