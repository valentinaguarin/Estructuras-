def registration():
  while True:
    vehicle = input("Enter vehicle type\nC:camión\tA:automóvil\tM:motocicleta ")
    vehicle = vehicle.upper()
    if not vehicle == "C" and not vehicle == "A" and not vehicle == "M":
      print("Invalid vehicle type. Try again!")
    else:
      break
  while True:
    origin = (input("\nEnter origin street\n1:Calle 37 Sur\t2:Carrera 43A (→)\t3:Carrera 43A (←) "))
    it_is=True
    try:
      int(origin)
      it_is = True
      break
    except ValueError:
      it_is = False
      print("Invalid vehicle type. Try again!")
    if it_is==True:
        if not origin == 1 and not origin == 2 and not origin == 3:
          print("Invalid origin street. Try again!\n")
        else:
          break
  while True:
    destination = int(input("\nEnter destination street\n1:Calle 37 Sur\t2:Carrera 43A (→)\t3:Carrera 43A (←) "))
    if origin == 2 and destination != 2:
      print(f"Invalid destination for street {origin}. Valid destination streets: 2")
    elif origin == 3 and destination != 3 and destination != 1:
      print(f"Invalid destination for street {origin}. Valid destination streets: 3 and 1")
    elif destination != 1 and destination != 2 and destination != 3:
      print("Invalid destination street. Valid destination streets: 1, 2 and 3\n")
    else:
      break
  # Add register to dictionary
  register = vehicle+str(origin)+str(destination)
  lista.append(register)

# Data visualization
def visualization(lista):
    C, A, M = 0, 0, 0
    total_giros = 0
    giroC, giroA, giroM = 0, 0, 0
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
        if vehicle == "A":
            A += 1
            if origin != destination:
                giroA += 1
        if vehicle == "M":
            M += 1
            if origin != destination:
                giroM += 1

        # Total of giros
        if origin != destination:
            total_giros += 1

        # realizando conteo de los giros y vehiculos

lista = []
contin = 1
while contin == 1:
  registration()
  contin = int(input("Do you want to add another register?\n1:yes\t0:no "))