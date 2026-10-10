"""Prepara las fotos, el logo y la composición OG de Espacio Funcional 25.

Desde la raíz: python docs/herramientas/imagenes.py fotos|logo|og|todo
Dependencias: Python 3, Pillow, numpy y opencv-python (cv2).
No genera contenido, no retoca objetos, no agranda ni modifica los originales.
"""

from __future__ import annotations

import argparse
from io import BytesIO
from math import ceil, sqrt
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, features


# Rutas de salida derivadas del script: el resultado no depende del directorio
# de ejecución. Solo se escribe en assets/img y en favicon.ico de la raíz.
RAIZ = Path(__file__).resolve().parents[2]
ORIGEN = RAIZ / "docs/fotos-instagram/fotogramas-reels"
DESTINO = RAIZ / "assets/img"
EXTENSION = ".webp"

# Original externo de solo lectura: nunca se modifica, redibuja ni retoca.
ORIGEN_LOGO = Path(
    r"C:\Users\Juan\Documents\espacio-funcional-25\logo-espacio-funcional-25.png"
)
LOGO_TAMANO_ORIGINAL = (1197, 1920)
LOGO_CAJA_ORIGINAL = (194, 525, 1053, 1386)
LOGO_CAJA_MAESTRO = (193, 525, 1054, 1386)
LOGO_TAMANO_MAESTRO = (861, 861)
LOGO_LADOS = (72, 80, 120)
FAVICON_LADOS = (16, 32, 48)
APPLE_LADO = 180
APPLE_LOGO_LADO = 152
APPLE_POSICION = (14, 14)

# Cajas PIL: derecha y abajo son límites EXCLUIDOS. Se conservan las seis
# cajas solicitadas salvo el traslado de 12 px de portada-compu explicado abajo;
# se comprobaron visualmente el original y los cuatro bordes de los recortes.
FOTOS = (
    {
        "nombre": "portada-movil",
        "archivo": "2026-07-28_DbUtD7_j4uj_f018s.jpg",
        "original": (716, 1274),
        # Fuera de la marca superior y de la cabeza que empieza hacia y=747;
        # se conservan los pies de las dos personas de pie.
        "caja": (0, 209, 716, 746),
        "recorte": (716, 537),
        "anchos": (400, 716),
    },
    {
        "nombre": "portada-compu",
        "archivo": "2026-07-28_DbUtD7_j4uj_f018s.jpg",
        "original": (716, 1274),
        # En (60, 170, 700, 970) quedaba un mechón de la persona acostada
        # hacia x=60..66. Se traslada 12 px a la derecha, sin cambiar 640 x 800.
        # El subtítulo y su contorno negro empiezan fuera del borde inferior.
        "caja": (72, 170, 712, 970),
        "recorte": (640, 800),
        "anchos": (480, 640),
    },
    {
        "nombre": "clase",
        "archivo": "2026-04-02_DWpl7tBNP0R_f004s.jpg",
        "original": (716, 1280),
        # Las salpicaduras decorativas quedan fuera SOLO por el recorte.
        # El brillo real del brazo/mancuerna en x=36..42, y=401..405 se conserva.
        # No hay máscaras de borrado, interpolación de objetos ni inpainting.
        "caja": (40, 366, 608, 792),
        "recorte": (568, 426),
        "anchos": (400, 568),
    },
    {
        "nombre": "profe",
        "archivo": "2026-07-28_DbUtD7_j4uj_f024s.jpg",
        "original": (716, 1274),
        "caja": (120, 200, 716, 945),
        "recorte": (596, 745),
        "anchos": (400, 596),
    },
    {
        "nombre": "avatar",
        "archivo": "2026-07-30_Dbbmv_gCadM_f016s.jpg",
        "original": (716, 1274),
        "caja": (235, 0, 535, 300),
        "recorte": (300, 300),
        # Excepción explícita a la salida a tamaño original: se pidieron
        # únicamente 104 y 156 px, ambas desde la corrección de 300 x 300.
        "anchos": (104, 156),
    },
    {
        "nombre": "donde",
        "archivo": "2026-02-06_DUa7Xy0DthX_f024s.jpg",
        "original": (716, 1274),
        # Se respeta 716 x 448: el 16:10 de la consigna es aproximado.
        "caja": (0, 250, 716, 698),
        "recorte": (716, 448),
        "anchos": (400, 716),
    },
)

