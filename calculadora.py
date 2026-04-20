#PC -> GUARDARLO EN GIT -> "git add."  git commit -m "mensaje"
#GIT -> pasa aca  -> git push
#GITHUB -> pasa aca.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

print("Calculadora")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El resultado es: ", suma(a, b))
elif opcion == 2:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El resultado es: ", resta(a, b))
elif opcion == 3:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El resultado es: ", multiplicacion(a, b))
elif opcion == 4:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    print("El resultado es: ", division(a, b))
else:
    print("Opcion invalida")