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
lista = []
contin = 1
while contin == 1:
  registration()
  contin = int(input("Do you want to add another register?\n1:yes\t0:no "))