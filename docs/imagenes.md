# Imágenes del sitio

09/10/2026 · tratamiento hecho con Codex CLI (`codex exec`), revisado a mano después de cada pasada.

**Ninguna imagen es generada.** Las fotos son fotogramas reales de los reels de Instagram de Espacio Funcional 25, solo recortados y con corrección de color. No hay inpainting, ni personas u objetos borrados o agregados, ni fondos nuevos, ni ampliaciones: ninguna salida es más grande que su recorte. El logo es el PNG original, solo recortado y achicado. La imagen para compartir (`og.jpg`) es una composición: el logo real, texto con las fuentes del sitio, una foto real y formas planas (cinta, chevrones y rombos).

Este documento reemplaza el contrato de imágenes de la sección 9 de `docs/plan.md` (plan v0), que quedó viejo con el rediseño.

## Cómo se rehacen

Desde la raíz del repo:

```
python docs/herramientas/imagenes.py todo     # o: fotos | logo | og
```

- Python 3.14 con Pillow 12.1.1, numpy y opencv (`cv2`). No usa internet.
- Lee los fotogramas de `docs/fotos-instagram/fotogramas-reels/` (solo en local, fuera de git) y el logo de `C:\Users\Juan\Documents\espacio-funcional-25\logo-espacio-funcional-25.png`. No modifica ningún original.
- Escribe solo en `assets/img/` y `favicon.ico`. Imprime las medidas, los pesos y los valores de color de cada foto.
- Es reproducible: al final se volvió a correr `todo` y los 22 archivos (21 en `assets/img/` más `favicon.ico`) salieron idénticos byte por byte a los anteriores (comparados por md5).

## Fotos

| Nombre | Fotograma de origen | Caja final (x0, y0, x1, y1) | Recorte | Salidas | Peso |
|---|---|---|---|---|---|
| portada-movil | `2026-07-28_DbUtD7_j4uj_f018s.jpg` | (0, 209, 716, 746) | 716×537 (4:3) | `portada-movil-400.webp` 400×300 · `portada-movil-716.webp` 716×537 | 11,8 · 20,0 KB |
| portada-compu | `2026-07-28_DbUtD7_j4uj_f018s.jpg` | (72, 170, 712, 970) | 640×800 (4:5) | `portada-compu-480.webp` 480×600 · `portada-compu-640.webp` 640×800 | 18,6 · 23,8 KB |
| clase | `2026-04-02_DWpl7tBNP0R_f004s.jpg` | (40, 366, 608, 792) | 568×426 (4:3) | `clase-400.webp` 400×300 · `clase-568.webp` 568×426 | 10,8 · 15,1 KB |
| profe | `2026-07-28_DbUtD7_j4uj_f024s.jpg` | (120, 200, 716, 945) | 596×745 (4:5) | `profe-400.webp` 400×500 · `profe-596.webp` 596×745 | 11,6 · 17,1 KB |
| avatar | `2026-07-30_Dbbmv_gCadM_f016s.jpg` | (235, 0, 535, 300) | 300×300 | `avatar-104.webp` 104×104 · `avatar-156.webp` 156×156 | 2,3 · 3,3 KB |
| donde | `2026-02-06_DUa7Xy0DthX_f024s.jpg` | (0, 250, 716, 698) | 716×448 (16:10) | `donde-400.webp` 400×250 · `donde-716.webp` 716×448 | 8,4 · 15,0 KB |

KB = 1024 bytes. Todas muy por debajo de los topes (60 KB las de 400 px, 120 KB las grandes).

**Cajas que cambiaron respecto de las pedidas** (todas con la misma proporción):

