# Auditoría de compu · Espacio Funcional 25

10/10/2026 · sitio servido en `http://127.0.0.1:8802/` · Chrome instalado vía Playwright · capturas en `docs/auditoria/compu/`

## Cómo se revisó

- **Tamaños:** 1366×768 y 1920×1080 (primer pantallazo, por partes y página completa), más un vistazo a 1024×768, 1100×800, 1280×800 y 1440×900.
- **Alto real de notebook:** 1366×630 y 1536×730.
- **Barra de scroll de Windows:** Playwright la esconde por defecto. Acá se prendió con `ignore_default_args=["--hide-scrollbars"]`, y ocupa 15 px.
- **Además:** DPR 1 y 2, teclado (Tab y Shift+Tab), hover, la animación del circuito congelada en 11 momentos y el encabezado con las fuentes bloqueadas.
- **Medidas:** salen de scripts de Playwright con `getBoundingClientRect`.
- **Arreglos probados:** los de PC-1 a PC-10 se probaron inyectando el CSS en la página, y las medidas de "después" salen de esa prueba.
- **Diseño:** el aprobado no se toca. Los arreglos cambian medidas o alineaciones, no colores, tipografías ni motivos.

## Resumen

En compu no hay nada roto de fondo:

- no hay scroll horizontal en ningún ancho;
- al tocar los links del menú, cada sección queda 19 px por debajo del encabezado fijo y ningún título queda tapado;
- el foco se ve en los 19 elementos que se pueden enfocar;
- el circuito está alineado al píxel en todas las paradas menos la última.

Lo que hay que arreglar, por orden:

1. **PC-1 (media):** en una notebook 1366×768 real, con la barra de Chrome y la de tareas, la cuota y los horarios de la portada quedan debajo del pliegue.
2. **PC-2 (media):** con la barra de scroll de Windows, a 1024 px los links "La clase", "Turnos y cuota" y "El profe" se parten en dos líneas.
3. **PC-3 (media):** en "El profe" la columna de la foto queda vacía entre 550 y 815 px, y más de 1100 px si se abre la lista de cursos.
4. **Alineación (menores):**
   - **PC-4:** a 1024 las paradas del circuito quedan desparejas.
   - **PC-5:** la bolita termina corrida respecto del ícono final.
   - **PC-6:** la foto de la clase y la tarjeta del 7 no terminan a la misma altura.
   - **PC-7:** la tarjeta "Turnos" tiene un hueco abajo.
   - **PC-8:** la banda inclinada queda cortada en recto en los extremos.
   - **PC-9:** el sello "$0" queda pegado al borde de la pantalla.
   - **PC-10:** en "El enfoque" el texto arranca antes que el título.
5. **Otras menores:**
   - **PC-11:** el hover de los botones naranjas casi no se ve.
   - **PC-12:** las fotos se estiran en pantallas 2x.
   - **PC-13:** lo que pasa por detrás se transparenta en el encabezado.

## Lo que está bien (verificado)

- **Sin desborde horizontal.** `scrollWidth` es igual a `clientWidth` en 1024, 1100, 1280, 1366, 1440 y 1920, con y sin barra de scroll.
- **Menú en línea a 1024, sin barra de scroll.**
  - Medidas: la marca termina en x 280, los links van de 317 a 809 y el botón WhatsApp de 841 a 984. Los 5 links miden 44 px de alto.
  - Con las `woff2` bloqueadas (Arial de respaldo) también entra: links de 307 a 803 y botón de 835 a 984 (`65-1024-sin-fuentes.jpg`).
  - Con la barra de scroll de Windows no entra: ver PC-2.
- **El encabezado fijo no tapa títulos.**
  - Prueba: clic en cada link del menú y en "$35.000" de la portada, se espera el fin del scroll suave y se mide.
  - En 1024, 1280, 1366 y 1920 la sección queda en y 96 (encabezado de 77 px más 19 de aire) y el h2 entre y 242 y 291.
  - "Dónde" deja la tarjeta en y 96 y el título del bloque final en 169, sin taparse.
  - Capturas `30-ancla-*`.
