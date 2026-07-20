"""
while True:    
    try:
        def leer_entero(num):
            return int(num)
        numero = int(input("ingresa un numero: "))
        entero = leer_entero(numero)
        print(entero)
        break
    except ValueError:
        print('Error  no puedes ingresar valores diferentes a numeros')

"""

while True:    
    try:
        def leer_datos(edad, cantidad_productos, codigo_postal):
            return f"edad: {edad} \ncantidad de productos: {cantidad_productos} \ncodigo_postal: {codigo_postal}"
        edad = int(input("ingresa tu edad: "))
        cantidad_productos = int(input("Ingresa la cantidad de productos: "))
        codigo_postal = int(input("ingresa el codigo postal: "))

        result = leer_datos(edad, cantidad_productos, codigo_postal)
        print(result)
        break
    except ValueError:
        print('Error  no puedes ingresar valores diferentes a numeros')
