# Auditoría de accesibilidad y rendimiento

10/10/2026 · commit `c8960e6` · sitio servido en http://127.0.0.1:8802/ · capturas y datos en `docs/auditoria/accesibilidad/`

El servidor local (`python -m http.server`) manda todo sin comprimir y sin caché. El `.htaccess` de producción comprime y cachea, así que los bytes de HTML, CSS y JS de abajo son el peor caso.

## Resumen

- **Lighthouse 13.5.0, celular** (Moto G Power emulado, 412×823, DPR 1,75, 4G lento simulado y CPU ×4): **Rendimiento 98 · Accesibilidad 100 · Buenas prácticas 100 · SEO 100**. FCP 1,7 s · LCP 2,2 s · TBT 0 ms · CLS 0,024 · Speed Index 1,7 s. Tardó 66 s.
- **axe-core 4.10.2**: una sola violación, `region` en `#barra` (a 390). A 1366 no hay ninguna. axe no pudo decidir el contraste de 77 textos por los `::before` de las tramas, así que lo medí con los píxeles reales.
- **Contraste**: 163 textos medidos a 390 y 175 a 1366. Falla uno solo, "El profe", y es porque el disco naranja lo tapa (A11Y-1).
- **12 hallazgos**: 1 grave, 3 medios y 8 menores. Lo que más importa:
  1. **A11Y-1**: en el celular y la tablet el disco naranja de la foto del profe tapa "El profe". A 768 también tapa el borde de arriba del `h2`.
  2. **A11Y-2 y A11Y-3**: el foco del teclado se pierde dos veces. Una en el botón fijo cuando está escondido. La otra cuando se abre el menú: el Tab sale del panel y el foco queda debajo de él.
  3. **A11Y-4**: en 4G lento, cuando llegan Barlow 400 y 600 el primer pantallazo salta 39 px (CLS 0,086–0,090). Precargar esas dos fuentes lo deja en 0 y adelanta el LCP medio segundo. Lo medí.

## Hallazgos

| Id | Gravedad | Dónde | Problema |
|---|---|---|---|
| A11Y-1 | grave | `#profe`, `.profe-foto::before` (style.css:262) | El disco naranja tapa "El profe" de 360 a 1023 px |
| A11Y-2 | media | `#barra` (style.css:317–323) | El botón fijo escondido se puede enfocar y el foco queda fuera de la pantalla |
| A11Y-3 | media | menú del celular (main.js:16–32, index.html:76–91) | Al abrir el menú, Tab sale del panel y el foco queda debajo de él |
| A11Y-4 | media | `<head>` (index.html:25) | Barlow 400 y 600 llegan tarde: salta el primer pantallazo (CLS 0,09 en 4G lento) |
| A11Y-5 | menor | `div#barra` (index.html:334) | axe `region`: el botón fijo está fuera de todo landmark |
| A11Y-6 | menor | `.marca span` (style.css:92) | A 320 px el "25" de la marca queda debajo del botón de WhatsApp |
| A11Y-7 | menor | `.dato dd` (style.css:128) | Con espaciado de texto, "18 y 19 h" se pisa con "7 h" |
| A11Y-8 | menor | `.cursos summary::after` (style.css:281) | El lector de pantalla anuncia "Cursos y capacitaciones +" |
| A11Y-9 | menor | `.corredor` (style.css:198–207) | La bolita gira sin fin y no hay forma de pausarla (WCAG 2.2.2) |
| A11Y-10 | menor | `@keyframes correr` / `correr-h` | La bolita anima `top`/`left`: layout en cada cuadro y unos 20 layout shifts cada 8 s |
| A11Y-11 | menor | `img` de la portada (index.html:124) | La imagen LCP no tiene `fetchpriority="high"` |
| A11Y-12 | menor | `assets/img/logo-120.webp` | El logo de 40 px pesa 16 KB (sin pérdida). La foto de portada pesa 20 KB |

---

### A11Y-1 · grave · El disco naranja tapa "El profe"