- **Foco visible y nunca debajo del encabezado.**
  - Contorno de 3 px tinta (blanco en el pie) en los 19 elementos (`51-foco-1366-hoja.jpg`, `51-foco-1920-hoja.jpg`).
  - Con Tab y con Shift+Tab, Chrome centra el elemento enfocado y ninguno quedó con `top` menor que 77.
- **Circuito alineado.**
  - En vertical, el centro de la bolita, la línea y los centros de las paradas coinciden (Δy = 0).
  - En las detenciones del 19, 39, 59 y 79 % el error horizontal es de ±0,4 px, a 1024, 1366 y 1920.
  - La línea empieza en el centro de la primera parada y termina debajo del ícono final.
  - Con `prefers-reduced-motion` la bolita queda quieta sobre "Sentadillas" (`57-reducido-1366.jpg`).
  - Lo único que falla es el final (PC-5).
- **1920.** El contenido queda en 1200 px centrados, con márgenes de 360. Solo la banda y los fondos van de lado a lado. No hay nada estirado.
- **Columnas izquierdas alineadas.** Todo arranca en x 83 a 1366 y en x 360 a 1920: titular, circuito, foto de la clase, tarjetas, profe, bloque final y pie.
- **Bloque final.** La tarjeta "Dónde estamos" queda centrada en vertical con el texto, con la dirección completa, botones de 48 px y la sombra entera.
- **Pie.** A 1280 o más, tres columnas en una línea y la del © abajo. A 1024 la frase del medio pasa a dos líneas sin chocar.
- **Datos visibles contra `TAREAS.md`.** Coinciden los turnos, la cuota y lo que incluye, el plan complemento ($10.000 y $25.000), la clase de prueba gratis y que se paga desde la segunda, la dirección y el WhatsApp. No vi nada inventado en lo que revisé.

## Qué imagen elige el `srcset`

Medido con el tamaño real de cada archivo. `naturalWidth` viene corregido por la densidad y para esto no sirve. "Ampliación" es cuánto se agranda el archivo para cubrir su caja: si pasa de 1, la foto se estira.

| Foto | Caja en compu (px CSS) | DPR 1 elige | Ampliación DPR 1 | DPR 2 elige | Ampliación DPR 2 |
|---|---|---|---|---|---|
| Portada (1024–1100) | 405×506 · 440×550 | portada-compu-480 | 0,84 · 0,92 | portada-compu-640 | 1,27 · 1,37 |
| Portada (≥ 1280) | 523×576 | portada-compu-640 | 0,82 | portada-compu-640 | **1,63** |
| Clase (≥ 1280) | 625×416 | clase-568 | **1,10** | clase-568 | **2,20** |
| Profe (≥ 1280) | 476×595 | profe-596 | 0,80 | profe-596 | **1,60** |
| Dónde (≥ 1280) | 560×350 | donde-716 | 0,78 | donde-716 | **1,56** |
| Logo del encabezado | 44×44 | logo-80 | 0,55 | logo-80 | 1,10 |
| Avatar y logo del pie | 52 y 36 | avatar-104 · logo-72 | ≤ 1 | avatar-104 · logo-72 | 1,00 |

## Hallazgos

