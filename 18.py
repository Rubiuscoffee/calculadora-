# 
# 18.programa para invertir un numero de cuatro dígitos
# 
def numeroinvertido():
    while True:
        print("Programa para invertir numero de 4 cifras")
        numeroainvertir = int(input("Ingrese un numero de 4 cifras: "))
        if 999 < numeroainvertir < 10000:
            numero_invertido = str(numeroainvertir)[::-1]
            print(f"Su numero invertido es {numero_invertido}")
            break 
        else:
            print("Ingrese un numero de 4 cifras.")

numeroinvertido()