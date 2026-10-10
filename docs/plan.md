# Plan del sitio · Espacio Funcional 25

> **09/10/2026 23:20 · el diseño de este plan quedó descartado.** Pablo vio la maqueta y la rechazó (todo naranja, bordes negros gruesos, tipografía condensada enorme). El diseño aprobado es el de `docs/diseno/` (maqueta con lorem ipsum) y está descripto en `docs/diseno.md`. De este plan siguen valiendo: el copy (sección 6, con los cambios que figuran en `docs/diseno.md`), los datos (7), el SEO local (8) y las preguntas (12). Las secciones 2 a 5, 9 (contrato de imágenes) y 10 quedan solo como registro.

09/10/2026 22:15 · plan de diseño y copy cerrado, listo para construir · sigue: construcción (HTML, CSS y JS en paralelo con el tratamiento de imágenes con Codex CLI)

Este documento alcanza para construir el sitio sin decidir nada importante. Fuentes: `PROMPT-SITIO.md` (brief), `TAREAS.md` (datos, valen siempre), `docs/relevamiento/fuentes.md`, `docs/relevamiento/referencias.md` y `docs/fotos-instagram/INDICE.md`. Se abrieron en tamaño completo los 12 fotogramas candidatos y el retrato de 2022, se probaron los recortes y la corrección de color con Pillow, y se armó una maqueta descartable del encabezado, la portada y el circuito (en el scratchpad, no en el sitio) para medir en 360×740, 390×844 y 1366×768. Los números de este plan salen de esas mediciones.

Reglas que valen para todo el sitio:

- Los datos (turnos, cuota, plan complemento, dirección, teléfono) son los de la sección "Datos del negocio" de `TAREAS.md`. Si algo de acá no coincide, vale `TAREAS.md`.
- Nada inventado: ni testimonios, ni cantidad de alumnos, ni años de experiencia, ni resultados, ni tiempos de trabajo por estación.
- Texto en español rioplatense, con voseo. El copy de la sección 6 es final: se copia palabra por palabra.
- No se copia nada de `Documents/espacio-funcional-25/` al sitio, salvo el logo.

---

## 1. Tesis

**Sujeto:** Espacio Funcional 25, el espacio de entrenamiento funcional del Prof. Nicolás Guido Valle en el Cuartel de Bomberos de 25 de Mayo: clases de una hora en estaciones, en grupos de máximo 7.
**Público:** gente de 25 de Mayo de todas las edades (incluye gente que arranca de cero y mayores de 50), que abre el link desde el celular, desde el Instagram o desde un WhatsApp que le pasaron.
**El único trabajo de la página:** que en el primer pantallazo se entienda qué es, dónde queda, cuánto sale y cuándo hay clase, y que la persona toque "Reservá tu clase de prueba gratis" y le escriba a Nicolás por WhatsApp.
**La firma:** la clase dibujada como una pista cerrada, con cinco estaciones marcadas con el rombo de señal de tránsito del logo (sentadillas, empujes, tracciones, core, aeróbico), sobre un campo naranja de alta visibilidad, y la vuelta que vuelve a empezar. Así se ve por qué el esfuerzo se sostiene: cada estación cambia el movimiento.

### Autocrítica contra los defaults

Lo que saldría para cualquier gimnasio: portada negra con una foto oscura de fondo y un eslogan en mayúsculas encima, tres tarjetas con íconos ("Funcional", "HIIT", "Fuerza"), tarjetas de precios con "Más popular", contadores, carrusel de testimonios y formulario. Cinco de los diez sitios relevados son eso, en negro con un color fuerte. Contra los tres defaults de diseño generado:

- **Fondo crema con serif:** no. El fondo claro es blanco puro (el del anillo del logo) y la tipografía es de cartel, sin serif.
- **Negro con un acento flúor:** no. El campo grande es naranja con texto negro, como una señal o un chaleco de bombero. El negro solo va en botones, bordes y el pie.
- **Diario con filetes finos y cero radio:** no. Los bordes son gruesos (3 y 5 px, como el borde de una señal) y las esquinas, apenas redondeadas (6 px, como las del rombo del logo).

Qué cambié después de compararlo con eso:

1. **El circuito.** Primero lo pensé como una matriz de "qué trabaja cada estación". Lo descarté porque daba una diagonal obvia que no dice nada más que "son cinco cosas distintas". También descarté las fotos o los pictogramas por estación: los pictogramas serían decoración dibujada a mano y las fotos sumaban caras de alumnos y peso. Quedó la pista, con el verbo cotidiano que usa Nicolás para cada patrón (levantar, empujar, tirar, estabilizar) y el material que se ve en sus videos.
2. **La portada.** No hay foto de fondo con texto encima. El texto va primero, sobre naranja, y la foto real abajo, sin texto encima.
3. **Las secciones no llevan etiquetas encima del título.** El título de cada sección es su nombre en el menú.
4. **El mapa.** Saqué el mapa embebido: es peso y todo el pueblo conoce el cuartel. Queda el botón "Cómo llegar".
5. **La tipografía.** Uso un solo peso de la de cartel (800), para gastar la audacia en un lugar.
6. **La barra fija de WhatsApp** se oculta mientras se ve otro botón de reserva, para no tener tres botones iguales en la misma pantalla.

---

## 2. Tokens de diseño

### Paleta

| Nombre | Hex | Uso |
|---|---|---|
| Naranja señal | `#FF7B02` | El del logo (moda de los píxeles opacos, medido). Campo grande: encabezado, portada, "Cómo es la clase", "Clase de prueba", barra fija. Banda chica de "la clase de prueba es gratis". |
| Negro | `#000000` | El del logo. Todo el texto sobre naranja y sobre blanco, bordes, rombos, botones, fondo del pie. |
| Blanco | `#FFFFFF` | El del anillo del logo. Fondo de "El enfoque" y "Turnos y cuota". Texto de los botones negros y del pie. |
| Cal | `#F2F2F2` | Fondo de "El profe", para separarla de "Turnos y cuota" sin poner otro color. Es gris neutro, no crema. |
| Gris | `#545454` | La frase "lo fácil" de El enfoque y las notas chicas sobre blanco o cal. Nunca sobre naranja. |
| Gris del pie | `#BDBDBD` | Texto secundario sobre negro, en el pie. |
| Negro de hover | `#2B2B2B` | Fondo del botón negro cuando se pasa el mouse. |

Prohibido, por contraste: texto blanco sobre naranja, texto naranja sobre blanco y gris sobre naranja.

### Contraste (WCAG 2.x, calculado con script)

Calculado con `docs/herramientas/contraste.py` (luminancia relativa de WCAG 2.x); se puede volver a correr en la auditoría. AA pide 4,5:1 para texto y 3:1 para texto grande y bordes de controles.

| Texto o elemento | Fondo | Ratio | Nivel | Dónde |
|---|---|---|---|---|
| `#000000` | `#FF7B02` | 8,09:1 | AAA | Todo el texto sobre naranja. También los bordes, rombos, botones negros y el contorno de foco sobre naranja. |
| `#000000` | `#FFFFFF` | 21,00:1 | AAA | Texto en El enfoque, Turnos y cuota y el menú abierto. |
| `#000000` | `#F2F2F2` | 18,76:1 | AAA | Texto en El profe. |
| `#545454` | `#FFFFFF` | 7,57:1 | AAA | Frase "lo fácil" y notas sobre blanco. |
| `#545454` | `#F2F2F2` | 6,76:1 | AA | Notas sobre cal. |
| `#FFFFFF` | `#000000` | 21,00:1 | AAA | Texto de botones negros y del pie. |
| `#FFFFFF` | `#2B2B2B` | 14,16:1 | AAA | Texto del botón negro en hover. |
| `#2B2B2B` (botón en hover) | `#FF7B02` | 5,45:1 | AA (borde de control) | El botón en hover sigue recortándose del naranja. |
| `#FF7B02` (logo, detalles) | `#000000` | 8,09:1 | AAA | Logo en el pie y foco de la barra. |
| `#BDBDBD` | `#000000` | 11,18:1 | AAA | Texto secundario del pie. |
| `#FFFFFF` (contorno de foco) | `#000000` | 21,00:1 | AAA | Foco dentro de la barra negra y en el pie. |
| `#FFFFFF` | `#FF7B02` | 2,60:1 | **No pasa** | No se usa para texto. |
| `#FF7B02` | `#FFFFFF` | 2,60:1 | **No pasa** | No se usa para texto ni para bordes de controles. |

No hay texto encima de fotos.

### Tipografías

| Rol | Familia | Pesos | Archivo en `assets/fonts/` | Peso del archivo |
|---|---|---|---|---|
| Titulares, números (horarios, precio, el 7), estaciones, logotipo de texto | **Big Shoulders Display** | 800 | `big-shoulders-display-latin-800-normal.woff2` | 14.556 B |
| Texto, botones, etiquetas, menú, notas | **Atkinson Hyperlegible Next** | 400 y 700 | `atkinson-hyperlegible-next-latin-400-normal.woff2`, `atkinson-hyperlegible-next-latin-700-normal.woff2` | 12.096 B y 12.732 B |

Total de fuentes: 39,4 KB. No hay itálicas: el texto no las necesita.

**De dónde se bajan** (paquetes `@fontsource` 5.3.0, publicados el 19/07/2026, licencia OFL-1.1; versión fija):

```
https://cdn.jsdelivr.net/npm/@fontsource/big-shoulders-display@5.3.0/files/big-shoulders-display-latin-800-normal.woff2
https://cdn.jsdelivr.net/npm/@fontsource/atkinson-hyperlegible-next@5.3.0/files/atkinson-hyperlegible-next-latin-400-normal.woff2
https://cdn.jsdelivr.net/npm/@fontsource/atkinson-hyperlegible-next@5.3.0/files/atkinson-hyperlegible-next-latin-700-normal.woff2
```

**Licencias** (texto completo de la OFL con el copyright correcto, del repo de Google Fonts):

```
https://raw.githubusercontent.com/google/fonts/main/ofl/bigshouldersdisplay/OFL.txt   → assets/fonts/LICENSE-big-shoulders-display.txt
https://raw.githubusercontent.com/google/fonts/main/ofl/atkinsonhyperlegiblenext/OFL.txt → assets/fonts/LICENSE-atkinson-hyperlegible-next.txt
```

Se usa el `OFL.txt` de google/fonts y no el `LICENSE` de fontsource, porque el de Big Shoulders en fontsource arranca con "Google Inc." en vez del copyright real ("Copyright 2019 The Big Shoulders Project Authors").

**Subconjunto latin, verificado:** se bajaron los tres archivos y se revisó el `cmap` con fontTools (en su versión `.woff`). Tienen ñ Ñ á é í ó ú Á É Í Ó Ú ü ¿ ¡ $ º ° · – — … “ ” ‘ ’ × y los dígitos. Ninguna de las dos tiene la flecha → (U+2192), así que no se usa en el texto: las flechas son SVG. Big Shoulders Display no tiene cifras tabulares (`tnum`): los horarios van alineados a la izquierda, no en columnas de números.

**`@font-face`** (al principio de `css/style.css`):

```css
@font-face { font-family: "Big Shoulders Display"; src: url("../assets/fonts/big-shoulders-display-latin-800-normal.woff2") format("woff2"); font-weight: 800; font-style: normal; font-display: swap; }
@font-face { font-family: "Atkinson Hyperlegible Next"; src: url("../assets/fonts/atkinson-hyperlegible-next-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: swap; }
@font-face { font-family: "Atkinson Hyperlegible Next"; src: url("../assets/fonts/atkinson-hyperlegible-next-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-style: normal; font-display: swap; }
/* respaldo con el mismo ancho, para que el cambio de fuente no mueva la portada */
@font-face { font-family: "BSD respaldo"; src: local("Arial Bold"), local("Arial-BoldMT"), local("Roboto Bold"), local("Roboto-Bold"), local("Arial"); font-weight: 800; size-adjust: 76%; }
@font-face { font-family: "AHN respaldo"; src: local("Arial"), local("ArialMT"), local("Roboto"); size-adjust: 99%; }
```

El `size-adjust` sale de medir el mismo texto con las dos fuentes en Chrome: Big Shoulders Display 800 mide el 75,9 % de Arial Bold (80,3 % de Roboto), y Atkinson Hyperlegible Next 400 mide el 99,1 % de Arial.

**Cambios respecto del punto de partida del brief:**

- **Big Shoulders Display: se mantiene.** Tiene aire de cartel municipal (está basada en la cartelería de Chicago), minúsculas, nueve pesos y todos los signos del español. La alternativa obvia, Bebas Neue, es justo la que usan GAN y Legión Box en el relevamiento. Hoy Google Fonts también ofrece "Big Shoulders" con eje óptico; la versión "Display" está ajustada para tamaños grandes, que es como se usa acá.
- **Un solo peso de la de cartel (800), no varios:** baja el peso y deja una sola voz de cartel.
- **Atkinson Hyperlegible → Atkinson Hyperlegible Next.** Es la versión 2 del mismo proyecto del Braille Institute: mismas formas pensadas para que no se confundan letras (I l 1, O 0), más pesos y mejor espaciado. Además, cada archivo pesa unos 5 KB menos (12,1 contra 17,2 KB).
- **Títulos en minúscula, no en mayúsculas.** En mayúscula solo van el logotipo de texto, los nombres de las estaciones (son el cartel de cada estación) y las etiquetas chicas. Un titular largo en mayúsculas condensadas se lee peor para la gente grande.

### Escala tipográfica

Valores en rem (1 rem = 16 px). Celular es la base (360 a 599 px); 600 o más es tablet; 1024 o más es compu.

