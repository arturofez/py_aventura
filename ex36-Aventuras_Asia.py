# Made by JP -> jimenez.me

from sys import stdout
import time

vacunas = False

def printlbl(string):
	for char in string:
		print(char, end="")
		stdout.flush()
		time.sleep(0.025)

def notunderstand(option):
	printlbl("No entiendo lo que quieres hacer... " + option + "\n")

def dead(why):
	printlbl(why + " Te esperaba más inteligente.\n")
	playagain()

def playagain():
	printlbl("¿Quieres volver a jugar?\n")
	while True:
		choice = input("> ").lower()

		if choice == "si" or choice == "sí":
			intro()
		elif choice == "no":
			exit(0)
		else:
			notunderstand("¿Quieres volver a jugar?")

def building():
	print("\nTodavía en desarrollo, espero que os guste ;)\n")
	playagain()

def intro():
	printlbl("\nMadrid. Son las 9am de la mañana, te duele la cabeza...\n"
	"Recuerdas que tienes las vacunas a las 10am, ¿qué haces?\n"
	"¿Correr o dormir (y perderte las vacunas)?\n")

	while True:
		choice = input("> ").lower()

		if choice == "correr":
			printlbl("Sales corriendo y coges el autobús de milagro.\n"
			"Tras un buen rápido en transporte público llegas al centro para vacunarte\n"
			"Ahora estás inmunizado de la rabia y el cólera.\n"
			"¡Bendita ciencia!\n")

			global vacunas
			vacunas = True

			london()

		elif choice == "dormir":
			printlbl("Se está demasiado bien durmiendo... Además, no creo que necesite vacunas, ¿verdad?\n"
			"Duermes hasta las 3pm\n")

			london()

		else:
			notunderstand("¿Correr o dormir?")


def london():
	printlbl("\n... Tras un primer vuelo bastante rápido estás en un aeropuerto en Londres esperando a coger el vuelo de escala destino a Mumbai.\n"
	"Tienes ganas de ir al baño, ¿qué haces con el pasaporte y tu billete?\n"
	"\t 1. Lo llevas encima\n"
	"\t 2. Se lo dejas a alguien para que te lo vigile\n")


	while True:
		choice = input("> ").lower()

		if choice == "1":
			printlbl("Eres precavido.\n"
			"Vas al baño con normalidad...\n"
			"Te subes al avión y te duermes rápidamente.\n")
			inicio_mumbai()

		elif choice == "2":
			printlbl("Vuelves y ¡tu pasaporte no está!\n"
			"¿Qué ha pasado con él?\n"
			"Tu imprudencia ha hecho que no te puedas subir al avión.\n")

			dead("Tu viaje acaba aquí.")

		else:
			printlbl("No entiendo lo que quieres hacer... ¿Opción 1 o 2?\n")

def inicio_mumbai():
	time.sleep(0.5)
	print("""\n\
	//////////////////////////////////////////////////
	//////////////////////////////////////////////////
	//////////////////////////////////////////////////
	//////////////////////////////////////////////////
	//////////////////////////////////////////////////
	.......................----.......................
	                     -/::::/-
	                    -/.+ss+./-
	                    -/.+ss+./-
	                     -/::::/-
	----------------------:////:----------------------
	hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
	hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
	hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
	hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
	hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
	""")
	time.sleep(0.5)

	printlbl("Llegas a Mumbai sin mucho problema\n"
	"Hace mucho calor y todo es un poco caótico...\n"
	"Te instalas en el hotel y vais a cenar...\n"
	"Una vez llegas al restaurante pides de comer y el camarero te pregunta: ¿Spicy?\n")

	while True:
		choice = input("> ").lower()

		if choice == "sí" or choice == "si":
			printlbl("Parece que este picante era mucho más picante de lo que esperabas\n")
			bebida()
		elif choice == "no":
			printlbl("El camarero ha ignorado tu petición y la comida está muy picante.\n")
			bebida()

		else:
			printlbl("No entiendo lo que quieres hacer... ¿Spicy?\n")

def bebida():
	printlbl("Te arde la boca y el camarero te pregunta si quieres algo de beber, ¿qué pides?\n"
	"¿Agua o Lassi?\n")

	while True:
		choice = input("> ").lower()

		if choice == "agua":
			printlbl("Aunque el agua tiene mala pinta, te la bebes de un trago.\n")
			agua()
		elif choice == "lassi":
			printlbl("¡Está delicioso!\n"
			"El picor baja, te empiezas a encontrar mejor\n")
			perros()

		else:
			printlbl("No entiendo lo que quieres hacer... ¿Agua o Lassi?\n")
def agua():
	global vacunas

	if vacunas == True:
		printlbl("En este momento te acuerdas que te vacunaste del cólera y te ves tranquilo\n")
		perros()
	else:
		printlbl("Empiezas a tener sudores fríos y te duele mucho el estómago.\n"
		"Parece que tienes el Cólera\n"
		"Te empiezas a preguntar, ¿por qué no me habré vacunado?\n")

		dead("Tu viaje acaba aquí.")


def perros():
	printlbl("Después de una rica (y picante) cena, volvéis andando al hotel.\n"
	"Todo parece muy tranquilo pero...\n"
	"¡De repende aparece una jauría de perros rabiosos?\n"
	"¿Qué haces? ¿Correr o no hacer nada?\n")

	choice = input("> ").lower()

	if choice == "correr":
		printlbl("Sales corriendo y ellos detrás tuya...\n"
		"Son más rápidos que tu y acaban mordiéndote un par...\n")
		mordida()
	else:
		printlbl("No haces nada y ellos se van por donde vinieron, la calma te ha ayudado esta vez\n"
		"¡Bien hecho!\n")
		building()

def mordida():
	global vacunas

	if vacunas == True:
		printlbl("Te han jodido la pierna, pero gracias a que tienes la vacuna de la rabia, te da tiempo a llegar al hospital\n")
		building()

	else:
		printlbl("Te han jodido la pierna y lo peor es que parecía que tenían la rabia...\n"
		"Corres al hospital pero te estás empezando a quedar inconsciente...\n"
		"Te empiezas a preguntar, ¿por qué no me habré vacunado?\n")

		dead("No llegas al hospital, estás muerto.")

intro()
exit(1)
