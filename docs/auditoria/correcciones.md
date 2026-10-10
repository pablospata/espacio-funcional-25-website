# Correcciones de las auditorías · Espacio Funcional 25

10/10/2026 · 58 hallazgos de las cinco auditorías (celular, compu, copy, datos, accesibilidad y rendimiento): **53 corregidos y 5 pendientes**. No se descartó ninguno, pero en algunos se usó un arreglo distinto del propuesto (se explica en cada fila) · cambios en `index.html`, `css/style.css`, `js/main.js`, `sitemap.xml`, `README.md` (nuevo), `docs/diseno.md` y `docs/plan.md` · sin commit · capturas en `docs/auditoria/correcciones/`

Cada hallazgo se reprodujo antes de tocarlo, y cada arreglo se volvió a medir con Playwright y el Chrome instalado (154). Los scripts están en el scratchpad de la sesión (`corr/`).

- Los datos siguen iguales a `TAREAS.md`.
- El precio sigue en un solo lugar: el bloque "Turnos y cuota" de `index.html`.
- Ningún texto nuevo agrega información sin fuente.

## Verificación final

| Qué | Resultado |
|---|---|
| axe-core 4.10.2 (wcag2a/aa, 21a/aa, 22aa, best-practice) | **0 violaciones** en 360 y 390 (inicial, cursos abiertos, menú abierto, barra visible) y en 1366 (inicial, cursos). Antes había 1: `region` en `#barra`. |
| Desborde horizontal | Ninguno en 320, 340, 360, 390, 414, 600, 768, 1024, 1366 y 1920. Tampoco a 1024 con la barra de scroll de Windows. |
| Tocables de menos de 44 px | Ninguno. Antes estaba "$35.000" de la portada (74×28); ahora toda la celda es el área táctil. |
| Texto tapado (`elementFromPoint`, de 320 a 1366) | Ninguno. "El profe" queda con 32 px de aire debajo del disco, de 320 a 1023. Solo aparecen "Cuota" y "por mes" debajo del área táctil transparente de la cuota, que no se ve. |
| Contraste a píxel (390 y 1366) | Pasan todos. Antes fallaba "El profe" (4,08:1). El script marca el "." `sr-only` del titular, que no se ve. |
| Menú del celular (360 y 390) | Enter abre, el Tab entra a "Enfoque" y recorre el panel, y al salir del encabezado se cierra. Escape cierra y devuelve el foco al botón. Tocar un link, la marca o fuera del panel lo cierra. Si queda abierto y se baja hasta perderlo de vista, se cierra solo y vuelve la barra. |
| Botón fijo (360 y 390) | Barrido de scroll de a 10 px de punta a punta: **en todas las posiciones hay un botón de reserva de WhatsApp entero a la vista**. Antes faltaba entre 6420 y 6740 y entre 7530 y 7640 px a 360. Escondida, la barra no recibe el foco; ningún foco queda debajo de ella ni fuera de la pantalla. |
| Bolita del circuito | 0 layout shifts en 8 s (antes, 21). Cae centrada en cada parada (±0,4 px) a 390, 1024, 1366 y 1920. |
| Espaciado de texto (WCAG 1.4.12) a 320, 360 y 390 | Nada se pisa. La marca no se mete debajo de los botones. |
| Sin JS | Los datos de la portada dicen "Cuota · Ver · más abajo". Con `main.js` retenido ya dicen "$35.000 · por mes". |

## Hallazgos

