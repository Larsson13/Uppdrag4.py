import replit

# Get the user to answer the question
print("Hej, jag är intresserad utav att köpa din bil. Skulle du kunna svara på några frågor om fordonet?"
)
svar = input()

# Let the user write the manufacture
print("Vilken tur! Den första frågan som jag skulle vilja få svar på är, vad är det för bilmärke?"
)
bilmärke = input()

# Let the user write down the carmodel
print("Vad är det för modell?")
modell = input()

# Let the user put the year model
print("Vad är det för årsmodell?")
årsmodell = input()

# Let the user write how many km the whicle has gone
print("Hur långt har den gått i km tror du?")
långt = input()

# Print out the information
print("Så du säger att du har en" + " " + bilmärke + " " + modell + " " +"från" + " " + årsmodell + " " + "som har gått cirka" + " " + långt +", det är något jag skulle vara intresserade utav att köpa!")

#Hållkod
print()

# Print out the information
print("Vi på företeget har nyligen köpt in några bilar som vi tror skulle passa dig!"
)

# Print out the information
print("Jaså, vad är det för några då?")

# Let the user write some cars both manufacture + model
print("Den första bilen är en!")
car1 = input()

# Let the user write the car manufacture + model
print("Den andra är en!")
car2 = input()

# Let the user write the car manufacture + model
print("Sen har vi även en!")
car3 = input()

# Let the user write the car manufacture + model
print("Och till sist en")
car4 = input()

# Print out the information
replit.clear()
print("En liten snabb recap, de senaste bilarna vi har fått in är alltså en, " +car1 + ", en " + car2 + ", " + car3 + "samt en " + car4 +". Skulle någon utav dessa bilar vara av intresse för dig?\n")
print("Om du känner att inte någon utav de bilarna finns av intresse så kan du ta dig din tid och besöka våran hemsida, där har vi några bilar som inte kommit till oss ännu men är påväg, då rekommenderar vi dig att gå in och titta på våran hemsida för lite mer inspiration!\n"
)
input("Genom att trycka på Enter tar vi dig till Menyn")

# Imported information from the second file
import second
