import json


def guardar_registro(registro):

    archivo = open("datos/registros.json", "r")

    registros = json.load(archivo)

    archivo.close()

    registros.append(registro)

    archivo = open("datos/registros.json", "w")

    json.dump(registros, archivo, indent=4)

    archivo.close()