# Misma receta para TODOS los recortes: balance y niveles se estiman con
# los mismos percentiles y límites, sin ajustes ni correcciones por zonas.
ESCALA_RGB = 255.0
PESOS_LUMINANCIA = np.array((0.2126, 0.7152, 0.0722), dtype=np.float32)
PERCENTILES_NEUTROS = (60.0, 98.0)
CROMA_NEUTRA_MAX = 10.0  # C*ab: evita tomar pieles u objetos de color como blancos.
MINIMO_NEUTROS = 1000   # Es preferible avisar a inventar un balance sin evidencia.
INTENSIDAD_BALANCE = 0.70
LIMITE_GANANCIAS = (0.92, 1.08)
CALIDEZ_B_LAB = 2.0    # Calidez sutil, sin sumar rojo a pieles que ya son rojizas.
PERCENTILES_NIVELES = (0.5, 99.7)
NEGRO_LAB = 4.0
BLANCO_LAB = 95.0
LIMITES_ESCALA = (1.00, 1.25)  # Nunca comprime el rango; limita la expansión.
FUERZA_CURVA_S = 0.25
PERCENTILES_LUMINANCIA = (1.0, 50.0, 99.0)
RANGO_P1_SALIDA = (8.0, 16.0)
EPSILON = 1e-6

# Nitidez DESPUÉS de cada reducción; el tamaño original recibe menos cantidad.
REESCALADO = Image.Resampling.LANCZOS
NITIDEZ_RADIO = 1.0
NITIDEZ_PORCENTAJE_REDUCIDA = 50
NITIDEZ_PORCENTAJE_ORIGINAL = 40
NITIDEZ_UMBRAL = 3

# WebP sin metadatos: se codifica desde una imagen RGB nueva y en memoria.
FORMATO = "WEBP"
CALIDAD_INICIAL = 80
CALIDAD_MINIMA = 70
METODO_WEBP = 6
WEBP_SIN_PERDIDA = False
ANCHO_SALIDA_CHICA = 400
KB_CHICAS = 60
KB_GRANDES = 120
BYTES_POR_KB = 1024

# Muestras de diagnóstico, en coordenadas del ORIGINAL: no son máscaras de
# corrección ni alteran el procesamiento. Se mide la mediana Lab de piel de
# cara/nariz/mejillas, evitando boca, pelo y ojos en lo posible. En clase la
# cara del chico está de espaldas: no se inventa una medición de piel facial.
MUESTRAS_PIEL = {
    "portada-movil": ((305, 387, 330, 413), (507, 442, 527, 463)),
    "portada-compu": ((305, 387, 330, 413), (507, 442, 527, 463)),
    "clase": (),
    "profe": ((350, 355, 410, 392),),
    "avatar": ((341, 157, 409, 202),),
    "donde": ((383, 424, 415, 450),),
}
# Zonas uniformes para el diagnóstico, también en coordenadas del original.
# Profe solo incluye un fragmento mínimo junto a la pelota; avatar no incluye
# piso. Se informa la falta de muestra fiable, sin medir otra superficie.
MUESTRAS_ENTORNO = {
    "portada-movil": {
        "techo": (420, 260, 460, 290), "piso": (135, 640, 185, 685),
    },
    "portada-compu": {
        "techo": (420, 260, 460, 290), "piso": (135, 640, 185, 685),
    },
    "clase": {
        "pared": (388, 406, 422, 466), "piso": (390, 656, 450, 701),
    },
    "profe": {"pared": (570, 360, 630, 415), "piso": None},
    "avatar": {"pared": (245, 10, 280, 40), "piso": None},
    "donde": {
        "pared": (525, 410, 605, 495), "piso": (595, 590, 655, 630),
    },
}


def leer_recorte(foto: dict) -> Image.Image:
    """Comprueba los límites para que PIL no rellene fuera del original."""
    with Image.open(ORIGEN / foto["archivo"]) as original:
        if original.size != foto["original"]:
            raise ValueError(f"Tamaño inesperado en {foto['archivo']}: {original.size}")
        izquierda, arriba, derecha, abajo = foto["caja"]
        if not (0 <= izquierda < derecha <= original.width
                and 0 <= arriba < abajo <= original.height):
            raise ValueError(f"Caja fuera del original: {foto['nombre']}")
        recorte = original.convert("RGB").crop(foto["caja"])
    if recorte.size != foto["recorte"]:
        raise ValueError(f"Tamaño de recorte inconsistente: {foto['nombre']}")
    if any(ancho <= 0 or ancho > recorte.width for ancho in foto["anchos"]):
        raise ValueError(f"No se permite agrandar: {foto['nombre']}")
    return recorte