| Id | Gravedad | Estado | Qué se hizo |
|---|---|---|---|
| COPY-1 | grave | corregido | La bajada de Cómo es la clase dice ahora «…en estaciones de trabajo que alternan patrones de movimiento.». `p.por-que` pasa a ser «Alternar patrones de movimiento permite mantener un buen nivel de esfuerzo sin generar fatiga excesiva, y que puedas sostener el entrenamiento durante toda la clase sin terminar destruido.». Es casi textual del PDF; "sin terminar destruido" es del reel del 28/07. En vez del «Eso permite» propuesto se repite el sujeto, porque después de la pista no queda claro a qué se refiere "eso". |
| A11Y-1 | grave | corregido | `.profe-foto { margin-bottom: 12.5% }` en la base y `0` desde 64em. La foto deja abajo el lugar que ocupa el disco: 32 px de aire hasta "El profe" de 320 a 1023, y desde 1024 no cambia nada. `cel-360-el-profe.jpg`, `cel-390-el-profe.jpg`, `tablet-600-el-profe.jpg`, `tablet-768-el-profe.jpg`. |
| CEL-1 | media | corregido | `.boton { text-wrap: balance }` y, hasta 383 px, `.boton--naranja, .boton--tinta { padding-inline: 1rem; gap: .5rem }`. A 360 los cuatro botones van en una línea: 56 px de alto y barra de 73 px (antes, 67 y 88). A 320 y 340 se parten en «Reservá tu clase / de prueba gratis». `cel-360-portada.jpg`, `cel-320-portada.jpg`, `cel-360-menu-abierto.jpg`, `cel-360-barra-a-mitad.jpg`. |
| CEL-2 | media | corregido | Con el arreglo de A11Y-1. El `gap: 3.5rem` propuesto no alcanzaba entre 600 y 1023 px. |
| CEL-3 | media | corregido | `actualizarBarra()` cierra el menú cuando el panel queda entero arriba de la pantalla (`menu.getBoundingClientRect().bottom < 0`). Se usa el panel y no la cabecera para que no se cierre mientras todavía se ve. Medido: con scroll de 300 sigue abierto; con 800 se cierra, `aria-expanded="false"` y vuelve la barra. |
| CEL-4 | media | corregido | La barra se esconde solo mientras `#cta-final` se ve entero, y aparece apenas `#cta-portada` empieza a salir. El arreglo propuesto (esconderla desde que aparece el botón final hasta abajo) dejaba sin botón el tramo entre el botón negro y el pie. Además contradecía la decisión 15 del plan: "El resto del tiempo está siempre abajo". Barrido: 0 posiciones sin botón. `cel-360-bloque-final.jpg`, `cel-360-donde-con-barra.jpg`. |
| PC-1 | media | corregido | `@media (min-width: 64em) and (max-height: 47.5em)` compacta la portada como se propuso: titular de 84 px en dos líneas, foto de 480 px de alto máximo y sello más arriba. A 1366×630 los datos terminan en y 603. Con 768 px o más de alto queda igual que antes. `compu-1366x630-pliegue.jpg`, `compu-1366x768-pliegue.jpg`, `compu-1024x640-pliegue.jpg`. |
| PC-2 | media | corregido | `.menu a { white-space: nowrap }` desde 64em, y `.cabecera .contenedor { gap: 1.25rem }` entre 64 y 72em. Con la barra de scroll visible, a 1024, 1030, 1040, 1100, 1152 y 1160, los cinco links miden 44 px (un renglón) y no hay desborde. `compu-1024-cabecera-con-barra-de-scroll.jpg`. |
| PC-3 | media | corregido | Desde 64em, `#profe { overflow: clip }` y `.profe-foto { position: sticky; top: 6.5rem }`. A 1366 la foto queda en y 104 mientras se lee la trayectoria y se suelta al final. Foto y disco entran en una ventana de 768 px. `compu-1366-profe-arriba.jpg`, `compu-1366-profe-a-mitad-foto-fija.jpg`. |
| COPY-2 | media | corregido | Los rótulos dicen ahora «Lo más fácil para un entrenador» y «Lo difícil, y lo que de verdad importa». Van en una línea de 320 a 1920. `cel-390-enfoque.jpg`, `compu-1366-enfoque.jpg`. |
| COPY-3 | media | corregido | Con el arreglo de A11Y-1. El `z-index` propuesto dejaba el rótulo encima del naranja: 4,08:1, y a 600–768 px el disco quedaba entero detrás del texto. |
| COPY-4 | media | corregido | Nuevo `alt` de la foto de la clase: «Una clase en el cuartel: un alumno hace remo con TRX contra la pared y una alumna, en cuatro apoyos, apoya una mano sobre una pelota medicinal. Atrás se ve una camioneta de Bomberos.». Se comparó con `clase-568.webp`. |
| COPY-5 | media | corregido | `README.md` nuevo, con "Decisiones tomadas sin Nicolás (revisar)": las frases exactas de la cita, "Valores de octubre de 2026", "¿Preferís llamar?", "Y otra vuelta", el CEF y los cursos, la síntesis de la bio y los apellidos sin tilde. También tiene las preguntas para Nicolás. La sección 12 de `docs/plan.md` quedó marcada como vieja y remite al README. |
| DAT-1 | media | corregido | La cuota de la portada la copia un `<script>` corto al final del `<body>`, antes de `main.js`, leyendo `#precio-cuota`. Con `main.js` retenido ya dice "$35.000 · por mes". Sin JS dice «Ver» y «más abajo»: el `small` lleva `data-copia="cuota-unidad"` y el script lo cambia por «por mes». El precio sigue en un solo lugar. `dat1-datos-sin-js-390.png`, `dat1-portada-main-js-demorado-390.png`. |
| A11Y-2 | media | corregido | `.barra { visibility: hidden; transition: transform .25s ease, visibility 0s linear .25s }` y `.barra.visible { visibility: visible; transition: transform .25s ease }`. En movimiento reducido, `transition: none` para las dos. `html { scroll-padding-bottom: calc(var(--barra) + .5rem) }` debajo de 64em. Escondida no recibe el foco; visible, sí. |
| A11Y-3 | media | corregido | Se resolvió con el orden del HTML (CEL-9) y no moviendo el foco. Además, `focusout` en la cabecera cierra el menú cuando el foco sale. Medido: Enter → Tab va a "Enfoque", y después del último ítem el foco pasa a la portada con el menú cerrado. |
| A11Y-4 | media | pendiente | **Decisión de Pablo.** Es real (CLS 0,086–0,090 en 4G lento), pero precargar Barlow 400 y 600 contradice el brief ("precarga solo de la del titular") y `docs/diseno.md`. El CLS medido está por debajo de 0,1. Anotado en el README. |
| CEL-5 | menor | corregido | `.marca { min-width: 0 }`, `.marca span { text-wrap: balance }` (sin `nowrap`). Hasta 352 px, `gap: .5rem` en la cabecera y en la marca, y la marca a 16 px. A 320 la marca va en una línea y termina en x 199; el botón empieza en 208. |
| CEL-6 | menor | corregido | `.dato:first-child { position: relative }` y `.dato dd a::after { content: ""; position: absolute; inset: 0 }`. Toda la celda de la cuota es tocable y no cambia cómo se ve. |
| CEL-7 | menor | corregido | `nowrap` en "Espacio Funcional 25" (pegado a "buscamos:" con `&nbsp;`), "San Pablo-Tucumán", "Goju-Ryu", "Karate-Do", "CEF Nº 198", "Prof. Nicolás Guido Valle", "calle 21 Nº 739" y "Veinticinco de Mayo" del pie. `&nbsp;` en "Buenos Aires", "CP 6660", "7 personas", "Yo Sé" y "19 h"/"7 h". `text-wrap: pretty` en `li, dt, dd, address, figcaption`; `balance` en `.cupo-num span`, `.trayectoria dd`, `.complemento-precios dt` y `.incluye li`. En vez del guion U+2011 se usó `nowrap`, para no depender de que el subconjunto de Barlow tenga ese glifo. Medido: ninguna de esas frases se parte de 320 a 1920. |
| CEL-8 | menor | corregido | El cierre por toque es `!menu.contains(e.target) && !boton.contains(e.target)`. Tocar la marca cierra el menú. |
| CEL-9 | menor | corregido | El link de WhatsApp con ícono y el botón del menú pasaron antes del `<nav id="menu">`. No cambia nada visible ni en el celular ni en la compu. Orden de Tab: marca, WhatsApp, menú, (links del menú), portada. |
| CEL-10 | menor | corregido | Con el arreglo de A11Y-2. Escondida, la barra tiene `visibility: hidden` y no está en el árbol de accesibilidad. |
| PC-4 | menor | corregido | `.pista { grid-template-columns: repeat(5, minmax(0, 1fr)) 9rem }` y `.pista b { font-size: clamp(1.75rem, 2.9vw, 2.125rem) }` desde 64em. Columnas de 160 px a 1024, de 175 a 1100 y de 211 desde 1280, sin desbordes. `compu-1024-pista.jpg`. |
| PC-5 | menor | corregido | `.pista .vuelta svg { left: -.25rem }` desde 64em. El centro del ícono queda a 9 px, como los puntos, y la bolita termina centrada (Δx = 0). |
| PC-6 | menor | corregido | Desde 64em, el pie de foto va con `position: absolute; top: 100%` y `.clase-lado` tiene `padding-bottom: 2rem`. La foto y la tarjeta del 7 terminan juntas: y 2405 a 1024, 2438 a 1100 y 2460 desde 1280. `compu-1366-clase.jpg`. |
| PC-7 | menor | corregido | Desde 600 px (el hueco también estaba a 600 y 768: 128 y 133 px), `.tarjeta--blanca` es flex en columna, `.horarios` es una grilla de filas iguales y cada turno se centra en su fila con baseline. Así las líneas quedan a mitad de camino entre turnos; el `space-evenly` propuesto las pegaba al turno de abajo. La nota queda abajo. `compu-1366-turnos.jpg`, `tablet-768-turnos.jpg`. |
| PC-8 | menor | corregido | `@supports (overflow: clip) { .banda { overflow: clip visible } }`. La banda tiene el mismo espesor de punta a punta. `compu-1920-banda.jpg`. |
| PC-9 | menor | corregido | `.sello { right: -1rem }` entre 64 y 85em. Le quedan 12 px de aire a la caja girada a 1024 y a 1280; a 1366 queda como antes. `compu-1024-sello.jpg`, `compu-1280-sello.jpg`. |
| PC-10 | menor | corregido | `.enfoque { align-items: start }` desde 64em. El título y el texto arrancan en y 960 a 1024, 1366 y 1920. |
| PC-11 | menor | corregido | `--naranja-2` pasa de `#F26F00` a `#E06500`: el texto tinta queda a 5,10:1 y el hover se distingue del normal a 1,34:1 (antes, 1,15:1). "$35.000" y "Cursos y capacitaciones" se subrayan con el hover. `compu-1366-hover-boton.jpg`. |
| PC-12 | menor | pendiente | Los `sizes` de las cuatro fotos se corrigieron para que coincidan con lo que miden de verdad en tablet y compu (clase, profe, dónde y portada en tablet). No se angostó la columna de la foto de la clase: es un cambio de layout para un estiramiento del 10 %. **Para 2x hacen falta originales de 1080 px o más** (pregunta para Nicolás). |
| PC-13 | menor | corregido | La cabecera de la compu es opaca: se sacó `background: rgb(255 255 255 / .96)` y queda el `--blanco` de la base. Con la página quieta se ve igual, y al bajar ya no se ve la banda detrás del menú. `compu-1366-cabecera-sobre-banda.jpg`. |
| COPY-6 | menor | pendiente | **Pregunta para Nicolás:** ¿se hace más de una vuelta? Si no, el rótulo pasa a «Y la estación siguiente». Anotado en el README. |
| COPY-7 | menor | corregido | La bio dice ahora «Da clases de Educación Física en escuelas de la zona desde 2017 y, desde 2022, es preparador físico de las inferiores de fútbol de Nuevo Globito. En el espacio planifica los entrenamientos y corrige la técnica de cada uno.» |
| COPY-8 | menor | corregido | «En escuelas de la zona, en todos los niveles de la educación obligatoria, y en el CEF», como en el CV. |
| COPY-9 | menor | corregido | Con el arreglo de CEL-1: a 360 entra en una línea y en menos de 360 se parte parejo. |
| COPY-10 | menor | corregido | Con el arreglo de DAT-1: sin JS se lee «Cuota · Ver · más abajo». |
| COPY-11 | menor | corregido | `<span id="precio-vigencia" data-desde="2026-10-01">octubre de 2026</span>`. El JSON-LD copia «valores de octubre de 2026». Que el mes es un supuesto quedó en el README. |
| COPY-12 | menor | corregido | «CEF Nº 198», con la forma de `TAREAS.md`, dentro de `nowrap`. Ya no hay "n.º". Con CEL-7, no se parten San Pablo-Tucumán ni Buenos Aires. `cel-390-trayectoria-y-cursos.jpg`, `cel-390-donde.jpg`. |
| COPY-13 | menor | corregido | «infantojuvenil». "Entrenamiento intermitente" y "Sistemas de entrenamiento" (Cantidad de Calidad, 2020) pasaron a ser dos ítems, como en el CV: ahora la lista tiene 13 cursos. Las tildes de Añón y González quedan como pregunta para Nicolás. |
| COPY-14 | menor | corregido | Las dos listas van de lo más nuevo a lo más viejo. Experiencia: 2025 – hoy, 2022 – hoy, 2017 – hoy, 2021 – 2022 y 2020 – 2022. Formación: 2025, 2023, 2020 y 2017. |
| COPY-15 | menor | corregido | «Los días que no venís, podés combinar el entrenamiento con algo más suave, como caminar o andar en bicicleta.». Se escribió el objeto en vez de «combinarlo», que no tenía un antecedente claro. |
| COPY-16 | menor | corregido | La oferta del JSON-LD se llama «Plan complemento, solo el plan (sin las clases)». |
| DAT-2 | menor | corregido | Se mantiene el diseño, para que el precio no esté en dos lugares. El README explica que `main.js` completa el precio del JSON-LD y que hay que verificarlo con la Prueba de resultados enriquecidos cuando se publique. |
| DAT-3 | menor | corregido | `oferta()` agrega `validFrom` (de `data-desde`) y `unitCode: 'MON'`. El JSON-LD final tiene las cuatro ofertas con `validFrom: 2026-10-01`. |
| DAT-4 | menor | corregido | `"streetAddress": "Calle 21 739"`. La dirección visible no cambia. |
| DAT-5 | menor | corregido | En el pie, el link dice «Instagram @espaciofuncional25». `cel-390-pie.jpg`. |
| DAT-6 | menor | corregido | `README.md` con el dominio pendiente y sus 9 lugares (y el `sed` para pasar a `.com`), cómo cambiar la cuota y la nota de DAT-2. |
| DAT-7 | menor | corregido | Con el `alt` de COPY-4. |
| A11Y-5 | menor | corregido | `<aside class="barra" id="barra" aria-label="Reservar la clase de prueba">`. axe ya no marca `region`. |
| A11Y-6 | menor | corregido | Con el arreglo de CEL-5: con espaciado de texto a 390, la marca termina en x 266 y el botón empieza en 276. |
| A11Y-7 | menor | corregido | `.dato dd` sin `nowrap`, y `&nbsp;` en "19 h" y "7 h". Con espaciado de texto, "18 y 19 h" pasa a dos renglones y no se pisa con "7 h". No se usó `overflow-wrap: anywhere` porque partía el precio en "$35.00 / 0". `cel-390-datos-con-espaciado-de-texto.jpg`. |
| A11Y-8 | menor | corregido | `<span class="signo" aria-hidden="true">` dentro del `summary`, con el "+" y el "–" en su `::after`. El árbol de accesibilidad dice «Cursos y capacitaciones», con `expanded` true o false. |
| A11Y-9 | menor | pendiente | **Decisión de Pablo:** cambia un comportamiento aprobado (la bolita "vuelve a empezar"). Opciones en el README. |
| A11Y-10 | menor | corregido | Los keyframes animan `transform: translateY/translateX(var(--dN))` y `main.js` carga `--d1…--d5` con la distancia pura. 0 layout shifts en 8 s a 390 y a 1366. Se ve igual. |
| A11Y-11 | menor | corregido | `fetchpriority="high"` en la imagen de la portada. Chrome la pide con prioridad High a 390 y a 1366 (antes, Low). |
| A11Y-12 | menor | pendiente | **Decisión de Pablo:** `docs/imagenes.md` eligió logos sin pérdida a propósito, y regenerar `assets/` está fuera de lo que se tocó en esta etapa. Anotado en el README. |