**Dónde:** `.profe-foto::before` (style.css:262) y `.profe` (style.css:260). Viene así desde la maqueta (`docs/diseno/index.html:285`).

**Problema:** en una sola columna (menos de 1024 px) el disco baja un 10 % del alto de la foto por debajo de ella, pero `.profe` deja solo 2rem (32 px) hasta el texto. `.profe-foto` está posicionada y aislada, así que el disco se pinta **arriba** del texto, que no está posicionado. Las letras quedan tapadas, no solo con poco contraste.

**Evidencia:**
- `elementFromPoint` sobre el renglón de "El profe" (script `tapados.py`). Sobre 30 puntos de muestra, devuelve `figure.profe-foto` en 7 a 360 px, en 18 a 390 y en los 30 a 600 y a 768. A 768 también tapa 7 de 30 puntos de "Nicolás Guido Valle". En ningún otro texto de la página pasa algo así (probé 360, 390, 600, 768, 1024 y 1366).
- El disco termina 9 px por debajo del comienzo del texto a 360, 13 a 390, 16 a 414, 37 a 600, 58 a 768 y 90 a 1023.
- Las partes que se ven sobre el disco quedan a 4,08:1 (`--tinta-2` sobre `--naranja`). Para 15 px hace falta 4,5:1. El punto naranja del antetítulo desaparece sobre el disco.
- Capturas: `contraste-el-profe-sobre-disco-390.png` (la mitad de arriba de "El profe" tapada), `-600.png` y `-768.png` (no se ve).

**Arreglo:** que la foto reserve abajo lo que baja el disco. El disco baja el 10 % del alto. La foto es 4:5, así que eso es el 12,5 % del ancho, y un margen en % se calcula sobre el ancho:

```css
.profe-foto { position: relative; isolation: isolate; margin-bottom: 12.5%; }   /* style.css:261 */
@media (min-width: 64em) { .profe-foto { margin-bottom: 0; } }                  /* dentro del bloque de 64em */
```

Lo probé en memoria. Quedan exactamente los 32 px del `gap` entre el disco y el texto en 360, 390, 414, 600, 768 y 1023, y a 1024 o más no cambia nada. El disco sigue en el mismo lugar y del mismo tamaño. Ver `arreglo-propuesto-el-profe-390.png`.

### A11Y-2 · media · El botón fijo escondido recibe el foco

**Dónde:** `.barra` (style.css:317–323). Esconderla con `transform: translateY(110%)` no la saca del orden de Tab.

**Problema:** a 390, cuando la barra está escondida (arriba de la página o mientras se ve el bloque final), su link sigue siendo enfocable. El último Tab de la página cae en un botón que está fuera de la pantalla y el foco no se ve en ningún lado. Además, el link escondido sigue en el árbol de accesibilidad: un lector de pantalla lo puede recorrer aunque no se vea (no lo probé con TalkBack). Falla WCAG 2.4.7 (foco visible) y 2.4.11 (foco no tapado).

**Evidencia:** `teclado-orden-tab.txt`, Tab 16. El foco va a "Reservá tu clase de prueba gratis" dentro de `#barra`, con el rect empezando en y = 862 en una ventana de 844 y la clase `barra` sin `visible` (`transform: matrix(1,0,0,1,0,80.3)`). La captura `foco-390-tab16.jpg` no muestra ningún foco.

**Arreglo:** esconderla también con `visibility`, demorada para que no corte la animación:

```css
.barra { /* … lo que ya tiene … */ visibility: hidden; transition: transform .25s ease, visibility 0s linear .25s; }
.barra.visible { transform: none; visibility: visible; transition: transform .25s ease; }
@media (prefers-reduced-motion: reduce) { .barra, .barra.visible { transition: none; } }   /* reemplaza la regla de style.css:329 */
```

