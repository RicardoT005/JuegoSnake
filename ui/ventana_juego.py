import pygame
import random

from settings.graficos import (
    ANCHO_PANTALLA,
    ALTO_PANTALLA,
    TAM_BLOQUE,
    COLOR_FONDO,
    COLOR_SERPIENTE,
    COLOR_COMIDA,
    COLOR_TEXTO,
    FUENTE_NORMAL
)

from settings.controles import obtener_controles


class VentanaJuego:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.controles = obtener_controles()
        self.reiniciar_juego()

    def reiniciar_juego(self):
        self.direccion = "derecha"
        self.serpiente = [(200, 200), (180, 200), (160, 200)]
        self.comida = self.generar_comida()
        self.puntuacion = 0
        self.juego_terminado = False

    def generar_comida(self):
        x = random.randrange(0, ANCHO_PANTALLA, TAM_BLOQUE)
        y = random.randrange(0, ALTO_PANTALLA, TAM_BLOQUE)
        return (x, y)

    def manejar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:

            # Si el juego terminó
            if self.juego_terminado:
                if evento.key == pygame.K_r:
                    self.reiniciar_juego()
                elif evento.key == self.controles["pausa"]:
                    return "menu"
                return None

            # Controles normales
            if evento.key == self.controles["arriba"] and self.direccion != "abajo":
                self.direccion = "arriba"
            elif evento.key == self.controles["abajo"] and self.direccion != "arriba":
                self.direccion = "abajo"
            elif evento.key == self.controles["izquierda"] and self.direccion != "derecha":
                self.direccion = "izquierda"
            elif evento.key == self.controles["derecha"] and self.direccion != "izquierda":
                self.direccion = "derecha"
            elif evento.key == self.controles["pausa"]:
                return "menu"

        return None

    def actualizar(self):
        if self.juego_terminado:
            return

        cabeza_x, cabeza_y = self.serpiente[0]

        if self.direccion == "arriba":
            cabeza_y -= TAM_BLOQUE
        elif self.direccion == "abajo":
            cabeza_y += TAM_BLOQUE
        elif self.direccion == "izquierda":
            cabeza_x -= TAM_BLOQUE
        elif self.direccion == "derecha":
            cabeza_x += TAM_BLOQUE

        nueva_cabeza = (cabeza_x, cabeza_y)

        # Colisión con bordes
        if (
            cabeza_x < 0 or cabeza_x >= ANCHO_PANTALLA or
            cabeza_y < 0 or cabeza_y >= ALTO_PANTALLA
        ):
            self.juego_terminado = True
            return

        # Colisión con el cuerpo
        if nueva_cabeza in self.serpiente:
            self.juego_terminado = True
            return

        self.serpiente.insert(0, nueva_cabeza)

        if nueva_cabeza == self.comida:
            self.puntuacion += 1
            self.comida = self.generar_comida()
        else:
            self.serpiente.pop()

    def dibujar(self):
        self.pantalla.fill(COLOR_FONDO)

        for segmento in self.serpiente:
            pygame.draw.rect(
                self.pantalla,
                COLOR_SERPIENTE,
                (*segmento, TAM_BLOQUE, TAM_BLOQUE)
            )

        pygame.draw.rect(
            self.pantalla,
            COLOR_COMIDA,
            (*self.comida, TAM_BLOQUE, TAM_BLOQUE)
        )

        texto_puntos = FUENTE_NORMAL.render(
            f"Puntos: {self.puntuacion}", True, COLOR_TEXTO
        )
        self.pantalla.blit(texto_puntos, (10, 10))

        if self.juego_terminado:
            mensaje = FUENTE_NORMAL.render(
                "Perdiste | R = Reiniciar | ESC = Menú",
                True,
                COLOR_TEXTO
            )
            rect = mensaje.get_rect(
                center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2)
            )
            self.pantalla.blit(mensaje, rect)

