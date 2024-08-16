# 
# 16 Dado un número entero positivo de cuatro dígitos, calcular la suma de dichos dígitos
# 
def suma():
    while True:
        print("Programa que recibe numero de 4 digitos y los suma")
        num = int(input("Ingrese numero de 4 digitos: "))
        if 999 < num < 10000:
            sum = num // 1000 + (num % 1000) // 100 + (num % 100) // 10 + num % 10
            print(f"La suma de todos los digitos de {num} es: {sum}")
            break 
        else:
            print("Ingrese un numero de 4 cifras.")
suma()