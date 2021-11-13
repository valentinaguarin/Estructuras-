def registration():
    while True:
        vehicle = input("Enter vehicle type\nC:camión A:automóvil M:motocicleta\n")
        vehicle = vehicle.upper()  # Convertir en mayuscula
        if not vehicle == "C" and not vehicle == "A" and not vehicle == "M":
            print("Invalid vehicle type. Try again!")
        else:
            break

    while True:
        origin = (input("\nEnter origin street\n1:Calle 37 Sur 2:Carrera 43A (→) 3:Carrera 43A (←)\n"))
        it_is = True
        try:  # comprobando que se ingrese un entero
            int(origin)
            break
        except ValueError:
            it_is = False
            print("Invalid vehicle type. Try again!")
        if it_is == True:  # comprobar que ingrese las calles correctas
            if not origin == 1 and not origin == 2 and not origin == 3:
                print("Invalid origin street. Try again!\n")
            else:
                break
    while True:  # giros permitidos
        destination = int(input("\nEnter destination street\n1:Calle 37 Sur\t2:Carrera 43A (→)\t3:Carrera 43A (←)\n"))
        if origin == 2 and destination != 2:
            print(f"Invalid destination for street", origin, ". Valid destination streets: 2")
        elif origin == 3 and destination != 3 and destination != 1:
            print(f"Invalid destination for street {origin}. Valid destination streets: 3 and 1")
        elif destination != 1 and destination != 2 and destination != 3:
            print("Invalid destination street. Valid destination streets: 1, 2 and 3\n")
        else:
            break
            # Add register
    register = vehicle + str(origin) + str(destination)  # uniendolo de la forma c11
    lista.append(register)


# Data visualization
def visualization(lista):
    C, A, M = 0, 0, 0  # contador de carros, motos, automoviles
    total_giros = 0
    total_rectos = 0
    giroC, giroA, giroM, giroRC, giroRA, giroRM = 0, 0, 0, 0, 0, 0  # giros por tipo de carro
    total_registers = len(lista)
    print("Register's table (index, register)")
    for i in range(len(lista)):
        register = lista[i]
        vehicle, origin, destination = register[0], register[1], register[2]
        # vehicles per type
        if vehicle == "C":
            C += 1
            # Giros per vehicle
            if origin != destination:
                giroC += 1
            else:
                giroRC += 1
        if vehicle == "A":
            A += 1
            if origin != destination:
                giroA += 1
            else:
                giroRA += 1
        if vehicle == "M":
            M += 1
            if origin != destination:
                giroM += 1
            else:
                giroRM += 1
        # Total of giros
        if origin != destination:
            total_giros += 1
        else:
            total_rectos += 1
        print("Dato: ", register, "corresponding to index ", i)
    print("Summary table")
    print(f"Total of registers             → {total_registers}")
    print(f"Vehicles per type              → C={C}\tA={A}\tM={M}")
    print(f"Giros per vehicle              → C={giroC}\tA={giroA}\tM={giroM}")
    print(f"Giros Straight per vehicule    → C={giroRC}\tA={giroRA}\tM={giroRM}")
    print(f"Giros Straight                 → {total_rectos}")
    print(f"Total of giros                 → {total_giros}")


# search and delete
# migue

# MAIN
# 1.2
lista = []
contin = 1
while contin == 1:
    registration()
    contin = int(input("Do you want to add another register?\n1:yes\t0:no "))
# 1.3
visualization(lista)