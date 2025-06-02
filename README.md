Sistema de Gestion Usuarios para Python.-

Este es un programa de consola desarrollado en Python que permite la gestión de usuarios con roles diferenciados: "administrador" y "usuario estandar".

---------------------------------------
CARACTERISTICAS:

- Registro de usuarios con validación de contraseña (mínimo 6 caracteres, debe incluir letras y números).
- Inicio de sesión con validación de credenciales.
- Control de acceso basado en roles:
  - Administradores pueden gestionar usuarios (registrar, modificar, eliminar).
  - Usuarios estándar tienen acceso limitado y no pueden modificar roles ni eliminar usuarios.
- Mensajes claros y manejo de errores para mejorar la experiencia del usuario.
- Datos almacenados en una base de datos SQLite local.

¿Cómo se usa? ¡Es fácil!

1. Clonar o descargar el repositorio.
2. Ejecutar el programa:
 
. Seguir las instrucciones del menú para registrar usuarios o iniciar sesión.

REQUISITOS----------------------------

- Python 3.x
- Biblioteca estándar sqlite3 (incluida en Python)

FUTURAS MEJORAS-----------------------

- Interfaz gráfica.
- Encriptación de contraseñas.
- Exportar datos a otros formatos.

------------------------------

¡Gracias por usar el sistema!
