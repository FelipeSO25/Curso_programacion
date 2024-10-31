def calcular_promedio(numeros):
    if len(numeros) == 0:   #Para evitarse errores no se permite que divida entre 0
        return None
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        if num > promedio:
            print(f"{num} es mayor que el promedio.")  #Después de los condicionales deben ir ":" para indicar la instrucción que sigue
        elif num < promedio:
            print(f"{num} es menor que el promedio.")
        else:
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    try:
        num = int(input("Introduce un número: ")) #Ya que se va a ingresar un número, el valor de el input debe ser un int
        numeros.append(num)
    except ValueError:
        print("No es un numero")

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)