import pygame
import sys

from ui.ventana_menu import VentanaMenu
from ui.ventana_juego import VentanaJuego
from ui.ventana_ajustes import VentanaAjustes
from ui.ventana_record import VentanaRecord

from settings.graficos import (
    ANCHO_PANTALLA,
    ALTO_PANTALLA,
    FPS,
    COLOR_FONDO
)

def main():
    pygame.init()
    pygame.mixer.init()

    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Snake Neón")

    reloj = pygame.time.Clock()

    # Estados posibles: "menu", "juego", "ajustes", "record", "salir"
    estado_actual = "menu"

    ventana_menu = VentanaMenu(pantalla)
    ventana_juego = VentanaJuego(pantalla)
    ventana_ajustes = VentanaAjustes(pantalla)
    ventana_record = VentanaRecord(pantalla)

    ejecutando = True
    while ejecutando:
        reloj.tick(FPS)
        pantalla.fill(COLOR_FONDO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if estado_actual == "menu":
                resultado = ventana_menu.manejar_evento(evento)
                if resultado:
                    estado_actual = resultado

            elif estado_actual == "juego":
                resultado = ventana_juego.manejar_evento(evento)
                if resultado:
                    estado_actual = resultado

            elif estado_actual == "ajustes":
                resultado = ventana_ajustes.manejar_evento(evento)
                if resultado:
                    estado_actual = resultado

            elif estado_actual == "record":
                resultado = ventana_record.manejar_evento(evento)
                if resultado:
                    estado_actual = resultado

        if estado_actual == "menu":
            ventana_menu.actualizar()
            ventana_menu.dibujar()

        elif estado_actual == "juego":
            ventana_juego.actualizar()
            ventana_juego.dibujar()

        elif estado_actual == "ajustes":
            ventana_ajustes.actualizar()
            ventana_ajustes.dibujar()

        elif estado_actual == "record":
            ventana_record.actualizar()
            ventana_record.dibujar()

        elif estado_actual == "salir":
            ejecutando = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

