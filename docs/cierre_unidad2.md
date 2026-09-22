# Cierre de Unidad 2 — Equipo de Mantenimiento Campus

**Sistema:** Sistema de reportes de mantenimiento para instalaciones universitarias
**Integrantes:** AAron Cruz San Juan
**Fecha:** 21 de septiembre de 2026

## 2.4 Propuesta de desarrollo

- **Alcance (qué incluye):** Registro de fallas en instalaciones, asignación de prioridades, seguimiento del estado de reparación y consulta filtrada de incidencias críticas.
- **Fuera de alcance (qué NO incluye):** Gestión de compras de repuestos, pago a proveedores externos ni facturación, ni asignación directa de personal técnico de mantenimiento.
- **Restricciones (tiempo, tecnología, tamaño del equipo):** Desarrollo de prototipo en un tiempo de 2 meses(proyecto total), utilizando Python 3, SQLite 3, tkinter y GitHub Codespaces.
- **Viabilidad en una frase:** Es altamente viable ya que aprovecha tecnologías ligeras y gratuitas para resolver la gestión centralizada de fallas universitarias.

## 2.5 Especificación funcional (mínimo 5 funciones)

| # | Función | Qué hace |
|---|---|---|
| 1 | Registrar reporte | Captura la ubicación de la falla, descripción, estado inicial y prioridad |
| 2 | Consultar todos los reportes | Muestra el listado completo de incidencias registradas en la base de datos |
| 3 | Filtrar incidencias críticas | Muestra únicamente los reportes con estado 'Pendiente' y prioridad 'Alta' |
| 4 | Actualizar estado de reporte | Cambia la condición de la incidencia (Pendiente, En proceso, Resuelto) |
| 5 | Borrar reporte | Elimina un registro de la base de datos seleccionándolo por su número de ID|

## 2.6 Entorno de desarrollo justificado

- **Evidencia técnica:** Prototipo funcional implementado en `prototipo_entorno.py` corriendo sobre Python 3.14.2 y SQLite 3.45.1.
- **Costo:** $0 USD (Utiliza software libre y el nivel gratuito de GitHub Codespaces).
- **Curva de aprendizaje:** Alto, debido a la sintaxis intuitiva de Python y el manejo básico del lenguaje SQL estándar.
- **Soporte / documentación disponible:** Documentación oficial extensa y activa para Python 3 y la librería estándar `sqlite3`.

## Declaración de uso de IA

| Herramienta | Para qué la usaron | Qué verificaron |
|---|---|---|
| Gemini AI | ayuda en la explicacion de codigo | Se verificó la correcta ejecución en la terminal y la coherencia del esquema con las instalaciones universitarias |