def estimar_balance(rgb: np.ndarray) -> tuple[np.ndarray, np.ndarray, int]:
    """Busca blancos claros poco cromáticos, sin imponer que el piso sea gris."""
    luminancia = rgb @ PESOS_LUMINANCIA
    inferior, superior = np.percentile(luminancia, PERCENTILES_NEUTROS)
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
    croma = np.hypot(lab[:, :, 1], lab[:, :, 2])
    mascara = ((luminancia >= inferior) & (luminancia <= superior)
               & (croma <= CROMA_NEUTRA_MAX))
    cantidad = int(mascara.sum())
    if cantidad < MINIMO_NEUTROS:
        raise ValueError(f"Solo {cantidad} píxeles neutros: revisar el origen.")

    # Normalizar cada píxel por su media separa tinte de luminosidad; la
    # mediana reduce la influencia de reflejos y bloques de compresión.
    neutros = rgb[mascara]
    cromaticidad = neutros / np.maximum(neutros.mean(axis=1, keepdims=True), EPSILON)
    tinte = np.median(cromaticidad, axis=0)
    calculadas = 1.0 / np.maximum(tinte, EPSILON)
    calculadas /= calculadas.mean()
    limitadas = np.clip(calculadas, *LIMITE_GANANCIAS)
    # Se limita antes de mezclar: la corrección efectiva nunca supera ±5,6 %.
    aplicadas = 1.0 + INTENSIDAD_BALANCE * (limitadas - 1.0)
    return calculadas, aplicadas, cantidad


def corregir(recorte: Image.Image) -> tuple[
    Image.Image, np.ndarray, np.ndarray, int, tuple[float, float, float]
]:
    """Corrige una sola vez a resolución completa; no retoca ninguna zona."""
    rgb = np.asarray(recorte, dtype=np.float32) / ESCALA_RGB
    calculadas, aplicadas, cantidad = estimar_balance(rgb)
    equilibrada = np.clip(rgb * aplicadas, 0.0, 1.0).astype(np.float32)

    # Calidez perceptual leve en Lab; la saturación no recibe ningún aumento.
    lab = cv2.cvtColor(equilibrada, cv2.COLOR_RGB2LAB)
    lab[:, :, 2] += CALIDEZ_B_LAB

    # cv2 recibe RGB float32 0-1: L* está en 0-100, a* y b* tienen signo.
    # Los niveles y la curva solo cambian L*: se conservan a* y b* tras
    # el balance y la calidez, sin añadir saturación ni un piso fijo en RGB.
    luminosidad = lab[:, :, 0]
    lo, hi = (float(v) for v in np.percentile(luminosidad, PERCENTILES_NIVELES))
    escala = float(np.clip(
        (BLANCO_LAB - NEGRO_LAB) / max(hi - lo, EPSILON), *LIMITES_ESCALA,
    ))
    t = np.clip(NEGRO_LAB + (luminosidad - lo) * escala, 0.0, 100.0) / 100.0
    lab[:, :, 0] = 100.0 * (t + FUERZA_CURVA_S * (t - 0.5) * t * (1.0 - t))
    salida = np.clip(cv2.cvtColor(lab, cv2.COLOR_LAB2RGB), 0.0, 1.0)
    pixeles = np.rint(salida * ESCALA_RGB).astype(np.uint8)
    return Image.fromarray(pixeles), calculadas, aplicadas, cantidad, (lo, hi, escala)


def preparar_tamano(corregida: Image.Image, ancho: int) -> Image.Image:
    """Reduce siempre desde el máster corregido; luego aplica nitidez leve."""
    alto = round(corregida.height * ancho / corregida.width)
    if ancho > corregida.width or alto > corregida.height:
        raise ValueError("No se permite agrandar ninguna salida.")
    es_original = (ancho, alto) == corregida.size
    imagen = corregida.copy() if es_original else corregida.resize((ancho, alto), REESCALADO)
    porcentaje = (NITIDEZ_PORCENTAJE_ORIGINAL if es_original
                  else NITIDEZ_PORCENTAJE_REDUCIDA)
    imagen = imagen.filter(ImageFilter.UnsharpMask(
        radius=NITIDEZ_RADIO, percent=porcentaje, threshold=NITIDEZ_UMBRAL,
    ))
    # Crear una imagen desde píxeles descarta cualquier EXIF, ICC o XMP heredado.
    return Image.fromarray(np.asarray(imagen))


def codificar_webp(imagen: Image.Image) -> tuple[bytes, int, int]:
    """Solo baja la calidad del archivo que exceda su presupuesto de bytes."""
    limite_kb = KB_CHICAS if imagen.width <= ANCHO_SALIDA_CHICA else KB_GRANDES
    for calidad in range(CALIDAD_INICIAL, CALIDAD_MINIMA - 1, -1):
        with BytesIO() as memoria:
            imagen.save(memoria, format=FORMATO, quality=calidad, method=METODO_WEBP,
                        lossless=WEBP_SIN_PERDIDA)
            contenido = memoria.getvalue()
        if len(contenido) < limite_kb * BYTES_POR_KB:
            return contenido, calidad, limite_kb
    raise ValueError(f"La imagen {imagen.size} supera {limite_kb} KB incluso a calidad 70.")


