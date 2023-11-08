#Funciones anonimas «lambda», con la palabra lambda no se necesita colocar el def
numero_palabras = lambda t: len(t.strip().split()) # La t es el argumento que toma la funcion lambda
# len() se utiliza para calcula la longitud de la lista
# strip() se utiliza para eliminar los espacios en blanco 
# split() se utiliza para dividir la cadena en palabras separadas por espacios en blanco.
# Llama a la funcion lambda con un argumento y lo imprime
print(numero_palabras("hola, esto es una prueba con lambda")) 