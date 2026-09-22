"""
Prototipo minimo de entorno -- Cierre de Unidad 2
Ingenieria de Software . Grupo 1359 / 1359A

Completen cada linea marcada con # COMPLETAR usando informacion real
de su sistema. No dejen texto de ejemplo ("prueba1", "dato1", etc.).
"""

import sqlite3

conexion = sqlite3.connect("prototipo.db")
cursor = conexion.cursor()

# COMPLETAR: nombren la tabla segun el objeto central de su sistema,
# y definan 3 o 4 columnas relevantes (ademas de id)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reportes_mantenimiento (
        id INTEGER PRIMARY KEY,
        edificio TEXT,
        descripcion TEXT,
        estado TEXT,
        prioridad TEXT
    )
""")

# COMPLETAR: inserten 3 registros de ejemplo con datos realistas de
# su propio sistema (no datos inventados tipo "prueba1", "prueba2")
cursor.executemany(
    "INSERT INTO reportes_mantenimiento (edificio, descripcion, estado, prioridad) VALUES (?, ?, ?, ?)",
    [
        ("Edificio A - Aula 102", "Proyector no enciende", "Pendiente", "Alta"),
        ("Biblioteca Central", "Fuga de agua en sanitario", "En proceso", "Alta"),
        ("Laboratorio 3", "Contacto eléctrico dañado", "Pendiente", "Media"),
        ("Cancha Polivalente", "Lámpara exterior fundida", "Resuelto", "Baja")
    ]
)

conexion.commit()

# Consulta 1: todos los registros
print("--- Todos los registros ---")
for fila in cursor.execute("SELECT * FROM reportes_mantenimiento"):
    print(fila)

# COMPLETAR: escriban una segunda consulta que filtre por alguna
# condicion relevante a su sistema (usen WHERE)
# Consulta 2: consulta filtrada (reportes pendientes de alta prioridad)
print("--- Consulta filtrada (Pendientes y Alta Prioridad) ---")
for fila in cursor.execute("SELECT * FROM reportes_mantenimiento WHERE estado = 'Pendiente' AND prioridad = 'Alta'"):
    print(fila)

conexion.close()