| ID | Gravedad | Dónde | En una línea |
|---|---|---|---|
| PC-1 | media | Portada, `css/style.css:370-378` | En una 1366×768 real, la cuota y los horarios quedan debajo del pliegue |
| PC-2 | media | Menú, `css/style.css:352` y `:359` | Con barra de scroll, a 1024 tres links del menú se parten en dos líneas |
| PC-3 | media | El profe, `css/style.css:410` y `:58` | Columna de la foto vacía entre 550 y 815 px (más de 1100 con los cursos abiertos) |
| PC-4 | menor | Circuito, `css/style.css:387` y `:391` | A 1024–1100 las paradas quedan desparejas (177/149 px) |
| PC-5 | menor | Circuito, `css/style.css:394` | La bolita termina 4 px a la izquierda del ícono de "Y otra vuelta" |
| PC-6 | menor | Cómo es la clase, `css/style.css:398-399` y `:217` | La tarjeta del 7 termina 32 px más abajo que la foto |
| PC-7 | menor | Turnos y cuota, `css/style.css:230-241` y `:404` | La tarjeta "Turnos" tiene 145 px vacíos abajo (224 a 1024) |
| PC-8 | menor | Banda inclinada, `css/style.css:149` | A partir de 1366 los extremos de la banda quedan cortados en recto (17 px a 1920) |
| PC-9 | menor | Sello "$0", `css/style.css:375` | De 1024 a 1280 el sello toca el borde de la pantalla y se le corta la sombra |
| PC-10 | menor | El enfoque, `css/style.css:381` | El texto de la derecha arranca 59 px antes que el título |
| PC-11 | menor | Botones y links, `css/style.css:79`, `:129`, `:279` y `:90` | El hover de los botones naranjas casi no se ve (1,15:1); la marca, "$35.000" y "Cursos" no cambian |
| PC-12 | menor | Fotos, `index.html:123`, `:189`, `:251` y `:307` | En pantallas 2x las fotos se estiran entre 1,6 y 2,2 veces; la de la clase ya se estira 1,10 en 1x |
| PC-13 | menor | Encabezado, `css/style.css:351` | El encabezado al 96 % deja ver la banda y los títulos que pasan por detrás |

### PC-1 · media · En una notebook 1366×768 real, la cuota y los horarios quedan debajo del pliegue

**Dónde:** portada en compu, `css/style.css:370-378`: `.portada` con `padding-block: 3.5rem 2.5rem`, h1 de 5.75rem y `.marco img` con `max-height: 36rem`.

**Problema:**

- La portada mide 683 px y el recuadro de datos termina en y 720. Entra en un viewport de 768, pero 768 es el alto de la pantalla, no el de la ventana.
- En una notebook de 1366×768 con Chrome (pestañas y barra de direcciones, unos 87 px) y la barra de tareas de Windows (48 px), quedan unos 630 px de alto.
- En ese alto se ven el titular y el botón, pero no "$35.000", "18 y 19 h" ni "7 h": del recuadro de datos solo asoma el borde de arriba. Tampoco se ven la etiqueta "En el Cuartel de Bomberos" ni los chevrones de la foto.
- El trabajo de la página es que se entienda en segundos cuánto sale y en qué horarios hay clase. En la compu más común de la zona eso queda abajo del pliegue.

**Evidencia:**

- `61-pliegue-real-1366x630.jpg`: cómo se ve hoy a 1366×630.
- Medido: `.datos` va de y 605 a 720, y los números de y 642 a 683.
- A 1536×730 (pantalla 1920×1080 al 125 %) entra justo: `62-pliegue-real-1536x730.jpg`.

**Arreglo:** una regla solo para pantallas bajas, que no cambia nada con 768 px o más.

```css
@media (min-width: 64em) and (max-height: 47.5em) {
  .portada { padding-block: 1.25rem 1.5rem; }
  .portada .h1 { font-size: 5.25rem; }
  .portada .h1 .antetitulo { margin-bottom: .75rem; }
  .portada-texto { gap: .75rem; }
  .portada-acciones { margin-top: 0; }
  .datos { margin-top: .5rem; }
  .dato { padding-block: .875rem; }
  .marco img { max-height: 30rem; }
  .sello { top: -1.75rem; }
}
```

- **Probado:** `.datos` termina en y 603, el titular sigue en dos líneas con la cinta (202 px de alto) y el disco del sello empieza en y 85, debajo del encabezado. A 1366×768 queda igual que hoy. Captura: `63-pliegue-1366x630-arreglo-propuesto.jpg`.
- **Límite:** no bajar el h1 de 5.25rem. Con 4.75rem "Que quieras volver." entra en una sola línea y cambia el titular aprobado.

### PC-2 · media · Con barra de scroll, a 1024 tres links del menú se parten en dos líneas

**Dónde:** `css/style.css:352` (`.cabecera .contenedor { gap: 2rem }`) y `:359` (`.menu a`, sin `white-space: nowrap`).

**Problema:**

