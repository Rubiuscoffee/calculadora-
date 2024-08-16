# 
# 9. programa para calcular el volumen de la esfera menor circunscrita y el volumen de la esfera mayor circunscrita en un cubo
# 
print("Programa para calcular el volumen de una esfera (mayor y menor) circunscrita")
lado = int(input("Ingrese uno de los lados del cubo: "))
Volumen1=lado**(3/6)
p=3.1416
Volumen2=lado**3*p**(0.5/2)
print(f"El volumen de la esfera menor circunscrita es {Volumen2}\nEl volumen de la esfera mayor circunscrita es {Volumen1}")