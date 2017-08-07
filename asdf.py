# Que se impriman las opciones de:

# Jugar

# Salir

# Y que el jugador pueda ingresar una opción.

# Luego que:
# Si se eligió uno, que avance a una función Play() //Por ahora no haga nada la funcion esa o solo imprima "jugando"..
# Si se eligió salir, que se termine la ejecución del programa.


print("Jugar")
print("Salir")

print("Precione 1 para jugar - 2 para salir")
jugar=int(input(""))

while (jugar <1 or jugar >2):
	print("Por Favor eliga opción 1 o 2")
	print("Precione 1 para jugar - 2 para salir")
	jugar=int(input(""))
pass

if (jugar==1):
	print("Jugando. . .")
else :
	print("Hasta luego. . .")

input("")
