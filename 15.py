# 
# 15. programa para calcular el cuanto dinero se tendría en una cuenta bancaria con la tasa de interés anual y el dinero estando x numero de años
# 
dinero = int(input("Ingrese dinero dentro de la cuenta: "))
años = int(input("Ingrese cuantos años esta el dinero dentro de la cuenta: "))
interes = int(input("Ingrese el interes: "))
i=interes/100
res=dinero*(1+i)**años
print(f"El dinero acumulado despues de {años} años con una tasa de interes del {interes}% es: {res}")