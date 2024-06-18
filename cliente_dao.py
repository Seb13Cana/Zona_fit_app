#DAO =  Data Object Management
from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    SENTENCIA_SELECCIONAR = 'SELECT * FROM cliente'
    SENTENCIA_INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s,%s,%s)'
    SENTENCIA_ELIMINAR = 'DELETE from cliente  WHERE id=%s'
    SENTENCIA_ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s  WHERE id=%s'

    @classmethod
    def seleccionar_info(cls):
        #Variable da estado de la conexion
        conexion = None

        try:
            #Obtiene la conexión a la BD
            conexion = Conexion.obtener_conexion()
            #Crea el objeto cursor por el cual se realizaran las operaciones o sentencias
            cursor = conexion.cursor()
            cursor.execute(cls.SENTENCIA_SELECCIONAR)
            #Obtiene el registro
            registros = cursor.fetchall()
            #Mapeo de Clase-tabla cliente
            registro_clientes = []
            for registro in registros:
                cliente = Cliente(registro[0],registro[1],
                                  registro[2],registro[3])
                registro_clientes.append(cliente)
            return registro_clientes

        except Exception as ex:
            print(f'Ocurrio error al selecionar regitro {ex}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar_datos(cls, cliente):
        # Variable da estado de la conexion
        conexion = None
        try:
            # Obtiene la conexión a la BD
            conexion = Conexion.obtener_conexion()
            # Crea el objeto cursor por el cual se realizaran las operaciones o sentencias
            cursor = conexion.cursor()
            #Obtiene los valores para ingresar en la BD
            valores = (cliente.nombre, cliente.apellido,cliente.membresia)
            #Ejecuta el script insertar
            cursor.execute(cls.SENTENCIA_INSERTAR, valores)
            #Realiza el commit a la base de datos
            conexion.commit()
            return cursor.rowcount

        except Exception as ex:
            print(f'Ocurrio un error al insertar el registro del cliente: {ex}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar_datos(cls, cliente):
        # Variable da estado de la conexion
        conexion = None
        try:
            # Obtiene la conexión a la BD
            conexion = Conexion.obtener_conexion()
            # Crea el objeto cursor por el cual se realizaran las operaciones o sentencias
            cursor = conexion.cursor()
            # Obtiene los valores para modificar en la BD
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            # Ejecuta el script insertar
            cursor.execute(cls.SENTENCIA_ACTUALIZAR, valores)
            # Realiza el commit a la base de datos
            conexion.commit()
            return cursor.rowcount
        except Exception as ex:
            print(f'Ocurrio un error al actualizar el registro del cliente: {ex}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar_datos(cls, cliente):

        conexion = None
        try:
            # Obtiene la conexión a la BD
            conexion = Conexion.obtener_conexion()
            # Crea el objeto cursor por el cual se realizaran las operaciones o sentencias
            cursor = conexion.cursor()
            # Obtiene los valores para modificar en la BD
            valores = (cliente.id,)
            # Ejecuta el script eliminar
            cursor.execute(cls.SENTENCIA_ELIMINAR, valores)
            # Realiza el commit a la base de datos
            conexion.commit()
            return cursor.rowcount
        except Exception as ex:
            print(f'Ocurrio un error al eliminar el registro del cliente: {ex}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)



if __name__ =='__main__':
    #Insertar datos
    # cliente_1 = Cliente(nombre='Mario',apellido='Jimenez', membresia=122)
    # cliente_registrado = ClienteDAO.insertar_datos(cliente_1)
    # print(cliente_registrado)

    #Actualizar datos
    # cliente_por_actualizar = Cliente(3,'Mariana', 'Tellez',122)
    # cliente_actualizado = ClienteDAO.actualizar_datos(cliente_por_actualizar)
    # print(cliente_actualizado)

    #Eliminar clientes de la BD
    cliente_a_eliminar = Cliente(id=4)
    cliente_eliminado = ClienteDAO.eliminar_datos(cliente_a_eliminar)
    print(cliente_eliminado)

    #Seleccionar clientes
    # prueba_clientes = ClienteDAO.seleccionar_info()
    # for regitro in prueba_clientes:
    #
    #    print(regitro)