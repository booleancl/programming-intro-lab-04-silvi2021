import random

print("¡Bienvenido al cachipun!")

user_input = ''

def add_point(winner):
    winner_file = winner + ".txt"
    file = open(winner_file,"a")
    file.write('|')
    file.close()

def results():
    user_count = len(open("user.txt","r").read())
    computer_count =len(open("computer.txt","r").read())
    tie_count =len(open("tie.txt","r").read())
    print("jugador:",user_count,"computador:",computer_count,"empate:",tie_count)
  
def play():
   options = ["piedra","tijera","papel"]

   print("hola juguemos cachipun")

   print ("ingresa su opción")
   print (1, "piedra")
   print (2, "tijera")
   print (3, "papel")

   user_input =int(input("jugador1\n"))
   user_option = options[user_input - 1]

   computer_option = random.choice(options)

   print("mi mano: ", user_option)
   print("mano del computador:", computer_option)
    
   if (user_option==computer_option):
     add_point("tie")
     print("Empatan jugadores")
   elif (user_option == "piedra" and computer_option =="tijera") or (user_option == "tijera" and computer_option =="papel") or (user_option == "papel" and computer_option == "piedra"):
      add_point("user")
      print("Felicitaciones! ganaste la partida")
   else:
     file = open("computer.txt","a")
     add_point("computer")
     print("Lo siento! el computador ha ganado") 
    

def main_menu():
    print("selecciona tu opción")
    print(1,"jugar")
    print(2,"ver resultados")
    print(3,"salir")

while user_input != "3":
    main_menu()
    user_input = input()

    if user_input == "1":
        play()
    elif user_input == "2":
        results()
    elif user_input == "3":
        print("chau chau")
    else:
        print("opción inválida")





    

     

