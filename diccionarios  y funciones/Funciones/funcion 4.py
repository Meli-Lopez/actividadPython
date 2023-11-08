#Funciones con Parametros Posicionales: 

# Definicion de una funcion llamada "compra" que toma tres argumentos: marca, cantidad y valor
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad
    )
# Llama la funcion "compra" con argumentos y almacena el resultado en un diccionario
resultado = compra("AMD", 3, 2500000)

# Imprime el resultado utilizando una cadena formateada (f-string)
print(f' Lo comprado fue: {resultado}') 