La regla de movimiento reducido tiene que nombrar también `.barra.visible`, porque esa regla nueva tiene más especificidad. Lo probé en memoria: después de "Cómo llegar" del pie el Tab vuelve a `body`, y con la barra visible el link se enfoca igual. De paso conviene agregar `html { scroll-padding-bottom: calc(var(--barra) + .5rem); }` para menos de 64em. Así, cuando el navegador desplaza la página hasta un elemento enfocado, no lo deja debajo de la barra. En mi recorrido no pasó, pero sin eso nada lo impide. A 1366 tampoco hay margen abajo: el anillo del último link del pie queda cortado por el borde de la ventana (`foco-1366-tab17.jpg`).

### A11Y-3 · media · Con el menú abierto, Tab se va detrás del panel

**Dónde:** `index.html:76–91`. El `nav#menu` está **antes** del botón en el DOM. `main.js:16–32` no mueve el foco.

**Problema:** se abre el menú con Enter o Espacio y el foco se queda en el botón. El Tab siguiente no entra al menú: va al CTA de la portada, que está debajo del panel abierto. El panel queda abierto mientras uno sigue tabulando por toda la página. Para llegar a los links hay que volver con Shift+Tab. Falla 2.4.3 (orden del foco) y 2.4.11.

**Evidencia:** `teclado-menu-cursos.log`. "Tab tras abrir → A Reservá tu clase de prueba gratis … abierto: True". Con `elementFromPoint` en el centro del foco (342–398 px) aparece "el panel del menú" (64–421 px). Captura: `menu-abierto-tab-foco-tapado-390.png`. Lo que sí anda bien: `aria-expanded` pasa de false a true, `aria-controls="menu"` apunta a un id que existe, la etiqueta cambia a "Cerrar el menú", Escape cierra y devuelve el foco al botón (aunque el foco esté afuera), y Enter en un link cierra el menú y baja a la sección.

**Arreglo** (main.js), probado en memoria:

```js
boton.addEventListener('click', function () {
  var abrir = boton.getAttribute('aria-expanded') !== 'true';
  abrirMenu(abrir);
  if (abrir) menu.querySelector('a').focus();
});
cabecera.addEventListener('focusout', function (e) {
  if (cabecera.classList.contains('menu-abierto') && e.relatedTarget && !cabecera.contains(e.relatedTarget)) abrirMenu(false);
});
```

Con esto, al abrir el menú el foco cae en "Enfoque". El Tab sigue por los cinco links, el CTA del menú, el ícono de WhatsApp y el botón. Al salir de la cabecera el menú se cierra y el foco cae en el CTA de la portada, que ya se ve. Si el menú se abre tocando la pantalla, no aparece el anillo: lo medí, y "Enfoque" recibe el foco pero `:focus-visible` da false. Con teclado da true.

### A11Y-4 · media · Las fuentes del texto llegan tarde y el primer pantallazo salta

**Dónde:** `index.html:25`. Solo se precarga `barlow-sc-700`. Barlow 400, 500 y 600 y Barlow SC 600 se descubren recién cuando el CSS ya se aplicó.

**Problema:** en una red lenta, la primera pintura sale con Arial. Con Arial la bajada ocupa 3 renglones en lugar de 2 y el CTA 2 en lugar de 1. Cuando llega Barlow todo sube: los datos, la foto y el sello se mueven 39 px. Es justo el pantallazo donde está el botón para reservar.

**Evidencia** (390×844, DPR 3, latencia 562,5 ms, 1,47 Mbps, CPU ×4; `rendimiento-390-dpr3.txt` y `prueba_precarga.py`):
- Las cuatro fuentes del texto se piden a los 2647 ms. La precargada se pidió a los 624.
- Layout shifts al cargar: 0,0836 + 0,0062 y 0,0862, en dos corridas. Las fuentes de los shifts son `DIV.marco`, `DIV.portada-acciones`, `DL.datos` y `svg`.
- Con todas las fuentes, la bajada mide 55 px y la foto empieza en y = 648. Con Arial, la bajada mide 83 px y la foto empieza en y = 687 (`salto_fuente.py`).
- Lighthouse lo ve más chico (CLS 0,024, "Web font loaded"), porque simula la red en vez de frenarla de verdad.