| Token | Uso | Familia y peso | Celular | ≥ 600 | ≥ 1024 | Interlineado |
|---|---|---|---|---|---|---|
| `--t-h1` | Titular de la portada | Display 800 | 4.25rem (68 px) | 5.5rem (88 px) | 8rem (128 px); ≥ 1440: 9rem (144 px) | 0.9 |
| `--t-h2` | Título de sección | Display 800 | 2.75rem (44 px) | 3.5rem (56 px) | 4.5rem (72 px) | 0.95 |
| `--t-destacado` | Frases de Nicolás (El enfoque, Clase de prueba) | Display 800 | 2.125rem (34 px) | 2.5rem (40 px) | 3.25rem (52 px) | 1.02 |
| `--t-h3` | Estaciones, horarios, "Plan complemento", "Dónde estamos", nombre del profe | Display 800 | 2rem (32 px) | 2rem | 2.5rem (40 px) | 1.0 |
| `--t-precio` | $35.000 | Display 800 | 5.5rem (88 px) | 5.5rem | 7.5rem (120 px) | 0.85 |
| `--t-siete` | El 7 | Display 800 | 7.5rem (120 px) | 7.5rem | 10rem (160 px) | 0.8 |
| `--t-dato` | Datos de la ficha de la portada, precios del plan complemento | Display 800 | 1.625rem (26 px) | 1.75rem | 2rem (32 px) | 1.05 |
| `--t-bajada` | Bajada de la portada y de cada sección | Texto 400 | 1.1875rem (19 px) | 1.25rem | 1.5rem (24 px) | 1.4 |
| `--t-cuerpo` | Texto corrido | Texto 400 / 700 | 1.125rem (18 px) | 1.125rem | 1.1875rem (19 px) | 1.5 |
| `--t-boton` | Botones | Texto 700 | 1rem (16 px); ≥ 390: 1.125rem (18 px) | 1.125rem | 1.125rem | 1.2 |
| `--t-etiqueta` | Primera línea del h1, etiqueta "Una vuelta…", rótulos de la ficha | Texto 700 | 1rem (16 px) | 1rem | 1.125rem (18 px) | 1.3 |
| `--t-chico` | Notas bajo botones, epígrafes, pie | Texto 400 | 0.9375rem (15 px) | 0.9375rem | 1rem (16 px) | 1.4 |

- Nada baja de 15 px.
- `letter-spacing`: display grande −0.005em; nombres de estación y logotipo de texto +0.01em; etiquetas en mayúscula +0.06em.
- `text-wrap: balance` en `h1`, `h2`, `.destacado` y `.h1-que`; `text-wrap: pretty` en párrafos.
- Largo de línea: máximo 40ch en bajadas y 62ch en texto corrido.

Medido en Chrome:

- "Que quieras volver." entra en 2 líneas a 360 px con 56, 60, 64 y 72 px.
- "Reservá tu clase de prueba gratis" mide 253 px a 16 px y 284 px a 18 px en Atkinson Next 700. Con el ícono de 22 px, 8 px de separación y 14 px de relleno por lado, entra en una línea a 360 px (16 px de letra) y a 390 px (18 px de letra).
- "Entrenamiento funcional en 25 de Mayo" mide 299 px a 16 px: entra en una línea a 360 px, donde hay 328 px.

### Espacios, medidas y formas

```css
:root {
  --naranja: #FF7B02; --negro: #000000; --blanco: #FFFFFF; --cal: #F2F2F2;
  --gris: #545454; --gris-pie: #BDBDBD; --negro-hover: #2B2B2B;
  --display: "Big Shoulders Display", "BSD respaldo", "Arial Narrow", sans-serif;
  --texto: "Atkinson Hyperlegible Next", "AHN respaldo", Arial, sans-serif;
  --e-1: .25rem; --e-2: .5rem; --e-3: .75rem; --e-4: 1rem; --e-5: 1.5rem;
  --e-6: 2rem; --e-7: 3rem; --e-8: 4rem; --e-9: 6rem; --e-10: 7rem;
  --gutter: 1rem;          /* 16 px; ≥600: 1.5rem; ≥1024: 2.5rem */
  --ancho: 70rem;          /* 1120 px de contenido como máximo */
  --seccion: 3.5rem;       /* relleno arriba y abajo de cada sección; ≥1024: 7rem */
  --borde: 3px solid var(--negro);
  --pista: 5px solid var(--negro);
  --radio: 6px;            /* botones, ficha, fotos, tabla */
  --radio-pista: 36px;     /* ≥1024: 64px */
  --cabecera: 64px;        /* alto del encabezado sin el borde; ≥1024: 80px */
  --barra: 72px;           /* alto de la barra fija (3 de borde + 8 + 53 + 8) */
  /* más los tokens --t-* de la tabla de arriba */
}
```

- **Contenedor:** `.contenedor { max-width: calc(var(--ancho) + 2 * var(--gutter)); margin-inline: auto; padding-inline: var(--gutter); }`.
- **Rejilla de compu (≥ 1024):** 12 columnas con 48 px entre columnas (`--e-7`). Las proporciones de cada sección están en la sección 4.
- **Bordes:** 3 px negros en el encabezado (abajo), en el borde de cada campo naranja, en la ficha, las fotos, la tabla y los botones de contorno. La pista del circuito lleva 5 px. No hay filetes finos ni sombras.
- **Radios:** 6 px. El rombo de estación lleva 3 px de esquina, como el del logo. La pista: 36 px en el celular y 64 px en la compu.
- **Botones:** al menos 44 px de alto. El principal mide 56 px (53 px dentro de la barra fija). Los links de texto van subrayados, con `text-underline-offset: .18em` y un área tocable de al menos 44 px de alto (relleno vertical).
- **Foco:** `:focus-visible { outline: 3px solid var(--negro); outline-offset: 3px; }`. Sobre negro (pie y barra): `outline-color: var(--blanco)`, y en la barra además `outline-offset: -7px`. Nunca se quita el contorno.
- **Puntos de corte:** base de 360 a 599 px, `min-width: 600px`, `min-width: 1024px` (columnas, sin barra fija), `min-width: 1200px` (menú en línea) y `min-width: 1440px` (titular más grande).

---

## 3. La firma: el circuito

### Qué cuenta

Una vuelta del circuito pasa por cinco estaciones, y cada una cambia el patrón de movimiento. Eso es lo que dice Nicolás en su PDF ("Las estaciones de trabajo están organizadas estratégicamente para alternar patrones de movimiento… Esto permite mantener un buen nivel de esfuerzo sin generar fatiga excesiva"). El dibujo lo hace visible:

- La pista es cerrada: termina donde empieza ("y otra vuelta").
- Las estaciones están en orden. El orden significa algo: es el recorrido, y en ese recorrido nunca se repite el mismo patrón dos veces seguidas. Por eso no llevan números: el orden lo da la línea, y además es un ejemplo.
- Cada estación dice el patrón en lenguaje de gimnasio (el cartel) y, abajo, el verbo de todos los días que usa Nicolás en su carrusel del 05/02/2026 ("la fuerza real, la que usás todos los días: empujar, tirar, levantar, estabilizar"), más el material que se ve en sus videos del cuartel. Las cinco estaciones salen de la lista del PDF, en el mismo orden.
- Debajo, una frase explica en criollo por qué se sostiene el esfuerzo, y otra dice el máximo de 7.

Es "por ejemplo": no se inventan tiempos por estación, cantidad de vueltas ni cantidad fija de estaciones.

### Contenido de cada estación (texto final)

| Cartel (`.estacion-nombre`, en mayúscula por CSS) | Verbo, en negrita | Material (visto en los videos de 2026) |
|---|---|---|
| Sentadillas | Levantar. | Con mancuernas. |
| Empujes | Empujar. | Press con mancuernas. |
| Tracciones | Tirar. | Remo con TRX. |
| Core | Estabilizar. | Con la pelota medicinal. |
| Aeróbico | Moverte. | Saltos, cubierta y maza. |

De dónde sale el material: sentadilla y press con mancuernas en el fotograma `DbUtD7_j4uj_f008s`; remo con TRX en `DUa7Xy0DthX_f024s`, `DXvBvnKDg29_f016s` y `DbUtD7_j4uj_f042s`; las manos en la pelota medicinal en `DWpl7tBNP0R_f004s`; saltos en la cubierta en `DXvBvnKDg29_f014s`; la maza en `DbUtD7_j4uj_f034s`.

### Cómo se ve en el celular (360 a 390 px)

Es una pista vertical: el borde izquierdo de la caja es la ida, con las estaciones de arriba a abajo; el borde derecho es la vuelta, con una flecha hacia arriba.

```
  UNA VUELTA DEL CIRCUITO, POR EJEMPLO          ← h3.etiqueta, 16 px, 700, mayúsculas
 ╭──────────────────────────────────────╮       ← .pista: borde 5 px, radio 36 px
 ◆ SENTADILLAS                          │       ← rombo 24 px (34 px en diagonal) sobre el borde
 │ Levantar. Con mancuernas.            │         nombre: display 32 px; línea: texto 17 px
 ◆ EMPUJES                              │
 │ Empujar. Press con mancuernas.       ▲       ← flecha de vuelta (SVG 22 px) sobre el borde
 ◆ TRACCIONES                           │         derecho, a media altura, con fondo naranja
 │ Tirar. Remo con TRX.                 │         para "cortar" la línea
 ◆ CORE                                 │
 │ Estabilizar. Con la pelota medicinal.│
 ◆ AERÓBICO                             │
 │ Moverte. Saltos, cubierta y maza.    │
 ╰─────────── y otra vuelta ────────────╯       ← texto 700 16 px sobre el borde de abajo,
                                                  con fondo naranja y 10 px de relleno
```

Medidas (probadas en la maqueta):

- `.pista`: `margin-left: 14px` (para que el rombo no se salga del contenedor); `padding: 20px 20px 28px 36px`; `border: var(--pista)`; `border-radius: var(--radio-pista)`; `position: relative`; `max-width: 520px`.
- Cada `li`: `position: relative; padding: 10px 0`.
- Rombo `li::before`: `content: ""; position: absolute; left: -50px; top: 6px; width: 24px; height: 24px; background: var(--negro); border-radius: 3px; transform: rotate(45deg); box-shadow: inset 0 0 0 3px var(--negro), inset 0 0 0 5px var(--naranja);`. Queda centrado sobre la línea izquierda y a la altura del nombre. Es el rombo del logo: borde negro, filete naranja y centro negro.
- `.estacion-nombre`: `display: block`, display 800, `var(--t-h3)` (32 px), interlineado 1, `text-transform: uppercase`, `letter-spacing: .01em`. El más largo, "SENTADILLAS", mide 142 px a 32 px.
- `.estacion-que`: `display: block`, texto 400 `1.0625rem` (17 px), interlineado 1.35; el verbo va en `<b>` 700.
- Flecha de vuelta `.pista-flecha`: `position: absolute; right: -17px; top: 50%; width: 29px; height: 29px; background: var(--naranja); display: grid; place-items: center;`, con un SVG de flecha hacia arriba de 22 px en negro, `aria-hidden="true"`.
- `.pista-vuelta` ("y otra vuelta"): `position: absolute; left: 50%; bottom: -15px; transform: translateX(-50%); background: var(--naranja); padding: 0 10px; font: 700 1rem/1.3 var(--texto); white-space: nowrap;`.

### Cómo se ve en la compu (1366 px)

Es la misma pista, acostada: el borde de arriba es la ida, con las cinco estaciones de izquierda a derecha; el borde de abajo es la vuelta, con la flecha hacia la izquierda y "y otra vuelta" al lado. Ocupa el ancho entero del contenido (1120 px).

```
  UNA VUELTA DEL CIRCUITO, POR EJEMPLO
  ◆━━━━━━━━━━━━━━━━━◆━━━━━━━━━━━━━━━━━◆━━━━━━━━━━━━━━━━━◆━━━━━━━━━━━━━━━━━◆━━━━━━━━━━━━━━━━━╮
 ┃ SENTADILLAS        EMPUJES            TRACCIONES         CORE               AERÓBICO          ┃
 ┃ Levantar. Con      Empujar. Press     Tirar. Remo con    Estabilizar. Con   Moverte. Saltos,  ┃
 ┃ mancuernas.        con mancuernas.    TRX.               la pelota medic.   cubierta y maza.  ┃
  ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◀  y otra vuelta ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
```

- `.pista` (≥ 1024): `margin: 0; max-width: none; padding: 44px 32px 48px; border-radius: 64px;`. El `ol` lleva `display: grid; grid-template-columns: repeat(5, 1fr); gap: 24px;` y cada `li` va sin relleno.
- Rombo: `left: 0; top: -58px` (44 px de relleno + 2,5 px de media línea + 12 px de medio rombo). Queda sobre la línea de arriba y alineado con el comienzo del texto de su columna.
- `.estacion-nombre` a 40 px, `.estacion-que` a 17 px.
- Flecha: `right: auto; left: 50%; top: auto; bottom: -17px; transform: translateX(-50%) rotate(-90deg);`, es decir, apunta a la izquierda sobre la línea de abajo.
- "y otra vuelta": `left: calc(50% + 40px); bottom: -15px; transform: none;`.
- De 600 a 1023 px se ve como en el celular, con `max-width: 560px`.

### Sin fotos dentro de la pista

La pista es tipografía y líneas, sin fotos. La prueba de que es real va al lado: el único fotograma que muestra el circuito de verdad, con tres personas en tres estaciones distintas al mismo tiempo en el salón del cuartel (`clase-circuito`, ver la sección 9). Las fotos por estación sumaban caras de alumnos y peso, y no explicaban mejor.

### Accesibilidad

- `<ol role="list" aria-label="Ejemplo de una vuelta del circuito">`. El `role="list"` hace falta porque Safari le saca la semántica de lista a un `ol` con `list-style: none`. Se usa `ol` porque el orden es real.
- La flecha va con `aria-hidden="true"`. "y otra vuelta" es texto real (un `<p>` dentro de `.pista`, después del `ol`), así que se lee.
- La pista no depende del color: es borde negro sobre naranja (8,09:1) y el texto está todo escrito.

---

## 4. Estructura y esquema de cada sección

Una sola página, en el orden del brief. No hay motivo para cambiarlo: la portada ya contesta precio y horarios en el primer pantallazo, así que "Turnos y cuota" puede ir donde la pone el brief.

| # | Sección | `id` | Fondo | Ítem del menú |
|---|---|---|---|---|
| 1 | Encabezado (fijo arriba) | — | Naranja, borde inferior de 3 px | — |
| 2 | Portada | `inicio` | Naranja | — |
| 3 | El enfoque | `enfoque` | Blanco | El enfoque |
| 4 | Cómo es la clase (la firma) | `clase` | Naranja | Cómo es la clase |
| 5 | Turnos y cuota (fuente única de datos) | `turnos` | Blanco | Turnos y cuota |
| 6 | El profe | `profe` | Cal | El profe |
| 7 | Clase de prueba y Dónde estamos | `prueba` (y `donde` en el h3) | Naranja | Dónde estamos (va a `#donde`) |
| 8 | Pie | — | Negro | — |
| — | Barra fija de WhatsApp (solo por debajo de 1024 px) | `barra` | Naranja con borde arriba | — |

