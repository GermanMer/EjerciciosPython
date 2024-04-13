--Script SQL para crear la base de datos y las tablas
-- Crear la tabla Hospital
CREATE TABLE IF NOT EXISTS Hospital (
    Hospital_Id INTEGER PRIMARY KEY,
    Hospital_Name TEXT NOT NULL,
    Bed_Count INTEGER NOT NULL
);

-- Insertar datos en la tabla Hospital
INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count)
VALUES
(1, 'Mayo Clinic', 200),
(2, 'Cleveland Clinic', 400),
(3, 'Johns Hopkins', 1000),
(4, 'UCLA Medical Center', 1500);

-- Crear la tabla Doctor
CREATE TABLE IF NOT EXISTS Doctor (
    Doctor_Id INTEGER PRIMARY KEY,
    Doctor_Name TEXT NOT NULL,
    Hospital_Id INTEGER NOT NULL,
    Joining_Date TEXT NOT NULL,
    Speciality TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Experience INTEGER,
    FOREIGN KEY (Hospital_Id) REFERENCES Hospital(Hospital_Id)
);

-- Insertar datos en la tabla Doctor
INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience)
VALUES
(101, 'David', 1, '2005-02-10', 'Pediatric', 40000, NULL),
(102, 'Michael', 1, '2018-07-23', 'Oncologist', 20000, NULL),
(103, 'Susan', 2, '2016-05-19', 'Gynecologist', 25000, NULL),
(104, 'Robert', 2, '2017-12-28', 'Pediatric', 28000, NULL),
(105, 'Linda', 3, '2004-06-04', 'Gynecologist', 42000, NULL),
(106, 'William', 3, '2012-09-11', 'Dermatologist', 30000, NULL),
(107, 'Richard', 4, '2014-08-21', 'Gynecologist', 32000, NULL),
(108, 'Karen', 4, '2011-10-17', 'Radiologist', 30000, NULL);



--EJECUTAR EL SCRIPT
--sqlite3 python_db.db < Database00.sql