- En Chrome y Edge de Windows la barra de scroll ocupa 15 px. Con la ventana en 1024 la página tiene 1009 px de ancho, pero el menú en línea ya se activa, porque `min-width: 64em` cuenta la barra.
- El encabezado necesita 1020 px: 40 + 240 (marca) + 32 + 492 (links) + 32 + 143 (WhatsApp) + 40. Los links se achican y "La clase", "Turnos y cuota" y "El profe" quedan en dos renglones dentro del mismo alto de 44 px.
- Pasa con ventanas de 1024 a unos 1034 px.
- En Playwright no se veía porque esconde la barra por defecto.

**Evidencia:**

- `68b-1024-cabecera-zoom.png` y `68-1024-con-barra-de-scroll.jpg`.
- Alto del texto de cada link: 20, 37, 37, 37 y 20 px. Los de 37 px están en dos líneas.
- Ancho de los links: "La clase" 86,9 px (sin barra, 89), "Turnos y cuota" 133,5 (136,6), "El profe" 83,2 (85,2).

**Arreglo:**

```css
@media (min-width: 64em) { .menu a { white-space: nowrap; } }
@media (min-width: 64em) and (max-width: 72em) { .cabecera .contenedor { gap: 1.25rem; } }
```

- **Probado con barra de scroll a 1024, 1030, 1100 y 1152:** los cinco links quedan en una línea (20 px de alto de texto), no hay desborde y el botón WhatsApp termina en x 969 con la página en 1009. Captura: `68c-1024-cabecera-arreglo-propuesto.png`.

### PC-3 · media · "El profe": la columna de la foto queda vacía entre 550 y 815 px

**Dónde:** `css/style.css:410` (`.profe { … align-items: start; }`) y `:58` (`.seccion { overflow: hidden }`).

**Problema:**

- La foto mide 595 px de alto y el texto con la trayectoria, 1145 px.
- Debajo de la foto y su disco queda una columna blanca de unos 550 px a 1366 y 1920, y de 815 px a 1024.
- Si se abre "Cursos y capacitaciones", el texto crece 453 px más y el hueco pasa los 1100 px: más de una pantalla con la mitad izquierda vacía.

**Evidencia:**

- `70-profe-1366-hueco.jpg` y `75-cursos-abierto-1366.jpg`.
- Medido a 1366: la foto va de y 3544 a 4139 y el texto de 3544 a 4689.
- Medido a 1024: la foto termina en 4089 y el texto en 4902.

**Arreglo:** que la foto acompañe el scroll. `sticky` no anda con el `overflow: hidden` de la sección, pero sí con `overflow: clip`, que recorta igual el disco y la trama.

```css
@media (min-width: 64em) {
  #profe { overflow: clip; }
  .profe-foto { position: sticky; top: 6.5rem; }
}
```

- **Probado a 1024:** con la sección a media altura, la foto queda fija en y 103, debajo del encabezado, y se suelta al llegar al final de la trayectoria.

### PC-4 · menor · A 1024–1100 las paradas del circuito quedan desparejas

**Dónde:** `css/style.css:387` (`grid-template-columns: repeat(5, 1fr) 9rem`) y `:391` (`.pista b { font-size: 2.125rem }`).

**Problema:**

- Una columna `1fr` no baja del ancho de su contenido. "Sentadillas" y "Tracciones" miden 149 px con letra de 34 px, más 28 de `padding-right`, así que esas dos columnas se estiran y las otras se achican.
- El recorrido tiene que verse regular y queda con tramos largos y cortos.
- Además, "Empujar. Press / con / mancuernas." queda en tres líneas, con "con" sola en una.

**Evidencia:**

- `43-pista-1024-dpr2.jpg`.
- Columnas medidas a 1024: 177, 149, 177, 149 y 149 px (la final, 144). Con barra de scroll: 177, 144, 177, 138 y 149.
- A 1100: 177, 174, 177, 174 y 174. Desde 1280, todas de 211.

**Arreglo:**

```css
@media (min-width: 64em) {
  .pista { grid-template-columns: repeat(5, minmax(0, 1fr)) 9rem; }
  .pista b { font-size: clamp(1.75rem, 2.9vw, 2.125rem); }
}
```

- **Probado a 1024:** las cinco columnas quedan de 160 px y ningún título desborda.
- **Desde 1280:** el título sigue en 2.125rem, como hoy.
- **Bolita:** se recalcula sola, porque `main.js` mide `offsetLeft`. Captura: `67-pista-1024-arreglo-propuesto.jpg`.