La página alterna campos naranja y franjas claras: naranja (portada), blanco, naranja (la clase), blanco, cal, naranja (la prueba), negro (el pie). Los campos naranja son los tres momentos clave: la tesis, la firma y la acción. Cada sección naranja lleva `border-block: var(--borde)`; la portada lleva solo el borde de abajo, porque arriba ya está el del encabezado.

Relleno de cada sección: `padding-block: var(--seccion)` (56 px en el celular y 112 px en la compu), salvo la portada (ver abajo). En el `html` va `scroll-padding-top: calc(var(--cabecera) + 3px + 12px)`. Por debajo de 1024 px va además `scroll-padding-bottom: calc(var(--barra) + 12px)`, para que el encabezado y la barra no tapen el destino de un link ni un elemento con foco.

### 4.1 Encabezado

Es `position: sticky; top: 0; z-index: 20;`, con fondo naranja y `border-bottom: var(--borde)`. Alto: `var(--cabecera)` (64 px en el celular y 80 px en la compu).

**Celular (360 a 419 px):**

```
┌──────────────────────────────────────────┐
│ (◉) ESPACIO          [■✆]  [ Menú ]       │   logo 44 px · logotipo de texto en 2 líneas
│     FUNCIONAL 25                          │   WhatsApp: botón negro de 44×44, solo ícono
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘   Menú: botón de contorno de 3 px
```

- `.marca` (link a `#inicio`): logo de 44×44 más el texto "Espacio" / "Funcional 25" en dos renglones (`<span>Espacio</span><span>Funcional 25</span>`, cada uno `display: block; white-space: nowrap`), en display 800 de 17 px, mayúsculas, interlineado 0.95. "FUNCIONAL 25" mide 84 px. La `.marca` lleva `margin-right: auto` y al menos 44 px de alto.
- WhatsApp (`.btn-chico.btn-chico--solido`): negro, ícono blanco de 20 px y texto "WhatsApp" en `<span class="sr-only">` hasta 419 px. Desde 420 px el texto se ve.
- Menú (`.btn-chico`, `<button>`): contorno de 3 px negro, texto 700 de 16 px, relleno de 0 12 px y 44 px de alto. Dice "Menú" y, abierto, "Cerrar".
- Separación de 8 px entre elementos. Medido: 44 + 8 + 84 + 8 + 44 + 8 + 71 = 267 px, contra 328 px disponibles a 360. A 420 px, con el texto "WhatsApp" a la vista, son 349 px contra 388.

**De 420 a 1199 px:** igual, con el texto "WhatsApp" visible.

**Compu (1200 px o más):**

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ (◉) ESPACIO FUNCIONAL 25     El enfoque   Cómo es la clase   Turnos y cuota   El profe   Dónde estamos   [✆ WhatsApp] │
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
```

- Logo de 56 px y logotipo de texto en una línea ("Espacio Funcional 25") de 22 px. Desde 1024 px los dos `span` pasan a `display: inline`.
- El menú va en línea: links en texto 700 de 16 px, negros y sin subrayar, con un subrayado de 3 px en hover y en foco, separados por 24 px y con 44 px de alto. El botón "Menú" se oculta. Medido: unos 1010 px contra 1120 disponibles.
- De 1024 a 1199 px queda el botón "Menú" (el menú en línea no entra).

### 4.2 Menú en el celular (por debajo de 1200 px)

Es un panel debajo del encabezado que ocupa toda la pantalla y aparece sin transición, como en pablospata-website.

```
┌──────────────────────────────────────────┐
│ (◉) ESPACIO          [■✆]  [ Cerrar ]     │  encabezado igual, el botón dice "Cerrar"
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
│ El enfoque                                │  ← links en display 800 de 30 px, 56 px de alto,
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│    separados por 2 px negros, fondo blanco
│ Cómo es la clase                          │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│ Turnos y cuota                            │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│ El profe                                  │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│ Dónde estamos                             │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│ [■ ✆ Reservá tu clase de prueba gratis ]  │  ← botón principal
│ Instagram: @espaciofuncional25            │  ← link
└──────────────────────────────────────────┘
```

- Marcado: `<button class="btn-chico boton-menu" type="button" aria-expanded="false" aria-controls="menu">Menú</button>` y `<nav class="menu" id="menu" aria-label="Secciones">` con una `<ul>` de links y, debajo, el botón y el link de Instagram (`.menu-extra`, que se oculta desde 1200 px).
- CSS (por debajo de 1200 px): `.menu { display: none; position: fixed; inset: calc(var(--cabecera) + 3px) 0 0 0; overflow-y: auto; background: var(--blanco); padding: 8px var(--gutter) 24px; }` y `.menu.abierto { display: block; }`. Desde 1200 px: `.menu { display: flex; position: static; background: none; padding: 0; }`.
- JS, con la función `ponerMenu(abierto)`:
  - alterna `.abierto` en el nav, `aria-expanded` y el texto del botón ("Menú" / "Cerrar");
  - pone `body.menu-abierto`, que deja `overflow: hidden` y oculta la barra fija;
  - pone `inert` en `main`, `footer` y `#barra` mientras está abierto, así el tabulador no se va detrás del panel;
  - lo cierra un toque en cualquier link del panel, la tecla Escape (que además devuelve el foco al botón) o el pasaje a ≥ 1200 px (`matchMedia('(min-width: 1200px)')`).

### 4.3 Barra fija de WhatsApp (por debajo de 1024 px)

```
            … contenido …
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐  ← borde de arriba de 3 px negro
│  [■ ✆  Reservá tu clase de prueba gratis ]│  ← botón principal negro, 53 px de alto
└──────────────────────────────────────────┘  ← fondo naranja; abajo, el área segura del iPhone
```

- `<div class="barra" id="barra">` con un único `<a class="btn btn--barra">`. `position: fixed; left: 0; right: 0; bottom: 0; z-index: 15; background: var(--naranja); border-top: var(--borde); padding: 8px var(--gutter) calc(8px + env(safe-area-inset-bottom));`. El botón lleva `min-height: 53px; width: 100%; max-width: 480px; margin-inline: auto;`. Total: 72 px más el área segura. Hace falta `<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">` para que `env()` funcione.
- **Reserva de lugar:** `body { padding-bottom: calc(var(--barra) + env(safe-area-inset-bottom)); }` por debajo de 1024 px, siempre, aunque la barra esté oculta. Así el final del pie nunca queda debajo de la barra. Desde 1024 px no hay barra ni ese relleno.
- **Cuándo se oculta**, siempre al instante y sin animación:
  - mientras se ve el botón de la portada (`#cta-portada`) o el de "Clase de prueba" (`#cta-prueba`), para no repetir el mismo botón en la misma pantalla. JS lo hace con un `IntersectionObserver` sobre los dos botones; si alguno está visible, la barra lleva `.barra--oculta { display: none }`;
  - con el menú abierto: `.menu-abierto .barra { display: none }`.
- Sin JS, la barra se ve siempre.
- Al abrir la página, la barra arranca oculta, porque el botón de la portada está a la vista. Aparece apenas ese botón sale de la pantalla, y desde ahí hay siempre un botón de WhatsApp abajo.

### 4.4 Portada

**Celular (390×844; también entra en 360×740):**

```
┌──────────────────────────────────────────┐ encabezado (67 px)
├──────────────────────────────────────────┤
│ Entrenamiento funcional en 25 de Mayo    │ h1, primera línea: texto 700 de 16 px
│ Que quieras                              │ h1, tesis: display 800 de 68 px
│ volver.                                  │
│ Grupos de máximo 7 personas en el        │ bajada de 19 px
│ Cuartel de Bomberos: calle 21 Nº 739,    │
│ entre 8 y 9.                             │
│ ┌──────────────────────────────────────┐ │
│ │ ✆  Reservá tu clase de prueba gratis │ │ botón principal (56 px) #cta-portada
│ └──────────────────────────────────────┘ │
│ Te abre WhatsApp. Pagás recién desde la  │ nota de 15 px
│ segunda clase.                           │
│ ┌──────────────────────────────────────┐ │ .ficha (borde 3 px, radio 6)
│ │ Cuota                                │ │  rótulo 700 de 15 px
│ │ $35.000 por mes                      │ │  dato: display de 26 px
│ │ 2 clases por semana. Valores de      │ │  nota de 15 px
│ │ octubre 2026.                        │ │
│ ├──────────────────────────────────────┤ │
│ │ Turnos                               │ │
│ │ Lunes y jueves: 18 o 19 h            │ │
│ │ Martes y viernes: 7 h                │ │
│ └──────────────────────────────────────┘ │
├━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┤ foto a sangre (de borde a borde), con borde arriba de 3 px
│ [ foto: Nicolás le muestra el ejercicio  │ portada-profe-corrige, 4:3
│   a una alumna; autobombas atrás ]       │ (en 844 px de alto asoman unos 190 px)
└──────────────────────────────────────────┘
```

- La portada lleva `padding: 20px 0 0` en el celular. La foto cierra la sección, sin relleno abajo, y la sección cierra con su borde de 3 px.
- Alto estimado con las medidas de la maqueta, a 360×740: encabezado 67 + 20 + primera línea 24 + 8 + h1 122 + bajada 112 + botón 56 + nota 50 + ficha 240 ≈ 700 px. Las cinco respuestas (qué, dónde, cuánto, cuándo y cómo se prueba) más el 7 entran en el primer pantallazo de los dos celulares.
- `.ficha`: es un `<dl>` con dos `<div>`; cada uno lleva un `<dt>` (rótulo) y un `<dd>` (dato), uno debajo del otro, alineados a la izquierda, con 12 px de relleno y un borde de 3 px entre los dos. `max-width: 420px`.
- Los `<dd>` los completa JS desde "Turnos y cuota" (ver la sección 7). Sin JS muestran un link: "Ver la cuota" y "Ver los turnos", a `#turnos`.
- El botón y la ficha tienen `max-width: 420px`.

**Compu (1366×768):**