def percentiles_luminancia(imagen: Image.Image) -> np.ndarray:
    """Misma medida sRGB 0-255 en originales, másteres y WebP decodificados."""
    luminancia = np.asarray(imagen, dtype=np.float32) @ PESOS_LUMINANCIA
    return np.percentile(luminancia, PERCENTILES_LUMINANCIA)


def medir_lab(foto: dict, imagen: Image.Image, caja: tuple[int, ...]) -> np.ndarray:
    """Mediana Lab de una muestra; adapta sus coordenadas al tamaño de salida."""
    x, y, _, _ = foto["caja"]
    l, t, r, b = caja
    ancho, alto = foto["recorte"]
    if not (0 <= l - x < r - x <= ancho and 0 <= t - y < b - y <= alto):
        raise ValueError(f"Muestra fuera del recorte: {foto['nombre']}, {caja}")
    sx, sy = imagen.width / ancho, imagen.height / alto
    local = (round((l - x) * sx), round((t - y) * sy),
             round((r - x) * sx), round((b - y) * sy))
    if local[0] >= local[2] or local[1] >= local[3]:
        raise ValueError(f"Muestra demasiado pequeña: {foto['nombre']}, {caja}")
    rgb = np.asarray(imagen.crop(local), dtype=np.float32) / ESCALA_RGB
    return np.median(cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB), axis=(0, 1))


def formatear(valores: np.ndarray) -> str:
    return "/".join(f"{v:.2f}" for v in valores)


def diagnosticar_entorno(foto: dict, antes: Image.Image, despues: Image.Image) -> None:
    """Solo informa pared/techo y piso; nunca usa las muestras para corregir."""
    for zona, caja in MUESTRAS_ENTORNO[foto["nombre"]].items():
        if caja is None:
            print(f"  {zona.capitalize()}: N/D (sin zona medible en este recorte).")
            continue
        inicial = medir_lab(foto, antes, caja)
        final = medir_lab(foto, despues, caja)
        print(f"  {zona.capitalize()}, caja original {caja}: "
              f"L*/a*/b* {formatear(inicial)} -> {formatear(final)}")


def diagnosticar_piel(foto: dict, antes: Image.Image, despues: Image.Image) -> None:
    """Informa Lab y h = atan2(b*, a*); no impone un color de piel ni lo retoca."""
    muestras = MUESTRAS_PIEL[foto["nombre"]]
    if not muestras:
        print("  Piel: N/D (sin muestra facial fiable en este recorte).")
    for numero, caja in enumerate(muestras, start=1):
        inicial = medir_lab(foto, antes, caja)
        final = medir_lab(foto, despues, caja)
        h_antes = float(np.degrees(np.arctan2(inicial[2], inicial[1])))
        h_despues = float(np.degrees(np.arctan2(final[2], final[1])))
        print(f"  Piel {numero}, caja original {caja}: "
              f"L*/a*/b* {formatear(inicial)} -> {formatear(final)}, "
              f"h {h_antes:.2f}° -> {h_despues:.2f}°")


