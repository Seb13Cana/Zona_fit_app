from cliente import Cliente
from cliente_dao import  ClienteDAO

print('*** Clientes de Zona Fit Gym ***')

opcion = None

while opcion != 5:
    print('''Menu:
    1. Mostrar clientes
    2. agregar clientes
    3. Modificar clientes
    4. Eliminar clientes
    5. Salir''')

    opcion = int(input('Ingresa la opcion a seleccionar (1-5): '))

    if opcion ==1:
        clientes_a_mostrar = ClienteDAO.seleccionar_info()
        print('\n*** Lista de clientes ***')
        for cliente in clientes_a_mostrar:
            print(cliente)
    elif opcion ==2:
        nombre_cliente = input('Ingresa el nombre del cliente: ')
        apellido_cliente = input('Ingresa el apellido del cliente: ')
        membresia = int(input('Ingresa el numero de membresia: '))
        cliente_para_registrar = Cliente(nombre=nombre_cliente,apellido=apellido_cliente,membresia=membresia)
        cliente_registrado = ClienteDAO.insertar_datos(cliente_para_registrar)
        print(cliente_registrado)
    elif opcion ==3:
        id_modificar = int(input('Ingresa el id del cliente a modificar'))
        nombre_cliente = input('Ingresa el nombre del cliente: ')
        apellido_cliente = input('Ingresa el apellido del cliente: ')
        membresia = int(input('Ingresa el numero de membresia: '))
        cliente_a_modificar = Cliente(id_modificar,nombre_cliente,apellido_cliente,membresia)
        cliente_modificado = ClienteDAO.actualizar_datos(cliente_a_modificar)
    elif opcion ==4:
        id_eliminar = int(input('Ingresa el id del cliente a modificar: '))
        cliente_a_eliminar = Cliente(id=id_eliminar)
        cliente_eliminado = ClienteDAO.eliminar_datos(cliente_a_eliminar)
    elif opcion ==5:
        print('Salimos d la aplicación')
        opcion = 5