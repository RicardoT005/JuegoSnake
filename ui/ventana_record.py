import pygame

from settings.graficos import (
    ANCHO_PANTALLA,
    ALTO_PANTALLA,
    COLOR_FONDO,
    COLOR_TEXTO,
    AZUL_NEON,
    FUENTE_TITULO,
    FUENTE_NORMAL
)

from datos_de_juego.almacenaje import obtener_dato


class VentanaRecord:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.record = obtener_dato("record") or 0

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                return "menu"

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                rect = self.obtener_rect_volver()
                if rect.collidepoint(evento.pos):
                    return "menu"

        return None

    def actualizar(self):
        # Recargar el récord por si cambió
        self.record = obtener_dato("record") or 0

    def dibujar(self):
        self.pantalla.fill(COLOR_FONDO)

        titulo = FUENTE_TITULO.render("RÉCORD", True, AZUL_NEON)
        rect_titulo = titulo.get_rect(center=(ANCHO_PANTALLA // 2, 120))
        self.pantalla.blit(titulo, rect_titulo)

        texto_record = FUENTE_NORMAL.render(
            f"Puntaje más alto: {self.record}", True, COLOR_TEXTO
        )
        rect_record = texto_record.get_rect(center=(ANCHO_PANTALLA // 2, 260))
        self.pantalla.blit(texto_record, rect_record)

        volver = FUENTE_NORMAL.render("VOLVER", True, AZUL_NEON)
        rect_volver = volver.get_rect(center=(ANCHO_PANTALLA // 2, 360))
        self.pantalla.blit(volver, rect_volver)

    def obtener_rect_volver(self):
        texto = FUENTE_NORMAL.render("VOLVER", True, COLOR_TEXTO)
        return texto.get_rect(center=(ANCHO_PANTALLA // 2, 360))
