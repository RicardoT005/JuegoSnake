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

class VentanaMenu:
    def __init__(self, pantalla):
        self.pantalla = pantalla

        self.opciones = [
            ("JUGAR", "juego"),
            ("AJUSTES", "ajustes"),
            ("RÉCORDS", "record"),
            ("SALIR", "salir")
        ]

        self.opcion_seleccionada = 0

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones)

            elif evento.key == pygame.K_DOWN:
                self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones)

            elif evento.key == pygame.K_RETURN:
                return self.opciones[self.opcion_seleccionada][1]

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for i, rect in enumerate(self.obtener_rects_opciones()):
                    if rect.collidepoint(evento.pos):
                        return self.opciones[i][1]

        return None

    def actualizar(self):
        pass

    def dibujar(self):
        self.pantalla.fill(COLOR_FONDO)

        titulo = FUENTE_TITULO.render("SNAKE NEÓN", True, AZUL_NEON)
        rect_titulo = titulo.get_rect(center=(ANCHO_PANTALLA // 2, 120))
        self.pantalla.blit(titulo, rect_titulo)

        for i, (texto, _) in enumerate(self.opciones):
            color = AZUL_NEON if i == self.opcion_seleccionada else COLOR_TEXTO
            superficie_texto = FUENTE_NORMAL.render(texto, True, color)

            rect = superficie_texto.get_rect(
                center=(ANCHO_PANTALLA // 2, 260 + i * 60)
            )

            self.pantalla.blit(superficie_texto, rect)

    def obtener_rects_opciones(self):
        rects = []
        for i in range(len(self.opciones)):
            texto = FUENTE_NORMAL.render(self.opciones[i][0], True, COLOR_TEXTO)
            rect = texto.get_rect(
                center=(ANCHO_PANTALLA // 2, 260 + i * 60)
            )
            rects.append(rect)
        return rects