**Arreglo:** precargar las dos que arman el primer pantallazo, la del texto (400) y la del CTA (600):

```html
<link rel="preload" href="assets/fonts/barlow-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/barlow-600.woff2" as="font" type="font/woff2" crossorigin>
```

Lo probé inyectando esas dos líneas en el HTML en memoria, dos corridas de cada versión. **CLS 0** contra 0,086–0,090, y **FCP/LCP 2,12–2,21 s** contra 2,62–2,80 s. Son 45 KB más al principio, que hoy igual se bajan antes del primer pantallazo. Habría que corregir también `docs/diseno.md:23` ("Se precarga solo `barlow-sc-700`").

### A11Y-5 · menor · axe: `region` en `#barra`

**Dónde:** `index.html:334`, `<div class="barra" id="barra">` entre `</footer>` y `<script>`.

**Problema:** el botón fijo es el único contenido fuera de un landmark. Según la regla de axe, eso significa que quien recorre la página por regiones con un lector de pantalla no lo encuentra.

**Evidencia:** `axe-resumen.json`. Violación `region` (impacto moderado), nodo `#barra`, en los cuatro estados medidos a 390: inicial, cursos abiertos, menú abierto y barra visible. A 1366 no aparece porque ahí la barra tiene `display: none`.

**Arreglo:** `<aside class="barra" id="barra" aria-label="Reservar la clase de prueba"> … </aside>`. La posición es fija, así que no cambia nada visual.

### A11Y-6 · menor · A 320 px la marca se mete debajo del botón de WhatsApp

**Dónde:** `.marca span { white-space: nowrap }` (style.css:92) dentro de `.marca`, que es un ítem flex sin `min-width: 0`.

**Problema:** 320 px es el ancho que pide WCAG 1.4.10 (equivale a 1280 px con zoom al 400 %), y también el de un iPhone SE de primera generación. A ese ancho "Espacio Funcional 25" termina en x = 227, pero el botón de WhatsApp empieza en x = 206. El "25" queda debajo del botón. No hay scroll horizontal (`scrollWidth` 320 = ventana), así que no se ve en ningún otro control.

**Evidencia:** `reflow-320-cabecera.jpg`. Con el espaciado de texto de WCAG 1.4.12, el texto se sale 13 px de su caja también a 390 (`espaciado-texto-390.png`).

**Arreglo:** `.marca { min-width: 0; } .marca span { white-space: normal; line-height: 1.05; }`. Lo probé en memoria. A 320 la marca pasa a dos renglones y termina en x = 196, antes del botón (206). La cabecera sigue midiendo 65 px. A 360 y a 390 queda en un renglón, como ahora. Ver `arreglo-propuesto-marca-320.png`.

### A11Y-7 · menor · Con espaciado de texto, los datos rápidos se pisan

**Dónde:** `.dato dd { white-space: nowrap }` (style.css:128).

**Problema:** si alguien aumenta el espaciado de letras y de palabras (WCAG 1.4.12, con una extensión o una hoja de estilo propia), "18 y 19 h" no puede cortar y se mete en la columna de "7 h". En pantalla se lee "18 y 19 h7 h". "$35.000" también se sale 6 px.

**Evidencia:** `espaciado-texto-390-datos.png`. El script `estructura.py` lo marca como "se sale del padre". A 1366 no pasa.

**Arreglo:** `.dato dd { white-space: normal; overflow-wrap: anywhere; }`. Lo probé en memoria. Con el espaciado normal todo sigue en un renglón: a 320 sobra 1 px, a 360 sobran 11 y a 390, 15. Con el espaciado aumentado corta en dos renglones en vez de pisarse (`arreglo-propuesto-datos-espaciado-390.png`).

### A11Y-8 · menor · El "+" del desplegable entra en su nombre

**Dónde:** `.cursos summary::after { content: "+" }` (style.css:281–282).

