#Definir una funcion 
def saludar():
    print("saludo") #El print se utliza dentro de la misma funcion y no altera el programa principal
#Definir una funcion 
def retornarNumero(): 
    return 1 # Devuelve el valor 1
#devuelve la informacion por medio del programa principal y si puede afectar el programa principal

# Se llama la funcion 'saludar' y la funcion 'retornarnumero'
saludar()
retornarNumero() 

# Se compara el resultado de la funcion 'retornarnumero' con 1
if retornarNumero()==1:
    print("devolvio un uno")
else:
    print("No devolvio un uno")
