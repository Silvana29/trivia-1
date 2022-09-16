# lo primero es mostrar en pantalla el texto de bienvenida para quien juegue con tu trivia 
print("Bienvenido a mi trivia sobre canciones") 
print("Pondremos a prueba tus conocimientos")

#agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input("Ingresa tu nombre:")

#es importante dar instrucciones sobre cómo jugar:
#ahora, lo personalizaremos, con el nombre el jugador, diciendole a print () que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separaremos con comas
print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra correcta y presionando *enter* para enviar tu respuesta:\n")

 # Ojo, el\n al final de la línea 6 es para dar un "salto de la línea"

#Pregunta 1 
print("1) Quién canta Y hubo alguien?")
print("a)Juanes")
print("b)Gianmarco")
print("c)Marc Anthony")

#Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\n Tu respuesta: ")

while respuesta_1 not in ("a", "b", "c"):
 respuesta_1 = input("debes responder a,b o C. Ingresa nuevamente tu respuesta: ")