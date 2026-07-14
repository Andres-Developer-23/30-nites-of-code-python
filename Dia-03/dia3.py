numero = int(input("Ingresa un numero del 1 al 7: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miercoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sabado")
elif numero == 7:
    print("Domingo")
else:
    print("Numero invalido")

if numero == 6 or numero == 7:
    print("¡Es finde! 🎉")

edad = int(input("Ingrese su edad: "))
if edad > 0 and edad <= 12:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Adolecente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")