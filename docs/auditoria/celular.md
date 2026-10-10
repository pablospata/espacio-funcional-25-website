# Auditoría de celular · Espacio Funcional 25

10/10/2026 · sitio en `http://127.0.0.1:8802/` (commit `c8960e6`) · 360×740 y 390×844, más controles en 320, 340 y 360×640 · capturas en `docs/auditoria/celular/`

## Cómo se revisó

- Capturas con `docs/herramientas/capturas.py` (Chrome 154, `is_mobile` y `has_touch` activados): una por pantallazo con `--partes`, el menú con `--clic ".menu-boton"`, la barra fija con `--scroll`, el detalle con `--dpr 3` y el movimiento con `--reducido`.
- Mediciones con scripts propios de Playwright sobre la página real:
  - desborde horizontal;
  - alto y ancho de cada `a`, `button` y `summary`;
  - cortes de línea palabra por palabra y cadenas que no se tienen que partir;
  - geometría de la pista, el sello y los discos;
  - menú: Escape, link, tocar afuera y `aria-expanded`;
  - botón fijo: cuándo aparece y cuándo se esconde.
- Los arreglos de CEL-1, CEL-2 y CEL-5 se probaron inyectando el CSS propuesto en el navegador, sin tocar los archivos del sitio.
- No se propone ningún cambio de diseño: todo lo de abajo son defectos dentro del diseño aprobado.

## Resumen

El celular está bien resuelto en lo importante:

- No hay desborde horizontal en 320, 360 ni 390.
- El primer pantallazo cuenta qué es, dónde, cuánto sale y los horarios, con el botón de la clase de prueba a la vista.
- El menú abre, cierra con Escape, con un link o tocando afuera, y lleva bien a cada sección.
- La pista del circuito está alineada al píxel.
- Precios, horarios y teléfono nunca se parten.

Hay **4 defectos de gravedad media**:

1. El botón principal se parte en dos líneas a 360 px y deja "gratis" sola.
2. El disco naranja del profe atraviesa el rótulo "El profe".
3. Si abrís el menú y bajás sin cerrarlo, desaparece el botón fijo de WhatsApp en toda la página.
4. Hay un tramo de unos 320 px, justo al empezar el bloque final, en el que no se ve ningún botón de WhatsApp.

Además hay 6 defectos menores: cortes de línea, un área táctil chica, foco y el encabezado por debajo de 351 px.

## Primer pantallazo: qué entra exactamente

**360×740** (`01-360x740-parte1.jpg`, detalle en `06-360x740-encabezado-dpr3.jpg`). Medidas en px desde arriba:

| Elemento | Posición | Entra |
|---|---|---|
| Encabezado: logo, "Espacio Funcional 25", botón de WhatsApp y botón del menú | 0–65 | entero |
| "Entrenamiento funcional en 25 de Mayo" (qué es y dónde) | 93–111 | entero |
| Titular "Que quieras volver." con la cinta | hasta 246 | entero |
| Bajada: "Grupos de máximo 7 personas en el Cuartel de Bomberos: calle 21 Nº 739, entre 8 y 9." | 260–342 | entera |
| Botón "Reservá tu clase de prueba gratis", **en 2 líneas** (ver CEL-1) | 370–437 | entero |
| "Te abre WhatsApp. Pagás recién desde la segunda clase." | 449–493 | entera |
| Datos: Cuota **$35.000** por mes · Tarde **18 y 19 h**, lunes y jueves · Mañana **7 h**, martes y viernes | 529–645 | enteros |
| Sello "$0" | 640–774 | la mitad de arriba |
| Foto de la portada | desde 685 | el borde de arriba |

Se cumple el trabajo de la página sin bajar: qué es, dónde, cuánto sale, horarios y el botón de la clase gratis.

En un celular real el alto útil es menor que 740, porque restan la barra de estado y la de direcciones (`07-360x640-primer-pantallazo-alto-util.jpg`):

- **Con 640 px** se lee todo; solo se corta el borde de abajo de la caja de datos (5 px).
- **Con 600 px** (el navegador interno de Instagram) se ven los montos pero se cortan "por mes", "lunes y jueves" y "martes y viernes".
- El arreglo de CEL-1 sube los datos 11 px, que terminan entonces en 634.

**390×844** (`02-390x844-parte1.jpg`): entra lo mismo. El botón va en una línea y los datos terminan en 608. Además entran el sello entero y el tercio de arriba de la foto.

## Lo que está bien (medido)

