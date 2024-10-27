# Calcular el precio total de una compra
# Supongamos que estas trabajando en una empresa que vende productos y necesitas crear un programa que calcule el precio total de una compra
# Incluyendo el impuesto sobre las ventas. (21%) 
# El programa deberá solicitar al usuario el nombre del producto, la cantidad comprada y el precio unitario del producto
# Luego calculará el  precio total y mostrará un resumen de la compra.

def calcular_precio_total(cantidad, precio_unitario):
    #calcular el precio total de la compra
    precio_total = cantidad * precio_unitario
    return precio_total

def main():
    print("BIENVENIDO A TU TIENDA")
    nombre_producto = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad comprada: "))
    precio_unitario = float(input("Ingresa el precio unitario: "))

    if cantidad <= 0 or precio_unitario <= 0:
        print("El importe introducido no es correcto")
    else:
        precio_total = calcular_precio_total(cantidad,precio_unitario)
        impuesto_ventas = precio_total * 0.21
        precio_total_con_impuestos = precio_total +impuesto_ventas

        # Mostrar el resumen de la compra por teclado
        print("RESUMEN DE LA COMPRA")    
        print(f"Producto: {nombre_producto}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio unitario: {precio_unitario:.2f} ")
        print(f"Precio total: {precio_total:.2f} ")
        print(f"IVA (21%): {impuesto_ventas:.2f} ")
        print(f"Total con impuestos: {precio_total_con_impuestos:.2f} ")


main()        
