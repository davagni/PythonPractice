# Config
menu = """
Bienvenido al conversor de monedas 💰
1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Elige una opción: """

# Código
opcion = input(menu)

if opcion == '1':
    pesos = input("¿Cuántos pesos Argentinos tienes?: ")
    valor_dolar = 82.49
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes U$S " + dolares + " dólares")
elif opcion == '2':
    pesos = input("¿Cuántos pesos Colombianos tienes?: ")
    valor_dolar = 3419.70
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes U$S " + dolares + " dólares")
elif opcion == '3':
    pesos = input("¿Cuántos pesos Mexicanos tienes?: ")
    valor_dolar = 19.95
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes U$S " + dolares + " dólares")
else:
    print("Ingresa una opción correcta")
