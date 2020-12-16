def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes U$S " + dolares + " dólares")


menu = """
Bienvenido al conversor de monedas 💰
1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Elige una opción: """

# Código
opcion = input(menu)

if opcion == '1':
    conversor("Argentinos", 82.49)
elif opcion == '2':
    conversor("Colombianos", 3419.70)
elif opcion == '3':
    conversor("Mexicanos", 19.95)
else:
    print("Ingresa una opción correcta")