```
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ encabezado de 83 px                                                                     │
├───────────────────────────────────────────────────────────────────────────────────────┤
│  Entrenamiento funcional en 25 de Mayo                     ┌─────────────────────────┐ │
│  Que quieras                                               │                         │ │
│  volver.                       (display 128 px)            │  foto 4:3, 447 px,      │ │
│  Grupos de máximo 7 personas en el Cuartel de              │  borde 3 px, radio 6    │ │
│  Bomberos: calle 21 Nº 739, entre 8 y 9. (24 px)           │                         │ │
│  [ ✆ Reservá tu clase de prueba gratis ]                   └─────────────────────────┘ │
│  Te abre WhatsApp. Pagás recién desde la segunda clase.                                │
│  ┌───────────────────────┬────────────────────────┐                                     │
│  │ Cuota                 │ Turnos                 │   ficha en 2 columnas               │
│  │ $35.000 por mes       │ Lunes y jueves: 18 o 19 h                                    │
│  │ 2 clases… octubre 2026│ Martes y viernes: 7 h  │                                     │
│  └───────────────────────┴────────────────────────┘                                     │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

- `.portada .contenedor`: `display: grid; grid-template-columns: 7fr 5fr; gap: 48px; align-items: center;`. Relleno: 56 px arriba y 64 px abajo.
- La ficha va en dos columnas (`grid-template-columns: 1fr 1fr`, con el borde de 3 px entre las dos en vez de entre filas) y `max-width: 600px`.
- La foto ya no va a sangre: `border: var(--borde); border-radius: var(--radio);`.
- En 1366×768 el h1 de 128 px ocupa unos 230 px. Si la ficha no entra entera arriba del pliegue de 768, se baja el h1 a 7.25rem entre 1024 y 1439 px. Hay que verificarlo en la auditoría de compu.
- De 600 a 1023 px: una sola columna, como el celular, con la foto de `max-width: 656px` con borde y radio (no a sangre).

### 4.5 El enfoque

**Celular:**

```
┌ blanco ──────────────────────────────────┐
│ El enfoque                               │ h2, 44 px
│                                          │
│ Lo más fácil para un entrenador es       │ .destacado.cita-facil: display de 34 px, gris #545454
│ simplemente agotarte hasta dejarte sin   │
│ aire.                                    │
│ Lo difícil, y lo que de verdad importa,  │ .destacado.cita-dificil: display de 34 px, negro
│ es lograr que quieras volver cada semana │
│ sin lastimarte entrenando.               │
│ Nicolás Valle                            │ figcaption: texto 700 de 16 px
│                                          │
│ Por eso en Espacio Funcional 25 buscamos:│ texto de 18 px
│ ✔ esfuerzo adaptado al nivel de cada…    │ ul.tildes: tilde SVG de 20 px en negro
│ ✔ progresión gradual                     │
│ ✔ técnica correcta                       │
│ ✔ entrenamientos sostenibles en el tiempo│
│                                          │
│ Porque el factor más importante para     │ .cierre: texto 700 de 21 px
│ mejorar no es una sesión intensa, sino   │
│ la continuidad.                          │
└──────────────────────────────────────────┘
```

**Compu:** dos columnas: 7fr para la cita y 5fr para la lista y el cierre, con `align-items: end`. El h2 va arriba, a todo el ancho.

```
│ El enfoque                                                                              │
│ Lo más fácil para un entrenador es              │ Por eso en Espacio Funcional 25        │
│ simplemente agotarte hasta dejarte sin aire.    │ buscamos:                              │
│ Lo difícil, y lo que de verdad importa, es      │ ✔ esfuerzo adaptado…                   │
│ lograr que quieras volver cada semana sin       │ ✔ progresión gradual …                 │
│ lastimarte entrenando.   (display 52 px)        │ Porque el factor más importante …      │
│ Nicolás Valle                                   │                                        │
```

- No lleva foto: es la sección de la voz de Nicolás.
- El contraste gris contra negro dice lo mismo que la frase: lo fácil queda atrás y lo que importa adelante.

### 4.6 Cómo es la clase (la firma)

**Celular:**

```
┌ naranja ─────────────────────────────────┐
│ Cómo es la clase                         │ h2
│ Entrenamos fuerza, resistencia y         │ bajada de 19 px, máx. 40ch
│ acondicionamiento físico con ejercicios  │
│ funcionales, organizados en estaciones   │
│ de trabajo. Cada clase dura una hora.    │
│                                          │
│ [ la pista vertical de la sección 3 ]    │
│                                          │
│ Cada estación cambia el movimiento, así  │ .por-que: texto 700 de 19 px
│ no cargás siempre la misma parte…        │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │ borde de 3 px
│ 7 │ personas como máximo por turno       │ .siete: el 7 en display de 120 px; rótulo
│   │ Es a propósito. En grupos chicos hay │ en display de 28 px; texto de 17 px
│   │ supervisión constante, corrección …  │
│ ┌──────────────────────────────────────┐ │
│ │ foto clase-circuito 16:9             │ │ borde 3 px, radio 6, loading="lazy"
│ └──────────────────────────────────────┘ │
│ Una clase en el cuartel: cada uno en su  │ figcaption de 15 px
│ estación, al mismo tiempo.               │
└──────────────────────────────────────────┘
```

**Compu:** el h2 y la bajada arriba (bajada de 24 px, máx. 40ch), la pista acostada a todo el ancho y, debajo, `.clase-pie` con `display: grid; grid-template-columns: 7fr 5fr; gap: 48px; margin-top: 56px;`. A la izquierda van `.por-que` y `.siete`; a la derecha, la foto con su epígrafe. El wireframe está en la sección 3.

- `.siete`: `display: grid; grid-template-columns: auto 1fr; gap: 4px 16px; align-items: center; border-top: var(--borde); padding-top: 20px; margin-top: 32px;`. El número ocupa dos filas.
- El 7 es un dato real y es el argumento, por eso va grande. No es un contador.

### 4.7 Turnos y cuota (la fuente única de datos)

**Celular:**

```
┌ blanco ──────────────────────────────────┐
│ Turnos y cuota                           │ h2
│ ┌──────────────────────────────────────┐ │ table.turnos (borde 3 px, radio 6)
│ │ Elegís un turno y venís 2 veces por  │ │ caption: texto de 17 px, a la izquierda
│ │ semana. Máximo 7 personas por turno. │ │
│ ├──────────────────────────────────────┤ │
│ │ Lunes y jueves         18 a 19 h     │ │ th: texto 700 de 18 px · td: display de 32 px
│ ├──────────────────────────────────────┤ │ filas de 64 px como mínimo, borde de 3 px
│ │ Lunes y jueves         19 a 20 h     │ │
│ ├──────────────────────────────────────┤ │
│ │ Martes y viernes       7 a 8 h       │ │
│ └──────────────────────────────────────┘ │
│ Los días que no venís podés combinar con │ texto de 17 px
│ algo más suave, como caminar o andar en  │
│ bicicleta.                               │
│                                          │
│ ┌──────────────────────────────────────┐ │ .cuota (borde 3 px, radio 6, relleno 20)
│ │ Cuota mensual                        │ │ h3
│ │ $35.000                              │ │ display de 88 px
│ │ por mes                              │ │ display de 26 px
│ │ Valores de octubre 2026.             │ │ texto 700 de 16 px
│ │ Incluye:                             │ │
│ │ ■ 2 clases por semana                │ │ cuadrito negro de 10 px
│ │ ■ planificación del entrenamiento    │ │
│ │ ■ seguimiento técnico                │ │
│ │ ■ adaptación de los ejercicios según │ │
│ │   tu nivel                           │ │
│ │┌────────────────────────────────────┐│ │ .banda: fondo naranja, texto negro 700 de 17 px
│ ││ La clase de prueba es gratis.      ││ │
│ ││ Empezás a pagar desde la segunda   ││ │
│ ││ clase.                             ││ │
│ │└────────────────────────────────────┘│ │
│ └──────────────────────────────────────┘ │
│                                          │
│ Plan complemento                         │ h3
│ Un plan personalizado para hacer por tu  │
│ cuenta: running, fuerza o lo que         │
│ necesites.                               │
│ $10.000 extra por mes                    │ dl.complemento: dt en display de 26 px
│ si ya entrenás en el espacio             │ dd: texto de 17 px
│ $25.000 por mes                          │
│ si querés solo el plan, sin venir a las  │
│ clases                                   │
│ [ ✆ Consultar por el plan complemento ]  │ .btn--contorno
└──────────────────────────────────────────┘
```

**Compu:** dos columnas de 6fr: a la izquierda la tabla y la línea de los otros días; a la derecha la tarjeta de la cuota y, debajo, el plan complemento.

```
│ Turnos y cuota                                                                          │
│ ┌─────────────────────────────────────┐      ┌─────────────────────────────────────────┐ │
│ │ Elegís un turno y venís 2 veces…    │      │ Cuota mensual                           │ │
│ │ Lunes y jueves        18 a 19 h     │      │ $35.000  por mes     (120 px)           │ │
│ │ Lunes y jueves        19 a 20 h     │      │ Valores de octubre 2026.                │ │
│ │ Martes y viernes      7 a 8 h       │      │ Incluye: ■ … ■ … ■ … ■ …                 │ │
│ └─────────────────────────────────────┘      │ [ La clase de prueba es gratis… ]       │ │
│ Los días que no venís podés combinar…        └─────────────────────────────────────────┘ │
│                                              Plan complemento                           │
│                                              … $10.000 … $25.000 … [Consultar…]          │
```

- La tabla es una `<table>` de verdad: `<caption>`, `<thead class="sr-only">` con "Días" y "Horario", y cada fila con un `<th scope="row">` de días y un `<td>` de horario. Las columnas van alineadas a la izquierda.
- Los turnos van en el orden de `TAREAS.md` (por el primer día de la semana).

### 4.8 El profe

**Celular:**

```
┌ cal #F2F2F2 ─────────────────────────────┐
│ El profe                                 │ h2
│ ┌──────────────────────────────────────┐ │
│ │ foto profe-nicolas 4:5               │ │ borde 3 px, radio 6, lazy (328×410 a 360)
│ │ (buzo con el logo, pelota naranja)   │ │
│ └──────────────────────────────────────┘ │
│ Nicolás Guido Valle                      │ p.profe-nombre: display de 32 px
│ Profesor en Educación Física y licenciado│ texto 700 de 19 px
│ en Alto Rendimiento Deportivo.           │
│ Da clases de Educación Física en escuelas│ texto de 18 px
│ de la zona desde 2017. Es preparador …   │
│ Formación                                │ h3: texto 700 de 16 px, mayúsculas
│ ■ Profesor en Educación Física, Instituto│ ul de 17 px
│   Santa Rosa (2017).                     │
│ ■ …                                      │
└──────────────────────────────────────────┘
```

**Compu:** `grid-template-columns: 5fr 7fr`, con la foto a la izquierda (447 px) y el texto a la derecha, alineados arriba; el h2 va en la columna del texto. De 600 a 1023 px, la foto con `max-width: 480px`.

### 4.9 Clase de prueba y Dónde estamos

**Celular:**

```
┌ naranja ─────────────────────────────────┐
│ Clase de prueba                          │ h2
│ No hace falta que estés en forma para    │ .destacado: display de 34 px
│ arrancar.                                │
│ Podés venir a una clase de prueba para   │ texto de 18 px
│ conocer cómo trabajamos. Es gratis: se … │
│ No necesitás experiencia previa: los …   │
│ ┌──────────────────────────────────────┐ │
│ │ ✆  Reservá tu clase de prueba gratis │ │ #cta-prueba (56 px)
│ └──────────────────────────────────────┘ │
│ Te abre WhatsApp con el mensaje listo.   │ nota de 15 px
│ Si preferís llamar: 2345-402547          │ link tel:, 44 px de alto
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │ borde de 3 px
│ Dónde estamos                            │ h3#donde: display de 32 px
│ Cuartel de Bomberos                      │ address: primera línea en 700
│ Calle 21 Nº 739, entre 8 y 9             │
│ Veinticinco de Mayo (CP 6660),           │
│ Buenos Aires                             │
│ [ ⌖ Cómo llegar ]                        │ .btn--contorno (56 px), Google Maps
│ ◎ Instagram: @espaciofuncional25         │ link con ícono, 44 px de alto
│ ┌──────────────────────────────────────┐ │
│ │ foto donde-cuartel 4:5               │ │ borde 3 px, radio 6, lazy
│ │ (TRX bajo "BOMBEROS VOLUNTARIOS")    │ │
│ └──────────────────────────────────────┘ │
└──────────────────────────────────────────┘
```

**Compu:** tres columnas: 5fr para la prueba, 4fr para "Dónde estamos" y 3fr para la foto (256 px), alineadas arriba. El borde de 3 px entre la prueba y "Dónde estamos" pasa a ser vertical (`border-left` de 3 px en la columna de Dónde estamos, con `padding-left: 48px`).

```
│ Clase de prueba                  │ Dónde estamos              │ ┌──────────────┐ │
│ No hace falta que estés en forma │ Cuartel de Bomberos        │ │ foto 4:5     │ │
│ para arrancar.  (52 px)          │ Calle 21 Nº 739, e/ 8 y 9  │ │ 256 px       │ │
│ Podés venir a una clase…         │ Veinticinco de Mayo…       │ │              │ │
│ [ ✆ Reservá tu clase de prueba ] │ [ Cómo llegar ]            │ └──────────────┘ │
│ Si preferís llamar: 2345-402547  │ Instagram: @…              │                  │
```

- Sin mapa embebido (ver la sección 7).

### 4.10 Pie

```
┌ negro ───────────────────────────────────┐
│ (◉) Espacio Funcional 25                 │ logo de 72 px (lazy) y nombre en display de 28 px, blanco
│ Entrenamiento funcional en grupos de     │ texto de 16 px, blanco
│ máximo 7 personas, en 25 de Mayo.        │
│ Prof. Nicolás Guido Valle, Lic. en Alto  │ #BDBDBD
│ Rendimiento Deportivo.                   │
│ Cuartel de Bomberos · Calle 21 Nº 739,   │
│ entre 8 y 9 · Veinticinco de Mayo (CP    │
│ 6660), Buenos Aires                      │
│ WhatsApp: 2345-402547                    │ links blancos subrayados, 44 px de alto
│ Instagram: @espaciofuncional25           │
│ © 2026 Espacio Funcional 25              │ el año en <span id="anio">, lo completa JS
└──────────────────────────────────────────┘
```

**Compu:** dos columnas: a la izquierda, el logo, el nombre y la descripción; a la derecha, la dirección y los links. Relleno de 48 px arriba y abajo.

---

## 5. Movimiento

**Hay uno solo: una pasada de luz por las estaciones del circuito**, una vez, cuando la pista entra en pantalla. Cada rombo, en orden (de arriba a abajo en el celular y de izquierda a derecha en la compu), crece y se le prende el centro en blanco, como una baliza que recorre la vuelta. Dice con el cuerpo lo que dice el texto: se pasa de una estación a la otra.

- JS: un `IntersectionObserver` sobre `.pista` con `threshold: 0.5`. La primera vez que entra, le agrega `.en-vista` y deja de observarla. No se repite.
- CSS, solo dentro de `@media (prefers-reduced-motion: no-preference)`:

```css
@media (prefers-reduced-motion: no-preference) {
  .pista.en-vista li::before { animation: estacion .8s ease-in-out both; }
  .pista.en-vista li:nth-child(2)::before { animation-delay: .6s; }
  .pista.en-vista li:nth-child(3)::before { animation-delay: 1.2s; }
  .pista.en-vista li:nth-child(4)::before { animation-delay: 1.8s; }
  .pista.en-vista li:nth-child(5)::before { animation-delay: 2.4s; }
  @keyframes estacion {
    0%, 100% { transform: rotate(45deg) scale(1); }
    40% { transform: rotate(45deg) scale(1.35); box-shadow: inset 0 0 0 3px var(--negro), inset 0 0 0 12px var(--blanco); }
  }
}
```

- Dura 3,2 s en total y termina en el estado de reposo (el rombo normal).
- **Con `prefers-reduced-motion: reduce`:** no hay animación. La pista se ve completa y quieta desde el principio, con la flecha y "y otra vuelta" marcando el sentido. No se pierde información.
- Sin JS, tampoco hay animación y se ve igual.

**Lo demás no se mueve:** el menú aparece y desaparece sin transición, la barra fija aparece y se oculta al instante, no hay `scroll-behavior: smooth`, no hay efectos al hacer scroll y no hay carruseles. Los hover solo cambian color o subrayado.

---

## 6. Copy completo y final

El texto de Nicolás sale del PDF "INFORMACIÓN Y ARANCELES" (transcripto en `fuentes.md`, sección 1) y de sus reels (en `INDICE.md`). Está recortado, no reemplazado. Las comillas tipográficas, "Nº", "·" y "–" van tal cual.

### 6.1 Prueba del titular

Se midió en Chrome con Big Shoulders Display 800 (líneas a 360 px, con 68 px de letra).

| Candidato | ¿Se entiende en 3 s desde Instagram? | ¿Es la voz de Nicolás? | ¿Distingue? | Líneas a 360 px |
|---|---|---|---|---|
| **A. "Que quieras volver."** | Solo, no: hay que leer la línea de arriba. Con "Entrenamiento funcional en 25 de Mayo" encima y la bajada debajo, sí. | Sí: "lograr que quieras volver cada semana" (reel del 28/07/2026) y "que una persona quiera volver" (PDF). | Mucho: ningún sitio de la muestra habla de la semana que viene. | 2 |
| B. "Entrenamiento funcional en el Cuartel de Bomberos." | Sí. | No: describe. | A medias: el lugar es único, pero la frase es una ficha. | 4 (no entra) |
| C. "Máximo 7 por turno." | A medias: ¿7 qué? Falta qué es. | A medias ("Grupos chicos"). | A medias: Lubaki dice "3 por hora" igual. | 2 |
| D. "Tu primera clase es gratis." | Sí la oferta; no qué es. | No: es promoción. | Poco: GAN pone lo mismo. | 3 |
| E. "Lo difícil es que quieras volver." | A medias: "lo difícil" pide la otra mitad. | Sí (PDF). | Mucho. | 3 |
| F. "Entrenamiento funcional en 25 de Mayo" | Sí. | No. | Poco: es lo que pone cualquiera. | 3 |

**Elegido: A, "Que quieras volver."** Es la tesis de la página y la idea de Nicolás. Lo que le falta en 3 segundos lo resuelven las piezas que lo rodean, y así no se pierde nada de las alternativas:

- B y F pasan a la primera línea del `h1` ("Entrenamiento funcional en 25 de Mayo") y a la bajada (el cuartel con la dirección).
- C pasa a la bajada ("Grupos de máximo 7 personas") y a la sección de la clase.
- D pasa al botón ("Reservá tu clase de prueba gratis") y a la nota.
- E queda para El enfoque, con la frase entera.

Así el `h1` completo se lee "Entrenamiento funcional en 25 de Mayo. Que quieras volver.": tiene las palabras que busca la gente y la tesis.

### 6.2 `<head>`

- `title`: **Entrenamiento funcional en 25 de Mayo | Espacio Funcional 25** (60 caracteres)
- `meta description`: **Entrenamiento funcional en grupos de máximo 7 personas, en el Cuartel de Bomberos de 25 de Mayo. La clase de prueba es gratis: reservala por WhatsApp.** (150 caracteres)
- `meta author`: **Espacio Funcional 25**
- `og:title`: **Espacio Funcional 25 · Entrenamiento funcional en 25 de Mayo**
- `og:description`: **Grupos de máximo 7 personas en el Cuartel de Bomberos, con el Prof. Nicolás Valle. La clase de prueba es gratis: reservala por WhatsApp.** (136 caracteres)
- `og:image:alt`: **Logo de Espacio Funcional 25 sobre naranja con el texto “Entrenamiento funcional en 25 de Mayo”, y una foto del profe con una alumna en el cuartel de bomberos.**
- El precio no va en el `head` ni en la imagen para compartir, porque cambia seguido y tiene que estar en un solo lugar.

### 6.3 Encabezado y menú

- Link de la marca (`.marca`): texto visible **Espacio** / **Funcional 25**; el logo va con `alt=""` porque el texto ya dice el nombre.
- Botón de WhatsApp del encabezado: **WhatsApp** (visible desde 420 px; antes solo para lectores de pantalla). Link: el mensaje 1.
- Botón del menú: **Menú** / **Cerrar**.
- Links del menú: **El enfoque** · **Cómo es la clase** · **Turnos y cuota** · **El profe** · **Dónde estamos**.
- Debajo, en el panel del celular: el botón **Reservá tu clase de prueba gratis** (mensaje 1) y el link **Instagram: @espaciofuncional25**.
- Link para saltar al contenido (el primero del `body`, visible al recibir foco): **Ir al contenido** (a `#contenido`, el `main`).

