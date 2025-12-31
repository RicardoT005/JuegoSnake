import pygame

# ------------------------------
# CONFIGURACIÓN DE AUDIO
# ------------------------------
VOLUMEN_MUSICA = 0.5
VOLUMEN_SONIDOS = 0.7

# ------------------------------
# VARIABLES DE SONIDO
# (se inicializan al cargar)
# ------------------------------
sonido_comer = None
sonido_choque = None
musica_fondo = None


def cargar_sonidos():
    """
    Carga todos los sonidos del juego.
    Este método debe llamarse una sola vez al iniciar el programa.
    """
    global sonido_comer, sonido_choque, musica_fondo

    try:
        sonido_comer = pygame.mixer.Sound("assets/sonidos/comer.wav")
        sonido_choque = pygame.mixer.Sound("assets/sonidos/choque.wav")

        sonido_comer.set_volume(VOLUMEN_SONIDOS)
        sonido_choque.set_volume(VOLUMEN_SONIDOS)

    except Exception:
        sonido_comer = None
        sonido_choque = None


def reproducir_comer():
    if sonido_comer:
        sonido_comer.play()


def reproducir_choque():
    if sonido_choque:
        sonido_choque.play()

