def calcular_imc(peso, altura):

    imc = peso / (altura * altura)

    return round(imc, 2)

def clasificar_imc(imc):

    if imc < 18.5:
        return "Bajo peso"

    elif imc < 25:
        return "Peso normal"

    elif imc < 30:
        return "Sobrepeso"

    else:
        return "Obesidad"