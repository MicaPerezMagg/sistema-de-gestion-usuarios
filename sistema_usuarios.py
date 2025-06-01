import sqlite3
import re

#Crear la base de datos
def crear_base_de_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL,
            rol TEXT CHECK(rol IN ('administrador', 'estandar')) NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

#Validar contraseña segura
def validar_contrasena(contrasena):
    if len(contrasena) < 6:
        return False
    tiene_letra = re.search(r"[A-Za-z]", contrasena)
    tiene_numero = re.search(r"[0-9]", contrasena)
    return bool(tiene_letra and tiene_numero)

#Registrar usuario
def registrar_usuario():
    nombre = input("Ingrese nombre de usuario: ").strip()
    contrasena = input("Ingrese contraseña (mín. 6 caracteres, letras y números): ").strip()
    rol = input("Rol (administrador / estandar): ").strip().lower()

    if rol not in ["administrador", "estandar"]:
        print("⚠️ Rol inválido. Debe ser 'administrador' o 'estandar'.")
        return

    if not validar_contrasena(contrasena):
        print("⚠️ Contraseña inválida. Debe tener al menos 6 caracteres y contener letras y números.")
        return

    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nombre_usuario, contrasena, rol) VALUES (?, ?, ?)", 
                       (nombre, contrasena, rol))
        conexion.commit()
        print("✅ Usuario registrado con éxito.")
    except sqlite3.IntegrityError:
        print("⚠️ Ese nombre de usuario ya existe.")
    conexion.close()

#Iniciar sesión
def iniciar_sesion():
    nombre = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()

    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT rol FROM usuarios WHERE nombre_usuario=? AND contrasena=?", (nombre, contrasena))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        rol = resultado[0]
        print(f"\n🎉 Inicio de sesión exitoso. Rol: {rol}")
        if rol == "administrador":
            menu_administrador(nombre)
        else:
            menu_estandar(nombre)
    else:
        print("❌ Usuario o contraseña incorrectos.")

#Ver todos los usuarios (solo admin)
def ver_usuarios():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre_usuario, rol FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.close()

    print("\n📋 Lista de usuarios:")
    for u in usuarios:
        print(f"ID: {u[0]} | Usuario: {u[1]} | Rol: {u[2]}")

#Eliminar usuario (solo admin)
def eliminar_usuario():
    id_usuario = input("Ingrese el ID del usuario a eliminar: ").strip()
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))
    if cursor.rowcount == 0:
        print("⚠️ No se encontró un usuario con ese ID.")
    else:
        print("🗑️ Usuario eliminado correctamente.")
    conexion.commit()
    conexion.close()

#Menú para administradores
def menu_administrador(nombre_usuario):
    while True:
        print(f"\n--- MENÚ ADMIN ({nombre_usuario}) ---")
        print("1. Ver usuarios")
        print("2. Eliminar usuario")
        print("3. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_usuarios()
        elif opcion == "2":
            eliminar_usuario()
        elif opcion == "3":
            print("👋 Sesión cerrada.")
            break
        else:
            print("⚠️ Opción inválida.")

#Menú para usuarios estándar
def menu_estandar(nombre_usuario):
    while True:
        print(f"\n--- MENÚ USUARIO ({nombre_usuario}) ---")
        print("1. Ver mi perfil")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"👤 Usuario: {nombre_usuario} (estandar)")
        elif opcion == "2":
            print("👋 Sesión cerrada.")
            break
        else:
            print("⚠️ Opción inválida.")

#Menú principal
def menu_principal():
    while True:
        print("\n=== SISTEMA DE USUARIOS ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("👋 Gracias por usar el sistema.")
            break
        else:
            print("⚠️ Opción inválida.")

#Punto de entrada
if __name__ == "__main__":
    crear_base_de_datos()
    menu_principal()

