import math

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

print(area_circulo(10))
print(area_rectangulo(3, 6))
print(area_triangulo(5, 9))