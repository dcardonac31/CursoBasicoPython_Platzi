print("-- Bienvenido al conversor de moneda --")
print("1. Dolares (USD) -> Pesos colombianos (COP)")
print("2. Pesos colombianos (COP) -> Dolares (USD)")
tipo_conversion = input("Digite tipo conversión: ")
tipo_conversion = int(tipo_conversion)
if tipo_conversion == 1:
    dolares = input("¿Cuántos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso = 0.00029
    pesos = dolares / valor_peso
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $ (COP)" + pesos)
else:
    pesos = input("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3424.81
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $USD " + dolares)