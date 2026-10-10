"""Capturas del sitio con Playwright y el Chrome instalado.

Uso (con el servidor local andando: python -m http.server 8802 --bind 127.0.0.1):

    python docs/herramientas/capturas.py --out docs/auditoria/movil --prefijo 01-movil-390 --ancho 390 --alto 844 --partes
    python docs/herramientas/capturas.py --out docs/auditoria/movil --prefijo 02-menu-abierto --ancho 360 --alto 740 --clic "[data-menu-boton]"
    python docs/herramientas/capturas.py --out docs/auditoria/compu --prefijo 10-compu-1366 --ancho 1366 --alto 768 --completa

Opciones:
    --partes        una captura por pantallazo, bajando de a un alto de ventana (parte1, parte2...)
    --completa      una sola captura de la página entera
    --clic SELECTOR hace clic en el selector antes de capturar (por ejemplo, abrir el menú)
    --scroll Y      baja Y px antes de capturar (para ver el botón fijo a mitad de página)
    --tab N         aprieta Tab N veces antes de capturar (para ver el foco)
    --reducido      emula prefers-reduced-motion: reduce
    --dpr N         densidad de píxeles (por defecto 1; usar 2 o 3 para ver detalle)

Ejecutar con python sin -I: Playwright está en el site-packages del usuario.
"""
import argparse
import os

from playwright.sync_api import sync_playwright


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://127.0.0.1:8802/")
    ap.add_argument("--out", required=True)
    ap.add_argument("--prefijo", required=True)
    ap.add_argument("--ancho", type=int, default=390)
    ap.add_argument("--alto", type=int, default=844)
    ap.add_argument("--dpr", type=float, default=1)
    ap.add_argument("--partes", action="store_true")
    ap.add_argument("--completa", action="store_true")
    ap.add_argument("--clic")
    ap.add_argument("--scroll", type=int, default=0)
    ap.add_argument("--tab", type=int, default=0)
    ap.add_argument("--reducido", action="store_true")
    ap.add_argument("--calidad", type=int, default=80)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    movil = a.ancho < 900
    with sync_playwright() as p:
        nav = p.chromium.launch(channel="chrome", headless=True)
        ctx = nav.new_context(
            viewport={"width": a.ancho, "height": a.alto},
            device_scale_factor=a.dpr,
            is_mobile=movil,
            has_touch=movil,
            locale="es-AR",
            reduced_motion="reduce" if a.reducido else "no-preference",
        )
        pag = ctx.new_page()
        pag.goto(a.url, wait_until="networkidle")
        # cargar las imágenes diferidas antes de capturar
        pag.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
        pag.wait_for_load_state("networkidle")
        pag.evaluate("document.fonts.ready")
        if a.scroll:
            pag.evaluate(f"window.scrollTo(0, {a.scroll})")
            pag.wait_for_timeout(300)
        if a.clic:
            pag.click(a.clic)
            pag.wait_for_timeout(400)
        for _ in range(a.tab):
            pag.keyboard.press("Tab")
        if a.tab:
            pag.wait_for_timeout(200)

        def guardar(nombre, **kw):
            ruta = os.path.join(a.out, nombre + ".jpg")
            pag.screenshot(path=ruta, type="jpeg", quality=a.calidad, **kw)
            print(ruta)

        if a.completa:
            guardar(a.prefijo, full_page=True)
        elif a.partes:
            alto_total = pag.evaluate("document.documentElement.scrollHeight")
            y, n = 0, 1
            while y < alto_total:
                pag.evaluate(f"window.scrollTo(0, {y})")
                pag.wait_for_timeout(250)
                guardar(f"{a.prefijo}-parte{n}")
                y += a.alto
                n += 1
        else:
            guardar(a.prefijo)
        nav.close()


if __name__ == "__main__":
    main()
