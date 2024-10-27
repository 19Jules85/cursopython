# Sacar la facturación media de 3 empresas
total = 7 + 8 + 9
media = total / 3

print("La facturación media es de: ", media)

total = 15 + 20 + 30
media = total / 3

print("La facturación media es de: ", media)

def facturacion_media(empresa1, empresa2, empresa3):
    total = empresa1 + empresa2 + empresa3
    media = total/3
    return media

resultado = facturacion_media(10,8,12)

print(resultado)
