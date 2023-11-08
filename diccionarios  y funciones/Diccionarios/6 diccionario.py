# BORRAR UN ELEMENTO DEL DICCIONARIO
# Diccionario 'calificaciones' con algunos elementos
calificaciones = {
    'Sandra': 5.0,
    'Adriana': 4.5,
    'Mauricio': 3.0,
    'Jose': 2.5
}

# Verifica si la clave 'Rosa' existe en el diccionario antes de eliminarla
if 'rosa' in calificaciones:
    del calificaciones['Rosa']
    print("'Rosa' eliminado del diccionario")

# Itera a través del diccionario 'calificaciones' después de eliminar la clave 'Rosa' e imprime las claves y sus valores restantes.
for i, j in calificaciones.items():
    print(i, j)
