"Crear una función que calcule el cuadrado de un número. Probar la función con los números entre -10 y +10. Crear otra-"
"función que lo único que hace es imprimir al final la frase “Programa finalizado”. Ejecutar ambas funciones."
print("inserta un numero para elevar al cuadrado")
valor = float(input())
def cuadrado(valor):
    ent = pow(valor, 2)
    return (ent)
fra = "Programa finalizado"
def frase(fra):
    return (print(fra))

elevacion = cuadrado(valor)
print ("\nR= ", elevacion)
#se manda llamar la funcion sin nececidad de imprimirla, si se manda a imprimir imprime lo- 
#retornado de la funcion mas el valor "none"
frase(fra)