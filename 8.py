# 
# 8. algoritmo para calcular el volumen y el área superficial de una pirámide con base cuadrada
# 
print("Programa para calcular el volumen y el área superficial de una pirámide de base cuadrada ")
altura = int(input("Ingrese la altura de la piramide: "))
lado = int(input("Ingrese un lado de la base de la piramide: "))
area=((4*altura**2+lado**2)*0.5+lado)*lado
volumen=lado**2*altura/3
print(f"El area superficial de la piramide es {area}\nEl volumen de la piramide es {volumen}")