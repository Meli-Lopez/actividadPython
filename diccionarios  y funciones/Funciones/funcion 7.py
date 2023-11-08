#Modificando parametros mutables, es decir que se puede cambiar
# Define una funcion llamada "lista" que toma dos argumentos: "arg" y "result".
def lista(arg, result=[]): # El argumento "result" tiene un valor predeterminado que es una lista vacia.
    result.append(arg) # La funcion agrega el argumento "arg" a la lista "result".
    # La funcion imprime la lista "result" despues de agregar "arg".
    print(result)
# Llamada la funcion "lista" con el argumento 'domingo' y una lista vacia como segundo argumento.
lista('domingo', []) 