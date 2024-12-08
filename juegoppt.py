cant_turnos = 0
cant_max_turnos = 3
ganador = False

print("Bienvenidos a piedra, papel o tijeras")

nombre1 = input("Ingrese nombre jugador 1: ")
nombre2 = input("Ingrese nombre jugador 2: ")

jugador1 = input(nombre1 + " que elijes: piedra, papel o tijeras: ")
jugador2 = input(nombre2 + " que elijes: piedra, papel o tijeras: ")



while jugador1 == jugador2 and cant_turnos < cant_max_turnos:
    print("Empataron")
    break

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if condicion1 or condicion2 or condicion3:
    print("Gano: ", nombre1)
    ganador = True 
else:
    print("Gano: ", nombre2)
    ganador = True
    
cant_turnos += 1 