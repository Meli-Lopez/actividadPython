#Funciones con Parametros Nominales: 
# Define una funcion llamada "compra" que toma tres argumentos: marca, cantidad y valor
def compra(marca, cantidad, valor):
    # La funcion retorna un diccionario con tres claves: "marca", "cantidad" y "valor"
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad
    )
# Llama la funcion "compra" con argumentos nombrados y almacenamiento del resultado en una variable "resultado"
resultado = compra(marca="AMD", cantidad=3, valor=2500000)
# Impresion del resultado en una cadena (f-string)
print(f'Lo comprado fue: {resultado}')