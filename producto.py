import sys
li=[]
class producto:
    idProducto=0
    nombre=" "
    cantidad=0
    precio=0
    
    
def menu():
    opcion=0
    while opcion!=salir:
        opcion=int(input("Que desea realizar? \n 1 Inngresar Producto \n 2 Consultar Producto \n 3 Salir\n"))
        if opcion==1:
            RegistrarProducto()
        elif opcion==2:
            ConsultarProducto()
        elif opcion==3:
            salir()
    
def RegistrarProducto():
    print("Registrar producto")
    p=producto()
    p.idProducto=int(input("ID Producto"))
    p.nombre=str(input("Nombre Producto"))
    p.cantidad=int(input("Cantidad"))
    p.precio=int(input("Precio"))
    
    li.append(p)
    
def ConsultarProducto():
    print("Consultar Producto")
    
    idProducto=int(input("Ingrese el Id del producto"))
    for p in li:
        if p.idProducto == idProducto:
            print(p.idProducto)
            print(p.nombre)
            print(p.cantidad)
            print(p.precio)
    
def salir():
    print("El programa finalizo")
    sys.exit()

            
menu()
            