**Problema:** Chrome incluye el contenido generado en el nombre accesible. El lector recibe "Cursos y capacitaciones +", y con el desplegable abierto, "Cursos y capacitaciones –". Cada lector pronuncia el signo a su manera; no lo probé con uno real.

**Evidencia:** árbol de accesibilidad por CDP (`teclado-menu-cursos.log`): `DisclosureTriangle | Cursos y capacitaciones + | expanded: False`. El desplegable en sí anda bien. Se enfoca con Tab, Enter y Espacio lo abren y lo cierran, y `expanded` cambia. El foco se ve: `foco-1366-tab12.jpg`.

**Arreglo:** mover el signo a un `span` oculto para el lector, sin cambiar cómo se ve: `<summary>Cursos y capacitaciones<span class="signo" aria-hidden="true"></span></summary>`, con `.cursos summary .signo::after { content: "+"; font: 600 1.5rem/1 var(--texto); }` y `.cursos[open] summary .signo::after { content: "–"; }`, en lugar de las reglas de `summary::after`.

### A11Y-9 · menor · La bolita no se puede pausar

**Dónde:** `.corredor { animation: correr 7s … infinite }` (style.css:198–207).

**Problema:** WCAG 2.2.2 (nivel A) pide que todo lo que se mueve solo, más de 5 s y al lado de otro contenido, se pueda pausar o detener. Con `prefers-reduced-motion` la bolita queda quieta, y eso está bien: lo comprobé, `getAnimations()` vuelve vacío y la bolita queda en la primera estación (`reducido-pista-390.png`, `reducido-pista-1366.png`). Pero quien no tiene esa opción activada no tiene forma de frenarla.

**Evidencia:** `document.getAnimations()` sin movimiento reducido: `['correr', 'corredor', Infinity, 7000]`.

**Arreglo:** Pablo elige, porque cambia el comportamiento aprobado. La opción mínima es cortarla después de dos vueltas (`animation-iteration-count: 2`, y que termine en la primera estación). Eso baja la distracción pero no cumple 2.2.2 al pie de la letra. Para cumplir del todo, que dé **una** vuelta de 5 s o menos cada vez que la pista entra en pantalla, con un `IntersectionObserver` que agregue una clase, o que se pause al tocar la pista.

### A11Y-10 · menor · La bolita anima `top` y `left`

**Dónde:** `@keyframes correr` y `correr-h` (style.css:203–212). `main.js:77–79` carga `--p1…--p5` como valores de `top`/`left`.

**Problema:** animar `top` y `left` obliga a recalcular el layout en cada cuadro en el hilo principal, y cada paso cuenta como layout shift. Es poco, pero es trabajo constante mientras la pista está en pantalla, y en un celular lento se nota más.

**Evidencia:** Lighthouse, "Avoid non-composited animations": `i.corredor`, "Unsupported CSS Property: top". En 8 s con la pista en pantalla el `PerformanceObserver` registró 21 layout shifts de `I.corredor` (suma 0,0031) sin red lenta, y 19 (suma 0,0016) con 4G lento.

**Arreglo:** dejar `top: .3125rem` fijo (y `left: .125rem` en la compu) y animar `transform: translateY(var(--dN))` o `translateX(var(--dN))`. En `main.js`, cargar `--dN` con la distancia sola: `(paradas[i].offsetTop - y0) + 'px'`, sin el `+ .3125rem`. Se ve igual, lo hace la placa de video y no genera layout shifts.

### A11Y-11 · menor · La imagen LCP no tiene `fetchpriority="high"`

**Dónde:** `index.html:124`, el `img` de `.marco`.

**Problema:** es el LCP en todas las corridas (`portada-movil-716.webp` a 390, 492 ms sin red lenta y 2,6–2,8 s con 4G lento). En 4G lento Chrome la pidió con prioridad **Low** a los 647 ms, y compitió con el logo y el CSS.

