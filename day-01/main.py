
print("🌙 Día 1 de #30NitesofCode")
# variables: python es sensible a mayusculas y minusculas es decir
nombre = "Juan" 
Nombre = "Juan"
# las variable (nombre) y (Nombre) no son iguales

# reglas para nombrar variables

"""
Inicio válido: Deben comenzar con una letra o un guion bajo _
Restricción de números: Nunca pueden comenzar con un dígito numérico
Caracteres permitidos: Solo se permiten letras, números y guiones bajos. No uses @, $, % ni espacios
Palabras reservadas: No puedes usar comandos del lenguaje como if, for, True o print
Estilo recomendado: Se utiliza el formato snake_case (palabras en minúsculas separadas por guiones bajos)

"""
# Ejemplo correctos
mi_variable = 30
usuario_id = 15

# Ejemplo incorrecto
"""
2mi_variable = "Error"
mi variable = "Error
""" 

# Comentarios: para los comentarios de una linea se utiliza la (#) 
# si quieres crear comentarios de varias lineas debes utilizar ("""Comentario""") 
# esto te permitira escribir comentarios multilineas

# Tipos de datos:
nombre =  "Andres"      # str (texto)
edad = 25               # int (entero)
altura = 1.81           # float (decimal)
soy_estudiante = True   # bool (booleano) la variable puede ser True o False

# Funcion print()
# La funcion sirve para imprimir por consola
# Cuenta con dos parametros especiales los cuales son (sep) y (end)
# sep: este parametro nos permite el separador de los elemento por ejemplo si quiero que todas mis palabras esten separadas por (-)
# end: print() por defecto al finalizar genera un salto de linea eso esta por defecto con el (end="\n")
# print() hace un salto de línea automático
# Si usas end, puedes definir qué se escribe al final (por ejemplo, un espacio para que el siguiente print continúe en la misma línea)

# Ejemplo sep (separador)
print("hola", "mundo", "python") # resultado sin (sep)
print("hola", "mundo", "python", sep="-") # Cambia el espacio por un guion con (sep)

# Ejemplo end (Final de linea)
print("Hola Mundo desde", end=" ") # si dejo el parametro (end) vacio le estamos indicando que no queremos que genere un salto de linea
print("Python")
