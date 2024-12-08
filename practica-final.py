#Paso 1: Definir 
tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

#Paso 2: Solicitar al usuario el tipo de conversión (Euro a Mex o Dolar a Mex)

tipo_de_conversion = input("Ingrese la moneda origen para la conversión (EUR/USD): ")

#Paso 3: Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir (EUR/USD): "))

#Paso 4: Realizar la conversión utilizando el tipo de cambio correspondiente

if tipo_de_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversion de EUR a MXN es: ", resultado)
elif tipo_de_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversion de USD a MXN es: ", resultado)
else: 
    print("No esta disponible este tipo de conversion actualmente")