- **Desborde horizontal:** `scrollWidth` es igual a `innerWidth` en 320, 360 y 390. Lo único que pasa del ancho es la tira de la banda inclinada, que recorta `.banda` a propósito. No hay textos que se salgan de su caja.
- **Encabezado a 360:**
  - Marca de 211 px, botón de WhatsApp y botón del menú de 44×44 cada uno, con 19 px de aire entre la marca y el de WhatsApp.
  - No se aprieta ni se corta. Por debajo de 351 px sí (CEL-5).
- **Menú:** `03-360x740-menu-abierto.jpg`, `04-390x844-menu-abierto.jpg`.
  - `aria-expanded` pasa de `false` a `true` y vuelve, y `aria-label` cambia entre "Abrir el menú" y "Cerrar el menú".
  - Escape lo cierra y devuelve el foco al botón; tocar un link o tocar afuera también lo cierra.
  - Links de 52 px de alto.
  - Cada link deja su sección a 16 px del borde de arriba, con el título visible: "El enfoque" a 104 px, "Cómo es la clase" y "Turnos y cuota" a 80, "Nicolás Guido Valle" a 556 y "Dónde estamos" a 241 (`10-…-menu-link-turnos.jpg`, `11-…-menu-link-enfoque.jpg`).
- **Botón fijo:**
  - Aparece justo cuando el botón de la portada sale de pantalla: a 360 está escondido con 432 px de scroll y visible con 442; a 390, con 393 y 403 (`13-360x740-barra-a-mitad.jpg`, `14-390x844-barra-a-mitad.jpg`, `18-360x740-barra-dpr3.jpg`).
  - Se esconde en el bloque naranja (`15-…-barra-escondida-bloque-final.jpg`) y con el menú abierto.
  - Abajo de todo el pie entero se ve y se lee: el último renglón termina a 624 de 740 y a 728 de 844, sin la barra encima (`16-…`, `17-…`). Recorriendo la página de a 40 px, en ningún momento la barra queda sobre el pie.
- **Pista del circuito:**
  - Línea, paradas, bolita e ícono de "Y otra vuelta" están centrados en la misma vertical (x = 25 px) en 360 y en 390.
  - Con la animación frenada en cada parada (19 %, 39 %, 59 %, 79 % y 97 % de los 7 s), la bolita queda a menos de 0,5 px del centro de cada parada y del ícono de la vuelta.
  - La línea termina justo en el centro del ícono de la vuelta, que la tapa con su fondo blanco.
  - Capturas a 1,5 s (en Empujes), 3 s (saliendo de Tracciones) y 5 s (llegando a Aeróbico): `20-*-pista-*-dpr3.jpg`.
  - Con `--reducido` no hay animación y la bolita queda quieta sobre Sentadillas (`21-360x740-pista-reducido-dpr3.jpg`, `19-360x740-reducido.jpg`).
- **Cinta, sello y disco de la portada a 360:**
  - La cinta no toca las colas de la "Q" ni de la "q" (`30-360-titular-cinta-dpr3.jpg`).
  - El disco del sello empieza 6 px debajo de la caja de datos: su caja cuadrada se toca con los datos, pero el círculo no. Termina en x = 346, así que no se corta, y el texto circular se lee entero (`31-360-sello-datos-dpr3.jpg`).
  - El disco naranja de la portada termina donde empieza la banda y no tapa la etiqueta "En el Cuartel de Bomberos" (`32-360-foto-portada-disco-banda-dpr3.jpg`).
- **Precios, horarios y teléfono no se parten nunca:** "$35.000", "$10.000", "$25.000", "18 y 19 h", "18 a 19 h", "19 a 20 h", "7 a 8 h", "2345-402547" y "21 Nº 739".
- **tel: y Maps:**
  - `tel:+5492345402547` ("¿Preferís llamar? 2345-402547"): 99×44 px.
  - "Cómo llegar" en la tarjeta: 155×48. "Cómo llegar" del pie: 77×44.
  - Los dos de Maps van a `google.com/maps/dir/?api=1&destination=-35.4387213,-60.1711055`.
  - El resto de lo tocable mide 44 px o más, salvo el link de la cuota (CEL-6).

## Hallazgos

