## Instalación

- Clonar el repositorio


- Crear e iniciar un entorno virtual

  `virtualenv venv`  
  `source venv/bin/activate`


- Instalar el proyecto

  `pip install -e .`


- Crear una base de datos PostgreSQL con el nombre `kenwin`


- Inicializar la base de datos con el comando: 

  `initialize_kenwinauth_db development.ini`

Este comando también creará un usuario en la base de datos con las credenciales:

  > Usuario: TestUser  
  > Pass: TestPass 


- Correr el servidor con pserve:

  `pserve development.ini --reload`