### 6.4 Portada

```
h1:
  [primera línea]  Entrenamiento funcional en 25 de Mayo
  [tesis]          Que quieras volver.
bajada:            Grupos de máximo 7 personas en el Cuartel de Bomberos: calle 21 Nº 739, entre 8 y 9.
botón (#cta-portada, mensaje 1):  Reservá tu clase de prueba gratis
nota:              Te abre WhatsApp. Pagás recién desde la segunda clase.
ficha:
  dt  Cuota
  dd  (JS) $35.000 por mes
      (JS) 2 clases por semana. Valores de octubre 2026.
      (sin JS) Ver la cuota          → link a #turnos
  dt  Turnos
  dd  (JS) Lunes y jueves: 18 o 19 h
      (JS) Martes y viernes: 7 h
      (sin JS) Ver los turnos        → link a #turnos
```

- Espacios duros: `calle&nbsp;21 Nº&nbsp;739`, `8&nbsp;y&nbsp;9`, `$35.000&nbsp;por mes`, `18&nbsp;a&nbsp;19&nbsp;h`, `7&nbsp;h`.
- Las dos partes del `h1` van en `<span class="h1-que">` y `<span class="h1-tesis">`, separadas por un espacio, y la primera termina en `<span class="sr-only">.</span>`, para que un lector de pantalla haga la pausa.

### 6.5 El enfoque

```
h2:  El enfoque
figure.cita
  blockquote
    p.destacado.cita-facil:    Lo más fácil para un entrenador es simplemente agotarte hasta dejarte sin aire.
    p.destacado.cita-dificil:  Lo difícil, y lo que de verdad importa, es lograr que quieras volver cada semana sin lastimarte entrenando.
  figcaption:  Nicolás Valle
p:   Por eso en Espacio Funcional 25 buscamos:
ul.tildes:
  esfuerzo adaptado al nivel de cada persona
  progresión gradual
  técnica correcta
  entrenamientos sostenibles en el tiempo
p.cierre:  Porque el factor más importante para mejorar no es una sesión intensa, sino la continuidad.
```

La cita es la del reel del 28/07/2026, reconstruida desde los subtítulos (`INDICE.md`): se le agregaron solo las comas. La lista y el cierre son textuales del PDF. Nicolás tiene que confirmar la cita (sección 12).

### 6.6 Cómo es la clase

```
h2:      Cómo es la clase
bajada:  Entrenamos fuerza, resistencia y acondicionamiento físico con ejercicios funcionales, organizados en estaciones de trabajo. Cada clase dura una hora.
h3.etiqueta:  Una vuelta del circuito, por ejemplo
pista (ol):
  SENTADILLAS  — Levantar. Con mancuernas.
  EMPUJES      — Empujar. Press con mancuernas.
  TRACCIONES   — Tirar. Remo con TRX.
  CORE         — Estabilizar. Con la pelota medicinal.
  AERÓBICO     — Moverte. Saltos, cubierta y maza.
p.pista-vuelta:  y otra vuelta
p.por-que:  Cada estación cambia el movimiento, así no cargás siempre la misma parte del cuerpo. Eso permite mantener un buen nivel de esfuerzo sin generar fatiga excesiva y sostener el entrenamiento toda la clase, sin terminar destruido.
.siete:
  span.siete-num:    7
  span.siete-rotulo: personas como máximo por turno
  p:                 Es a propósito. En grupos chicos hay supervisión constante, corrección técnica, adaptación de los ejercicios según tu nivel y seguimiento de tu progreso.
figure: foto clase-circuito
  figcaption:  Una clase en el cuartel: cada uno en su estación, al mismo tiempo.
```

- En el HTML los nombres de estación se escriben en minúscula con mayúscula inicial ("Sentadillas") y el CSS los pasa a mayúscula.
- Cada estación es `<li><span class="estacion-nombre">Sentadillas</span> <span class="estacion-que"><b>Levantar.</b> Con mancuernas.</span></li>`.
- La bajada adapta "¿Qué hacemos?" del PDF; "sin generar fatiga excesiva" viene de "¿Cómo trabajamos?"; "sin terminar destruido" es del reel del 28/07; la lista del 7 sale de "Modalidad de trabajo", y lo de "a propósito", de `TAREAS.md`.

### 6.7 Turnos y cuota

```
h2:  Turnos y cuota
table.turnos
  caption:  Elegís un turno y venís 2 veces por semana. Máximo 7 personas por turno.
  thead (sr-only):  Días | Horario
  Lunes y jueves    | 18 a 19 h
  Lunes y jueves    | 19 a 20 h
  Martes y viernes  | 7 a 8 h
p:  Los días que no venís podés combinar con algo más suave, como caminar o andar en bicicleta.

.cuota
  h3:         Cuota mensual
  p.precio:   $35.000  (span.precio-unidad) por mes
  p.vigencia: Valores de octubre 2026.
  p:          Incluye:
  ul:         2 clases por semana
              planificación del entrenamiento
              seguimiento técnico
              adaptación de los ejercicios según tu nivel
  p.banda:    La clase de prueba es gratis. Empezás a pagar desde la segunda clase.

.complemento
  h3:  Plan complemento
  p:   Un plan personalizado para hacer por tu cuenta: running, fuerza o lo que necesites.
  dl:
    dt  $10.000 extra por mes
    dd  si ya entrenás en el espacio
    dt  $25.000 por mes
    dd  si querés solo el plan, sin venir a las clases
  a.btn.btn--contorno (mensaje 2):  Consultar por el plan complemento
```

### 6.8 El profe

```
h2:  El profe
figure: foto profe-nicolas
p.profe-nombre:  Nicolás Guido Valle
p.profe-titulo:  Profesor en Educación Física y licenciado en Alto Rendimiento Deportivo.
p:   Da clases de Educación Física en escuelas de la zona desde 2017. Es preparador físico de las inferiores de fútbol del Club Atlético Nuevo Globito desde 2022, y entre 2020 y 2022 lo fue de las categorías M12, M14 y M16 de Tacuara Rugby Club.
h3:  Formación
ul:
  Profesor en Educación Física, Instituto Santa Rosa (2017).
  Licenciado en Alto Rendimiento Deportivo, Universidad de San Pablo-Tucumán.
  Seminario interdisciplinario de ejercicio físico para personas con obesidad (2023).
  Curso de RCP y primeros auxilios (2022).
  Tercer dan de karate Goju-Ryu (2025).
```

Todo sale del CV (`fuentes.md`, sección 2), sin datos personales. La licenciatura va sin año, porque el CV dice 2023 y el diploma está fechado el 27/03/2024, y con el nombre de la universidad tal como figura en el diploma. Quedan afuera: los dos años de Medicina, el cargo en el CEF n.º 198, los cursos cortos y la etapa anterior de la marca. No hay años de experiencia contados ni cantidad de alumnos.

### 6.9 Clase de prueba y Dónde estamos

```
h2:  Clase de prueba
p.destacado:  No hace falta que estés en forma para arrancar.
p:   Podés venir a una clase de prueba para conocer cómo trabajamos. Es gratis: se reserva por WhatsApp y empezás a pagar desde la segunda clase.
p:   No necesitás experiencia previa: los ejercicios se adaptan a tu nivel.
botón (#cta-prueba, mensaje 1):  Reservá tu clase de prueba gratis
nota:  Te abre WhatsApp con el mensaje listo.
p:   Si preferís llamar: <a href="tel:+5492345402547">2345-402547</a>

h3#donde:  Dónde estamos
address:
  Cuartel de Bomberos           (700)
  Calle 21 Nº 739, entre 8 y 9
  Veinticinco de Mayo (CP 6660), Buenos Aires
a.btn.btn--contorno (Cómo llegar):  Cómo llegar
  (debajo, nota de 15 px)  Se abre en Google Maps.
a (Instagram):  Instagram: @espaciofuncional25
figure: foto donde-cuartel
```

"No hace falta que estés en forma para arrancar" es del reel del 28/07; "Podés venir a una clase de prueba para conocer cómo trabajamos" es textual del PDF; "No necesitás experiencia previa" y "los ejercicios se adaptan" son del reel del 05/10/2026.

### 6.10 Pie

```
p.pie-marca:  Espacio Funcional 25
p:  Entrenamiento funcional en grupos de máximo 7 personas, en 25 de Mayo.
p:  Prof. Nicolás Guido Valle, Lic. en Alto Rendimiento Deportivo.
p:  Cuartel de Bomberos · Calle 21 Nº 739, entre 8 y 9 · Veinticinco de Mayo (CP 6660), Buenos Aires
p:  WhatsApp: <a>2345-402547</a>   (link al mensaje 1)
p:  Instagram: <a>@espaciofuncional25</a>
p:  © <span id="anio">2026</span> Espacio Funcional 25
```

### 6.11 Barra fija

Botón: **Reservá tu clase de prueba gratis** (mensaje 1), con el ícono de WhatsApp.

### 6.12 Mensajes prellenados de WhatsApp

Los dos dicen que vienen de la página, así Nicolás sabe de dónde llegó cada uno (paso 2 del embudo de `TAREAS.md`). El primero termina en una pregunta, porque un turno está lleno y no sabemos cuál: que Nicolás conteste con el turno libre.

1. **Mensaje 1, clase de prueba** (encabezado, portada, menú, barra fija, "Clase de prueba" y pie):
   > Hola, Nicolás. Vi la página de Espacio Funcional 25 y quiero reservar la clase de prueba gratis. ¿Qué turno tenés libre?

   ```
   https://wa.me/5492345402547?text=Hola%2C%20Nicol%C3%A1s.%20Vi%20la%20p%C3%A1gina%20de%20Espacio%20Funcional%2025%20y%20quiero%20reservar%20la%20clase%20de%20prueba%20gratis.%20%C2%BFQu%C3%A9%20turno%20ten%C3%A9s%20libre%3F
   ```
2. **Mensaje 2, plan complemento:**
   > Hola, Nicolás. Vi la página de Espacio Funcional 25 y quiero consultar por el plan complemento.

   ```
   https://wa.me/5492345402547?text=Hola%2C%20Nicol%C3%A1s.%20Vi%20la%20p%C3%A1gina%20de%20Espacio%20Funcional%2025%20y%20quiero%20consultar%20por%20el%20plan%20complemento.
   ```

Codificados con `urllib.parse.quote(texto, safe='')`. En el HTML van tal cual: no tienen `&`. Los links de WhatsApp, Instagram y Maps no llevan `target="_blank"` (en el celular abren la app). Los de Instagram y Maps llevan `rel="noopener"`.

### 6.13 Texto alternativo de cada imagen

| Imagen | `alt` |
|---|---|
| Logo en encabezado y pie | `""` (el link o el texto de al lado ya dicen el nombre) |
| `portada-profe-corrige` | Nicolás Valle le muestra un ejercicio a una alumna en el cuartel de bomberos, con las autobombas estacionadas atrás. |
| `clase-circuito` | Clase en el cuartel: un alumno hace remo con TRX, una alumna apoya las manos en una pelota medicinal y otra hace una estocada con mancuerna. |
| `profe-nicolas` | Nicolás Valle con el buzo de Espacio Funcional 25 y una pelota de ejercicio naranja, en el cuartel. |
| `donde-cuartel` | Una alumna hace remo con TRX en el salón del cuartel, debajo del letrero de Bomberos Voluntarios. |
| Íconos SVG | `aria-hidden="true"` y `focusable="false"`: el texto de al lado dice qué hacen |

---

## 7. Datos y configuración

### 7.1 Los datos, exactamente como en `TAREAS.md`

