print("¡Hola! En esta función sumarás todos los numeros pares.")


numbers = []
sumables = []
no_sumables = []

print("Escribe 'listo' cuando hayas terminado de \n agregar los números")
while True:
    numero_str = input("Ingresa los números: ")
    if numero_str in ["listo"]:
        break
    
    while True:
        try:
            float(numero_str)
            numero = float(numero_str)
            break
        except ValueError:
            numero_str = input("Inserte un numero valido: ")
    
    numbers.append(numero)

print(numbers)

for x in numbers:
    y = x % 2
    if y == 0:
        sumables.append(x)
    else:
        no_sumables.append(x)

resultado = sum(sumables)

print(f"El resultado de la suma de los pares es {resultado}, \ny los numeros que no se pudieron sumar son {no_sumables}.")
