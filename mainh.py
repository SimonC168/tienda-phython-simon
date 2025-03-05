nombreVendedor=None
productos=[]
producto={}

opcion=100

print("mercado")
print("++++++++++++++++++++++++")
print("1. agregar producto")
print("2. ver lista de mercado")
print("3. editar producto de la lista")
print("4. eliminar producto de la lista")
print("preciona 5 para salir")
while opcion!=5:
    opcion=int(input("ingrese una opcion:"))
    if opcion==1:
        print("bienvenido a la creacion de tu lista de peoductos")

        #creaando clave valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("digite el nombre del producto:  ")
        producto["precio"]=int(input("digita el precio del producto:  "))
        producto["cantidad"]=input("digite la cantidad del producto:   ")
        producto["presentacion"]=input("cual presentacion llevara:  ")

        #mostrando mi diccionario
        print(producto)

        #pablando una lista 
        productos.append(producto)
        print(productos)
    elif opcion == 2:
        print("estoy en la dos")
    elif opcion == 3:
        print("estoy en la tres")
    elif opcion==4:
        print("estoy en la cuatro")
    else:
        print("no hay opcion")
        