| Dato | Valor |
|---|---|
| Turno 1 | Lunes y jueves, 18 a 19 h |
| Turno 2 | Lunes y jueves, 19 a 20 h |
| Turno 3 | Martes y viernes, 7 a 8 h |
| Frecuencia y cupo | 2 clases por semana, se elige un turno, máximo 7 personas por turno |
| Cuota | $35.000 por mes. Incluye 2 clases por semana, planificación, seguimiento técnico y adaptación según nivel |
| Vigencia | Valores de octubre 2026 (supuesto: ninguna fuente lo dice; se confirma con Nicolás) |
| Plan complemento | $10.000 extra por mes si ya entrena en el espacio; $25.000 por mes si no hace funcional (solo el plan) |
| Clase de prueba | Gratis, se reserva por WhatsApp, se paga desde la segunda clase |
| Dirección | Cuartel de Bomberos, Calle 21 Nº 739 e/ 8 y 9, Veinticinco de Mayo (CP 6660), Buenos Aires |
| WhatsApp y teléfono | 2345-402547 → `+5492345402547` |
| Instagram | https://www.instagram.com/espaciofuncional25/ |

### 7.2 Precio y turnos en un solo lugar del código

**La sección "Turnos y cuota" del HTML es la fuente única**, y el texto visible es el dato. No hay copias en `data-` atributos, en el JS ni en el JSON-LD estático. Así no pueden quedar dos valores distintos. JS lee de ahí y completa la ficha de la portada y el JSON-LD. Sin JS, el precio y los turnos se ven igual en su sección, y la ficha de la portada muestra links a `#turnos`.

Hay un cambio respecto de la propuesta sugerida (los `data-` atributos con el valor): si el valor va en un `data-precio="35000"` y también en el texto visible "$35.000", son dos lugares, aunque estén en la misma línea. Acá se marcan los elementos con `data-dato` y el número sale del texto.

Marcado de la fuente (dentro de `#turnos`, con un comentario arriba):

```html
<!-- FUENTE ÚNICA de turnos y precios. Si cambia algo, se cambia acá y nada más.
     Formato: días "Lunes y jueves" (días separados por coma o " y "); horario "18 a 19 h" o "7:30 a 8:30 h";
     precios "$35.000"; vigencia "mes año" en minúscula ("octubre 2026"). -->
<table class="turnos" id="tabla-turnos">
  …
  <tr data-turno><th scope="row" data-dato="dias">Lunes y jueves</th><td data-dato="horario">18&nbsp;a&nbsp;19&nbsp;h</td></tr>
  <tr data-turno><th scope="row" data-dato="dias">Lunes y jueves</th><td data-dato="horario">19&nbsp;a&nbsp;20&nbsp;h</td></tr>
  <tr data-turno><th scope="row" data-dato="dias">Martes y viernes</th><td data-dato="horario">7&nbsp;a&nbsp;8&nbsp;h</td></tr>
</table>
…
<p class="precio"><span data-dato="cuota">$35.000</span> <span class="precio-unidad">por mes</span></p>
<p class="vigencia">Valores de <span data-dato="vigencia">octubre 2026</span>.</p>
<ul><li data-dato="frecuencia">2 clases por semana</li> …</ul>
…
<dt><span data-dato="complemento-con-clases">$10.000</span> extra por mes</dt>
<dt><span data-dato="complemento-solo">$25.000</span> por mes</dt>
```

Lo que hace `js/main.js` (función `leerDatos()`):

- **Precio:** `Number(texto.replace(/\D/g, ''))`. "$35.000" da 35000.
- **Vigencia:** "octubre 2026" → mes por nombre (enero a diciembre) y año → `validFrom: "2026-10-01"`.
- **Días:** se pasa a minúscula, se le sacan las tildes y se separa por `/,|\sy\s/`. Cada día se traduce: lunes → `Monday`, martes → `Tuesday`, miercoles → `Wednesday`, jueves → `Thursday`, viernes → `Friday`, sabado → `Saturday`, domingo → `Sunday`.
- **Horario:** `/(\d{1,2})(?:[:.](\d{2}))?\s*a\s*(\d{1,2})(?:[:.](\d{2}))?/` → `opens: "18:00"`, `closes: "19:00"`.
- **Resumen de la portada** (`[data-copia="turnos"]`): agrupa las filas con el mismo texto de días, en el orden en que aparecen, y une las horas de inicio con " o ". Da `Lunes y jueves: 18 o 19 h` y `Martes y viernes: 7 h`. Cada grupo va en un `<span class="ficha-dato">` en bloque. Si hay minutos, se escriben ("7:30 h").
- **Cuota de la portada** (`[data-copia="cuota"]`): `<span class="ficha-dato">$35.000 por mes</span><span class="ficha-nota">2 clases por semana. Valores de octubre 2026.</span>`. Usa los textos de `cuota`, `frecuencia` y `vigencia`.
- **Errores:** si algo no se puede leer (por ejemplo, un horario mal escrito), no se toca esa mención: queda el link "Ver la cuota" o "Ver los turnos", se avisa con `console.warn` y el JSON-LD sale sin ese campo. Nunca se muestra un dato a medias.

### 7.3 WhatsApp, teléfono y Maps

- **WhatsApp: `https://wa.me/5492345402547`**, con el 9. Es el formato internacional de un celular argentino (+54 9, el área sin 0 y el número sin 15). En las pruebas del relevamiento, `wa.me` lo muestra como "+54 9 2345 40-2547" y WhatsApp Web abre el chat con foto de perfil. El formato sin 9 (el de la bio de Instagram) solo anda si WhatsApp lo corrige. Falta probarlo en un celular: queda para la auditoría de celular. Los links con mensaje están en la sección 6.12.
- **Teléfono:** `tel:+5492345402547`, que se muestra como "2345-402547" (como lo escribe Nicolás en el PDF y en `TAREAS.md`).
- **Instagram:** `https://www.instagram.com/espaciofuncional25/`.
- **Cómo llegar:** `https://www.google.com/maps/dir/?api=1&destination=-35.4387213%2C-60.1711055`, probado en el relevamiento: lleva a la ficha "Bomberos Voluntarios", C. 21 739, que es el cuartel y no el punto "Estación de Bomberos" de una cuadra al norte. En el HTML va con `&amp;`: `https://www.google.com/maps/dir/?api=1&amp;destination=-35.4387213%2C-60.1711055`.
- **Mapa embebido: no va.** Pesa más de 1 MB de Google y suma cookies. Todo 25 de Mayo conoce el Cuartel de Bomberos, y en el celular "Cómo llegar" abre la app de Maps con el recorrido, que sirve más que un mapa chico. Salud en Movimiento carga dos mapas al abrir: 95 descargas y 2 MB. Una fachada que se toca para cargar sería un accesorio más. Si Nicolás lo pide, el embebido probado es `https://www.google.com/maps?q=-35.4387213,-60.1711055&z=17&output=embed`, detrás de un botón "Ver el mapa acá" que crea el `iframe` recién al tocarlo.

### 7.4 El dominio: `espaciofuncional25.com.ar`

Está pendiente elegir entre `.com.ar` y `.com`. Va en el README como pendiente. Aparece solo en estas líneas:

| Archivo | Línea |
|---|---|
| `index.html` | `<link rel="canonical" href="https://espaciofuncional25.com.ar/">` |
| `index.html` | `<meta property="og:url" content="https://espaciofuncional25.com.ar/">` |
| `index.html` | `<meta property="og:image" content="https://espaciofuncional25.com.ar/assets/img/og-espacio-funcional-25.jpg">` |
| `robots.txt` | `Sitemap: https://espaciofuncional25.com.ar/sitemap.xml` |
| `sitemap.xml` | `<loc>https://espaciofuncional25.com.ar/</loc>` |
| `README.md` | título y la línea de pendientes |

No aparece en otros lugares:

- **JSON-LD:** `url`, `@id`, `image` y `logo` los arma JS a partir del `canonical`. El JSON-LD estático no lleva el dominio.
- **`.htaccess`:** la regla de www va sin el dominio: `RewriteCond %{HTTP_HOST} ^www\.(.+)$ [NC]` y `RewriteRule ^(.*)$ https://%1/$1 [R=301,L]`.
- **`twitter:image`:** no se pone, porque X toma `og:image`.

**Cómo cambiarlo de una vez** (probado en Git Bash):

```sh
sed -i 's/espaciofuncional25\.com\.ar/espaciofuncional25.com/g' index.html robots.txt sitemap.xml README.md
grep -rn "espaciofuncional25\.com" --exclude-dir=docs --exclude-dir=.git .
```

---

## 8. SEO local

- `title`, `description`, `og:*` y `twitter:card`: los textos están en la sección 6.2, y el orden del `head`, en la sección 11.
- Open Graph completo:
  - `og:type` `website`, `og:locale` `es_AR`, `og:site_name` `Espacio Funcional 25`;
  - `og:url` y `og:image` absolutos;
  - `og:image:type` `image/jpeg`, `og:image:width` `1200`, `og:image:height` `630` y `og:image:alt`;
  - `twitter:card` `summary_large_image`.
- `h1` con "Entrenamiento funcional en 25 de Mayo"; dirección completa en un `<address>`; "Cuartel de Bomberos" con el link a Maps.
- Más adelante, el Perfil de Empresa de Google apuntando al sitio (ya figura en `TAREAS.md`). Cuando exista, cambiar `hasMap` por la ficha propia.

### JSON-LD

**Estático en el HTML** (`<script type="application/ld+json" id="datos-ld">`), con lo que no cambia y sin el dominio:

```json
{
  "@context": "https://schema.org",
  "@type": "ExerciseGym",
  "name": "Espacio Funcional 25",
  "description": "Entrenamiento funcional en grupos de máximo 7 personas, en el Cuartel de Bomberos de 25 de Mayo, con el Prof. Nicolás Guido Valle, Lic. en Alto Rendimiento Deportivo.",
  "telephone": "+5492345402547",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle 21 Nº 739, entre 8 y 9 (Cuartel de Bomberos)",
    "addressLocality": "Veinticinco de Mayo",
    "addressRegion": "Buenos Aires",
    "postalCode": "6660",
    "addressCountry": "AR"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": -35.4387213, "longitude": -60.1711055 },
  "hasMap": "https://maps.google.com/?cid=8828057531265068567",
  "areaServed": { "@type": "City", "name": "Veinticinco de Mayo" },
  "currenciesAccepted": "ARS",
  "sameAs": ["https://www.instagram.com/espaciofuncional25/"]
}
```

**Completo, después de `js/main.js`** (es lo que ve Google, que ejecuta JS). JS lee el estático, le agrega estos campos y lo vuelve a escribir en el mismo `<script>`. Si JS falla, queda el estático, que es válido.

```json
{
  "@context": "https://schema.org",
  "@type": "ExerciseGym",
  "@id": "https://espaciofuncional25.com.ar/#espacio",
  "name": "Espacio Funcional 25",
  "description": "Entrenamiento funcional en grupos de máximo 7 personas, en el Cuartel de Bomberos de 25 de Mayo, con el Prof. Nicolás Guido Valle, Lic. en Alto Rendimiento Deportivo.",
  "url": "https://espaciofuncional25.com.ar/",
  "image": "https://espaciofuncional25.com.ar/assets/img/og-espacio-funcional-25.jpg",
  "logo": "https://espaciofuncional25.com.ar/assets/img/logo-ef25-512.png",
  "telephone": "+5492345402547",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle 21 Nº 739, entre 8 y 9 (Cuartel de Bomberos)",
    "addressLocality": "Veinticinco de Mayo",
    "addressRegion": "Buenos Aires",
    "postalCode": "6660",
    "addressCountry": "AR"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": -35.4387213, "longitude": -60.1711055 },
  "hasMap": "https://maps.google.com/?cid=8828057531265068567",
  "areaServed": { "@type": "City", "name": "Veinticinco de Mayo" },
  "currenciesAccepted": "ARS",
  "sameAs": ["https://www.instagram.com/espaciofuncional25/"],
  "priceRange": "$35.000 por mes",
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["https://schema.org/Monday", "https://schema.org/Thursday"], "opens": "18:00", "closes": "19:00" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["https://schema.org/Monday", "https://schema.org/Thursday"], "opens": "19:00", "closes": "20:00" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["https://schema.org/Tuesday", "https://schema.org/Friday"], "opens": "07:00", "closes": "08:00" }
  ],
  "makesOffer": [
    {
      "@type": "Offer",
      "name": "Cuota mensual: 2 clases por semana en un turno de máximo 7 personas",
      "price": "35000", "priceCurrency": "ARS", "validFrom": "2026-10-01",
      "priceSpecification": { "@type": "UnitPriceSpecification", "price": "35000", "priceCurrency": "ARS", "unitText": "mes" }
    },
    { "@type": "Offer", "name": "Clase de prueba", "price": "0", "priceCurrency": "ARS" },
    {
      "@type": "Offer",
      "name": "Plan complemento, para quien ya entrena en el espacio",
      "price": "10000", "priceCurrency": "ARS", "validFrom": "2026-10-01",
      "priceSpecification": { "@type": "UnitPriceSpecification", "price": "10000", "priceCurrency": "ARS", "unitText": "mes" }
    },
    {
      "@type": "Offer",
      "name": "Plan complemento, solo el plan",
      "price": "25000", "priceCurrency": "ARS", "validFrom": "2026-10-01",
      "priceSpecification": { "@type": "UnitPriceSpecification", "price": "25000", "priceCurrency": "ARS", "unitText": "mes" }
    }
  ]
}
```

- `url` sale del `canonical`, `@id` es `url + "#espacio"`, y `image` y `logo` son `new URL(ruta, url)`.
- `priceRange` es el texto de la cuota más " por mes".
- Las horas son las de las clases: es lo que vale para alguien que busca cuándo ir.
- No se pone `paymentAccepted` (no se sabe), ni `founder` (la marca la fundaron otros profes en 2018), ni reseñas.

---

## 9. Imágenes: contrato para `assets/img/` (lo ejecuta Codex CLI)

### 9.1 Reglas

- **Originales:** solo de `docs/fotos-instagram/fotogramas-reels/` (fotogramas de 716×1274 de los reels de 2026, todos del cuartel) y el logo de `C:\Users\Juan\Documents\espacio-funcional-25\logo-espacio-funcional-25.png`, que solo se lee y no se copia entero. No se toca ningún original.
- **Nada generado ni rellenado:** sin inpainting, sin quitar ni agregar personas u objetos, sin cielos ni fondos nuevos y sin agrandar (ningún ancho de salida supera el del recorte). El logo no se redibuja. Si alguna salida no se puede lograr con esto, se avisa en vez de inventarla.
- **Script reproducible:** `docs/herramientas/imagenes.py` (Python 3.14 con Pillow, ejecutado sin `-I`), que lee los originales, aplica esta tabla y escribe en `assets/img/`. Al final imprime una tabla con archivo, medidas y peso en KB. Cada salida se mira abierta antes de darla por buena.
- **Orden de cada foto:**
  1. recorte en píxeles del fotograma (`im.crop((x0, y0, x1, y1))`);
  2. corrección de color con los valores de la tabla, al tamaño del recorte;
  3. reducción con `Image.LANCZOS` a cada ancho;
  4. enfoque suave en cada salida: `ImageFilter.UnsharpMask(radius=0.8, percent=35, threshold=2)`;
  5. guardado en WebP con `quality=74, method=6`, sin metadatos.
