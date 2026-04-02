#practica hito3- Desarrollo de problemas Struc y Punteros
#1Crear una matriz 5x4 con números aleatorios
import random
print("1. Matriz 5*4:")
matriz = []
for i in range(5):
    fila = []
    for j in range(4):
        fila.append(random.randint(1, 100))
    matriz.append(fila)

for fila in matriz:
    print(fila)

#2Crear una lista con los números que empiecen desde 505 y termine en 615
print("2. Lista del 505 al 615:")
lista = list(range(505, 616))
print(lista)


#3Crear una tupla elija sus elementos
print("3. Tupla:")
tupla = ("manzana", "banana", "naranja")
print(tupla)


#4En una lista creada lo rustes clasifique los primos y compuestos
print("4. Primos y compuestos:")

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numeros = [10, 7, 3, 8, 11]

for num in numeros:
    if es_primo(num):
        print(num, "es prino")
    else:
        print(num, "es compuesto")


#5 Multiplicar dos valores de 7 dígitos cada uno, expresar el resultado en caracteresde lectura

print("5. Multiplicación:")

a = 1234567
b = 7654321

resultado = a * b
print("Resulado:", resultado)
print("En texto:", str(resultado))


#6¿Como programa esta imagen? la que esta en el pdf xD
print("6. Simulación tipo red:")

entrada = [1, 0]  
pesos = [0.8, 0.2]
# gato=1, perro=0
salida = 0
for i in range(len(entrada)):
    salida += entrada[i] * pesos[i]

print("Salida:", salida)