def fotos() -> None:
    """Produce exactamente las variantes fotográficas declaradas y su tabla."""
    if not features.check("webp"):
        raise RuntimeError("Esta instalación de Pillow no admite WebP.")
    # Validar todos los originales antes de empezar a escribir las salidas.
    recortes = [(foto, leer_recorte(foto)) for foto in FOTOS]
    preparadas = []
    print("Balance RGB: calculado -> aplicado (70 %, límite previo ±8 %).")
    print(f"Niveles en L*: p0,5/p99,7, destino 4/95, s 1-1,25; S {FUERZA_CURVA_S:.2f}.")
    print("Luminancia sRGB 0-255: 0,2126 R + 0,7152 G + 0,0722 B; p1/p50/p99.")
    print("Lab: medianas L*/a*/b*; entorno y piel: original -> WebP de mayor tamaño.")
    print("Piel: h orientativo 40°-60°; <40° rosado, >65° amarillo/verde. Solo diagnóstico.")
    for foto, recorte in recortes:
        corregida, calculadas, aplicadas, cantidad, niveles = corregir(recorte)
        ganancias = lambda valores: "/".join(f"{v:.6f}" for v in valores)
        print(f"{foto['nombre']}: caja {foto['caja']}; neutros {cantidad}; "
              f"{ganancias(calculadas)} -> {ganancias(aplicadas)}")
        lo, hi, escala = niveles
        print(f"  lo={lo:.3f}; hi={hi:.3f}; s={escala:.3f}")
        print(f"  p1/p50/p99 original -> máster: {formatear(percentiles_luminancia(recorte))}"
              f" -> {formatear(percentiles_luminancia(corregida))}")
        for ancho in foto["anchos"]:
            imagen = preparar_tamano(corregida, ancho)
            contenido, calidad, limite_kb = codificar_webp(imagen)
            ruta = DESTINO / f"{foto['nombre']}-{ancho}{EXTENSION}"
            preparadas.append((ruta, imagen.size, contenido, calidad, limite_kb))
            with Image.open(BytesIO(contenido)) as webp:
                salida = webp.convert("RGB")
            percentiles = percentiles_luminancia(salida)
            print(f"  {ruta.name}: p1/p50/p99 {formatear(percentiles)}")
            if not RANGO_P1_SALIDA[0] <= percentiles[0] <= RANGO_P1_SALIDA[1]:
                print(f"  AVISO: p1 {percentiles[0]:.2f} fuera de 8-16 tras reducción, "
                      "nitidez y WebP; se conserva la receta común y la nitidez.")
            if ancho == max(foto["anchos"]):
                diagnosticar_entorno(foto, recorte, salida)
                diagnosticar_piel(foto, recorte, salida)

    # Las doce codificaciones ya están listas: no se dejan temporales en disco.
    DESTINO.mkdir(parents=True, exist_ok=True)
    for ruta, _, contenido, calidad, limite_kb in preparadas:
        ruta.write_bytes(contenido)
        if calidad != CALIDAD_INICIAL:
            print(f"AVISO: {ruta.name}: calidad {calidad} para quedar bajo {limite_kb} KB.")
    print("\nPesos en KB = 1024 bytes. WebP sin metadatos.")
    print(f"{'Archivo':<39} {'Ancho×alto':>11} {'KB':>9}")
    print("-" * 61)
    for ruta, (ancho, alto), contenido, _, _ in preparadas:
        relativa = ruta.relative_to(RAIZ).as_posix()
        print(f"{relativa:<39} {f'{ancho}×{alto}':>11} {len(contenido) / BYTES_POR_KB:>9.2f}")


def leer_maestro_logo() -> Image.Image:
    """Recorta el cuadrado exacto y comprueba sus márgenes transparentes."""
    with Image.open(ORIGEN_LOGO) as original:
        if original.size != LOGO_TAMANO_ORIGINAL or original.mode != "RGBA":
            raise ValueError(f"Logo inesperado: {original.size}, {original.mode}.")
        if original.getchannel("A").getbbox() != LOGO_CAJA_ORIGINAL:
            raise ValueError("La caja visible del logo cambió: revisar el original.")
        maestro = original.crop(LOGO_CAJA_MAESTRO)
    if maestro.size != LOGO_TAMANO_MAESTRO:
        raise ValueError(f"Maestro del logo inesperado: {maestro.size}.")
    alfa = maestro.getchannel("A")
    ancho, alto = maestro.size
    for caja in ((0, 0, 1, alto), (ancho - 1, 0, ancho, alto)):
        if alfa.crop(caja).getextrema() != (0, 0):
            raise ValueError("Las columnas laterales del maestro deben ser transparentes.")
    izquierda, arriba, derecha, abajo = alfa.getbbox()
    centro = ((izquierda + derecha) / 2, (arriba + abajo) / 2)
    if any(abs(valor - esperado) > 1
           for valor, esperado in zip(centro, (ancho / 2, alto / 2))):
        raise ValueError(f"Logo descentrado en el maestro: {centro}.")
    # Una imagen nueva desde los mismos píxeles descarta sRGB/EXIF/ICC/XMP.
    return Image.frombytes("RGBA", maestro.size, maestro.tobytes())


def codificar_logo(imagen: Image.Image, formato: str, **opciones) -> bytes:
    """Codifica en memoria; el procesamiento del logo no usa temporales."""
    with BytesIO() as memoria:
        imagen.save(memoria, format=formato, **opciones)
        return memoria.getvalue()


def comprobar_ico(ruta: Path, imagenes: dict[int, Image.Image]) -> None:
    """Reabre el ICO y exige los tres RGBA originales, píxel por píxel."""
    with Image.open(ruta) as icono:
        esperados = {(lado, lado) for lado in FAVICON_LADOS}
        if (icono.format != "ICO" or icono.ico.sizes() != esperados
                or len(icono.ico.entry) != len(FAVICON_LADOS)):
            raise ValueError("El ICO debe contener exactamente 16, 32 y 48 px.")
        for lado in FAVICON_LADOS:
            imagen = icono.ico.getimage((lado, lado))
            if (imagen.mode != "RGBA"
                    or imagen.getchannel("A").getextrema() != (0, 255)
                    or imagen.tobytes() != imagenes[lado].tobytes()):
                raise ValueError(f"El ICO de {lado} px perdió alfa o fue reescalado.")