- **Corrección de color**, igual para cada canal c:
  `v = clip((orig_c × ganancia_c − negro) / (blanco − negro), 0, 1) ^ gamma × 255`, y después `ImageEnhance.Color(img).enhance(saturación)`. Los valores salen de medir una pared blanca de cada fotograma (balance de blancos) y los percentiles 1 y 99 del recorte, y se probaron en la maqueta: aclaran la portada, que está oscura, le sacan el tono rosado a la del profe y le dan contraste a las que tienen los negros lavados. El objetivo es que las paredes del cuartel queden blanco neutro y el piso verde, con su color.

### 9.2 Fotos

| Archivo (sin el ancho) | Original en `fotogramas-reels/` | Recorte (x0, y0, x1, y1) y tamaño | Relación | Qué tiene que quedar adentro y qué afuera | Ganancias R, G, B | Negro y blanco | Gamma | Saturación | Anchos de salida |
|---|---|---|---|---|---|---|---|---|---|
| `portada-profe-corrige` | `2026-07-28_DbUtD7_j4uj_f018s.jpg` | (60, 330, 716, 822) → 656×492 | 4:3 | Adentro: Nicolás entero (cabeza a unos 35 px del borde de arriba), la alumna con la bolsa, las autobombas y la camioneta. Afuera: el logo sobreimpreso (y < 170), el subtítulo (y ≈ 975–1020) y la cara de la alumna acostada a la izquierda (x < 60). Punto focal: entre los dos, en x ≈ 330, y ≈ 160 del recorte. | 0,98 · 1,01 · 1,01 | 10 · 200 | 0,85 | 1,05 | 360, 480, 656 |
| `clase-circuito` | `2026-04-02_DWpl7tBNP0R_f004s.jpg` | (0, 368, 716, 771) → 716×403 | 16:9 | Adentro: el alumno en el TRX, la alumna con las manos en la pelota medicinal, la de la estocada (cortada en el borde izquierdo) y la camioneta "BOMBEROS" al fondo. Afuera: el logo y las salpicaduras blancas de edición de la izquierda (llegan hasta y ≈ 362), las de la derecha (desde y ≈ 790) y el degradé naranja de abajo. Verificado con zoom en los dos bordes. | 0,99 · 1,00 · 1,01 | 24 · 215 | 1,00 | 1,05 | 360, 480, 716 |
| `profe-nicolas` | `2026-07-28_DbUtD7_j4uj_f024s.jpg` | (0, 200, 716, 1095) → 716×895 | 4:5 | Adentro: Nicolás de la cabeza (unos 75 px de aire arriba) a las rodillas, el logo bordado en el buzo, la pelota naranja, las bolsas y las mancuernas. Afuera: el logo sobreimpreso (y < 170). Punto focal: la cara, en x ≈ 385, y ≈ 160 del recorte. | 0,95 · 1,04 · 1,02 | 8 · 225 | 0,95 | 1,00 | 360, 480, 716 |
| `donde-cuartel` | `2026-02-06_DUa7Xy0DthX_f024s.jpg` | (0, 180, 716, 1075) → 716×895 | 4:5 | Adentro: el letrero "BOMBEROS VOLUNTA…" con el escudo, los carteles "CABALLEROS" y "DAMAS", la alumna en el TRX de cuerpo entero y el piso del salón. Este fotograma no tiene texto ni logo agregado. | 0,99 · 0,99 · 1,02 | 34 · 222 | 1,00 | 1,05 | 360, 480, 716 |

Nombres de salida: `assets/img/<archivo>-<ancho>.webp`, por ejemplo `portada-profe-corrige-656.webp`. El alto sale de la relación (redondeado): 4:3 da 360×270, 480×360 y 656×492; 16:9 da 360×203, 480×270 y 716×403; 4:5 da 360×450, 480×600 y 716×895.

**Peso objetivo** (medido en la prueba con calidad 70 a 78): el ancho de 360 pesa 6 a 11 KB, el de 480 pesa 9 a 15 KB y el máximo, 14 a 25 KB. Tope por archivo: 30 KB. Si alguno lo pasa, se baja la calidad a 68.

**`srcset` y `sizes`** (el `img` lleva `width` y `height` del ancho mayor, para que no se mueva la página al cargar):

| Imagen | `sizes` | Carga |
|---|---|---|
| `portada-profe-corrige` | `(min-width: 1200px) 447px, (min-width: 1024px) calc((100vw - 128px) * 5 / 12), (min-width: 656px) 656px, 100vw` | Sin `loading="lazy"`, con `fetchpriority="high"` y `decoding="async"` (asoma en el primer pantallazo del celular). |
| `clase-circuito` | `(min-width: 1200px) 447px, (min-width: 1024px) calc((100vw - 128px) * 5 / 12), (min-width: 764px) 716px, (min-width: 600px) calc(100vw - 48px), calc(100vw - 32px)` | `loading="lazy" decoding="async"` |
| `profe-nicolas` | `(min-width: 1200px) 447px, (min-width: 1024px) calc((100vw - 128px) * 5 / 12), (min-width: 600px) 480px, calc(100vw - 32px)` | `loading="lazy" decoding="async"` |
| `donde-cuartel` | `(min-width: 1200px) 256px, (min-width: 1024px) calc((100vw - 176px) * 3 / 12), (min-width: 600px) 480px, calc(100vw - 32px)` | `loading="lazy" decoding="async"` |

Ejemplo:

```html
<img src="assets/img/portada-profe-corrige-656.webp"
     srcset="assets/img/portada-profe-corrige-360.webp 360w, assets/img/portada-profe-corrige-480.webp 480w, assets/img/portada-profe-corrige-656.webp 656w"
     sizes="(min-width: 1200px) 447px, (min-width: 1024px) calc((100vw - 128px) * 5 / 12), (min-width: 656px) 656px, 100vw"
     width="656" height="492" fetchpriority="high" decoding="async"
     alt="Nicolás Valle le muestra un ejercicio a una alumna en el cuartel de bomberos, con las autobombas estacionadas atrás.">
```

**Alternativas**, por si Nicolás o algún alumno no quiere que se use una foto: para la portada, `2026-02-06_DUa7Xy0DthX_f040s.jpg` (la camioneta roja de bomberos; la cara está movida), recorte (0, 100, 716, 637), 716×537, 4:3; para el profe, `2026-07-30_Dbbmv_gCadM_f016s.jpg`, recorte (0, 0, 716, 895), sin el subtítulo que empieza en y ≈ 1120; para la clase, `2026-07-28_DbUtD7_j4uj_f026s.jpg` (el pasillo con TRX y bolsa), recorte (0, 170, 716, 773). Se tratan con los valores de la fila más parecida y se vuelven a mirar.

### 9.3 Logo

- **Recorte cuadrado sin redibujar:** `im.crop((192, 524, 1054, 1386))` → 862×862, con el centro del círculo (623, 955) en el centro exacto del cuadrado. Queda entero, desvanecido del borde incluido (bbox medido: 194, 525, 1053, 1386). Fuera del círculo todo es transparente. Se reduce con `LANCZOS`, desde el recorte de 862 cada vez y no en cadena.

| Archivo | Medida | Formato | Uso |
|---|---|---|---|
| `assets/img/logo-ef25-64.webp` | 64×64 | WebP con alfa, `quality=90, method=6` | Encabezado 1x |
| `assets/img/logo-ef25-128.webp` | 128×128 | ídem | Encabezado 2x |
| `assets/img/logo-ef25-192.webp` | 192×192 | ídem (unos 13 KB) | Encabezado 3x y pie 2x |
| `assets/img/logo-ef25-288.webp` | 288×288 | ídem | Pie 3x |
| `assets/img/logo-ef25-512.png` | 512×512 | PNG con alfa, optimizado | `logo` del JSON-LD |
| `assets/img/icono-192.png` | 192×192 | PNG con alfa | `<link rel="icon" sizes="192x192">` (Android) |
| `apple-touch-icon.png` (en la raíz) | 180×180 | PNG **opaco**: fondo `#FF7B02` y el logo de 164×164 pegado en (8, 8) | iPhone (no admite transparencia) |
| `favicon.ico` (en la raíz) | 16, 32 y 48 | ICO con alfa: `img.save('favicon.ico', sizes=[(16,16),(32,32),(48,48)])` | Pestaña |

- Encabezado: `<img src="assets/img/logo-ef25-128.webp" srcset="assets/img/logo-ef25-64.webp 64w, assets/img/logo-ef25-128.webp 128w, assets/img/logo-ef25-192.webp 192w" sizes="(min-width: 1024px) 56px, 44px" width="44" height="44" alt="">`, sin `lazy`. Desde 1024 px el CSS lo lleva a 56×56.
- Pie: `srcset` con 128, 192 y 288, `sizes="72px"`, `width="72" height="72"`, `loading="lazy"`.
- **¿Hace falta un SVG? No.** El PNG original es bueno: se probó a 48 px y se lee el disco naranja con el anillo blanco y el dibujo. El uso más grande en pantalla es la imagen para compartir, a 224 px, y el recorte de 862 px lo cubre de sobra. Un SVG "fiel" obligaría a redibujar el pictograma, que tiene bordes blandos y una figura que ni siquiera se lee del todo clara (`fuentes.md`, sección 4), y eso es justo lo que el brief pide evitar. Tampoco hay `favicon.svg`.
- Sobre fondo naranja, el aro naranja exterior del logo se funde con el fondo y el borde que se ve es el anillo blanco. Está bien así, y es el mismo efecto que en el apple-touch-icon.

### 9.4 Imagen para compartir: `assets/img/og-espacio-funcional-25.jpg`

- **1200×630, JPEG con `quality=86`, de 150 KB como máximo.** La prueba pesó 100 KB.
- Se arma con una plantilla HTML, `docs/herramientas/og/og.html`, que usa las mismas fuentes del sitio (`../../../assets/fonts/…`) y se captura con Playwright (`p.chromium.launch(channel="chrome")`, viewport de 1200×630, `device_scale_factor=1`, esperando `document.fonts.ready`). Así la tipografía es la real y no hay texto dibujado a mano. Los archivos intermedios quedan en `docs/herramientas/og/`.
- Composición (probada):

```
┌────────────────────────────────────────────────────────────┬┬──────────────────┐
│  (◉ logo 224×224 en x 64, y 56)                            ││                  │
│                                                            ││  foto real       │
│  Entrenamiento funcional          ← display 800 de 68 px,  ││  420×630         │
│  en 25 de Mayo                      interlineado .92, en    ││  (Nicolás y la   │
│                                     x 64, y 318             ││  alumna, con las │
│  Grupos de máximo 7 · Cuartel de Bomberos  ← Atkinson Next ││  autobombas)     │
│  Clase de prueba gratis por WhatsApp         700 de 28 px,  ││                  │
│                                              y 478          ││                  │
└────────────────────────────────────────────────────────────┴┴──────────────────┘
   fondo #FF7B02, texto #000                                 línea negra de 6 px en x 774–780
```

- Foto: `2026-07-28_DbUtD7_j4uj_f018s.jpg`, recorte (180, 228, 654, 939) → 474×711 (2:3), con la misma corrección de color que `portada-profe-corrige`, reducida a 420×630 (no se agranda) y guardada como `docs/herramientas/og/og-foto-420x630.jpg`.
- Logo: recorte de 862 reducido a 224×224, en `docs/herramientas/og/logo-224.png`.
- Medido: "Entrenamiento funcional" a 68 px ocupa unos 620 px, y la línea de 28 px, 575 px. Las dos entran en los 660 px del campo naranja.
- No lleva precio (cambia) ni nada generado: la foto es real.

### 9.5 Lo que tiene que dejar listo el agente de imágenes

```
assets/img/portada-profe-corrige-{360,480,656}.webp
assets/img/clase-circuito-{360,480,716}.webp
assets/img/profe-nicolas-{360,480,716}.webp
assets/img/donde-cuartel-{360,480,716}.webp
assets/img/logo-ef25-{64,128,192,288}.webp
assets/img/logo-ef25-512.png
assets/img/icono-192.png
assets/img/og-espacio-funcional-25.jpg
apple-touch-icon.png
favicon.ico
docs/herramientas/imagenes.py
docs/herramientas/og/og.html, og-foto-420x630.jpg, logo-224.png
```

En total son 21 archivos para el sitio: 19 en `assets/img/` más `favicon.ico` y `apple-touch-icon.png` en la raíz. Ninguna imagen del sitio es generada; el README lo dice en "Fotos".

---

## 10. Mobile first y rendimiento

- **CSS desde el celular:** la base es para 360 a 390 px y todo lo demás se agrega con `@media (min-width: …)` (600, 1024, 1200 y 1440). No hay ningún `max-width` en las media queries.
- **Sin desborde horizontal:** `html, body { overflow-x: clip }` como red de seguridad, pero la auditoría tiene que dar `scrollWidth === innerWidth` a 360 sin depender de eso. Las fotos a sangre usan `margin-inline: calc(var(--gutter) * -1)`, no `100vw`.
- **Toques:** botones y links de al menos 44 px de alto (el principal, 56). Los links dentro de texto llevan relleno vertical o son de línea propia.
- **Foco:** contorno de 3 px, negro sobre naranja, blanco y cal, y blanco sobre negro, con `outline-offset: 3px`. Con `scroll-padding` arriba y abajo, nada con foco queda tapado por el encabezado o la barra.
- **Contraste:** todo AA o más (tabla de la sección 2).
- **Idioma y carga:** `<html lang="es-AR">`. `<meta name="format-detection" content="telephone=no">`: el teléfono ya tiene su `tel:` y así iOS no cambia el estilo de otros números. `<meta name="color-scheme" content="light">`.
- **Imágenes:** WebP con `srcset`, `sizes`, `width` y `height`. `loading="lazy"` en todas las que están debajo del pliegue (clase, profe, dónde y el logo del pie); la de la portada y el logo del encabezado, no.
- **Fuentes:** WOFF2 con `font-display: swap` y respaldo ajustado (sección 2). Se precarga solo la del titular: `<link rel="preload" href="assets/fonts/big-shoulders-display-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>`.
- **Sin librerías:** nada de frameworks, iconos externos, analytics, Google Fonts ni mapas. Los íconos van en un sprite SVG inline (`<symbol>`): `i-whatsapp`, `i-instagram`, `i-telefono`, `i-mapa`, `i-tilde` y `i-flecha`.
- **CSS y JS** con versión en la URL (`?v=AAAAMMDD`, la fecha de la construcción) y `defer` en el script.
- **Presupuesto de peso.** Las fotos y fuentes están medidas; HTML, CSS y JS son topes.

