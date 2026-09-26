from imc import calcular_imc, clasificar_imc
from historial import guardar_registro

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

imc = calcular_imc(peso, altura)

categoria = clasificar_imc(imc)

registro = {
    "nombre": nombre,
    "peso": peso,
    "altura": altura,
    "imc": imc,
    "categoria": categoria
}

guardar_registro(registro)

print("\nRESULTADO")
print("Nombre:", nombre)
print("Peso:", peso, "kg")
print("Altura:", altura, "m")
print("IMC:", round(imc, 2))
print("Categoría:", categoria)