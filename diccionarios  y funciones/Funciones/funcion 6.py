# Parametros por defecto: 
# Define una funcion llamada "compra" que toma tres argumentos: marca, cantidad y valor y tiene un valor por defecto
def compra(marca, cantidad, valor=2500000):
    # La funcion retorna un diccionario con tres claves: "marca", "cantidad" y "valor"
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor = valor * cantidad
    )
# Llama la funcion "compra" con argumentos y almacena el resultado en una variable
resultado = compra("AMD", 3)
# Imprimir el resultado en una cadena (f-string)
print(f'Lo comprado fue: {resultado}') 