- **portada-movil:** pedida (0, 230, 716, 767). Abajo a la izquierda asomaban unos 20 px de la cabeza de una alumna acostada en el piso (empieza en y ≈ 747). Se subió 21 px: termina en 746. Los pies de los dos de pie terminan en y ≈ 735, así que quedan enteros. La marca de agua de arriba termina en y ≈ 168: no entra.
- **portada-compu:** pedida (60, 172, 700, 972). El borde negro del subtítulo quemado ("y licenciado en alto rendimiento") empieza en y = 971, así que la caja termina en 970 (subió 2 px). Codex además la corrió 12 px a la derecha para que no asomara en el borde izquierdo un mechón de la alumna acostada.
- **clase:** pedida (40, 330, 716, 837), 676×507. El reel tiene salpicaduras de puntitos blancos agregadas en la edición: arriba a la izquierda (las grandes en x 48-73, y 315-363, y otras chicas en x < 30 hasta y ≈ 425) y abajo a la derecha (x > 590, y > 785). Con 676×507 no hay ninguna caja que esquive las dos a la vez, y borrarlas sería retocar la foto. Por eso el recorte quedó más chico, 568×426, siempre 4:3: arranca debajo de las salpicaduras grandes, sin cortar la cabeza del alumno del TRX (empieza en y ≈ 392), y termina antes de las de abajo a la derecha. Las salidas son `clase-400` y `clase-568` (no hay `clase-676`). El brillo chico en (36-42, 401-405) es real: es del brazo o la mancuerna de la alumna de la izquierda.
- **profe, avatar y donde:** sin cambios. No tienen marca de agua, subtítulos, franja naranja ni salpicaduras adentro.

### Corrección de color

La misma receta y los mismos parámetros para las seis, para que se vean como una serie. Lo único que se mide en cada foto, con la misma regla, es el balance de blancos y los niveles.

1. **Recorte** del fotograma a tamaño original, sin reescalar.
2. **Balance de blancos** con las paredes y el techo blancos: píxeles entre los percentiles 60 y 98 de luminancia y con croma Lab ≤ 10. Se calculan las ganancias por canal que los vuelven neutros, se limitan a ±8 % y se aplican al 70 %. No se fuerza el piso a gris: es verde grisáceo de verdad y sigue así.
3. **Calidez** leve: b* +2 en Lab.
4. **Niveles sobre L\*** (Lab), sin tocar a* ni b*, así no cambian la saturación ni el matiz. El percentil 0,5 de L* va a L* 4 (≈ sRGB 12) y el percentil 99,7 va a L* 95 (≈ sRGB 242). La escala queda entre 1,00 y 1,25: nunca comprime el rango y no estira de más.
5. **Curva S suave** sobre L*, con fuerza 0,25.
6. **Saturación** sin cambios.
7. **Reducción** con Lanczos desde la foto ya corregida, cada tamaño por separado.
8. **Nitidez** después de reducir: `UnsharpMask(radius=1, percent=50, threshold=3)` en las reducidas y `percent=40` en las de tamaño original. El umbral evita realzar el ruido y los bloques de compresión del video. No se ven halos con zoom.
9. **WebP** `quality=80, method=6`, RGB, sin metadatos.

| Foto | Ganancias R/G/B aplicadas | Niveles L* (lo → hi, escala) | Luminancia p1 / p50 / p99, antes → después |
|---|---|---|---|
| portada-movil | 0,981 / 1,009 / 1,010 | 3,6 → 99,6, ×1,00 | 13 / 95 / 211 → 13 / 95 / 217 |
| portada-compu | 0,994 / 0,999 / 1,007 | 3,6 → 99,5, ×1,00 | 14 / 100 / 195 → 14 / 99 / 201 |
| clase | 0,986 / 1,000 / 1,013 | 10,6 → 81,3, ×1,25 | 30 / 137 / 200 → 14 / 152 / 232 |
| profe | 0,976 / 1,022 / 1,002 | 3,5 → 86,7, ×1,09 | 14 / 118 / 211 → 14 / 134 / 238 |
| avatar | 0,996 / 1,007 / 0,997 | 2,0 → 81,1, ×1,15 | 8 / 119 / 193 → 11 / 146 / 242 |
| donde | 0,984 / 0,995 / 1,022 | 18,6 → 87,4, ×1,25 | 47 / 174 / 215 → 15 / 172 / 223 |

