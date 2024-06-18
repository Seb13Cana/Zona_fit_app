#Se crea la clase de conexion a la DB, tema POOL de conexiones

#Se  importa la clase connector, pooling, para crear conexiones
from mysql.connector import pooling, Error

class Conexion:
    DATABASE  = 'zona_fit_db'
    USERNAME  = 'root'
    PASSWORD  = 'admin'
    DB_PORT   = '3306'
    HOST      = 'localhost'
    POOL_SIZE = 5 #Tamaño del pool, (# de conexiones perimitidas), se recomienda no sea tan grande
    POOL_NAME = 'zona_fit_pool'
    pool      = None

    @classmethod
    def obtener_pool(cls): #Se crea el metodo para obtener el pool de conexiones
        if cls.pool is None: # Se crea el pool de conexion
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls.POOL_NAME,
                    pool_size= cls.POOL_SIZE,
                    host= cls.HOST,
                    port= cls.DB_PORT,
                    database= cls.DATABASE,
                    password=cls.PASSWORD
                )
                #print(f'Nombre pool: {cls.pool.pool_name}')
                return cls.pool #Regresamos el objeto de pool, la variable por la cual se realiza la conexion
            except Error as ex:
                print(f'Error al obtener pool: {ex}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        #print(f'Se ejecuta el metodo liberar, {conexion}')
        conexion.close()

if __name__ == '__main__':
    #Crear objeto de conexion
    #pool = Conexion.obtener_pool()
    #print(pool)

    #Obtener un objeto de conexion
    conn = Conexion.obtener_conexion()
    print(f'Conexion realizada: {conn}')
    Conexion.liberar_conexion(conn)
