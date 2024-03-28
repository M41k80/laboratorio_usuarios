from psycopg2 import pool
import sys
from laboratorio_usuarios import logger_base

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON, cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._DB_PORT,
                    database = cls._DATABASE)
                logger_base.debug(f'SUCCESSFUL POOL CREATION: {cls._pool}')
                return cls._pool
            except Exception as e:
                logger_base.error(f'AN ERROR OCCURRED IN THE CREATION OF THE POOL: {e}')
                sys.exit()
        else:
            return cls._pool



    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        logger_base.debug(f'SUCCESSFUL CONNECTION TO THE POOL: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        logger_base.debug(f'RETURNED THE CONNECTION TO THE POOL: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()

    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()
