import json
import os

# ------------------------------
# RUTA DEL ARCHIVO DE DATOS
# ------------------------------
RUTA_DATOS = "datos_de_juego/datos.json"

# ------------------------------
# DATOS POR DEFECTO
# ------------------------------
DATOS_POR_DEFECTO = {
    "record": 0,
    "monedas": 0,
    "vidas": 3,
    "color_serpiente": "azul_neon",
    "controles": {},
    "volumen_musica": 0.5,
    "volumen_sonidos": 0.7
}


def cargar_datos():
    """
    Carga los datos del juego desde el archivo JSON.
    Si no existe, crea uno con valores por defecto.
    """
    if not os.path.exists(RUTA_DATOS):
        guardar_datos(DATOS_POR_DEFECTO)
        return DATOS_POR_DEFECTO.copy()

    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception:
        return DATOS_POR_DEFECTO.copy()


def guardar_datos(datos):
    """
    Guarda los datos del juego en el archivo JSON.
    """
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)


def actualizar_dato(clave, valor):
    """
    Actualiza un solo dato dentro del archivo.
    """
    datos = cargar_datos()
    datos[clave] = valor
    guardar_datos(datos)


def obtener_dato(clave):
    """
    Obtiene un valor específico del archivo de datos.
    """
    datos = cargar_datos()
    return datos.get(clave)
