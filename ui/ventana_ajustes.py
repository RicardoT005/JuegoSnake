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


class VentanaAjustes:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.opciones = ["VOLVER"]
        self.opcion_seleccionada = 0

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                return "menu"
            elif evento.key == pygame.K_ESCAPE:
                return "menu"

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                rect = self.obtener_rect_volver()
                if rect.collidepoint(evento.pos):
                    return "menu"

        return None

    def actualizar(self):
        pass

    def dibujar(self):
        self.pantalla.fill(COLOR_FONDO)

        titulo = FUENTE_TITULO.render("AJUSTES", True, AZUL_NEON)
        rect_titulo = titulo.get_rect(center=(ANCHO_PANTALLA // 2, 120))
        self.pantalla.blit(titulo, rect_titulo)

        texto = FUENTE_NORMAL.render(
            "Configuración disponible próximamente", True, COLOR_TEXTO
        )
        rect_texto = texto.get_rect(center=(ANCHO_PANTALLA // 2, 260))
        self.pantalla.blit(texto, rect_texto)

        volver = FUENTE_NORMAL.render("VOLVER", True, AZUL_NEON)
        rect_volver = volver.get_rect(center=(ANCHO_PANTALLA // 2, 360))
        self.pantalla.blit(volver, rect_volver)

    def obtener_rect_volver(self):
        texto = FUENTE_NORMAL.render("VOLVER", True, COLOR_TEXTO)
        return texto.get_rect(center=(ANCHO_PANTALLA // 2, 360))
