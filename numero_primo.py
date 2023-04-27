import sys

print("En este programa podrás determinar")
print("si un numero entero es primo")

while True:
    numero = input("Inserta un numero entero: ")
    try:
        numero_int = int(numero)
        break
    except ValueError:
        print("Error!")

numero_float = float(numero)

resultado = ""

if numero_int > 0:
    for check in (reversed(range(2, numero_int-1))):
        x = numero_float / check
        if x.is_integer() is True:
            resultado = int(x)
            print(f"El numero primo es {resultado}.")
            sys.exit()
            
else:
    for check in range(numero_int+1, -2):
        x = numero_float / check
        if x.is_integer() is True:
            resultado = int(-x)
            print(f"El numero primo es {resultado}.")
            sys.exit()


if resultado in [""]:
    print(f"El numero primo es {numero}.")
    sys.exit()

