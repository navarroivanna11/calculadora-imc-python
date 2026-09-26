import json

def guardar_registro(registro):

    archivo = open("datos/registros.json", "r")

    registros = json.load(archivo)

    archivo.close()

    registros.append(registro)

    archivo = open("datos/registros.json", "w")

    json.dump(registros, archivo, indent=4)

    archivo.close()


def mostrar_historial():


    archivo = open("datos/registros.json", "r")

    registros = json.load(archivo)

    archivo.close()

    print("\n================================")
    print("          HISTORIAL")
    print("================================")

    if len(registros) == 0:
        print("No existen registros.")

    else:
        for registro in registros:
            print("\nNombre:", registro["nombre"])
            print("Peso:", registro["peso"], "kg")
            print("Altura:", registro["altura"], "m")
            print("IMC:", registro["imc"])
            print("Categoría:", registro["categoria"])


