"Se genera un número aleatorio entero entre 1 y 100. El usuario debe adivinar el número "
"secreto, diciendo en cada tirada si es mayor o meno"
import random
numero_a = random.randint(1, 100)
#print(numero_a)
c = 0
while True:
    print("adivina el numero:\n" )
    i = int(input())
    c += 1
    if i > numero_a:
        print("\n---es menor \n")
    if i < numero_a:
        print("\n---es mayor \n")
    if i==numero_a:
        break
print("\nCorrecto el numero era: ","\"", numero_a,"\"", "\nTu numeros de intentos fueron: ", c, "\n")
    
