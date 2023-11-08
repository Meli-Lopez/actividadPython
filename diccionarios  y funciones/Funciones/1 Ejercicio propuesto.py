# EJERCICIO:  Escriba una función en Python que reproduzca lo siguiente: 𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2 Valor para X=3 y valor para Y=5

# Se le asignan los valores a "x" y "y" 
x = 3
y = 5
# Definir una funcion
def calcularF(x, y):
    resultado = x**2 + y**2 # los "**" son para elevar un numero 
    return resultado 
# Llamar la funcion con los valores asigandos
resultadoF = calcularF(x, y) 
# Imprimir el resultado
print(f'El valor de f ({x}, {y}) es {resultadoF}')