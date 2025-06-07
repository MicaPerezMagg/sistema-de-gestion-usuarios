------------------------ Sistema de Gestión de Usuarios (Python + SQLite) -----------------------------

Este proyecto es una aplicación de consola desarrollada para la EVIDENCIA 3 , que permite gestionar usuarios diferenciando sus roles (Administrador y Usuario Estándar).


---------- Funciones principales

- Registro de nuevos usuarios con validación de contraseña.
- Inicio de sesión con verificación en base de datos.
- Diferenciación de roles:
  - **Usuario estándar:** puede ver sus datos personales.
  - **Administrador:** puede ver todos los usuarios, cambiar roles y eliminar cuentas.
- Control de acceso según rol.
- Menú interactivo y mensajes informativos.
- Gestión de datos a través de una base SQLite.

---

--------- Base de datos

Se utiliza SQLite para almacenar los datos de los usuarios y los roles.

- Tablas creadas: `Usuario`, `Rol`
- Scripts SQL incluidos:
  - `crear_base_datos.sql`: crea las tablas necesarias.
  - Consultas CRUD para usuarios.
- Archivo `usuarios.db` incluido para pruebas.

---

 -------- Estructura del código

- `import sqlite3.py`: archivo principal del programa.
- Modularidad con clases: `Usuario`, `UsuarioEstandar`, `Administrador`.
- Uso de Programación Orientada a Objetos.
- Validaciones y separación de funcionalidades por rol.

---

-------- Herramientas utilizadas

- Python 3.x
- SQLite
- Git & GitHub

---

------ Realizado por: 

- ALUMNA: Carla Micaela Perez Maggetti
- LINK al repositorio: https://github.com/MicaPerezMagg/sistema-de-gestion-usuarios

Proyecto realizado para la carrera Desarrollo Web y Aplicaciones Digitales del ISPC.

---------------
