# Dado un número leído desde la entrada estándar,
# escribir un programa que adivine en el menor número de pasos
# posible un número pensado por el usuario desde 0 al número
# leído.

numero_pensado_usuario = int(input("Introduzca un número entero: "))

for enumeracion in range(numero_pensado_usuario + 1):
    if enumeracion == numero_pensado_usuario:
        print("He adivinado el numero que introdujiste en la iteraccion numero %i!" % enumeracion)
        break
    else:
        print("Aun no he adivinado el numero que introdujiste :(")