**Evidencia:** Lighthouse, "LCP request discovery": "fetchpriority=high should be applied: false". En `rendimiento-390-dpr3.txt` figura la prioridad `Low` en la corrida 4G. En esas corridas el LCP quedó atado a la primera pintura y no a la imagen, que llegó a los 1661 ms. Por eso la ganancia esperada es chica.

**Arreglo:** agregar `fetchpriority="high"` al `<img>` de la portada. El `<source>` de la compu hereda la prioridad del `img`.

### A11Y-12 · menor · El logo de la cabecera pesa casi como la foto de portada

**Dónde:** `assets/img/logo-120.webp`, que es la que se baja a 3x, y `logo-80.webp` / `logo-72.webp`. Las tres son WebP sin pérdida (`VP8L`).

**Problema:** 16.159 bytes para un logo de 40 px. La foto de portada pesa 20.675. Es el tercer archivo más pesado del primer pantallazo, después de las fuentes y el CSS.

**Evidencia:** pedidos en `rendimiento-390-dpr3.txt`. Lighthouse calcula que se ahorran 7,4 KB solo en `logo-80`. Lo convertí a WebP con pérdida, color al 90 % y alfa al 100 %: queda en 7.646 bytes (prueba en el scratchpad, no toqué `assets/`).

**Arreglo:** regenerar los tres logos con pérdida (calidad 90, `alpha_quality` 100) y revisarlos a 3x antes de reemplazar. `docs/imagenes.md` eligió "sin pérdida" a propósito, así que es una decisión de Pablo: se ahorran unos 8,5 KB del primer pantallazo.

---

## Lo que verifiqué y está bien

**Estructura** (`estructura.py`, árbol de accesibilidad por CDP)
- `lang="es-AR"`. Hay un solo `h1` ("Entrenamiento funcional en 25 de Mayo. Que quieras volver."), con el punto `sr-only` para que el lector haga la pausa. Los títulos no saltan niveles: h1 → h2 (enfoque, clase, turnos, profe, prueba) → h3.
- Landmarks: `header` (banner), `nav "Secciones"`, un solo `main#contenido`, seis `section` con `aria-labelledby` y nombre, `footer` (contentinfo) y `nav "Contacto"`. La única excepción es la barra (A11Y-5).
- Imágenes: las cuatro fotos tienen alt descriptivo. Los tres logos y el avatar tienen `alt=""` porque van al lado del nombre. Todas tienen `width`/`height`.
- Los SVG decorativos están todos con `aria-hidden="true"` o dentro de algo que lo tiene, y no queda ninguno expuesto. La banda inclinada, el sello y las siete personitas están ocultos, y lo que dicen ya está en el texto.
- Botones de ícono: "Escribir por WhatsApp" y "Abrir el menú"/"Cerrar el menú". No hay ids repetidos ni `aria-*` que apunten a ids que no existen. No hay `target`. El viewport permite zoom.

**Teclado** (`teclado-orden-tab.txt`, capturas `foco-*`)
- 390: saltar → marca → ícono WhatsApp → menú → CTA de la portada → $35.000 → Consultar por el plan → Cursos → CTA final → teléfono → Cómo llegar → Instagram → los tres del pie → barra escondida (A11Y-2).
- 1366: saltar → marca → cinco links del menú → WhatsApp → CTA → $35.000 → plan → cursos → CTA final → teléfono → Cómo llegar → Instagram → pie.
- El orden sigue al visual. Con Shift+Tab a 1366 la cabecera fija nunca tapa el foco (`scroll-padding-top: 6rem`).
- "Ir al contenido" aparece arriba de todo (`foco-390-tab01.jpg`, `foco-1366-tab01.jpg`). Con Enter, el Tab siguiente cae en el CTA de la portada.
- El foco se ve en todos los fondos. Es un contorno `--tinta` de 3 px separado 3 px: 17,8:1 sobre blanco (`foco-390-tab05.jpg`, `foco-1366-tab03.jpg`) y 6,8:1 alrededor del botón negro sobre naranja (`foco-390-tab09.jpg`). En el pie es blanco, 17,8:1 sobre negro (`foco-390-tab13.jpg`). En la tarjeta negra no hay nada enfocable.
- Detalle chico: el anillo de "$35.000" toca el rótulo "Cuota" (`foco-390-tab06.jpg`), pero se lee.
- Blancos táctiles: todos miden 44 px o más de alto, salvo "$35.000", que mide 81×30 a 390 y 110×41 a 1366. Igual supera el mínimo de 24×24 de WCAG 2.5.8.