## Preguntas para Nicolás que salieron de estas correcciones

Están todas en el README, sección "Preguntas para Nicolás":

- ¿Se hace más de una vuelta del circuito? (COPY-6)
- ¿Los valores son de octubre de 2026? (COPY-11)
- ¿Añón y González llevan tilde? (COPY-13)
- ¿Hay videos o fotos originales de 1080 px o más? (PC-12)

## Capturas (`docs/auditoria/correcciones/`)

- **Celular:**
  - `cel-320-portada.jpg`, `cel-360-portada.jpg`, `cel-390-portada.jpg` (marca, botón y datos);
  - `cel-360-menu-abierto.jpg`;
  - `cel-*-el-profe.jpg`;
  - `cel-*-barra-a-mitad.jpg`;
  - `cel-*-bloque-final.jpg` (el botón negro entero, sin barra) y `cel-*-donde-con-barra.jpg` (la barra vuelve);
  - `cel-390-enfoque.jpg`, `cel-390-clase-bajada-y-pista.jpg`, `cel-390-clase-por-que.jpg`, `cel-390-turnos.jpg`, `cel-390-trayectoria-y-cursos.jpg`, `cel-360-trayectoria.jpg`, `cel-390-donde.jpg`, `cel-390-pie.jpg`;
  - `cel-360-datos-portada.jpg` y `cel-390-datos-con-espaciado-de-texto.jpg`;
  - `dat1-datos-sin-js-390.png` y `dat1-portada-main-js-demorado-390.png`.
