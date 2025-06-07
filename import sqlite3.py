import sqlite3
import re

# ==================== CLASES ====================

class Usuario:
    def __init__(self, username, password, rol):
        self.username = username
        self.password = password
        self.rol = rol

    def mostrar_info(self):
        print(f"Usuario: {self.username} - Rol: {self.rol}")

class Administrador(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def eliminar_usuario(self, username, conexion):
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
        conexion.commit()
        print(f"Usuario {username} eliminado correctamente.")

class UsuarioEstandar(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password, "estandar")

    def ver_datos(self):
        print(f"Bienvenido {self.username}. Solo puedes ver tus datos.")

# ==================== FUNCIONES ====================

def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            rol TEXT NOT NULL CHECK (rol IN ('admin', 'estandar'))
        )
    ''')
    conexion.commit()

def validar_password(password):
    return len(password) >= 6 and re.search(r'[A-Za-z]', password) and re.search(r'\d', password)

def registrar_usuario(conexion):
    print("\n=== Registro de usuario ===")
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña (mínimo 6 caracteres, letras y números): ")

    if not validar_password(password):
        print("Contraseña inválida. Debe tener mínimo 6 caracteres, incluir letras y números.")
        return

    rol = input("Ingrese rol (admin/estandar): ").lower()
    if rol not in ["admin", "estandar"]:
        print("Rol inválido.")
        return

    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (username, password, rol) VALUES (?, ?, ?)", (username, password, rol))
        conexion.commit()
        print("Usuario registrado correctamente.")
    except sqlite3.IntegrityError:
        print("El nombre de usuario ya existe.")

def iniciar_sesion(conexion):
    print("\n=== Iniciar sesión ===")

    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    usuario = cursor.fetchone()

    if usuario:
        print("Inicio de sesión exitoso.")
        if usuario[2] == 'admin':
            user = Administrador(usuario[0], usuario[1])
            menu_admin(user, conexion)
        else:
            user = UsuarioEstandar(usuario[0], usuario[1])
            menu_estandar(user)
    else:
        print("Credenciales incorrectas.")

def menu_admin(usuario, conexion):
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Ver mi información")
        print("2. Eliminar un usuario")
        print("3. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            usuario.mostrar_info()
        elif opcion == '2':
            username_a_eliminar = input("Nombre de usuario a eliminar: ")
            if username_a_eliminar == usuario.username:
                print("No puedes eliminarte a ti mismo.")
            else:
                usuario.eliminar_usuario(username_a_eliminar, conexion)
        elif opcion == '3':
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida.")

def menu_estandar(usuario):
    while True:
        print("\n=== Menú Usuario Estándar ===")
        print("1. Ver mi información")
        print("2. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            usuario.ver_datos()
        elif opcion == '2':
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida.")

def menu_principal(conexion):
    while True:
        print("\n=== Sistema de Gestión de Usuarios ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(conexion)
        elif opcion == '2':
            iniciar_sesion(conexion)
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

# ==================== INICIO DEL PROGRAMA ====================

conexion = sqlite3.connect("usuarios.db")
crear_tabla(conexion)
menu_principal(conexion)
conexion.close()
