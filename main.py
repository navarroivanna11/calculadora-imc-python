from imc import calcular_imc, clasificar_imc
from historial import guardar_registro, mostrar_historial

def mostrar_menu():
    print("\n================================")
    print("       CALCULADORA DE IMC")
    print("================================")
    print("1. Calcular IMC")
    print("2. Ver historial")
    print("3. Salir")
    
def calcular():

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

opcion = ""

while opcion != "3":

    mostrar_menu()

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        calcular()

    elif opcion == "2":
        mostrar_historial()

    elif opcion == "3":
        print("Programa finalizado.")

    else:
        print("Opción no válida.")