- **Tablet:** `tablet-600-el-profe.jpg`, `tablet-768-el-profe.jpg`, `tablet-600-turnos.jpg`, `tablet-768-turnos.jpg`.
- **Compu:**
  - `compu-1366x630-pliegue.jpg`, `compu-1366x768-pliegue.jpg`, `compu-1024x640-pliegue.jpg`, `compu-1920x950-pliegue.jpg`;
  - `compu-1024-cabecera-con-barra-de-scroll.jpg` y `compu-1366-cabecera-sobre-banda.jpg`;
  - `compu-1366-enfoque.jpg`, `compu-1366-clase.jpg`, `compu-1366-turnos.jpg`;
  - `compu-1366-profe-arriba.jpg` y `compu-1366-profe-a-mitad-foto-fija.jpg`;
  - `compu-1024-pista.jpg`, `compu-1280-pista.jpg`, `compu-1024-sello.jpg`, `compu-1280-sello.jpg`, `compu-1920-banda.jpg`, `compu-1366-hover-boton.jpg`.

Las capturas por elemento (`cel-390-turnos.jpg`, `cel-390-trayectoria-y-cursos.jpg` y otras) se sacaron con la barra fija escondida. Playwright hace scroll para capturar el elemento y la dejaba encima, cosa que no pasa al leer la página.
