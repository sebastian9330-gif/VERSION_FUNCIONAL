# mini_turtle/drawer_logic.py

     --- ESTADO GLOBAL (Variables) ---
     
      ANCHO = 50
      ALTO = 30
      # Creamos el canvas una sola vez al iniciar el módulo
      canvas = [[" " for _ in range(ANCHO)] for _ in range(ALTO)]
      
      # Posición inicial de la tortuga (x es la "posicion_x" del requerimiento)
      x = 0
      y = 0
    
    
    # --- FUNCIONES DE LÓGICA Y DIBUJO ---
    
    def resultado():
        """Imprime el estado actual del canvas."""
        for fila in canvas:
            print("".join(fila))
    
    def adelante(pasos):
        """Mueve la tortuga hacia adelante, dibujando un trazo horizontal."""
        global x, y, ANCHO
        # Aseguramos que la posición no se salga del canvas
        pasos = min(pasos, ANCHO - x - 1) 
    
        for i in range(pasos):
            canvas[y][x] = "-"     # linea horizontal
            x += 1                 # avanzar un paso
        
        if pasos > 0:
            canvas[y][x] = ">"         # flecha final
    
    def abajo(pasos):
        """Mueve la tortuga hacia abajo, dibujando un trazo vertical."""
        global x, y, ALTO
    
        # El punto de inicio del trazo vertical es la posición actual
        y_inicio = y
    
        for i in range(pasos):
            # Aseguramos que la posición no se salga del canvas
            if y_inicio + i >= ALTO - 1:
                break
            
            y_coordenada = y_inicio + i
            canvas[y_coordenada][x] = "|" 
        
        # Actualizar la posición y con el total de pasos
        y = y_inicio + pasos
        
        # Dibujar la flecha final
        if y < ALTO:
            canvas[y][x] = "v"
        
        # Ajuste: El código original hacía y += 1 dos veces después del bucle.
        # Lo he cambiado para que 'y' sea la posición final de la flecha 'v'.
        # Si quieres replicar el comportamiento exacto, puedes añadir `y += 1` extra.
    
    def reiniciar():
        """Resetea la posición X (horizontal) a 0."""
        global x
        x = 0
        print("\n--- Posición horizontal (x) reiniciada a 0 ---\n")
