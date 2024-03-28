from laboratorio_usuarios import logger_base
from conexion import Conexion
from laboratorio_usuarios.Usuario import Usuario
from UsuarioDAO import UsuarioDAO
from cursor_del_pool import CursorDelPool


option = None
while option != 5:
    try:
        print('OPTIONS'.center(25,'-'))
        print('1--- LISTAR USUARIO')
        print('2--- AGREGAR USUARIO')
        print('3--- ACTUALIZAR USUARIO')
        print('4--- ELIMINAR USUARIO')
        print('5--- SALIR... ')
        option = int(input('INSERT YOUR OPTION (1 - 5): '))

        if option == 1:
            usuarios =  UsuarioDAO.select()
            for usuario in usuarios:
                logger_base.info(usuario)


        elif option == 2:
            id_usuario = None
            username = input('USER NAME TO INSERT: ')
            password = input('PASSWORD TO INSERT: ')
            usuario1 = Usuario(id_usuario, username, password)
            UsuarioDAO.insert(usuario1)
            logger_base.info(usuario1)
        elif option == 3:
            id_usuario = int(input('USER_ID TO UPDATE: '))
            username = input('USER NAME TO UPDATE: ')
            password = input('PASSWORD TO UPDATE: ')
            usuario1 = Usuario(id_usuario, username, password)
            UsuarioDAO.update(usuario1)
        elif option == 4:
            id_usuario = int(input('ID_USUARIO TO DELETE: '))
            usuario1 = Usuario(id_usuario)
            UsuarioDAO.delete(usuario1)
            logger_base.info(usuario1)



    except Exception as e:
        print(f'ERROR TYPE: {e}')
        option = None
else:
    print('EXIT'.center(50,'-'))

