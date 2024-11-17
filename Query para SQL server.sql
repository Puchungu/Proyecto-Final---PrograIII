use master
go
create database contrasenas
go
use contrasenas
go
CREATE TABLE contrasenas (
    id INT IDENTITY(1,1) PRIMARY KEY,  -- Columna de identificaci�n �nica y autoincremental
	 contrasena NVARCHAR(255) NOT NULL,  -- Columna para la contrase�a (256 es un buen tama�o)
    usuario NVARCHAR(100) NOT NULL,     -- Columna para el nombre de usuario
    correo NVARCHAR(100) NOT NULL,      -- Columna para el correo electr�nico
    fecha_guardado DATETIME DEFAULT GETDATE()  -- Columna para almacenar la fecha y hora de cuando se guard� la contrase�a
);
go

select * from contrasenas

