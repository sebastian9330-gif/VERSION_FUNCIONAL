# ⚙️ mini-turtle-funcional: Paquete Python Modular y Funcional

Este repositorio contiene la primera versión del paquete Python (`mini_turtle`), diseñada para simular una "tortuga" de dibujo simple en la terminal.

El objetivo principal de este proyecto es demostrar los principios de **Modularidad** y **Separación de Responsabilidades** en el diseño de un paquete Python:

1.  **Lógica vs. Interfaz:** El código se divide claramente entre la lógica interna del motor de dibujo (`drawer_logic.py`) y la interfaz pública que usa el usuario (`__init__.py`).
2.  **Estado Controlado:** Se utiliza el concepto de **estado global** (la variable `posicion_x` y el `canvas`) para persistir la información del dibujo entre las llamadas a las funciones.
3.  **Encapsulamiento de Funciones:** El usuario solo interactúa con funciones limpias y directas (`adelante`, `abajo`, `reiniciar`), sin necesidad de conocer los detalles internos de la implementación.

---

## 📦 Estructura del Proyecto

El paquete sigue una estructura estándar para módulos de Python con foco en la separación del código:

```text
mini_turtle_task/
├── mini_turtle/             <-- Carpeta del paquete
│   ├── __init__.py          <-- La Interfaz (Expone las funciones al usuario)
│   └── drawer_logic.py      <-- La Lógica (Contiene el canvas y el estado global)
├── main.py                  <-- Script de prueba (Utiliza las funciones importadas)


