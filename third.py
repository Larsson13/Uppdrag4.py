import replit

# Variable to hold users menuchoiche
x = 0

while True:
 # Fixing & clearing the menu
 replit.clear()
 # Text to show menu
 print("ReplitCars AB")
 print("------------------")
 print("1. Våra fordon!")
 print("2. Våra kunder!")
 print("3. Om oss\n")
 print("4. Avlsuta programmet\n")

  #Getting users choice
 x = int(input("Skriv in ditt val: "))

  # Conditions to get the function of choice
 if x == 1:
   replit.clear()
   print("Fordon i lager:\n")
   print("De fordon vi har i lager just nu är:\n" + bil1 + "\n" + bil2 + "\n" + bil3 + "\n" + bil4 + "\n" "För mer information kontakta oss på nr.xxx-xxxxxxx eller via våran mail replitcars@mail.com\n")
   input("Tryck Enter för att gå tillbaka till menyn!")
 elif x == 2:
   replit.clear()
   print("Våra fantastiska kunder:\n")
   print("Vi jobbar på att visa vilka underbara kunder vi har!\n")
   input("Tryck Enter för att gå tillbaka till menyn")
 elif x == 3:
   replit.clear()
   print("Om oss\n")
   print("ReplitCars AB grundes 2022, med ett mål att bli en utav Sveriges ledande bilhandlare. Det kommer först och främst börja med begagnade bilar vilket vi sedan hoppas kan bli nybilsförsäljning.\n")
   print("Vår vision!")
   print("-Skapa en enklare vardag för alla medmänniskor-\n")
   input("Tryck Enter för att gå tillbaka till menyn")
   # To exit the program
 elif x == 4:
   replit.clear()
   print("Du har valt att avsluta programmet\n")
   input("Tryck Enter för att avsluta programmet")
   replit.clear()
   break
   # If users press a number outside of the menuchoices
 else:
   replit.clear()
   print("Du gjorde ett ogiltigt val \nGå tillbaka till menyn och gör ett annat val!\n")
   input("Tryck Enter för att komma tillbaka till menyn")
print("Programmet har avslutats!")