def logo() -> None:
    """Produce los logos transparentes, el favicon y el icono opaco de Apple."""
    if not features.check("webp"):
        raise RuntimeError("Esta instalación de Pillow no admite WebP.")
    maestro = leer_maestro_logo()
    # Cada lado sale DIRECTAMENTE del maestro. Pillow premultiplica el alfa
    # al reducir RGBA con Lanczos; no se separan los canales ni se encadenan
    # reducciones. Sin UnsharpMask: se conserva el dibujo también a 16/32 px.
    lados = sorted({*LOGO_LADOS, *FAVICON_LADOS, APPLE_LOGO_LADO})
    reducidas = {
        lado: maestro.resize((lado, lado), Image.Resampling.LANCZOS)
        for lado in lados
    }
    preparadas = []
    for lado in LOGO_LADOS:
        for formato, extension, opciones in (
            ("WEBP", "webp", {"lossless": True, "method": 6}),
            ("PNG", "png", {"optimize": True}),
        ):
            contenido = codificar_logo(reducidas[lado], formato, **opciones)
            ruta = DESTINO / f"logo-{lado}.{extension}"
            preparadas.append((ruta, f"{lado}×{lado}", contenido))

    # Pillow 12 elige la imagen provista que coincide con cada tamaño.
    # Se entrega 48 como base y 16/32 en append_images: no hay reescalado
    # interno. El contenedor lleva tres PNG RGBA y se verifica al reabrirlo.
    contenido = codificar_logo(
        reducidas[48], "ICO", sizes=[(lado, lado) for lado in FAVICON_LADOS],
        append_images=[reducidas[16], reducidas[32]],
    )
    preparadas.append((RAIZ / "favicon.ico", "16/32/48", contenido))
    contenido = codificar_logo(reducidas[32], "PNG", optimize=True)
    preparadas.append((DESTINO / "favicon-32.png", "32×32", contenido))

    apple = Image.new("RGBA", (APPLE_LADO, APPLE_LADO), (255, 255, 255, 255))
    apple.alpha_composite(reducidas[APPLE_LOGO_LADO], dest=APPLE_POSICION)
    contenido = codificar_logo(apple.convert("RGB"), "PNG", optimize=True)
    preparadas.append((DESTINO / "apple-touch-icon.png", "180×180", contenido))

    DESTINO.mkdir(parents=True, exist_ok=True)
    for ruta, _, contenido in preparadas:
        ruta.write_bytes(contenido)
    comprobar_ico(RAIZ / "favicon.ico", reducidas)

    print(f"Logo: maestro {maestro.size}, caja {LOGO_CAJA_MAESTRO}; "
          "columnas laterales transparentes y centro verificados.")
    print("Lanczos directo en RGBA, sin retoques ni nitidez adicional.")
    print("ICO verificado: 16, 32 y 48 px con alfa y píxeles exactos.")
    print("Apple: RGB opaco, blanco; logo de 152×152 en (14, 14).")
    print("\nPesos en KB = 1024 bytes. WebP lossless y PNG sin metadatos.")
    print(f"{'Archivo':<39} {'Ancho×alto':>11} {'KB':>9}")
    print("-" * 61)
    for ruta, tamano, contenido in preparadas:
        relativa = ruta.relative_to(RAIZ).as_posix()
        print(f"{relativa:<39} {tamano:>11} {len(contenido) / BYTES_POR_KB:>9.2f}")


# Composición OG: solo fotografía y logo originales, TTF y geometría plana.
# Estas opciones son independientes de las recetas de fotos() y logo().
OG_TTF = Path(__file__).resolve().parent / "ttf"
OG_TAMANO = (1200, 630)
OG_X_FOTO = 720
OG_X_TEXTO = 64
OG_AIRE_FOTO = 40
OG_LOGO_LADO = 150
OG_SUPERMUESTREO = 4
OG_NARANJA = "#FF7B02"
OG_TINTA = "#17181A"
OG_TINTA_2 = "#3B3F45"
OG_BLANCO = "#FFFFFF"
OG_CALIDAD = 85
OG_LIMITE_BYTES = 200_000
OG_TITULO = "Espacio Funcional 25"
OG_BAJADA = "Entrenamiento funcional en 25 de Mayo"
OG_CINTA = "Clase de prueba gratis"


