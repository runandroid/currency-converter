# CURRENCY CONVERTER

# Currency Converter using a API (ExchangeRate-API: (https://api.exchangerate-api.com/v4/latest/{base}).
# This API (Application Programming Interface) provides up-to-date exchange rates in JSON format.
# The JSON format is used to structure data in text form and enables the exchange of information between applications in a simple, lightweight, and rapid manner.
# API ==> Interface that allows one Software to request data or services from another without needing to know its internal workings.

import requests

def obtener_tasa_cambio(base, destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"  # This API provides up-to-date exchange rates in JSON format. 
    response = requests.get(url)    
    datos = response.json()         
    return datos["rates"].get(destino, None)


def convertir_moneda(cantidad, base, destino):
    tasa = obtener_tasa_cambio(base, destino)
    if tasa:
        return cantidad * tasa
    else:
        return None

def main():
    print("Conversor de Monedas")
    cantidad = float(input("Ingrese la cantidad de dinero: "))
    base = input("Ingrese la moneda de origen (ej: USD, EUR, JPY, CAD, CNY, AUD, NZD, ZAR, ILS, RUB, INR, ARS, BRL, UYU, MXN, VES): ").upper()
    destino = input("Ingrese la moneda de destino (ej: USD, EUR, JPY, CAD, CNY, AUD, NZD, ZAR, ILS, RUB, INR, ARS, BRL, UYU, MXN, VES): ").upper()
    
    resultado = convertir_moneda(cantidad, base, destino)
    
    if resultado is not None:
        print(f"{cantidad} {base} equivale a {resultado:.2f} {destino}")
    else:
        print("No se pudo obtener la tasa de cambio. Verifique las monedas ingresadas.")

if __name__ == "__main__":
    main()
