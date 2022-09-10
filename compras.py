from os import remove


print("***MENU***")
print("1. Agregar producto.")
print("2. Mostrar productos.")
print("3. Buscar producto por código y editar.")
print("4. Buscar producto por código y eliminar.")
print("0. SALIR")

i = 100

productos=[]

while(i !=0):
    producto = {}
    i = int(input("Digite una opción del menú: "))
    if (i == 1):
        producto['codigo'] = int(input("Digite el código del producto: "))
        producto['nombre'] = input("Digite el nombre del producto: ")
        producto['precio'] = input("Digite el precio del producto: ")
        productos.append(producto)
    elif(i == 2):
        print(productos)
    elif(i == 3):
        for n in productos:
            cod = int(input("Digite el código de producto a editar: "))
            if (cod == n['codigo']):
                n['precio'] = input("Digite el nuevo precio del producto: ")
                break
            else:
                print("No existen productos con el código ingresado.")
    elif(i == 4):
        for n in productos:
            cod = int(input("Digite el código del producto a eliminar: "))
            if(cod == n['codigo']):
                productos.remove(n)
                print("Se ha eliminado el producto.")
            else:
                print("No existen productos con el código ingresado.")
    else:
        print("Por favor digite una opción del menú.")
else:
    print("Fin del programa.")
            
        
