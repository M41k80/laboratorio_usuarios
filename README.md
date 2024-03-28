# laboratorio_usuarios
laboratorio usuarios python con postgreSQL
1.---- instalar PostgreSQL desde la pagina  https://www.postgresql.org/download/
2.---- en usuario poner admin
3.---- en password poner admin
4.---- y ya que este instalada crear una base de datos que se llame "test_db"
5.---- crear una nueva tabla que tenga el nombre usuario y dejan lo demas por default
6.---- en columnas agrenan
       id_usuario tipo integer     que sea not null  y llave primaria activado
       username   tipo character varying  solo que sea no null
       password   tipo character varying  solo que sea no null
7.---- instalar PSYCOPG2 en visual code o pycharm o el IDE que esten utilizando...
      -----     pip install psycopg2-binary

      despues de eso ya pueden agregar el codigo para crear usuarios en una base de datos...
      
