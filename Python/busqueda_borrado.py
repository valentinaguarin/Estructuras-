# Data registration
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
        try:   # comprobando que se ingrese un entero
            int(origin)
            break
        except ValueError:
            it_is = False
            print("Invalid vehicle type. Try again!")
        if it_is == True: #comprobar que ingrese las calles correctas
            if not origin == 1 and not origin == 2 and not origin == 3:
                print("Invalid origin street. Try again!\n")
            else:
                break
    while True:  #giros permitidos
        destination = int(input("\nEnter destination street\n1:Calle 37 Sur\t2:Carrera 43A (→)\t3:Carrera 43A (←)\n"))
        if origin == 2 and destination != 2:
            print(f"Invalid destination for street",origin,". Valid destination streets: 2")
        elif origin == 3 and destination != 3 and destination != 1:
            print(f"Invalid destination for street {origin}. Valid destination streets: 3 and 1")
        elif destination != 1 and destination != 2 and destination != 3:
            print("Invalid destination street. Valid destination streets: 1, 2 and 3\n")
        else:
            break
            # Add register
    register = vehicle + str(origin) + str(destination)  #uniendolo de la forma c11
    lista.append(register)

# Data visualization
def visualization(lista):
    C, A, M = 0, 0, 0  #contador de carros, motos, automoviles
    total_giros = 0
    total_rectos = 0
    giroC, giroA, giroM, giroRC, giroRA, giroRM = 0, 0, 0, 0, 0, 0   #giros por tipo de carro
    giro_12, giro_C12, giro_13, giro_C13, giro_31, giro_C31 = 0, 0, 0, 0, 0, 0
    giro_M12, giro_M13= 0, 0
    recto_11, recto_22, recto_33 = 0, 0 ,0
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
                if destination=="2":
                    giro_C12 += 1
                    giro_12 += 1
                elif destination=="3":
                    giro_C13 += 1
                    giro_13 += 1
                elif origin=="3" and destination==1:
                    giro_C31 += 1
                    giro_31 += 1
                elif origin == 1:
                    recto_11 += 1
                elif origin == 2:
                    recto_22 += 1
                elif origin == 3:
                    recto_33 += 1
            else:
                giroRC += 1
                a=[origin,destination,giroRC]
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
                if destination =="2":
                    giro_M12 += 1
                    giro_12 +=1
                elif destination=="3":
                    giro_M13 += 1
                    giro_13 += 1
            else: giroRM +=1
            if origin != destination:
                giroM += 1

        # Total of giros
        if origin != destination:
            total_giros += 1
        else:
            total_rectos += 1
        print("Dato: ",register," Corresponding to index: ",i)
    print("Summary table")
    print(f"Total of registers             → {total_registers}")
    print(f"Vehicles per type              → C={C}\tA={A}\tM={M}")
    print(f"Giros per vehicle              → C={giroC}\tA={giroA}\tM={giroM}")
    print(f"Giros Straight per vehicule    → C={giroRC}\tA={giroRA}\tM={giroRM}")
    print(f"Giros Straight                 → {total_rectos}")
    print(f"Total of giros                 → {total_giros}")
    print(f"Total of giros origin:1 and destination:2       → {giro_12}")
    print(f"Total of giros origin per vehicle origen:1 and destination:2  → C12={giro_C12}")
    print(f"Tipos de rectos: C={recto_11} recto_22, recto_33")

# search and delete
#migue
def search_delete(lista):
    index = int(input("Enter the index of the record you want to search: "))
    record = lista[index]
    print(f"Record for index {index}: {record}")
    delete = input("Do you want to delete this record?\n1:yes\t0:no ")
    if delete == "1":
        removed = lista.pop(index)
        print(f"\nThe register {removed} has been removed successfully!")
        visualization(lista)
# MAIN
# 1.2
lista = []

contin = 1
while contin == 1:
  registration()
  contin = int(input("Do you want to add another register?\n1:yes\t0:no "))

print("Summary table Specific Giros")
print("Giros per camion and origen 1: C11:",lista.count("C11"),"C12",lista.count("C12"),"C13",lista.count("C13"))
print("Giros per camion and origin 2 C22",lista.count("C22"))
print("Giros per camion and origin 3 C31",lista.count("C31"), "C33",lista.count("C33"))
print("Giros per automoviles and origin 1: A11",lista.count("A11"),"A12",lista.count("A12"),"A13",lista.count("A13"))
print("Giros per automoviles and origin 2: A22",lista.count("A22"))
print("Giros per automoviles and origin 3: A31",lista.count("A31"))
print("Giros per motocicleta and origen 1: M11:",lista.count("M11"),"M12",lista.count("M12"),"M13",lista.count("M13"))
print("Giros per motocicleta and origin 2: M22:",lista.count("M22"))
print("Giros per motocicleta and origin 3: M31",lista.count("M31"),"M33",lista.count("M33"))
visualization(lista)
#1.4
sd = int(input("Do you want to search for a register by index?\n1:yes\t0:no "))
while sd == 1:
  search_delete(lista)
  sd = int(input("Do you want to search for another register by index?\n1:yes\t0:no "))

