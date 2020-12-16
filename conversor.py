# Config Valor Dolar
valor_dolar = 82.49
# Código
pesos = input("¿Cuántos pesos argentinos tienes?: ")
pesos = float(pesos)
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print("Tienes U$S " + dolares + " dólares")