Qué se ve: las portadas casi no cambian (ya tenían negros profundos y las luces del techo al máximo). En clase, profe y avatar las paredes pasan de gris (~200) a blanco sin quemarse. En donde se va la neblina: el negro pasa de 47 a 15. A la pared del profe se le saca casi todo el tinte rosado (a* 6,5 → 3,2). El piso sigue verde grisáceo (en clase, a* −6,8 → −7,2). Las pieles quedan naturales, ni naranjas ni verdes. En las portadas, bajo los tubos, siguen un poco rosadas (matiz Lab ~31-35°): es la luz del lugar y no se corrigió localmente.

## Logo, favicon e íconos

Origen: `logo-espacio-funcional-25.png` (1197×1920, RGBA, fondo transparente). El logo ocupa la caja (194, 525, 1053, 1386), de 859×861. Se recorta (193, 525, 1054, 1386): es la misma caja con 1 px transparente de cada lado, así queda un cuadrado de 861×861 con el círculo centrado. Cada salida sale de ese cuadrado con **una sola** reducción Lanczos (con alfa premultiplicado, así el borde no queda oscuro). No se redibuja, no se retoca y no se le aplica nitidez. No hay SVG.

| Archivo | Medida | Formato | Peso | Uso |
|---|---|---|---|---|
| `assets/img/logo-72.webp` / `.png` | 72×72 | RGBA, WebP sin pérdida / PNG optimizado | 7,2 / 9,0 KB | pie (36 px, 2x) |
| `assets/img/logo-80.webp` / `.png` | 80×80 | ídem | 8,3 / 10,5 KB | encabezado (40 px, 2x) |
| `assets/img/logo-120.webp` / `.png` | 120×120 | ídem | 15,6 / 19,6 KB | encabezado 3x |
| `favicon.ico` (raíz) | 16, 32 y 48 | ICO con alfa | 8,8 KB | pestaña |
| `assets/img/favicon-32.png` | 32×32 | PNG RGBA | 2,7 KB | `<link rel="icon" type="image/png">` |
| `assets/img/apple-touch-icon.png` | 180×180 | PNG RGB opaco | 24,6 KB | iPhone |

- `favicon.ico`: los tres tamaños se reducen por separado y se guardan juntos (la de 48 con `append_images` de 16 y 32). Así cada tamaño es el reducido con Lanczos y no un reescalado interno de Pillow. Al abrirlo de nuevo se comprobó que tiene 16, 32 y 48 con alfa y los mismos píxeles.
- `apple-touch-icon.png`: fondo blanco `#FFFFFF`, sin canal alfa, con el logo de 152×152 en (14, 14). Ocupa el 84 %.
- Revisado sobre blanco, negro, naranja y gris claro, ampliado: el círculo está entero y centrado, sin halo ni dientes, y el naranja del disco es #FF7B02. A 16 px el dibujo de adentro no se distingue (es el límite del tamaño), pero se lee el disco naranja con el anillo blanco.

## Imagen para compartir: `assets/img/og.jpg`

1200×630, JPEG con calidad 85, progresivo, RGB, sin metadatos. Pesa **78,7 KB** (tope: 200 KB).

