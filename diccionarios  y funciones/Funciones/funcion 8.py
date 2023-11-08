#Modificando parametros mutables
# Define una funcion llamada "listalimpia" que toma dos argumentos = "arg" y "result"
def listalimpia(arg, result=None): # "None" indica que si no se proporciona un valor al parametro cuando se llama a la funcion, se le asignara un valor predeterminado de "None"
    # Verificar si "result" es None 
    if result is None:
        # Si "result" es None, se inicializa como una lista vacia
        result = []
    # Se agrega el valor de "arg" a la lista "result"
    result.append(arg)
    # Se imprime la lista
    print(result)
# Llama la funcion "listalimpia" con el argumento "a" y "b"
listalimpia("a")
listalimpia("b") 