CREATE DATABASE IF NOT EXISTS PEPS;
CREATE USER 'agente'@'%' IDENTIFIED BY '0traClave';
GRANT ALL PRIVILEGES ON PEPS.* TO 'agente'@'%';
FLUSH PRIVILEGES;
USE PEPS;
CREATE TABLE juegos(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
	foto VARCHAR(255),
    tipo VARCHAR(255) NOT NULL
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    estado VARCHAR(10) NOT NULL,
    numAccesosErroneos INTEGER,
    fechaUltimoAcceso DATE
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`,`estado`, `numAccesosErroneos`,`fechaUltimoAcceso`) VALUES ('root', '$2b$10$hJtLt4u0SqSf.h3S5Uuev.nu98ARhn.6SpvFCYbc1eeynJmy81cmK', 'admin', 'activo', 0, '2022-03-01 00:00');