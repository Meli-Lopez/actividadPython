#Definir una funcion 
def saludar():
    print("saludo") #El print se utliza dentro de la misma funcion y no altera el programa principal
#Definir una funcion 
def retornarnumero(): 
    return 1 # Devuelve el valor 1
#devuelve la informacion por medio del programa principal y si puede afectar el programa principal

# Se llama la funcion 'saludar' y la funcion 'retornarnumero'
saludar()
retornarnumero() 

# Se compara el resultado de la funcion 'retornarnumero' con 1
if retornarnumero()==1:
    print("devolvio un uno")
else:
    print("No devolvio un uno")