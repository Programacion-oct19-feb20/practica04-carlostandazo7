"""
    @autor: carlostandazo7
    nombre: ejercicio6.py
    descripción: ...

    Carlos Tandazo -- 18
    Su suma de notas es: 30
    Su promedio es: 15
"""

nombre = input("ingrese su nombre: ")
edad = input("ingrese la edad: \n")
nota1 = input("ingrese el valor de su nota 1: ")
nota2 = input("ingrese el valor de su nota 2: ")

suma = int(nota1) + int(nota2);
promedio = suma / 2 

print("%s -- %s\nSu suma de notas es %s\nSu promedio es %s\n" % (nombre, edad, suma, promedio))





