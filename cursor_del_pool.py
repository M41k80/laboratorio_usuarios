from conexion import Conexion
import logger_base
class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        logger_base.debug('START THE METHOD WITH __ENTER__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger_base.debug('START THE METHOD __EXIT__')
        if exc_val:
            self._conexion.rollback()
            logger_base.error(f'EXCEPTION OCCURRED: {exc_type} {exc_val} {exc_tb}')
        else:
            self._conexion.commit()
            logger_base.debug('COMMIT OF THE TRANSACTION')

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        logger_base.debug('INSIDE OF THE WITH')
        cursor.execute('SELECT * FROM usuario')
        logger_base.debug(cursor.fetchall())
