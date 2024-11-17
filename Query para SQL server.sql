use master
go
create database contrasenas
go
use contrasenas
go
CREATE TABLE contrasenas (
    id INT IDENTITY(1,1) PRIMARY KEY,  -- Columna de identificación única y autoincremental
	 contrasena NVARCHAR(255) NOT NULL,  -- Columna para la contraseña (256 es un buen tamaño)
    usuario NVARCHAR(100) NOT NULL,     -- Columna para el nombre de usuario
    correo NVARCHAR(100) NOT NULL,      -- Columna para el correo electrónico
    fecha_guardado DATETIME DEFAULT GETDATE()  -- Columna para almacenar la fecha y hora de cuando se guardó la contraseña
);
go

select * from contrasenas

