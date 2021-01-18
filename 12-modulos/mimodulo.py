def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

def calculadora(numero1, numero2, operacion):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    if operacion == 'Suma':
        return suma
    if operacion == 'Resta':
        return resta
    if operacion == 'Multi':
        return multi
    if operacion == 'Division':
        return division

    