def texto_og(texto: str, fuente: ImageFont.FreeTypeFont, color: str) -> Image.Image:
    """Rasteriza con la línea base real y ajusta a la tinta visible del texto."""
    izquierda, arriba, derecha, abajo = fuente.getbbox(texto, anchor="ls")
    capa = Image.new("RGBA", (derecha - izquierda, abajo - arriba))
    ImageDraw.Draw(capa).text(
        (-izquierda, -arriba), texto, font=fuente, fill=color, anchor="ls",
    )
    # getbbox incluye el avance lateral de algunos glifos. El alfa permite
    # alinear las letras visibles (no ese espacio) exactamente en x=64.
    return capa.crop(capa.getchannel("A").getbbox())


def cinta_og() -> Image.Image:
    """Rótulo completo a 4×, inclinado 1,6° antihorario y reducido una vez."""
    escala = OG_SUPERMUESTREO
    fuente = ImageFont.truetype(
        str(OG_TTF / "BarlowSemiCondensed-Bold.ttf"), 40 * escala,
    )
    texto = texto_og(OG_CINTA, fuente, OG_TINTA)
    lateral, vertical = 15 * escala, 7 * escala
    ancho, alto = texto.width + 2 * lateral, texto.height + 2 * vertical
    capa = Image.new("RGBA", (ancho, alto))
    ImageDraw.Draw(capa).rounded_rectangle(
        (0, 0, ancho - 1, alto - 1), radius=2 * escala, fill=OG_NARANJA,
    )
    capa.alpha_composite(texto, dest=(lateral, vertical))
    capa = capa.rotate(1.6, resample=Image.Resampling.BICUBIC, expand=True)
    capa = capa.resize(
        (round(capa.width / escala), round(capa.height / escala)), REESCALADO,
    )
    return capa.crop(capa.getchannel("A").getbbox())


def chevrones_og(ancho: int) -> Image.Image:
    """Rayas / de 10 px perpendiculares: x+y constante, con bordes a 4×."""
    escala = OG_SUPERMUESTREO
    alto = 18
    capa = Image.new("RGB", (ancho * escala, alto * escala), OG_NARANJA)
    dibujo = ImageDraw.Draw(capa)
    paso = 10 * sqrt(2) * escala
    for numero in range(ceil((capa.width + capa.height) / paso)):
        inicio, fin = numero * paso, (numero + 1) * paso
        dibujo.polygon(
            ((inicio, 0), (fin, 0),
             (fin - capa.height, capa.height), (inicio - capa.height, capa.height)),
            fill=OG_NARANJA if numero % 2 == 0 else OG_TINTA,
        )
    return capa.resize((ancho, alto), REESCALADO)


def rombos_og(ancho: int, alto: int) -> Image.Image:
    """Tresbolillo de 8 px cada 24 px; alfa hasta 22 %, que se desvanece."""
    escala = OG_SUPERMUESTREO
    capa = Image.new("RGBA", (ancho * escala, alto * escala))
    dibujo = ImageDraw.Draw(capa)
    for fila, y in enumerate(range(0, alto, 24)):
        for x in range(12 * (fila % 2), ancho + 1, 24):
            horizontal, vertical = x / ancho, 1 - y / alto
            # Smoothstep evita saltos en ambos extremos de cada degradado.
            horizontal = horizontal ** 2 * (3 - 2 * horizontal)
            vertical = vertical ** 2 * (3 - 2 * vertical)
            alfa = round(255 * 0.22 * horizontal * vertical)
            dibujo.polygon(
                ((x * escala, (y - 4) * escala),
                 ((x + 4) * escala, y * escala),
                 (x * escala, (y + 4) * escala),
                 ((x - 4) * escala, y * escala)),
                fill=(255, 123, 2, alfa),
            )
    return capa.resize((ancho, alto), REESCALADO)