**Contraste** (`contraste_px.py`, datos en `contraste-medido.json`): saqué la captura con todo el texto transparente y comparé el color computado de cada texto contra **cada píxel** del fondo debajo de su caja. Así entran las tramas, los discos, la marca del enfoque y las fotos. Reporto el percentil 2, o sea el peor fondo.

| Texto | Colores | Medido (peor fondo) | Pide |
|---|---|---|---|
| Texto y botones sobre naranja (CTA, cinta, sello, bloque final) | `--tinta` / `#FF7B02` | 6,84; 5,88–6,38 sobre los rombos del bloque final | 4,5 |
| "El profe" sobre el disco | `--tinta-2` / `#FF7B02` | **4,08** (A11Y-1) | 4,5 |
| Tarjeta negra: precio, "Valores de octubre 2026", "por mes", vigencia | `#B9BDC3` y blanco / `--tinta` | 9,42 / 17,77 | 4,5 |
| Notas chicas `.chico`, rótulos y "por mes" de los datos (14–15 px) | `--gris` / blanco, niebla, niebla-2 | 6,16 / 5,55 / 5,11 | 4,5 |
| Rótulos chicos sobre la trama gris (`.contraste small`) | `--gris` / niebla + rombos | 5,02–5,55 | 4,5 |
| "En el Cuartel de Bomberos" sobre la foto | `--tinta` / pastilla blanca al 94 % | 15,7–16,3 | 4,5 |
| Pie | `#C9CCD1` y blanco / `--tinta` | 11,03 / 17,77 | 4,5 |
| Banda inclinada (oculta para el lector, pero se ve) | blanco y naranja / `--tinta` | 17,77 / 6,84 | 3 (grande) |
| Hover del botón naranja / negro | `--tinta` / `#F26F00` · blanco / `#2C2E32` | 5,96 / 13,60 | 4,5 |

El texto circular del sello mide 9,7 px a 390 y pasa en contraste (6,8:1). Está oculto para el lector y lo que dice se repite en el texto.

**Movimiento reducido** (`--reducido`): no queda ninguna animación (`getAnimations()` vacío), la barra aparece sin transición (`transition-duration: 0s`) y `scroll-behavior` es `auto`.

**Reflow a 320 px**: no hay scroll horizontal (`scrollWidth` 320). Lo único que se pierde es el "25" de la marca (A11Y-6).

## Rendimiento simulando celular (Playwright, 390×844, DPR 3, sin caché)

Datos crudos en `rendimiento-390-dpr3.txt`.

| | Sin freno | 4G lento + CPU ×4 |
|---|---|---|
| Pedidos de red antes de bajar | 12 (más 3 `data:` de las tramas, que no salen a la red) | 13 (Chrome adelanta `clase-568.webp` porque en red lenta el lazy carga desde más lejos) |
| Bytes antes de bajar | 221.419 (216 KiB) | 237.116 (232 KiB) |
| Total después de bajar hasta el pie | 16 pedidos · 277.846 B (271 KiB) | igual |
| FCP / LCP | 492 / 492 ms | 2624–2804 ms (las dos métricas igual) |
| Elemento LCP | `portada-movil-716.webp` | igual |
| CLS al cargar | 0 | 0,086–0,090 por las fuentes (A11Y-4) |
| Dominios | solo `127.0.0.1:8802` | igual |
| Consola | sin errores ni advertencias, ni a 390 ni a 1366 | igual |

