empresas = [4,6,7,9,5]

def facturacion_media(empresas):
    total = sum(empresas)
    media = total / len(empresas)
    return media

resultado = facturacion_media(empresas)

print("La facturacion media es de: ", resultado)