### PC-5 · menor · La bolita termina 4 px a la izquierda del ícono de "Y otra vuelta"

**Dónde:** `css/style.css:394` (`.pista .vuelta svg { left: 0 }`), junto con `js/main.js:78` (`offsetLeft - x0 + .125rem`).

**Problema:**

- En cada parada el centro de la bolita cae 9 px a la derecha del borde izquierdo de su `li`, igual que el punto.
- El ícono final mide 26 px y arranca en el borde mismo, así que su centro queda 13 px a la derecha.
- Cuando la bolita llega al final (del 97 al 100 % de la animación) se apoya corrida y deja asomar la punta de la flecha a la derecha.

**Evidencia:**

- `42-pista-1366-fin-dpr2.jpg` y el último cuadro de `41-pista-1920-secuencia.jpg`.
- Medido: Δx = −4,0 px en 1024, 1366 y 1920. En las otras paradas, ±0,4 px.

**Arreglo:** centrar el ícono en la misma vertical que los puntos, con `.pista .vuelta svg { left: -.25rem; }` dentro de `@media (min-width: 64em)`.

- **Línea:** termina en `right: 8.25rem` y sigue cayendo debajo del ícono.
- **Probado:** la bolita termina centrada. Captura: `67-pista-1024-arreglo-propuesto.jpg`.
- **Celular:** ya está alineado y no hay que tocarlo.

### PC-6 · menor · La tarjeta del 7 termina 32 px más abajo que la foto de la clase

**Dónde:** `css/style.css:398-399` (`.clase-lado { … align-items: stretch }` y `.clase-foto img { height: 100%; max-height: 26rem }`) y `:217` (el pie de foto).

**Problema:**

- Desde 1100 px la foto llega al tope de 416 px de alto, pero la fila de la grilla incluye también el pie de foto (31,8 px).
- La tarjeta del 7 se estira hasta el pie y su borde de abajo queda 32 px más abajo que el de la foto.
- A 1024 coinciden, porque ahí la foto no llega al tope.

**Evidencia:**

- `71-clase-1366-foto-vs-cupo.jpg`.
- Medido a 1366 y 1920: la foto termina en y 2460 y la tarjeta en 2492.

**Arreglo:** sacar el pie de foto del cálculo de la fila y reservarle el lugar abajo.

```css
@media (min-width: 64em) {
  .clase-foto { position: relative; }
  .clase-foto figcaption { position: absolute; top: 100%; left: 0; right: 0; }
  .clase-lado { padding-bottom: 2rem; }
}
```

- **Probado:** a 1366 y 1920 la foto y la tarjeta terminan las dos en y 2460, y a 1024 en 2405.

### PC-7 · menor · La tarjeta "Turnos" tiene 145 px vacíos abajo

**Dónde:** `css/style.css:404` (las tres tarjetas se estiran a la altura de la más alta) y `:230-241` (`.tarjeta--blanca` y `.horarios`).

**Problema:**

- La tarjeta de la cuota es la más alta: 453 px a 1366 y 532 a 1024.
- La de turnos termina su contenido mucho antes y le queda un bloque blanco vacío abajo: 145 px a 1366 y 1920, y 224 a 1024.
- A la de plan complemento le sobran 41 px (76 a 1024).
- En la maqueta las tres tarjetas tenían contenido parecido. Con el texto real, la de la cuota quedó más larga.

**Evidencia:**

- `72-turnos-1366-hueco.jpg`, y en `06-1024-completa.jpg` la franja de y 2870 a 3410.
- Medido: el hueco (el fondo de la tarjeta, menos el padding, menos el fondo del último elemento) da 144,7 px a 1366 y 223,6 a 1024.

**Arreglo:** repartir los tres horarios en el alto disponible y dejar la nota "Máximo 7 personas por turno" abajo, a la altura de "Empezás a pagar desde la segunda clase." de la tarjeta de al lado.

```css
@media (min-width: 64em) {
  .tarjeta--blanca { display: flex; flex-direction: column; }
  .horarios { flex: 1; display: flex; flex-direction: column; justify-content: space-evenly; }
  .horarios li:first-child { padding-top: .875rem; }
}
```

