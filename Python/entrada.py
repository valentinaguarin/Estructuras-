def registration():
  while True:
    vehicle = input("Enter vehicle type\nC:camión\tA:automóvil\tM:motocicleta ")
    vehicle = vehicle.upper()
    if not vehicle == "C" and not vehicle == "A" and not vehicle == "M":
      print("Invalid vehicle type. Try again!")
    else:
      break

  while True:
    origin = int(input("\nEnter origin street\n1:Calle 37 Sur\t2:Carrera 43A (→)\t3:Carrera 43A (←) "))
    if not origin == 1 and not origin == 2 and not origin == 3:
      print("Invalid origin street. Try again!\n")
    else:
      break
contin = 1
while contin == 1:
  registration()
  contin = int(input("Do you want to add another register?\n1:yes\t0:no "))