| Primer pantallazo del celular | Tope |
|---|---|
| `index.html` | 30 KB sin comprimir (unos 9 con gzip) |
| `css/style.css` | 20 KB |
| `js/main.js` | 8 KB |
| Las 3 fuentes | 39,4 KB |
| Logo del encabezado (192 o 128) | 13 KB |
| Foto de la portada (656) | 22 KB |
| **Total del primer pantallazo** | **menos de 150 KB transferidos, en 8 pedidos** |
| **Total de la página entera** | **menos de 300 KB**, contra los 6,4 MB de GAN, los 17,7 MB de 5Zurdo y los 0,4 MB de AB |

---

## 11. Archivos del sitio

Siguen la estructura de pablospata-website.

```
espacio-funcional-25-website/
├─ index.html
├─ css/style.css
├─ js/main.js
├─ assets/
│  ├─ fonts/
│  │  ├─ big-shoulders-display-latin-800-normal.woff2
│  │  ├─ atkinson-hyperlegible-next-latin-400-normal.woff2
│  │  ├─ atkinson-hyperlegible-next-latin-700-normal.woff2
│  │  ├─ LICENSE-big-shoulders-display.txt
│  │  └─ LICENSE-atkinson-hyperlegible-next.txt
│  └─ img/                      (los 19 archivos de la sección 9.5)
├─ favicon.ico
├─ apple-touch-icon.png
├─ docs/                        no se publica (404 en .htaccess y Disallow en robots.txt)
│  ├─ plan.md                   este archivo
│  ├─ relevamiento/             fuentes.md, referencias.md, referencias/ (capturas de terceros)
│  ├─ fotos-instagram/          originales e índice (fuera del repo: ver .gitignore)
│  ├─ herramientas/             capturas.py, contraste.py, imagenes.py, og/
│  └─ auditoria/                capturas e informes de las auditorías
├─ README.md
├─ .htaccess
├─ robots.txt
├─ sitemap.xml
└─ .gitignore
```

**`index.html`.** El `head` va en este orden:

1. `<!doctype html>`, `<html lang="es-AR">`, `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">`;
2. `color-scheme` `light`, `theme-color` `#FF7B02`, `format-detection` `telephone=no`;
3. `title`, `description`, `author`;
4. `canonical`;
5. los `og:*` y `twitter:card`;
6. los íconos: `<link rel="icon" href="favicon.ico" sizes="48x48">`, `<link rel="icon" href="assets/img/icono-192.png" type="image/png" sizes="192x192">` y `<link rel="apple-touch-icon" href="apple-touch-icon.png">`;
7. la precarga de la fuente del titular;
8. `css/style.css?v=…`, `js/main.js?v=…` con `defer`;
9. el JSON-LD estático `#datos-ld`.

El `body` lleva, en orden:

- el link "Ir al contenido";
- el sprite SVG oculto;
- `header.cabecera` con `.marca`, el WhatsApp, el botón del menú y `nav#menu`;
- `main#contenido` con las secciones `#inicio`, `#enfoque`, `#clase`, `#turnos`, `#profe` y `#prueba`;
- `footer.pie`;
- `div#barra`.

Todo el texto es el de la sección 6.

**`css/style.css`.** En este orden:

1. `@font-face`;
2. `:root` con los tokens;
3. base: `box-sizing`, `body` con `font: var(--t-cuerpo)/1.5 var(--texto)`, color negro y fondo blanco; `img { display: block; max-width: 100%; height: auto }`; `.sr-only`; `:focus-visible`; el link para saltar al contenido;
4. componentes:
   - `.contenedor`;
   - `.btn` (negro, texto blanco 700, 56 px de alto, radio 6, ícono de 22 px, separación de 8 px y 14 px de relleno por lado; en hover, `--negro-hover`);
   - `.btn--contorno` (transparente, borde de 3 px negro y texto negro; en hover, fondo negro y texto blanco);
   - `.btn-chico`, `.ficha`, `.pista`, `.siete`, `.turnos`, `.cuota`, `.banda`, `.complemento`, `.tildes`;
5. secciones, en el orden de la página;
6. encabezado y menú;
7. barra fija;
8. media queries de 600, 1024, 1200 y 1440;
9. el bloque de movimiento, dentro de `prefers-reduced-motion: no-preference`.

Cuidado con la especificidad: los espacios de sección se ponen solo con `.seccion` y su modificador (`.seccion--naranja`, `--blanca`, `--cal`), nunca con selectores de elemento que compitan con `.btn` o `.ficha`.

**`js/main.js`.** Una IIFE sin dependencias, con `$` y `$$`, que hace en orden:

1. `ponerMenu()` y sus eventos (sección 4.2);
2. la barra fija con `IntersectionObserver` (sección 4.3);
3. `leerDatos()`, que completa `[data-copia]` y arma el JSON-LD (secciones 7.2 y 8);
4. el circuito, con `.en-vista` (sección 5);
5. el año en `#anio`.

Cada parte va en su propio `try`, así un error en una no rompe las otras. Si no hay `IntersectionObserver`, la barra queda visible y no hay animación.

**`.htaccess`:**

```apache
RewriteEngine On
# www a sin www (sin el dominio escrito: sirve para .com.ar y para .com)
RewriteCond %{HTTP_HOST} ^www\.(.+)$ [NC]
RewriteRule ^(.*)$ https://%1/$1 [R=301,L]
# /index.html a /
RewriteCond %{THE_REQUEST} \s/+(.*/)?index\.html[\s?] [NC]
RewriteRule ^(.*/)?index\.html$ /$1 [R=301,L]
# material interno: no se sirve
RedirectMatch 404 ^/docs(/|$)
RedirectMatch 404 ^/_mobile-(frame|preview)\.html$
RedirectMatch 404 ^/README\.md$
RedirectMatch 404 ^/\.git(/|$)
RedirectMatch 404 ^/\.gitignore$
AddDefaultCharset UTF-8
AddType font/woff2 .woff2
AddType image/webp .webp
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html "access plus 0 seconds"
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType text/javascript "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType image/webp "access plus 30 days"
  ExpiresByType image/png "access plus 30 days"
  ExpiresByType image/jpeg "access plus 30 days"
  ExpiresByType image/x-icon "access plus 30 days"
</IfModule>
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript text/javascript application/xml text/plain image/svg+xml
</IfModule>
```

El CSS y el JS van con versión en la URL, por eso pueden cachearse un año. Las imágenes cambian de contenido sin cambiar de nombre (por ejemplo, si llegan las fotos originales), así que van a 30 días. El paso de HTTP a HTTPS se activa en el panel de Hostinger ("Forzar HTTPS"), no acá, para no arriesgar un bucle de redirecciones.

**`robots.txt`:**

```
User-agent: *
Allow: /
Disallow: /docs/
Sitemap: https://espaciofuncional25.com.ar/sitemap.xml
```

**`sitemap.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://espaciofuncional25.com.ar/</loc>
    <lastmod>AAAA-MM-DD</lastmod>
  </url>
</urlset>
```

`lastmod` es la fecha del último cambio de contenido.

**`.gitignore`:**

```
_mobile-preview.html
_mobile-frame.html
*.log
.DS_Store
docs/fotos-instagram/
```

La última línea es nueva respecto de pablospata-website. La carpeta tiene fotos de alumnos, antes y después de cuerpos, y menores (`INDICE.md`, "Privacidad"), y el repo va a GitHub. Las originales quedan en el disco, pero no en el repo. Si la carpeta ya se agregó al índice de git, el orquestador la saca con `git rm -r --cached docs/fotos-instagram`.

**`README.md`.** Mismo formato que el de pablospata-website:

1. `# espaciofuncional25.com.ar` (con "(dominio pendiente: .com.ar o .com)");
2. la línea de estado;
3. un párrafo: qué es y para qué;
4. **Qué hay**, un ítem por archivo o carpeta;
5. **Cómo verlo**: `python -m http.server 8802 --bind 127.0.0.1` y `http://127.0.0.1:8802/`;
6. **Cómo cambiar el precio, los turnos o el dominio**: la sección 7, resumida en tres pasos;
7. **Decisiones tomadas sin Nicolás (revisar)**: la sección 12;
8. **Fotos**: de dónde sale cada una, que no hay imágenes generadas y qué falta (permiso de alumnos, originales);
9. **Qué falta**;
10. **Preguntas para Nicolás**: la lista de la sección 12.

**Capturas de las auditorías,** en `docs/auditoria/`:

- `01-movil-360x740-pliegue.jpg` y `02-movil-390x844-pliegue.jpg`;
- `03-movil-390-parteN.jpg`;
- `04-movil-menu-abierto.jpg`;
- `05-movil-boton-fijo.jpg` (con la barra visible, a mitad de página y al final del pie);
- `06-compu-1366x768-pliegue.jpg` y `07-compu-1920x1080-pliegue.jpg`;
- `08-compu-1366-parteN.jpg`;
- `NN-zoom-*.jpg`, por ejemplo `09-zoom-circuito-390.jpg` y `10-zoom-circuito-1366.jpg`.

La ronda final va en `docs/auditoria-final/`.

---

## 12. Decisiones tomadas sin Nicolás y preguntas

### Decisiones tomadas sin Nicolás (revisar)

1. **Titular: "Que quieras volver."**, de su reel, con "Entrenamiento funcional en 25 de Mayo" arriba. Se probó contra cinco alternativas (sección 6.1).
2. **Su frase del reel del 28/07/2026 como cita en El enfoque**, reconstruida desde los subtítulos, con comas agregadas. Puede faltar alguna palabra.
3. **WhatsApp con el 9 (`wa.me/5492345402547`)**, no el `542345402547` de la bio. Se probó en WhatsApp Web y en wa.me; falta probarlo en un celular.
4. **Mensaje prellenado nuevo**, que dice "Vi la página de Espacio Funcional 25" (para saber de dónde vino cada uno) y pregunta qué turno tiene libre, en vez de "Escribime y....¡Empecemos a entrenar!".
5. **"Valores de octubre 2026"**: el mes del precio es un supuesto.
6. **Precio y turnos en la página**, con la sección "Turnos y cuota" como única fuente. La portada y los datos para Google los copia el JS de ahí.
7. **La clase dibujada como un circuito de ejemplo** con cinco estaciones en el orden del PDF y el material que se ve en sus videos. No se dicen tiempos ni cantidad de vueltas.
8. **Bio:** la licenciatura va sin año (el CV dice 2023 y el diploma 27/03/2024) y con el nombre del diploma ("Universidad de San Pablo-Tucumán"). Quedan afuera Medicina, el cargo en el CEF n.º 198 y los cursos cortos.
9. **No se cuenta la etapa anterior de la marca** (2018–2022, con otros profes y en otros lugares), y no se usa ninguna foto anterior a 2026.
10. **Fotos de alumnos que se reconocen** en la portada, el circuito y Dónde estamos, con la autorización de Nicolás para usar las de Instagram. Si alguien no quiere, hay alternativas en la sección 9.2.
11. **No se ofrecen "personalizados"**, porque no están en `TAREAS.md` (sí en algunas placas de 2026).
12. **El teléfono para llamar es el mismo número** (`tel:+5492345402547`).
13. **Sin mapa embebido**: solo el botón "Cómo llegar", que abre Google Maps en la ficha del cuartel.
14. **No se dice cuántos lugares quedan por turno**, porque habría que actualizarlo cada vez.
15. **La barra fija de WhatsApp no se ve mientras está a la vista el botón de la portada o el de "Clase de prueba"**, para no repetir el mismo botón en la misma pantalla. El resto del tiempo está siempre abajo.
16. **El botón dice "Reservá tu clase de prueba gratis"**, y "pagás recién desde la segunda clase" va justo debajo y en la tarjeta de la cuota. No entra en el botón sin partirlo en dos líneas a 360 px.
17. **Tipografía de texto:** Atkinson Hyperlegible Next en vez de Atkinson Hyperlegible (misma familia, versión nueva).
18. **`docs/fotos-instagram/` fuera del repo** (en `.gitignore`), por las fotos de alumnos y menores.
19. **Dominio `espaciofuncional25.com.ar`**, pendiente de confirmar. Cambiarlo es un `sed` (sección 7.4).

### Preguntas para Nicolás

1. ¿El dominio va con `.com.ar` (a tu nombre, con tu CUIT, en NIC Argentina) o `.com`?
2. ¿Los $35.000 son los valores de octubre 2026?
3. ¿Cuál de los tres turnos está lleno?
4. ¿Los alumnos que se ven en las fotos de la portada (la alumna con la bolsa), del circuito y del TRX bajo el letrero están de acuerdo, o preferís fotos sin caras?
5. ¿Nos pasás los videos originales de los reels del 28/07, 06/02 y 02/04 (sin texto y en la calidad del celular) y, si tenés, una foto de la entrada del cuartel?
6. ¿La licenciatura es de 2023 o de 2024?
7. ¿Está bien tu frase del video tal como la escribimos ("Lo más fácil para un entrenador es simplemente agotarte…")? ¿Y el resto del texto?
8. ¿El 2345-402547 atiende llamadas, o solo WhatsApp?
9. ¿Seguís dando entrenamiento personalizado aparte del plan complemento?
10. ¿Cómo se paga la cuota (efectivo, transferencia, Mercado Pago)? ¿Qué hay que llevar a la clase de prueba? ¿Pedís apto médico?
11. ¿Querés que la bio diga los dos años de Medicina en la UBA o tu cargo en el CEF n.º 198?