- **Probado:** captura `76-turnos-1366-arreglo-propuesto.jpg`.

### PC-8 · menor · A partir de 1366 los extremos de la banda inclinada quedan cortados en recto

**Dónde:** `css/style.css:149` (`.banda { overflow: hidden; padding-block: 1.5rem }`).

**Problema:**

- La banda mide el 112 % del ancho y está girada 2,2°. Cuanto más ancha la pantalla, más sube la punta derecha y más baja la izquierda.
- El `overflow: hidden` del contenedor la recorta con líneas horizontales. Abajo a la izquierda (de x 0 a unos 330 a 1920) y arriba a la derecha (desde unos x 1590) los bordes quedan rectos en vez de inclinados.
- Resultado: la banda se ve como una cuña que se afina en las puntas.

**Evidencia:**

- `64-banda-1920-recorte-y-arreglo.jpg`: arriba, hoy; abajo, con el arreglo.
- Medido: la banda girada sobresale del contenedor 18 px arriba y 17 abajo a 1920, 6 y 5 a 1366, y nada a 1024.

**Arreglo:** recortar solo en horizontal, igual que la portada.

```css
.banda { overflow: hidden; }
@supports (overflow: clip) { .banda { overflow: clip visible; } }
```

- **Probado a 1920:** la banda queda de espesor parejo de punta a punta.
- **Lo que cambia:** tapa unos píxeles más del disco de la portada y del fondo gris del enfoque, que ya quedan debajo por el `z-index: 3`.

### PC-9 · menor · De 1024 a 1280 el sello "$0" toca el borde de la pantalla

**Dónde:** `css/style.css:375` (`.sello { right: -2.5rem; … }`).

**Problema:**

- El sello sobresale 2,5rem de la foto, y entre 1024 y 1280 el margen lateral es justo 2,5rem (40 px).
- El disco termina a 2,5 px del borde de la pantalla y su sombra (`drop-shadow` de 14 px) se corta en seco.
- Desde 1366 el margen crece y se ve bien: 46 px de aire.

**Evidencia:**

- `60-sello-borde-1280-1024-dpr2.jpg`: el borde derecho de cada recorte es el borde de la pantalla.
- Medido: la caja del sello, girada, termina en x 1036 a 1024 (12 px afuera de la pantalla) y en x 1292 a 1280.

**Arreglo:**

```css
@media (min-width: 64em) and (max-width: 85em) { .sello { right: -1rem; } }
```

- **Probado:** quedan 27 px de aire entre el disco y el borde de la pantalla a 1024 y a 1280. A 1366 no se aplica y quedan los 46 px de hoy.

### PC-10 · menor · En "El enfoque" el texto de la derecha arranca 59 px antes que el título

**Dónde:** `css/style.css:381` (`.enfoque { … align-items: end; }`).

**Problema:**

- La columna derecha (la lista y la firma, 332 px) es más alta que la izquierda (el título y el contraste).
- Con `align-items: end`, "Por eso en Espacio Funcional 25 buscamos:" empieza más arriba que el título "El enfoque". El ojo lee primero ese "Por eso…", que depende de lo que está a la izquierda ("Lo que de verdad importa: que quieras volver…").
- En la maqueta, con lorem ipsum, la columna alta era la izquierda y esto no pasaba.

**Evidencia:**

- `74-enfoque-1366.jpg` y `10-1366-parte2.jpg`.
- Medido a 1366 y 1920: `.enfoque-texto` empieza en y 960 y el título `#enfoque-t` en y 1019.

**Arreglo:** `.enfoque { align-items: start; }` dentro de `@media (min-width: 64em)`.

- **Probado:** el título y el texto arrancan los dos en y 960.

### PC-11 · menor · El hover de los botones naranjas casi no se ve, y tres links no cambian

**Dónde:** `css/style.css:79` (`.boton--naranja:hover { background: var(--naranja-2) }`), `:129` (`.dato dd a`), `:279` (`.cursos summary`) y `:90` (`.marca`).

**Problema:**