| Elemento | Posición (x, y) | Medida | Detalle |
|---|---|---|---|
| Fondo | — | 1200×630 | blanco `#FFFFFF` |
| Logo | 64, 120 | 150×150 | del cuadrado de 861, con Lanczos |
| Título "Espacio Funcional 25" | 64, 298 | 615×67 | Barlow Semi Condensed Bold, **73 px** (no 76), `#17181A` |
| Bajada "Entrenamiento funcional en 25 de Mayo" | 64, 379 | 579×32 | Barlow Medium 34 px, `#3B3F45` |
| Cinta "Clase de prueba gratis" | 64, 447 | 390×62 | Barlow Semi Condensed Bold 40 px, `#17181A`, sobre `#FF7B02`, con 7 px de aire arriba y abajo y 15 a los costados, esquinas de 2 px, girada 1,6° en sentido antihorario (como `rotate(-1.6deg)` en CSS). Armada a 4x y achicada. |
| Foto | 720, 0 | 480×630 | la de portada-compu corregida (640×800). Se toma una ventana de 480×630 en (108, 65, 588, 695), a escala 1:1, sin reducir. Las dos personas entran enteras, de la cabeza a los pies. |
| Chevrones | 720, 612 | 480×18 | rayas "/" naranja `#FF7B02` y tinta `#17181A`, de 10 px de ancho en perpendicular, como el `--chevron` del CSS. Dibujadas a 4x. |
| Rombos | 400, 0 | 320×220 | rombos de 8 px cada 24 px en tresbolillo, naranja al 22 % como máximo. Se desvanecen hacia abajo y hacia la izquierda. No pasan por detrás de ningún texto ni del logo. |

- A 76 px el título mide 646 px y no entra en una línea con el margen de 64 y 40 px de aire hasta la foto. El script usa el tamaño más grande que entra, y quedó en 73.
- El texto se ubica con las métricas reales de la fuente. El borde izquierdo de las letras queda alineado con el del logo y el de la cinta.
- Revisada a tamaño completo y achicada a 400×210 (como se ve en WhatsApp): el título, la bajada y la cinta se leen y las dos personas se reconocen.

## Las llamadas a Codex

Todas con `codex exec --sandbox workspace-write -C .` desde la raíz del repo, con la instrucción por stdin y una imagen de referencia con `-i`. Cada instrucción decía qué archivos se podían escribir (solo el script y las salidas), que no se generara ni se rellenara nada y que no se hicieran commits.

1. **Fotos (primer intento, cortado).** A los dos minutos se frenó a mano, cuando Codex todavía estaba mirando los originales y no había escrito nada. La instrucción le permitía borrar con inpainting las salpicaduras de "clase", y eso va contra la regla de no retocar. Se relanzó con el recorte más chico.
2. **Fotos.** Crear `imagenes.py` con los subcomandos `fotos`, `logo`, `og` y `todo`, con las seis cajas medidas y la explicación de cada una (cabeza de la alumna acostada, subtítulo, marca de agua y salpicaduras). Receta de color común: balance de blancos con paredes y techo blancos, calidez leve, contraste suave, sin saturación extra y nitidez leve después de cada reducción. WebP con calidad 80 y método 6, y revisión visual. Codex corrió portada-compu 12 px por el mechón.
3. **Fotos, corrección de color.** Al revisar la primera pasada, el mapeo fijo de salida 10-248 levantaba los negros (la ropa negra quedaba gris) y "donde", "clase" y "profe" seguían lavadas. Se le pidió reemplazarlo por niveles por percentiles y una curva S suave sobre L*, sin tocar a* ni b*, sacar el recorte por canal después de la nitidez y medir la piel por el matiz Lab.
4. **Logo.** Cuadrado de 861 sin redibujar, Lanczos directo a cada tamaño, WebP sin pérdida y PNG, ICO con 16/32/48 reducidas por separado y apple-touch-icon opaco sobre blanco. Revisión sobre fondos claros y oscuros.
5. **OG.** Composición con Pillow según el diseño pedido: logo, título, bajada, cinta girada, foto a la derecha con chevrones y trama de rombos. Supermuestreo para los bordes, métricas reales de la fuente y revisión a 400×210.
6. **OG, encuadre.** La foto estaba reducida a 504×630 y las personas se veían chiquitas en la vista de WhatsApp. Se le pidió una ventana de 480×630 a escala 1:1, centrada en las dos personas.

Después de cada pasada se revisaron aparte las medidas, el modo, los pesos y los metadatos. También se miraron las imágenes enteras, con zoom en los bordes (cabezas, subtítulo, marca de agua, puntitos) y lado a lado con el original para el color. Antes de las pasadas de logo y OG se guardaron los md5, para confirmar que no cambiaban las salidas anteriores.
