print("================================")
print("       CALCULADORA DE IMC")
print("================================")

nombre = input("Ingrese su nombre: ")

peso = float(input("Ingrese su peso en kg: "))

while peso <= 0:
    print("El peso debe ser mayor que 0.")
    peso = float(input("Ingrese nuevamente el peso: "))

altura = float(input("Ingrese su altura en metros: "))

while altura <= 0:
    print("La altura debe ser mayor que 0.")
    altura = float(input("Ingrese nuevamente la altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    categoria = "Bajo peso"

elif imc < 25:
    categoria = "Peso normal"

elif imc < 30:
    categoria = "Sobrepeso"

else:
    categoria = "Obesidad"

print("\nRESULTADO")
print("Nombre:", nombre)
print("Peso:", peso, "kg")
print("Altura:", altura, "m")
print("IMC:", round(imc, 2))
print("Categoría:", categoria)