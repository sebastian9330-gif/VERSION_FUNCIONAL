# main.py
from mini_turtle import adelante, abajo, reiniciar, resultado

print("Ejecutando prueba de escalera...")

# --- 1. Dibujar una escalera ---
# Escalón 1
adelante(5)
abajo(2)

# Escalón 2
adelante(5)
abajo(2)

# Escalón 3
adelante(5)
abajo(2)

print("\n--- Resultado de la Escalera ---")
resultado()

# --- 2. Probar la nueva funcionalidad: reiniciar() ---
reiniciar()

# --- 3. Dibujar algo nuevo desde cero (debe empezar desde la columna 0) ---
print("\nDibujando nueva línea tras reinicio (debe empezar en la columna 0):")
adelante(15)
abajo(1)
adelante(2)
resultado()