- **Botones naranjas:** el hover pasa de `#FF7B02` a `#F26F00`, y entre esos dos colores hay un contraste de 1,15:1. Con el mouse encima de "Reservá tu clase de prueba gratis" (en la portada y en el encabezado) apenas se nota.
- **Links que no cambian:** en "$35.000" de la portada (un link a "Turnos y cuota"), en "Cursos y capacitaciones" y en la marca no cambia nada: ni fondo, ni color, ni subrayado.
- **Lo que sí se ve bien:** los links del menú (fondo gris), el botón negro y los botones con borde.

**Evidencia:**

- `55-hover-1366-hoja.jpg`: a la izquierda el estado normal, a la derecha el hover.
- Estilos medidos antes y durante el hover: la marca, "$35.000", "Cursos", el teléfono y el WhatsApp del pie no cambian. Los dos últimos ya están subrayados, así que igual se reconocen como link.

**Arreglo:**

- Mantener la paleta y oscurecer más el naranja en hover: `.boton--naranja:hover { background: #E06500; }`. El texto tinta sobre `#E06500` da 5,1:1 (sigue pasando AA) y el cambio contra el naranja normal pasa a 1,34:1.
- Para los links que no cambian: `.dato dd a:hover, .cursos summary:hover { text-decoration: underline; text-underline-offset: .2em; }`.

### PC-12 · menor · En pantallas 2x las fotos se estiran entre 1,6 y 2,2 veces; la de la clase ya se estira en 1x

**Dónde:** `index.html:123` (portada), `:189` (clase), `:251` (profe) y `:307` (dónde). Ver la tabla del `srcset`.

**Problema:**

- **En 1x, la foto de la clase:** se muestra a 625×416 y el archivo más grande mide 568 de ancho, así que se estira un 10 % en cualquier compu de 1280 o más.
- **En 1x, los `sizes`:** el de la clase dice 38rem (608 px) y mide 625. El del profe dice 28rem (448) y mide 476. Las dos diferencias no cambian qué archivo se elige.
- **En 2x** (Mac, y notebooks Windows al 150 o 200 %): se estiran todas, la portada 1,63 veces, la clase 2,20, el profe 1,60 y dónde 1,56. Se ven blandas, como la foto de "Dónde estamos" en `50-foco-1366-tab13.jpg`, capturada a DPR 2.
- **No es error del `srcset`:** los fotogramas de origen miden 716 px de ancho (`docs/imagenes.md`) y no hay de dónde sacar más.

**Evidencia:** la tabla del `srcset`, medida a 1366×768 y 1920×1080 con DPR 1 y 2.

**Arreglo:**

- **En 1x:** que la foto de la clase no pase su ancho real, con `.clase-lado { grid-template-columns: minmax(0, 35.5rem) 1fr; }` (568 px; la tarjeta del 7 se queda con el resto).
- **Los `sizes`:** corregirlos a `(min-width: 64em) 35.5rem` en la clase y `(min-width: 64em) 30rem` en el profe.
- **En 2x:** pedirle a Nicolás los videos o las fotos originales, de 1080 px o más, y sumar al `srcset` salidas de 1040 a 1280 px. Va a la lista de preguntas para Nicolás.

### PC-13 · menor · Se transparentan la banda y los títulos detrás del encabezado

**Dónde:** `css/style.css:351` (`.cabecera { … background: rgb(255 255 255 / .96) }`).

**Problema:**

- Con el fondo al 96 % de opacidad, lo que pasa por detrás se ve como un fantasma gris detrás del menú: la banda negra con su texto blanco, el título "Cómo es la clase", el disco naranja y la foto del bloque final.
- Sobre el bloque final, el encabezado entero se tiñe de color durazno.
- En el celular el encabezado es blanco opaco.
- Viene de la maqueta, así que es opcional. Pero al bajar se nota como un defecto.

**Evidencia:**

- `73-cabecera-1366-transparencia.jpg`: la banda con "RESISTENCIA · TÉCNICA" detrás de la marca y del menú.
- `10-1366-parte3.jpg`: "Cómo es la clase" detrás del logo.
- `50-foco-1366-tab13.jpg`: la foto de "Dónde estamos" detrás del botón WhatsApp.

