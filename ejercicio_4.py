"crea un programa que calcule cual es tu peso en la luna y los planetas que quieras"
"y que calcule en cual pesas mas"

print("¿cuanto pesas?: ")
peso = float(input())
gravedadTierra= 9.8
gravedadLuna=1.622
gravedadJupiter=24.79
gravedadMarte=3.721
T=(peso/gravedadTierra)
L=(peso/gravedadTierra)*gravedadLuna
J=(peso/gravedadTierra)*gravedadJupiter
M=(peso/gravedadTierra)*gravedadMarte

if J > L & J > M & J > T:
    print("en jupiter pesas mas")
#print(min(lista))

print("tu peso en la Luna seria de: ", L)
print("tu peso en la Jupiter seria de: ", J)
print("tu peso en la Marte seria de: ", M)
