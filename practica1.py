#calculadora basica
#by: camille araujo 

#Definimos funciones para cada operacion matematica
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    #validamos que no se divida entre cero
    if b == 0:
        return "Error: no se puede dividir entre cero"
    else:
        return a / b
    
#inicia el programa
print("¡Bienvenido a la calculadora basica ;3!")
print("Opciones: +,-,*,/, o 'salir' para terminar")

#usamos un bucle para repetir el programa hasta que el usuario decida salir
while True:
    #pedimos al usuario que elija una opcion
   opcion = input("elige una operacion (+,-,*,/) o 'salir':")

#condicion para terminar el programa
   if opcion.lower() == "salir":
    print("¡Gracias por usar la calculadora ;3!")
    break

#pedimos los numeros al usuario
num1 = float(input("ingresa el primer numero:"))
num2 = float(input("ingresa el segundo numero:"))

#usamos condiciones para ejecutar la operacion elegida
if opcion == "+":
    print("resultado:", sumar(num1, num2))
elif opcion == "-":
    print("resultado:", restar(num1, num2))
elif opcion == "*":
    print("resultado:", multiplicar(num1, num2))
elif opcion == "/":
    print("resultado:", dividir(num1, num2))
else:

    print("Opcion no valida, intenta otra vez :(.")