**Arreglo:** fondo opaco, `.cabecera { background: var(--blanco); }`, como ya está en el celular. Con la página quieta no cambia nada.

## Observaciones sin hallazgo

- **Precio de la portada a 1024:** "$35.000" mide 109,8 px y su celda tiene 118,4 de ancho (116 con barra de scroll), con `white-space: nowrap`. Una cuota de seis cifras ("$100.000" mide 122 px) se saldría de la celda. Hoy no pasa. Si llega a pasar, bajar `.dato dd` a 1.875rem entre 64em y 80em.
- **Disco detrás de la foto del profe:** a 1024 y 1280 se sale de la pantalla por la izquierda (19 y 36 px). En el celular pasa lo mismo y es parte del diseño, así que no lo cuento como defecto.
- **Trama de rombos detrás del profe:** tiene el borde recto arriba y a la derecha, igual que en la maqueta aprobada.
- **Columnas derechas:** no arrancan todas en la misma x: 639 en el profe, 723 en la clase, los turnos y el final, 760 en la portada y 779 en el enfoque. Sale de las proporciones de cada grilla, viene de la maqueta y no se ve como error.
- **Banda en el primer pantallazo:** a 1366×768 asoma una cuña negra de 14 px abajo a la derecha, y a 1280×800 la banda queda cortada a la mitad. Es el corte normal del pliegue, no un defecto.

## Capturas

Todas en `docs/auditoria/compu/`.

| Archivo | Qué muestra |
|---|---|
| `01-1366-pliegue.jpg`, `03-1920-pliegue.jpg`, `05-1024-pliegue.jpg`, `07-1280-pliegue.jpg` | Primer pantallazo en cada ancho |
| `02-1366-completa.jpg`, `04-1920-completa.jpg`, `06-1024-completa.jpg`, `08-1280-completa.jpg` | Página completa |
| `10-1366-parte1…8.jpg`, `20-1920-parte1…6.jpg` | La página de a un pantallazo por vez |
| `30-ancla-1024-*.jpg`, `30-ancla-1366-*.jpg` | Después de cada clic en el menú y en "$35.000" |
| `41-pista-1920-secuencia.jpg` | Circuito congelado en el 2, 10, 19, 30, 59, 90, 97 y 99,5 % de la animación |
| `42-pista-1366-fin-dpr2.jpg`, `43-pista-1024-dpr2.jpg` | PC-5 y PC-4 |
| `50-foco-1366-tab*.jpg`, `51-foco-1366-hoja.jpg`, `51-foco-1920-hoja.jpg`, de `52` a `54`, `56-tab09-capturaspy-1366.jpg` | Foco con Tab y Shift+Tab |
| `55-hover-1366-hoja.jpg` | Hover: normal a la izquierda, hover a la derecha (PC-11) |
| `57-reducido-1366.jpg` | `prefers-reduced-motion`: la bolita queda quieta |
| `60-sello-borde-1280-1024-dpr2.jpg` | PC-9 |
| `61-pliegue-real-1366x630.jpg`, `62-pliegue-real-1536x730.jpg`, `63-pliegue-1366x630-arreglo-propuesto.jpg` | PC-1: hoy y con el arreglo |
| `64-banda-1920-recorte-y-arreglo.jpg` | PC-8: hoy (arriba) y con el arreglo (abajo) |
| `65-1024-sin-fuentes.jpg` | Menú a 1024 con las fuentes de respaldo |
| `67-pista-1024-arreglo-propuesto.jpg` | PC-4 y PC-5 con el arreglo |
| `68-1024-con-barra-de-scroll.jpg`, `68b-1024-cabecera-zoom.png`, `68c-1024-cabecera-arreglo-propuesto.png` | PC-2: hoy y con el arreglo |
| `70-profe-1366-hueco.jpg`, `75-cursos-abierto-1366.jpg` | PC-3 |
| `71-clase-1366-foto-vs-cupo.jpg` | PC-6 |
| `72-turnos-1366-hueco.jpg`, `76-turnos-1366-arreglo-propuesto.jpg` | PC-7: hoy y con el arreglo |
| `73-cabecera-1366-transparencia.jpg` | PC-13 |
| `74-enfoque-1366.jpg` | PC-10 |