- **Qué se baja en el primer pantallazo:**

  | Recurso | Bytes | Parte del primer pantallazo |
  |---|---|---|
  | 5 fuentes | 114.149 | 52 % |
  | CSS | 27.271 | |
  | HTML | 25.873 | |
  | Logo | 16.159 | |
  | Foto de portada | 20.675 | |
  | favicon.ico | 9.172 | |
  | JS | 4.592 | |
  | Avatar | 3.528 | |

  Con la compresión del `.htaccess`, el HTML, el CSS y el JS (57 KB) bajarían a una fracción. Es una estimación, no lo medí en producción.
- **Precarga del titular**: `barlow-sc-700.woff2` se pide una sola vez, a los 25 ms (a los 624 ms en 4G), con prioridad High, y se usa. No hay pedido repetido por `crossorigin`. Esperé 5 s después de `load`, a 390 y a 1366, y no apareció el aviso de "preloaded but not used".
- **srcset que elige cada `img`** a 390 con DPR 3:

  | Imagen | Archivo elegido | Densidad | Nota |
  |---|---|---|---|
  | Logo de la cabecera | `logo-120.webp` (3x) | 3x | |
  | Portada | `portada-movil-716.webp` | 2,0x | la más grande que hay |
  | Avatar | `avatar-156.webp` | 3x | |
  | Clase | `clase-568.webp` | 1,6x | |
  | Profe | `profe-596.webp` | 1,7x | |
  | Dónde | `donde-716.webp` | 2,0x | |
  | Logo del pie | `logo-72.webp` | 2x | único candidato |

  A 1366 con DPR 1 la portada usa `portada-compu-640.webp`, que es la correcta para 33rem. Las fotos tienen menos densidad que la pantalla porque no hay recortes más grandes (`docs/imagenes.md`). No es un error.
- **Lazy**: avatar, clase, profe, dónde y el logo del pie tienen `loading="lazy"`, y el logo de la cabecera y la foto de portada no, como corresponde. Profe, dónde y el logo del pie recién se piden al bajar. El avatar, que está a 1595 px, y en 4G también la foto de la clase, se piden enseguida porque Chrome carga lo lazy desde 1250 a 2500 px antes según la red.
- **Lighthouse** (`lighthouse-resumen.json`): avisa del CSS que bloquea el renderizado (27 KB, ahorro estimado de 590 ms), de la falta de compresión y de caché (es por el servidor local; el `.htaccess` lo resuelve), de que el CSS no está minificado (4,5 KB), de A11Y-10, A11Y-11 y A11Y-12, y del CLS por fuentes (A11Y-4). No marca nada de accesibilidad.

## Cómo se midió

Todo con Playwright y el Chrome instalado (`channel="chrome"`), en modo headless. Los scripts están en el scratchpad de la sesión, en `…/scratchpad/a11y-scripts/`:

| Script | Qué mide |
|---|---|
| `axe_run.py` | axe en 390 y 1366: inicial, cursos abiertos, menú abierto y barra visible |
| `contraste_px.py` | contraste contra los píxeles reales del fondo |
| `tapados.py` | texto tapado por otros elementos, en seis anchos |
| `teclado.py`, `menu_teclado.py` | orden del Tab, menú, desplegable, salto al contenido, árbol de accesibilidad |
| `estructura.py` | títulos, landmarks, alt, SVG, blancos táctiles, movimiento reducido, reflow a 320, espaciado de texto |
| `rendimiento.py` | pedidos, bytes, srcset, lazy, consola, LCP, CLS, con y sin freno por CDP |
| `salto_fuente.py`, `prueba_precarga.py` | salto de las fuentes y prueba de la precarga |
| `prueba_arreglo_*.py`, `prueba_marca.py`, `prueba_datos.py` | arreglos probados en memoria, sin tocar el sitio |

Las capturas de foco salieron de `docs/herramientas/capturas.py --tab N --reducido`. Lighthouse: `npx --yes lighthouse http://127.0.0.1:8802/ --form-factor=mobile --chrome-flags="--headless=new"`. No modifiqué ningún archivo del sitio.
