import pygame

# ------------------------------
# CONTROLES POR DEFECTO
# ------------------------------
CONTROLES_POR_DEFECTO = {
    "arriba": pygame.K_w,
    "abajo": pygame.K_s,
    "izquierda": pygame.K_a,
    "derecha": pygame.K_d,
    "pausa": pygame.K_ESCAPE,
    "aceptar": pygame.K_RETURN
}

# ------------------------------
# CONTROLES ACTUALES
# (pueden ser modificados desde ajustes)
# ------------------------------
controles_actuales = CONTROLES_POR_DEFECTO.copy()


def obtener_controles():
    """
    Devuelve el diccionario de controles actuales.
    """
    return controles_actuales


def cambiar_control(accion, nueva_tecla):
    """
    Cambia la tecla asignada a una acción específica.
    """
    if accion in controles_actuales:
        controles_actuales[accion] = nueva_tecla


def restablecer_controles():
    """
    Restaura los controles a sus valores por defecto.
    """
    global controles_actuales
    controles_actuales = CONTROLES_POR_DEFECTO.copy()