| Id | Gravedad | Qué |
|---|---|---|
| CEL-1 | media | El botón "Reservá tu clase de prueba gratis" se parte en 2 líneas a 360 px, con "gratis" sola |
| CEL-2 | media | El borde del disco naranja atraviesa el rótulo "El profe" |
| CEL-3 | media | Con el menú abierto y bajando, el botón fijo no aparece nunca |
| CEL-4 | media | Al entrar al bloque final hay ~320 px de scroll sin ningún botón de WhatsApp a la vista |
| CEL-5 | menor | Por debajo de 351 px, el "25" de la marca queda debajo del botón de WhatsApp |
| CEL-6 | menor | El link "$35.000" de la portada mide 28–30 px de alto |
| CEL-7 | menor | Cortes de línea feos: la marca, guiones de nombres propios y palabras solas |
| CEL-8 | menor | Tocar la marca con el menú abierto no lo cierra |
| CEL-9 | menor | Al abrir el menú, el foco salta al contenido y no a los links del menú |
| CEL-10 | menor | El botón fijo escondido sigue siendo enfocable |

### CEL-1 · media · El botón principal se parte en dos líneas a 360 px

**Dónde:**

- `.boton`: `css/style.css:71-77`.
- Botones afectados: `#cta-portada` (`index.html:104`), el botón del menú (`:84`), la barra (`:335`) y `#cta-final` (`:303`).

**Problema:** a 360 px los cuatro botones de la clase de prueba quedan "Reservá tu clase de prueba / gratis", con la palabra clave sola en el segundo renglón. La barra fija pasa de 73 px de alto a 88 y tapa más contenido mientras se lee.

**Evidencia:**

- El texto mide 262,3 px y el lugar disponible es de 248: 328 de botón menos 48 de padding, 10 de espacio y 22 del ícono.
- A 390 hay 278 y entra.
- Capturas: `01-360x740-parte1.jpg`, `03-360x740-menu-abierto.jpg`, `13-360x740-barra-a-mitad.jpg`, `01-360x740-parte11.jpg` y `06-360x740-encabezado-dpr3.jpg`.

**Arreglo:**

```css
@media (max-width: 23.99em) { .boton:has(svg) { padding-inline: 1rem; gap: .5rem; } }
.boton { text-wrap: balance; }
```

- Quedan 266 px para el texto. Probado: los cuatro botones van en una línea a 360 (`40-360-prueba-arreglo-boton-una-linea.jpg`).
- A 320, donde no entra igual, `balance` lo parte en "Reservá tu clase / de prueba gratis".

### CEL-2 · media · El disco naranja del profe atraviesa el rótulo "El profe"

**Dónde:**

- `.profe { gap: 2rem }`: `css/style.css:260`.
- `.profe-foto::before { bottom: -10% }`: `css/style.css:262`.
- El rótulo: `index.html:254`.

**Problema:** el disco sale 41 px debajo de la foto a 360 y 44,7 px a 390, pero el texto arranca a 32 px. El borde del disco corta "El profe" por la mitad: arriba gris sobre naranja, abajo gris sobre blanco. Casi no se lee, sobre todo a 390.

**Evidencia:**

- El 36 % del área del texto queda sobre el disco a 360 y el 51 % a 390.
- Capturas: `33-360-disco-profe-antetitulo-dpr3.jpg`, `34-390-disco-profe-antetitulo-dpr3.jpg`, `01-360x740-parte8.jpg` y `02-390x844-parte7.jpg`.

**Arreglo:** correr el texto debajo del disco sin mover el disco. La regla de ≥ 64em ya pisa el `gap`. Hay dos opciones:

- **La más simple:** `.profe { gap: 3.5rem; }` en la base. Probado: deja 15 px de aire a 360 y 11 a 390.
- **La proporcional,** que también sirve entre 600 y 1023 px: `.profe-foto { margin-bottom: calc(12.5% - 1rem); }` en la base y `margin-bottom: 0` en ≥ 64em. El disco sale el 10 % del alto de la foto, que es el 12,5 % de su ancho.

### CEL-3 · media · Con el menú abierto y bajando, el botón fijo no aparece nunca

**Dónde:** `js/main.js:95-96`. `actualizarBarra` esconde la barra mientras exista la clase `menu-abierto`.

**Problema:** el encabezado no es fijo en el celular. Si alguien abre el menú y en vez de tocar un link baja con el dedo, el menú queda abierto fuera de pantalla y el botón de WhatsApp no vuelve en toda la página hasta que suba y lo cierre.

**Evidencia:**

- Script: con el menú abierto y 2500 px de scroll, el menú ya no está en pantalla, sigue `aria-expanded="true"` y la barra está escondida. Pasa igual en 360 y en 390.
- Captura: `12-360x740-menu-abierto-y-bajar.jpg`, sin barra.

