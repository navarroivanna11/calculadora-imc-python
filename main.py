print("================================")
print("       CALCULADORA DE IMC")
print("================================")

nombre = input("Ingrese su nombre: ")

peso = float(input("Ingrese su peso en kg: "))

altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

print("\nRESULTADO")
print("Nombre:", nombre)
print("Peso:", peso, "kg")
print("Altura:", altura, "m")
print("IMC:", round(imc, 2))