import pygame

# ------------------------------
# CONFIGURACIÓN DE PANTALLA
# ------------------------------
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
FPS = 60

# ------------------------------
# COLORES (NEGRO Y AZUL NEÓN)
# ------------------------------
NEGRO = (0, 0, 0)
AZUL_NEON = (0, 180, 255)

COLOR_FONDO = NEGRO
COLOR_TEXTO = AZUL_NEON
COLOR_SERPIENTE = AZUL_NEON
COLOR_COMIDA = AZUL_NEON
COLOR_BORDES = AZUL_NEON

# ------------------------------
# TAMAÑOS Y ESCALA
# ------------------------------
TAM_BLOQUE = 20
GROSOR_BORDE = 2

# ------------------------------
# FUENTES
# ------------------------------
pygame.font.init()

FUENTE_TITULO = pygame.font.SysFont("arial", 48, bold=True)
FUENTE_NORMAL = pygame.font.SysFont("arial", 24)
FUENTE_PEQUENA = pygame.font.SysFont("arial", 18)