**Arreglo:** cerrar el menú cuando el encabezado sale de pantalla, al principio de `actualizarBarra`:

```js
if (cabecera.classList.contains('menu-abierto') && cabecera.getBoundingClientRect().bottom < 0) { abrirMenu(false); return; }
```

`abrirMenu(false)` vuelve a llamar a `actualizarBarra`.

### CEL-4 · media · Al entrar al bloque final no hay ningún botón de WhatsApp a la vista

**Dónde:** `js/main.js:93-94`.

```js
var enFinal = r.top < window.innerHeight && r.bottom > 0;
```

`r` es el rectángulo de toda la sección `#prueba`.

**Problema:** la barra se esconde apenas asoma la franja de chevrones del bloque naranja. El botón negro de ese bloque está unos 330 px más abajo, después del título de tres renglones y el párrafo. En ese tramo, justo en el remate ("No hace falta que estés en forma para arrancar."), no hay botón de WhatsApp en pantalla. El brief pide el botón "siempre visible abajo".

**Evidencia:**

- Barrido de scroll de a 10 px buscando links a wa.me visibles.
- A 360 no hay ninguno entre 6420 y 6740 px de scroll, y otra vez entre 7530 y 7640.
- A 390 no hay ninguno entre 6040 y 6360.
- Captura: `15-360x740-barra-escondida-bloque-final.jpg`.

**Arreglo:** esconder la barra recién cuando aparece el botón del bloque final y dejarla escondida hasta el final:

```js
var enFinal = document.getElementById('cta-final').getBoundingClientRect().top < window.innerHeight;
```

Sigue escondida dentro del bloque naranja, como está aprobado.

### CEL-5 · menor · Por debajo de 351 px el "25" de la marca queda debajo del botón de WhatsApp

**Dónde:** `.marca` y `.marca span { white-space: nowrap }`: `css/style.css:90-92`.

**Problema:** el encabezado entra justo a 360 (19 px de aire), pero no tiene margen. En celulares Android con el tamaño de pantalla o el zoom aumentado (común en gente grande) el ancho baja a 320–340 px, y ahí el botón tapa la marca.

**Evidencia:**

| Ancho | Solape del botón sobre la marca |
|---|---|
| 340 px | 0,9 px |
| 320 px | 21 px |

Capturas: `08-340-encabezado-solapado-dpr3.jpg` y `35-320x568-parte1.jpg`.

**Arreglo:**

```css
@media (max-width: 22em) { .marca { gap: .5rem; min-width: 0; } .marca span { font-size: 1rem; } }
```

Probado: quedan 6,5 px de aire a 320 y 26,5 px a 340. No cambia nada desde 352 px.

### CEL-6 · menor · El link "$35.000" de la portada es chico para tocar

**Dónde:** `.dato dd a` (`css/style.css:129`), en `index.html:108`.

**Problema:** es el único elemento tocable de menos de 44 px. Sin JavaScript, además, dice "Ver".

**Evidencia:**

- 74×28 px a 360 y 81×30 a 390.
- Captura: `31-360-sello-datos-dpr3.jpg`.

**Arreglo:** que toda la celda de la cuota sea el área táctil, sin cambiar cómo se ve:

```css
.dato:first-child { position: relative; }
.dato dd a::after { content: ""; position: absolute; inset: 0; border-radius: inherit; }
```

La celda mide 109×116 px.

### CEL-7 · menor · Cortes de línea feos

**Problema:** se parte la marca, se parten nombres propios en el guion y quedan palabras solas al final de renglón. Precios, horarios y teléfono están bien.

**Evidencia:**

| Ancho | Corte | Dónde | Captura |
|---|---|---|---|
| 360 | "Por eso en Espacio Funcional / 25 buscamos:" | `index.html:151` | `11-360x740-menu-link-enfoque.jpg` |
| 360 | "Tercer dan de karate Goju- / Ryu" | `index.html:273` | `01-360x740-parte10.jpg` |
| 360 | "Traditional Okinawan Goju- / Ryu Karate-Do Federation" | `index.html:273` | `01-360x740-parte10.jpg` |
| 360 y 390 | "Universidad de San Pablo- / Tucumán" | `index.html:270` | `02-390x844-parte8.jpg` |
| 360 y 390 | "Prof. Nicolás Guido / Valle" | `index.html:330` | `01-360x740-parte12.jpg`, `02-390x844-parte10.jpg` |
| 360 y 390 | "máximo 7 / personas" | `index.html:324` | `01-360x740-parte12.jpg`, `02-390x844-parte10.jpg` |
| 390 | "Veinticinco de Mayo (CP 6660), Buenos / Aires" | `index.html:310` | `02-390x844-parte10.jpg` |
| 390 | "7 personas como máximo por / turno" | `index.html:193` | `02-390x844-parte4.jpg` |
| 390 | "Solo el plan, sin venir a las / clases" | `index.html:239` | `02-390x844-parte6.jpg` |

