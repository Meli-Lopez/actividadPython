# Definir una funcion llamada 'validarsiexiste' que tiene un argumento llamado 'obj'
def validarsiexiste(obj):
    # Comprobar si 'obj' tiene un valor que es verdadero (True)
    if obj:
        # Si 'obj' es verdadero, imprime un mensaje indicando que es True y muestra el valor de 'obj'
        print(f"{obj} is True")
    else:
        # Si 'obj' es falso, imprime un mensaje indicando que es False y muestra el valor de 'obj'
        print(f"{obj} is False") 

# Llamar a la funcion 'validarsiexiste' con el argumento 1
validarsiexiste(1)