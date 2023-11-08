#EJERCICIO: Tome el presente ejercicio, y pase a la funcion la lista con los dias de la semana restantes
def lista(arg, result=[]):
    result.append(arg)
    print(result)
# Lista con los dias de la semana
diasDeSemana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']
# Llama la funcion "lista" con el argumento 'domingo' y la lista "diasDeSemana"
for dia in diasDeSemana:
    lista(dia, []) 