#Data definition language -- > Crear y gestionar las estructuras
#Data manipulation language -- > Crear y gestionar los datos dentro de la estructura

#Definition of the schema of the DB


# Comentario sobre de que es la base de datos

#Crea la base de datos
CREATE DATABASE IF NOT EXISTS agenda_db;

#Selecciona la base de datos con la cual se va a trabajar
USE agenda_db;

#Crea las tablas centrales (kernel): Contactos y Clientes
CREATE TABLE IF NOT EXISTS contactos( 
	idContacto INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(70) NOT NULL,
	telefono VARCHAR(13) NOT NULL,
    correo VARCHAR(35),
    direccion VARCHAR(70),
    PRIMARY KEY(idContacto)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS citas(
	idCita INT NOT NULL AUTO_INCREMENT,
    fecha VARCHAR(10) NOT NULL,
    hora_inicio VARCHAR(10),
    hora_final VARCHAR(10),
    lugar VARCHAR(70),
    descripcion VARCHAR(70),
    PRIMARY KEY (idCita)
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS citas_detalles( 
	idCita INT NOT NULL,
    idContacto INT NOT NULL,
    PRIMARY KEY (idCita, idContacto),
	CONSTRAINT fkcitas_cc FOREIGN KEY(idCita)
		REFERENCES citas(idCita)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fkcontactos_cc FOREIGN KEY(idContacto)
		REFERENCES contactos(idContacto)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;