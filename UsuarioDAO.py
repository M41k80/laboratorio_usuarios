from Usuario import Usuario
from cursor_del_pool import CursorDelPool
from laboratorio_usuarios import logger_base

class UsuarioDAO:

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _UPDATE = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _DELETE = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                 usuario = Usuario(registro[0], registro[1], registro[2])
                 usuarios.append(usuario)
            return usuarios


    @classmethod
    def insert(cls, usuario):
       with CursorDelPool() as cursor:
            logger_base.debug(f'USER TO INSERT: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERT, valores)
            logger_base.debug(f'USER INSERTED: {usuario}')
            return cursor.rowcount

    @classmethod
    def update(cls, usuario):

        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._UPDATE, valores)
            logger_base.debug(f'USER UPDATED: {usuario}')
            return cursor.rowcount

    @classmethod
    def delete(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario._id_usuario,)
            cursor.execute(cls._DELETE, valores)
            logger_base.debug(f'USER DELETED: {usuario}')
            return  cursor.rowcount

