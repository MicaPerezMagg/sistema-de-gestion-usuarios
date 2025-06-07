crear_base_datos.sql
script ejecutable para crear las tablas (estructura completa)
sql
Copiar
Editar
CREATE TABLE Rol (
    id_rol INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_rol TEXT NOT NULL UNIQUE
);

CREATE TABLE Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario TEXT NOT NULL UNIQUE,
    contraseña TEXT NOT NULL,
    id_rol INTEGER NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES Rol(id_rol)
);



 poblar la tabla Rol con los datos iniciales:

sql
Copiar
Editar
INSERT INTO Rol (nombre_rol) VALUES ('admin'), ('estandar');