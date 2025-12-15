# mini_turtle/__init__.py

# Importamos las funciones que queremos exponer desde el módulo de lógica
from .drawer_logic import adelante, abajo, reiniciar, resultado

# Definimos qué se exporta cuando alguien hace: from mini_turtle import *
__all__ = ['adelante', 'abajo', 'reiniciar', 'resultado']