def og() -> None:
    """Compone la tarjeta de 1200×630 desde originales y fuentes reales."""
    foto = next(foto for foto in FOTOS if foto["nombre"] == "portada-compu")
    corregida, *_ = corregir(leer_recorte(foto))
    # Ventana 480×630 del maestro corregido, sin reescalar y con ambas personas enteras.
    # A este tamaño, preparar_tamano aplica NITIDEZ_PORCENTAJE_ORIGINAL.
    ancho_foto = OG_TAMANO[0] - OG_X_FOTO
    caja_foto = (108, 65, 588, 695)
    retrato = preparar_tamano(corregida.crop(caja_foto), ancho_foto)
    marca = leer_maestro_logo().resize((OG_LOGO_LADO, OG_LOGO_LADO), REESCALADO)

    ancho_texto = OG_X_FOTO - OG_AIRE_FOTO - OG_X_TEXTO
    for tamano_titulo in range(76, 67, -1):
        fuente = ImageFont.truetype(
            str(OG_TTF / "BarlowSemiCondensed-Bold.ttf"), tamano_titulo,
        )
        titulo = texto_og(OG_TITULO, fuente, OG_TINTA)
        if titulo.width <= ancho_texto:
            break
    else:
        raise ValueError("El título no entra en una línea a un mínimo de 68 px.")
    bajada = texto_og(
        OG_BAJADA,
        ImageFont.truetype(str(OG_TTF / "Barlow-Medium.ttf"), 34), OG_TINTA_2,
    )
    cinta = cinta_og()
    if max(bajada.width, cinta.width) > ancho_texto:
        raise ValueError("La bajada o la cinta invaden el aire junto a la foto.")

    # Separaciones medidas entre los límites visibles, incluidos los
    # descendentes de las letras y la caja completa de la cinta inclinada.
    alto_bloque = marca.height + 28 + titulo.height + 14 + bajada.height + 36 + cinta.height
    y_logo = (OG_TAMANO[1] - alto_bloque) // 2
    if y_logo < 64:
        raise ValueError("El bloque no respeta los márgenes verticales de 64 px.")
    y_titulo = y_logo + marca.height + 28
    y_bajada = y_titulo + titulo.height + 14
    y_cinta = y_bajada + bajada.height + 36

    lienzo = Image.new("RGBA", OG_TAMANO, OG_BLANCO)
    # La trama termina al menos 24 px antes del título y queda a la derecha
    # del logo: no se dibuja detrás de ninguna letra ni de la marca.
    trama = rombos_og(OG_X_FOTO - 400, min(220, y_titulo - 24))
    lienzo.alpha_composite(trama, dest=(400, 0))
    lienzo.paste(retrato, (OG_X_FOTO, 0))
    franja = chevrones_og(ancho_foto)
    lienzo.paste(franja, (OG_X_FOTO, OG_TAMANO[1] - franja.height))
    for elemento, y in ((marca, y_logo), (titulo, y_titulo),
                        (bajada, y_bajada), (cinta, y_cinta)):
        lienzo.alpha_composite(elemento, dest=(OG_X_TEXTO, y))

    # Imagen RGB nueva: sin EXIF, ICC, XMP ni comentarios heredados.
    rgb = Image.frombytes("RGB", lienzo.size, lienzo.convert("RGB").tobytes())
    with BytesIO() as memoria:
        rgb.save(memoria, format="JPEG", quality=OG_CALIDAD,
                 optimize=True, progressive=True, subsampling=2)
        contenido = memoria.getvalue()
    if len(contenido) >= OG_LIMITE_BYTES:
        raise ValueError("La composición OG supera el límite de 200 KB.")
    DESTINO.mkdir(parents=True, exist_ok=True)
    ruta = DESTINO / "og.jpg"
    ruta.write_bytes(contenido)

    print(f"Logo: ({OG_X_TEXTO}, {y_logo}), {marca.width}×{marca.height}, maestro de 861.")
    print(f"Título: ({OG_X_TEXTO}, {y_titulo}), {titulo.width}×{titulo.height}, "
          f"Barlow Semi Condensed Bold {tamano_titulo} px; "
          f"aire hasta foto {OG_X_FOTO - OG_X_TEXTO - titulo.width} px.")
    print(f"Bajada: ({OG_X_TEXTO}, {y_bajada}), {bajada.width}×{bajada.height}, "
          "Barlow Medium 34 px.")
    print(f"Cinta: ({OG_X_TEXTO}, {y_cinta}), {cinta.width}×{cinta.height}, "
          "Barlow Semi Condensed Bold 40 px; giro +1,6° en Pillow.")
    print(f"Foto: original {foto['caja']} -> {corregida.size} corregida -> "
          f"ventana {caja_foto} a escala 1:1; "
          f"({OG_X_FOTO}, 0), {retrato.width}×{retrato.height}.")
    print(f"Chevrones: ({OG_X_FOTO}, {OG_TAMANO[1] - franja.height}), "
          f"{franja.width}×{franja.height}; rombos: (400, 0), {trama.width}×{trama.height}.")
    print(f"{ruta.relative_to(RAIZ).as_posix()}: {rgb.width}×{rgb.height}, "
          f"RGB, JPEG {OG_CALIDAD}, progresivo 4:2:0, sin metadatos; "
          f"{len(contenido)} bytes ({len(contenido) / BYTES_POR_KB:.2f} KiB).")


def todo() -> None:
    fotos()
    logo()
    og()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subcomandos = parser.add_subparsers(dest="comando", required=True)
    for nombre, funcion in (("fotos", fotos), ("logo", logo), ("og", og), ("todo", todo)):
        subparser = subcomandos.add_parser(nombre, help=funcion.__doc__)
        subparser.set_defaults(funcion=funcion)
    argumentos = parser.parse_args()
    argumentos.funcion()


if __name__ == "__main__":
    main()