Palabras solas al final en listas, a 360: "persona", "tiempo", "espacio", "Física" (×2), "funcional", "Globito", "Argentina" y los años "(2024)" y "(2023)" de los cursos (`09-360x740-cursos-abiertos.jpg`).

**Arreglo:**

- `<span class="nowrap">` en "Espacio Funcional 25", "Buenos Aires", "Nicolás Guido Valle" y "7 personas".
- Guion que no se parte (U+2011) en Goju‑Ryu, Karate‑Do y San Pablo‑Tucumán.
- `text-wrap: pretty` también en `li, dt, dd, address` (hoy solo lo tiene `p`).
- `text-wrap: balance` en `.cupo-num span`.

### CEL-8 · menor · Tocar la marca con el menú abierto no lo cierra

**Dónde:** `js/main.js:29-31`. Solo cierra si el toque es fuera de toda la cabecera.

**Problema:** al tocar el logo o el nombre con el menú abierto, la página salta a `#contenido` (49 px) y el menú queda abierto.

**Evidencia:** script: después del toque, `aria-expanded="true"` y `scrollY` 49, en 360 y en 390.

**Arreglo:**

```js
if (cabecera.classList.contains('menu-abierto') && !menu.contains(e.target) && !boton.contains(e.target)) abrirMenu(false);
```

### CEL-9 · menor · Al abrir el menú, el foco salta al contenido y no a los links

**Dónde:** `index.html:76-91`. El `<nav id="menu">` está en el HTML antes que el botón de WhatsApp y el del menú.

**Problema:** con teclado, o con TalkBack o VoiceOver (que siguen el orden del HTML), después de "Cerrar el menú" lo siguiente es el contenido de la página. Los links del menú quedan "atrás".

**Evidencia:** script: se abre el menú con Enter y Tab lleva a "Reservá tu clase de prueba gratis" de la portada, después a "$35.000" y después a "Consultar por el plan". Nunca pasa por "Enfoque".

**Arreglo:** mover en el HTML los dos `<a>`/`<button>` de íconos (`index.html:87-91`) antes del `<nav id="menu">`.

- En el celular el menú es `position: absolute`, así que no cambia nada visible.
- En la compu esos dos íconos están ocultos.

### CEL-10 · menor · El botón fijo escondido sigue siendo enfocable

**Dónde:** `.barra` (`css/style.css:317-323`). Se esconde solo con `transform: translateY(110%)`.

**Problema:** arriba de todo y en el bloque final, el link de la barra está fuera de pantalla pero se puede enfocar con Tab y lo anuncia el lector de pantalla.

**Evidencia:** script: con la barra escondida, `visibility: visible`, `tabIndex 0`, sin `inert` ni `aria-hidden`.

**Arreglo:**

```css
.barra { visibility: hidden; transition: transform .25s ease, visibility 0s linear .25s; }
.barra.visible { visibility: visible; transition: transform .25s ease; }
```

En `prefers-reduced-motion` queda `transition: none`, como ahora.

## Capturas

| Archivo | Qué muestra |
|---|---|
| `01-360x740-parte1…12.jpg`, `02-390x844-parte1…10.jpg` | Pantallazos de toda la página |
| `03`, `04`, `05` | Menú abierto (el 05 se pidió a mitad de página: el clic sube hasta la cabecera, que no es fija) |
| `06` | Encabezado y portada a 360 con dpr 3 |
| `07` | Alto útil de 640 |
| `08`, `35` | Encabezado a 340 y página a 320 |
| `09` | Cursos abiertos |
| `10`, `11` | Destino de los links del menú |
| `12` | Menú abierto y bajando (CEL-3) |
| `13`–`18` | Barra fija: a mitad de página, escondida en el bloque final y abajo de todo |
| `19`, `21` | Movimiento reducido |
| `20-*` | Pista a 1,5, 3 y 5 s |
| `30`–`34` | Cinta, sello, disco de la portada y disco del profe con dpr 3 |
| `40` | CEL-1 con el arreglo inyectado |
