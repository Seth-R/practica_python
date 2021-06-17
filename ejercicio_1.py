#crea un programa que te sume dos numeros pero 
# al momento de sumar 2 + 2 te de pez

print ("escribe un numero: ")
numero1 = input()
numero1 = float(numero1)
print ("escribe un segundo numero: ")
numero2 = input()
numero2 = float(numero2)
pez = "pez"
suma=0
if (numero1 == 2) & (numero2 == 2):
    print ("suma: " + pez)
else:
    suma = numero1 + numero2
    print ("suma: ", suma)
