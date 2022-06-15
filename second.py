import replit
from getkey import getkey, keys

# Menuchoices, select one using your keys
def FirstChoice():
   replit.clear()
   print("Fordon i lager:\n")
   print("De fordon vi har i lager just nu är:\n")

   carList = ["Lexus\n" "Mercedes GLE\n" "Toyota RAV4\n" "Mazda 6\n" "Volkswagen Passat\n" "Volkwagen ID4\n" "Kia Sorento\n"]

   for i in carList:
    print(i, end= "")

    print()
    print()
  
    print("För mer information kontakta oss på nr.xxx-xxxxxxx eller via våran mail replitcars@mail.com\n")
   input ("Press ENTER to continue...")

# Menuchoices, select one using your keys
def SecondChoice():
   replit.clear()
   print("Vår personal:\n")
   print("Sabina Hansson \nVD \n")
   print("Filip Gustavsson \n Marknadschef \n")
   print("Oskar Josefsson \n Ekonomichef \n")
   print("Gunnar Torstensson\n Bilförsäljare \n")
   print("Anna Andersson \n Bilförsäljare \n")
   print("Lisa Månsson \n Bilförsäljare \n")
   input ("Press ENTER to continue...")

# Menuchoices, select one using your keys
def ThirdChoice():
   replit.clear()
   print("Om oss\n")
   print("ReplitCars AB grundes 2022, med ett mål att bli en utav Sveriges ledande bilhandlare. Det kommer först och främst börja med begagnade bilar vilket vi sedan hoppas kan bli nybilsförsäljning.\n")
   print("Vår vision!")
   print("-Skapa en enklare vardag för alla medmänniskor-\n")
   input ("Press ENTER to continue...")

# Menuchoices, select one using your keys
def EndProgram():
   replit.clear()
   print ("\nAvslutar programmet!")
   input ("Press ENTER to end the program...")

menuOptions = ["Våra fordon!\t\t", "Vår personal!\t\t", "Om oss\t\t", "Avsluta\t\t"]
menuSelected = 0

# If key pressed go to either menuoption 0 - 3
while(True):
  replit.clear()
  print("\x1b[?25l")
  
  if menuSelected == 0:
   print(menuOptions[0] + "<--")
   print(menuOptions[1])
   print(menuOptions[2])
   print(menuOptions[3])
  elif menuSelected == 1:
   print(menuOptions[0])
   print(menuOptions[1] + "<--")
   print(menuOptions[2])
   print(menuOptions[3])
  elif menuSelected == 2:
   print(menuOptions[0])
   print(menuOptions[1])
   print(menuOptions[2] + "<--")
   print(menuOptions[3])
  elif menuSelected == 3:
   print(menuOptions[0])
   print(menuOptions[1])
   print(menuOptions[2])
   print(menuOptions[3] + "<--")

  keyPressed = getkey()
  if keyPressed == keys.DOWN and menuSelected + 1 != len(menuOptions):
   menuSelected += 1
  elif keyPressed == keys.UP and not (menuSelected == 0):
   menuSelected -= 1
  elif keyPressed == keys.ENTER:
    if menuSelected == 0:
      FirstChoice()
    elif menuSelected == 1:
     SecondChoice()
    elif menuSelected == 2:
     ThirdChoice()
    elif menuSelected == 3:
     EndProgram()
     print()
     break