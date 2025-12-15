# 🐢 mini-turtle-oo: Paquete Python Orientado a Objetos

Este repositorio contiene la implementación de un pequeño paquete Python (`mini_turtle_oo`) diseñado para simular una "tortuga" de dibujo básica en la terminal, refactorizando el diseño desde un enfoque funcional a un enfoque **Orientado a Objetos (POO)**.

El objetivo principal es demostrar:
1.  **Encapsulamiento:** El estado del dibujo (posición `x`, `y`, y el `canvas`) está completamente contenido dentro de la **Clase `Turtle`**.
2.  **Independencia de Instancia:** La capacidad de crear múltiples objetos `Turtle` (`t1`, `t2`, etc.) que operan y mantienen su propio estado de forma totalmente independiente.
3.  **Diseño Modular:** Separación clara entre la lógica del motor de dibujo (`turtle_class.py`) y la interfaz pública (`__init__.py`).

---

## 📦 Estructura del Proyecto

El paquete sigue una estructura estándar para módulos de Python:

```text
mini_turtle_oo_task/
├── mini_turtle_oo/             <-- Carpeta del paquete
│   ├── __init__.py             <-- Interfaz (Exporta la Clase Turtle)
│   └── turtle_class.py         <-- Lógica (Define la Clase Turtle)
├── main.py                     <-- Script de prueba (Utiliza los objetos Turtle)
└── pyproject.toml              <-- Metadatos para la instalación (Opcional)
