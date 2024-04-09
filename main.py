import math
def calculadora():
  while True:
# OPERACIONES DISPONIBLES
    print("1. Para Suma")
    print("2. Para Resta")
    print("3. Para Multiplicacion")
    print("4. Para la Division")
    print("5. Para la Potenciacion")
    print("6. Numeros Imaginarios")
    print("7. Funciones Trigonometricas")
    print("8. Programas Secuenciales")
    operacion = int(input("Introduce que operacion deseas realizar: "))
  # SUMA
    if operacion == 1:
      N1 = int(input("Ingreso N1: "))
      N2 = int(input("Ingreso N2: "))
      R = N1 + N2
      print("El resultado es: ",R)
  # RESTA
    elif operacion == 2:
      N1 = int(input("Ingreso N1: "))
      N2 = int(input("Ingreso N2: "))
      R = N1 - N2
      print("El resultado es: ",R)
  # MULTIPLICACION
    elif operacion == 3:
      N1 = Int(input("Ingreso N1: "))
      N2 = Int(input("Ingreso N2: "))
      R = N1 * N2
      print("El resultadoes: ",R)
  # DIVISION
    elif operacion == 4:
      N1 = int(input("Ingreso N1: "))
      N2 = int(input("Ingreso N2: "))
      R = N1 / N2
      print("El resultado es: ",R)
  # POTENCIACION
    elif operacion == 5:
      N1 = int(input("Ingreso N1: "))
      N2 = int(input("Ingreso N2: "))
      N2 = int(input())
      R = N1**N2
      print("El resultado es: ",R)
  # IMAGINARIOS
    elif operacion == 6:
      print("Numeros imaginarios")
  # FUNCIONES TRIGONOMETRICAS

    elif operacion == 7:
      x = int(input("Ingrese el valor de x: "))
      print("\n1.Seno\n2.Coseno\n3.Tangente\n4.Cotangente\n5.Cecante")
      print("6.Cosecante\n7.Salir")
      opcion = int(input("Ingrese opcion"))
      while (opcion != 7):
        if opcion == 1:
          print("El seno de x: " + str(math.sin(x)))
        elif opcion == 2:
          print("El coseno de x: " + str(math.cos(x)))
        elif opcion == 3:
          print("El tangente de x: " + str(math.tan(x)))
        elif opcion == 4:
          print("El cotangente de x: " + str(math.cot(x)))
        elif opcion == 5:
          print("El secante de x: " + str(math.sec(x)))
        elif opcion == 6:
          print("El cosecante de x: " + str(math.cosec(x)))
        else:
          break
while True:
    calculadora()
    respuesta = input("desea hacer otra operacion? (si) / (s): ")
    if respuesta.lower() not in ["s", "si"]:
      break



#elif operacion not in [1,2,3,4,5,6]:
#print("Numero no valido (No se encuentra en la lista de operaciones disponibles)")
#elif operacion=='6':
