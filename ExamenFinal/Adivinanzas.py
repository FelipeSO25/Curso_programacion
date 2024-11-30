# Examen Final Programación IIS 

import random
import os
import json

class JuegoAdivinanza:
    def __init__(self):
        
        self.numero_secreto = random.randint(1, 100)  # Crea un numero secreto del 1 al 100
        self.intentos = 0  # Al principio los intentos son 0

    def validarNumero(self, numero):
        if numero > self.numero_secreto:
            return "El número es menor"
        elif numero < self.numero_secreto:
            return "El número es mayor"
        else:
            return "Adivinaste!!"

    def registrarIntento(self):
        self.intentos += 1

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0


class Jugador:
    def __init__(self, nombre):
       
        self.nombre = nombre
        self.historial = self.cargarStats()

    def Partidas (self, intentos, victoria):
        
        self.historial.append({'intentos': intentos, 'victoria': victoria})

    def MostrarStats (self):

        Partidas = len(self.historial)
        Victorias = sum(1 for partida in self.historial if partida ['victoria'])

        if Partidas == 0:
            Winrate = 0
        else:
            Winrate = (Victorias/Partidas)*100   

        print(f"Jugador: {self.nombre}")
        print(f"Partidas jugadas: {Partidas}")
        print(f"Partidas ganadas: {Victorias}")
        print(f"Porcentaje de aciertos: {Winrate:.2f}%")   

    def guardarStats(self):

        datos = {
            'nombre': self.nombre,
            'historial': self.historial
        }
        with open('Stats.txt', 'w') as archivo:
            json.dump(datos, archivo)

    def cargarStats(self):
        
        if os.path.exists('Stats.txt'):
            with open('Stats.txt', 'r') as archivo:
                datos = json.load(archivo)
                if datos['nombre'] == self.nombre:
                    return datos['historial']
        return []

def Menu():
    print("Bienvenido al menú del juego de adivinanzas")
    print("1. Comenzar una nueva partida")
    print("2. Ver estadisticas del jugador")
    print("3. Salir del juego")

def jugar():
    nombre = input("Ingrese su nombre: ")
    jugador = Jugador(nombre)

    while True:
        Menu()
        Seleccion = input("Seleccione una opcion del menu: ")

        if Seleccion == "1":
            
            juego = JuegoAdivinanza()
            print("Comienza la partida, intenta adivinar un numero entre el 1 y 100: ")
            jugando = True

            while jugando:
                try:
                    if juego.intentos >= 10:
                        print("Ya no quedan intentos, perdiste")
                        jugador.Partidas(juego.intentos, False)
                        jugando = False
                        break

                    numero = int(input(f"Intento {juego.intentos + 1}/10. Ingresa otro numero: "))
                    juego.registrarIntento()
                    resultado = juego.validarNumero(numero)
                    print(resultado)

                    if resultado == "Adivinaste!!":
                        jugador.Partidas(juego.intentos, True)
                        jugando = False

                    else:
                        print("Numero equivocado, intenta de nuevo")

                except ValueError:  
                    print("Ingrese un valor adecuado")      
                    

        elif Seleccion == "2":
            jugador.MostrarStats()

        elif Seleccion == "3":
            jugador.guardarStats()
            print("Gracias por jugar, vuelve pronto!")  
            break  

        else:
            print("Escoja una opcion valida")       

jugar()               

