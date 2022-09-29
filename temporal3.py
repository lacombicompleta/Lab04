contador = 0 
suma = 0

while True: 
    numero = input("Ingrese un numero: ")
    if(numero == "salir"):
        break
    else:
        contador = contador + 1
        suma = suma + int(numero)
        promedio = suma/contador
print("Contador", contador)
print("Suma", suma)

print("Promedio", promedio)
