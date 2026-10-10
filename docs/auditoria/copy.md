# Auditoría de copy · Espacio Funcional 25

10/10/2026 00:13 · auditoría adversarial de copy sobre el sitio v1 (commit `c8960e6`) · sigue: correcciones y revisión de Nicolás

Capturas en `docs/auditoria/copy/`. Se miró todo el texto de `index.html` (title, meta description, Open Graph, JSON-LD antes y después del JS, alt, aria-label, los dos mensajes prellenados de WhatsApp decodificados) contra las fuentes:

- `docs/relevamiento/fuentes.md` (sección 1, PDF de información; sección 2, CV). Además, se volvió a sacar el texto de los dos PDF originales del hub con PyMuPDF, solo para leerlos, y coincide con la transcripción.
- `docs/fotos-instagram/INDICE.md` (reel del 28/07/2026 y demás textos de 2026).
- `TAREAS.md`, sección "Datos del negocio" (vale ante cualquier diferencia).
- `docs/diseno.md`, para las decisiones que ya aprobó Pablo (licenciatura 2023, trayectoria completa).

Cómo se midió: scripts de Playwright con el Chrome instalado (en el scratchpad): `innerText` y `textContent` de la página, alto y cantidad de líneas de cada botón entre 320 y 414 px, la página con JS apagado, el JSON-LD que arma `main.js`, la superposición del disco naranja con el rótulo "El profe" (`getBoundingClientRect`) y pruebas de los arreglos inyectando CSS o texto en la página, sin tocar los archivos. Cada imagen de `assets/img/` se miró con Read, y la de la clase también al lado de su fotograma original.

## Resumen

- **No hay testimonios, cantidades de alumnos, años de experiencia ni resultados inventados.** Los datos (dirección, turnos, cuota, plan complemento, clase de prueba gratis, teléfono) coinciden con `TAREAS.md`, y la trayectoria del profe sale toda del CV.
- **Grave (1):** una frase de "Cómo es la clase" explica el método con algo que no dice ninguna fuente ("cada estación trabaja otra parte del cuerpo") y que le cambia el sentido al PDF ("alternar patrones de movimiento").
- **Media (4):**
  - el recorte de la frase central de El enfoque perdió "para un entrenador" y "lo difícil", que son la idea de Nicolás;
  - el disco naranja tapa la mitad de arriba del rótulo "El profe" en el celular;
  - el alt de la foto de la clase describe a una alumna que quedó afuera del recorte;
  - las cosas del texto que Nicolás tiene que confirmar no están anotadas en ningún lado vigente: no hay README y la sección 12 del plan v0 quedó vieja.
- **Menor (11):**
  - "gratis" queda sola en la segunda línea de los tres botones a 360 px o menos;
  - con el JS apagado, la portada dice "Ver / por mes";
  - falta confirmar "Y otra vuelta";
  - hay una ambigüedad de fechas en la bio;
  - hay detalles de ortografía, tipografía y orden en la trayectoria;
  - el nombre de una oferta del JSON-LD no coincide con el de la página.
- **Claridad en segundos:** bien. A 390×844 y a 360×740, sin bajar, se ve qué es, dónde queda, cuánto sale, los horarios y el botón. También se ve que la clase de prueba es gratis (en el botón y en el sello "$0") y que se paga desde la segunda clase (en la nota de abajo del botón). Ver `01-movil-390x844-pliegue.jpg`, `02-movil-360x740-pliegue.jpg` y `09-compu-1366x768-pliegue.jpg`.
- **Voz de Nicolás:** se nota. La lista de "buscamos", el cierre de la continuidad, "Vení a una clase de prueba para conocer cómo trabajamos" y "No hace falta que estés en forma para arrancar" son textuales. No hay frases de gimnasio ("transformá tu cuerpo", "tu mejor versión"). Los dos únicos lugares donde el recorte le cambió el sentido son COPY-1 y COPY-2.

## Hallazgos

### COPY-1 · grave · "Cómo es la clase", `p.por-que` (index.html:185) y bajada (index.html:172)

**Problema.** "Como cada estación trabaja otra parte del cuerpo, mantenés un buen nivel de esfuerzo…" es una afirmación sin fuente. El PDF dice otra cosa: "Las estaciones de trabajo están organizadas estratégicamente para **alternar patrones de movimiento** […] Esto permite mantener un buen nivel de esfuerzo sin generar fatiga excesiva". El reel del 05/10/2026 dice "combinando ejercicios de diferentes patrones de movimiento". Ninguna fuente habla de "otra parte del cuerpo". Además, con el propio circuito de ejemplo no se cumple: sentadillas y saltos cargan las piernas, y "aeróbico" no es una parte del cuerpo. La bajada ("Cada estación cambia el movimiento") va por el mismo lado y pierde la palabra clave de Nicolás, "patrones de movimiento".

**Evidencia.** index.html:172 y :185. PDF "¿Cómo trabajamos?" (`fuentes.md`, líneas 44 y 54). `INDICE.md`, línea 168.

**Arreglo (en su voz, casi textual del PDF):**
- Bajada: «Una hora de fuerza, resistencia y acondicionamiento físico, en estaciones de trabajo que alternan patrones de movimiento.»
- `p.por-que`: «Eso permite mantener un buen nivel de esfuerzo sin generar fatiga excesiva, y que puedas sostener el entrenamiento durante toda la clase sin terminar destruido.»

### COPY-2 · media · El enfoque, `.contraste` (index.html:146-147)

**Problema.** El recorte de la frase del reel le sacó el sujeto y la antítesis, que son justo la idea de Nicolás:
- Reel: "Lo más fácil **para un entrenador** es simplemente agotarte hasta dejarte sin aire. **Lo difícil** y lo que de verdad importa es lograr que quieras volver cada semana sin lastimarte entrenando."
- PDF: "Eso es lo más fácil **para un entrenador**. Lo difícil es lograr que una persona quiera volver".
- Sitio: "LO MÁS FÁCIL · Agotarte hasta dejarte sin aire." / "LO QUE DE VERDAD IMPORTA · Que quieras volver…".

Sin "para un entrenador", "agotarte" se puede leer como reflexivo: "lo más fácil es que te agotes vos". Ahí la frase deja de ser la autocrítica del entrenador y pasa a parecer un consejo o un reproche al alumno. Sin "lo difícil" se pierde el contraste fácil/difícil que pide el brief ("agotar al alumno es lo más fácil; lo difícil es que quiera volver").

**Evidencia.** `innerText`: "LO MÁS FÁCIL / Agotarte hasta dejarte sin aire." `INDICE.md`, línea 165. `fuentes.md`, líneas 60-62. Fotograma `DbUtD7_j4uj_f008s` con el subtítulo "lo más fácil para un entrenador es simplemente".

**Arreglo.** Cambian solo los dos rótulos `<small>`, sin tocar el diseño:
- `<small>Lo más fácil para un entrenador</small>Agotarte hasta dejarte sin aire.`
- `<small>Lo difícil, y lo que de verdad importa</small>Que quieras volver cada semana, sin lastimarte entrenando.`

Medido inyectando el texto: los dos rótulos siguen en **una línea** a 320, 360, 375, 390, 414, 768, 1366 y 1920 px.

### COPY-3 · media · El profe, rótulo `.profe-texto .antetitulo` ("El profe")

**Problema.** En el celular, el disco naranja de atrás de la foto (`.profe-foto::before`) se pinta encima de la mitad de arriba de "El profe". El texto queda cortado.

**Evidencia.**
- `06-movil-390-antetitulo-profe.jpg`, `06-movil-360-antetitulo-profe.jpg` y `07-movil-390-zoom-el-profe-tapado.png`.
- Medido: el disco baja 41-48 px por debajo de la foto y el rótulo empieza 32 px por debajo. Se superponen 9 px a 360, 12,75 px a 390 y 15,75 px a 414 (el rótulo mide 18 px de alto).

**Arreglo.** `.profe-texto { position: relative; z-index: 1; }`. Probado inyectándolo: el rótulo queda entero y el disco no cambia (`11-movil-360-el-profe-arreglo-probado.png`). No es un cambio de estilo: el disco sigue igual.

### COPY-4 · media · alt de la foto de la clase (index.html:189)

**Problema.** El alt dice "un alumno hace remo con TRX, una alumna apoya **las manos** en una pelota medicinal y **otra hace una estocada con mancuerna**".
- La de la estocada está en el fotograma original, pero el recorte (40, 366, 608, 792) la dejó afuera: en `clase-568.webp` solo asoma un pedazo de brazo y de pierna en el borde izquierdo. No se reconoce ni la estocada ni la mancuerna.
- La alumna del piso apoya **una** mano en la pelota; la otra está en el piso.

**Evidencia.** `08-clase-recorte-vs-fotograma.jpg`: a la izquierda, el fotograma `2026-04-02_DWpl7tBNP0R_f004s.jpg` con la caja del recorte en naranja; a la derecha, `clase-568.webp`. Recorte según `docs/imagenes.md`, línea 28.

**Arreglo:** «Una clase en el cuartel: un alumno hace remo con TRX contra la pared y una alumna, en cuatro apoyos, apoya una mano sobre una pelota medicinal. Atrás se ve una camioneta de Bomberos.»

### COPY-5 · media · Preguntas del copy para Nicolás: no están en ningún lado vigente

**Problema.** El brief pide que lo que falta o se supuso "quede como pregunta en el README", y `TAREAS.md` tiene pendiente "Revisar el texto del sitio antes de publicar". El repo no tiene `README.md`. La única lista es la sección 12 de `docs/plan.md`, que es del plan v0 y contradice al sitio:
- dice que la licenciatura va sin año, y el sitio pone 2023;
- dice que quedan afuera el cargo en el CEF n.º 198 y los cursos cortos, y el sitio los muestra.

Lo que hoy está en la página sin confirmar:
1. La cita de El enfoque está **reconstruida desde los subtítulos** del reel ("puede faltar alguna palabra", `INDICE.md`, línea 164) y se presenta firmada por él.
2. "Valores de octubre 2026" es un supuesto (`fuentes.md`, tabla de discrepancias).
3. "¿Preferís llamar? 2345-402547": no se sabe si ese número atiende llamadas (pregunta 8 del plan).
4. "Y otra vuelta" (ver COPY-6).
5. "Equipo de conducción del CEF n.º 198 · Secretario" y la lista de cursos: los pidió Pablo (`diseno.md`), pero el plan los tenía como pregunta para Nicolás.

**Evidencia.** `find . -iname "readme*"` no devuelve nada. `docs/plan.md`, líneas 1483 y 1504-1508.

**Arreglo.** En el README, en "Decisiones tomadas sin Nicolás (revisar)", anotar estos cinco puntos con la frase exacta que se usó. Sacar o actualizar la lista vieja del plan.

### COPY-6 · menor · "Y otra vuelta" (index.html:183)

**Problema.** Afirma que la clase repite el circuito. Ninguna fuente lo dice: el PDF habla de "estaciones de trabajo" y de "sostener el entrenamiento durante toda la clase", y el brief de "un circuito de estaciones". Con una hora y cinco estaciones es casi seguro que haya más de una vuelta, y es parte del diseño aprobado. Por eso es menor, pero hay que confirmarlo.

**Arreglo.** Preguntárselo a Nicolás (va en la lista de COPY-5). Si no repite el circuito, cambiar el rótulo por «Y la estación siguiente».

### COPY-7 · menor · Bio del profe, `p.profe-bio` (index.html:257)

**Problema.** "Es preparador físico de las inferiores de fútbol de Nuevo Globito y da clases de Educación Física en escuelas de la zona desde 2017." El "desde 2017" se puede leer como de las dos cosas, y lo de Nuevo Globito es desde 2022 (CV: "Club Atlético Nuevo Globito, 2022 - Actualidad").

**Arreglo:** «Da clases de Educación Física en escuelas de la zona desde 2017 y desde 2022 es preparador físico de las inferiores de fútbol de Nuevo Globito. En el espacio planifica los entrenamientos y corrige la técnica de cada uno.»

### COPY-8 · menor · Experiencia, docencia (index.html:262)

**Problema.** "En escuelas de la zona, en todos los niveles y en el CEF". El CV dice "en todos los niveles **de la educación obligatoria** y CEF". Sin eso, "todos los niveles" puede incluir terciario o universitario, y no es lo que dice el CV.

**Arreglo:** «En escuelas de la zona, en todos los niveles de la educación obligatoria, y en el CEF».

### COPY-9 · menor · Los tres botones "Reservá tu clase de prueba gratis" a 360 px o menos

**Problema.** A 320 y 360 px el texto se parte en dos líneas y **"gratis" queda sola** en la segunda, en el botón de la portada, en el del bloque final y en el de la barra fija. Es justo la palabra que el brief pide que quede clara en el botón. La decisión 16 del plan suponía que entraba en una línea a 360 px. A 375 y 390 px entra.

**Evidencia.** Medido con un `Range` sobre el texto del botón: 2 líneas, la última palabra es "gratis" y el botón mide 67 px de alto (contra 56 px a 375). Ver `02-movil-360x740-pliegue.jpg`, `04-movil-360-bloque-final.jpg` y `05-movil-360-barra-fija.jpg`.

**Arreglo.** `.boton { text-wrap: balance; }`. Probado inyectándolo a 360 px: queda «Reservá tu clase / de prueba gratis», con 130 y 129 px por línea (`10-movil-360-boton-con-balance-prueba.jpg`). No cambia el texto ni el estilo.

### COPY-10 · menor · Datos de la portada sin JS (index.html:108)

**Problema.** Con el JS apagado, el dato de la cuota dice "Cuota / **Ver** / por mes", que no se entiende.

**Evidencia.** `03-movil-390-sin-js-datos.jpg`. `innerText` de `.datos` con `java_script_enabled=False`.

**Arreglo.** Que el texto de reserva diga algo completo y que el JS escriba la unidad. Por ejemplo, `<a href="#turnos" data-copia="cuota">Ver la cuota</a><small data-copia="cuota-unidad">más abajo</small>`, y en `main.js` cambiar ese `small` por «por mes» cuando copia el precio. El precio sigue en un solo lugar.

### COPY-11 · menor · "Valores de octubre 2026" (index.html:224 y main.js:57)

**Problema.** Con mes y año, la forma correcta es "octubre **de** 2026". Se repite en el `priceRange` del JSON-LD ("valores de octubre 2026").

**Arreglo.** `<span id="precio-vigencia">octubre de 2026</span>`. Así el JS lo copia bien al JSON-LD. Además, confirmarlo con Nicolás (COPY-5).

### COPY-12 · menor · "Nº" y "n.º", y cortes de línea en nombres

**Problema.**
- La dirección usa "Nº 739" (4 veces) y el CEF usa "n.º 198": dos formas de la misma abreviatura en la misma página.
- En el celular se cortan nombres que tendrían que ir juntos:
  - "Equipo de conducción del CEF / n.º 198";
  - "Universidad de San Pablo- / Tucumán" (corta en el guion);
  - "Veinticinco de Mayo (CP 6660), Buenos / Aires".

**Evidencia.** Conteo en el HTML: `Nº` 4 veces, `n.º` 1 vez, ningún espacio duro ni guion que no corte. Capturas `12-movil-390-cortes-trayectoria.jpg` (CEF y universidad) y `13-movil-390-cortes-direccion.jpg` ("Buenos / Aires").

**Arreglo.**
- Escribir «CEF Nº&nbsp;198», con la misma forma que la dirección (la de `TAREAS.md`), dentro de `<span class="nowrap">`.
- Escribir «San&nbsp;Pablo&#8209;Tucumán», con un guion que no corta (U+2011).
- Escribir «Buenos&nbsp;Aires» en el `address`.

### COPY-13 · menor · Lista de cursos (index.html:283, 285-287)

**Problema.**
- "infanto-juvenil": la forma correcta es «infantojuvenil», en una palabra. El CV dice "infanto juvenil".
- "Entrenamiento intermitente y sistemas de entrenamiento, Cantidad de Calidad (2020)" junta dos cursos distintos del CV ("entrenamiento intermitente" y "sistemas de entrenamiento") en un título que parece uno solo.
- El CV escribe "Pablo Añon" y "Emiliano Gonzalez" sin tilde, y el sitio lo copia igual. Si los apellidos son Añón y González, hay que corregirlos. No se puede confirmar desde las fuentes.

**Arreglo.**
- «Preparación física de fútbol infantojuvenil, Yo Sé (2023)».
- «Entrenamiento intermitente y Sistemas de entrenamiento (dos cursos), Cantidad de Calidad (2020)».
- Preguntarle a Nicolás por las dos tildes.

### COPY-14 · menor · Orden de Experiencia y Formación (index.html:260-274)

**Problema.** Ninguna de las dos listas sigue un orden que se entienda:
- Experiencia: 2022 – hoy, 2017 – hoy, **2025 – hoy**, 2021 – 2022, 2020 – 2022.
- Formación: 2023, 2020, 2017, **2025**.

El 2025 después del 2017 parece un error.

**Arreglo.** Ordenar de lo más nuevo a lo más viejo:
- Formación: 2025 (Tercer dan), 2023, 2020 y 2017.
- Experiencia: primero lo vigente (2025 – hoy, 2022 – hoy, 2017 – hoy) y después 2021 – 2022 y 2020 – 2022.

Si se prefiere dejar primero lo más relevante (fútbol), alcanza con pasar el karate a la última línea con un rótulo propio.

### COPY-15 · menor · Bajada de Turnos y cuota (index.html:209)

**Problema.** "Los días que no venís podés combinar con algo más suave" deja a "combinar" sin objeto. Viene del PDF ("que el alumno combine con actividades de menor intensidad"), pero al pasarlo a segunda persona se nota más.

**Arreglo:** «Elegís un turno y venís 2 veces por semana. Los días que no venís podés combinarlo con algo más suave, como caminar o andar en bicicleta.»

### COPY-16 · menor · Nombre de una oferta del JSON-LD (main.js:62)

**Problema.** En la página, el plan de $25.000 es "Plan complemento · Solo el plan, sin venir a las clases". En el JSON-LD se llama "Plan personalizado, sin las clases", otro nombre para lo mismo.

**Arreglo.** `oferta('Plan complemento, solo el plan (sin las clases)', …)`.

## Cada afirmación del sitio → de dónde sale

Siglas: **T** = `TAREAS.md`, "Datos del negocio". **PDF** = "INFORMACIÓN Y ARANCELES" (`fuentes.md`, sección 1). **CV** = `fuentes.md`, sección 2, y el PDF del CV. **R28** = reel del 28/07/2026 (`INDICE.md`, línea 165). **R05** = reel del 05/10/2026. **B** = brief (`PROMPT-SITIO.md`). **D** = `docs/diseno.md`.

| Línea | Afirmación en el sitio | Fuente | Estado |
|---|---|---|---|
| 6 | title "Entrenamiento funcional en 25 de Mayo \| Espacio Funcional 25" | B, "SEO local" | OK (60 caracteres) |
| 7 | meta description: grupos de máximo 7, Cuartel de Bomberos de 25 de Mayo, clase de prueba gratis por WhatsApp | T | OK (150 caracteres) |
| 14-15 | og:title y og:description, "con el Prof. Nicolás Valle" | T | OK |
| 20 | og:image:alt: logo, «Entrenamiento funcional en 25 de Mayo», «Clase de prueba gratis», foto de una clase en el cuartel | `og.jpg` (visto) | OK |
| 33 | JSON-LD description, "con el Prof. Nicolás Guido Valle" | T | OK |
| 37 | telephone "+54 9 2345 40-2547" | T + `INDICE.md` (wa.me con el 9) | OK |
| 40-44 | Calle 21 Nº 739, entre 8 y 9 (Cuartel de Bomberos), Veinticinco de Mayo, Buenos Aires, 6660 | T | OK |
| 46-47 | coordenadas y `hasMap` | `INDICE.md`, "Google Maps" | OK (la ficha es la del cuartel; cambiarla cuando haya Perfil de Empresa) |
| 48-50 | lunes y jueves de 18:00 a 20:00; martes y viernes de 07:00 a 08:00 | T | OK |
| main.js 57-63 | priceRange y ofertas de $0, $35.000, $10.000 y $25.000 | T | OK. Nombre: COPY-16. "octubre 2026": COPY-11 |
| 101 | "Entrenamiento funcional en 25 de Mayo." | T, B | OK |
| 101 | "Que quieras volver." | R28 ("lograr que quieras volver cada semana"), PDF ("quiera volver"), B | OK, su idea |
| 102 | "Grupos de máximo 7 personas en el Cuartel de Bomberos: calle 21 Nº 739, entre 8 y 9." | T | OK |
| 104, 303, 335 | "Reservá tu clase de prueba gratis" | B, T | OK. Corte de línea: COPY-9 |
| 105 | "Te abre WhatsApp. Pagás recién desde la segunda clase." | T ("Empieza a pagar desde la segunda clase") | OK |
| 108 | Cuota $35.000 por mes (lo copia el JS) | T | OK. Sin JS: COPY-10 |
| 109-110 | "18 y 19 h, lunes y jueves" · "7 h, martes y viernes" | T; la forma es la de la placa del R28 ("Lunes y jueves 18 y 19 hs / Martes y viernes 7 hs") | OK |
| 118-119 | sello "Clase de prueba · gratis · 25 de Mayo", "$0" | T | OK |
| 124 | alt de la portada (ver tabla de alt) | fotograma `DbUtD7_j4uj_f018s` | OK |
| 128 | "En el Cuartel de Bomberos" | T, `INDICE.md` | OK |
| 135 | banda: Fuerza, Resistencia, Técnica, Continuidad, Máximo 7 por turno, 25 de Mayo | PDF ("fuerza, resistencia", "técnica correcta", "la continuidad"), T | OK |
| 146 | "Lo más fácil · Agotarte hasta dejarte sin aire." | R28 y PDF | **Recorte que cambia el sentido: COPY-2** |
| 147 | "Lo que de verdad importa · Que quieras volver cada semana, sin lastimarte entrenando." | R28 | **Falta "Lo difícil": COPY-2** |
| 151-158 | "Por eso en Espacio Funcional 25 buscamos:" + 4 ítems + "Porque el factor más importante…" | PDF, textual | OK |
| 161 | "Nicolás Valle · Profe de Espacio Funcional 25" | T | OK. La cita está reconstruida: COPY-5 |
| 172 | "Una hora" | T (cada turno dura una hora) | OK |
| 172 | "de fuerza, resistencia y acondicionamiento físico, en estaciones de trabajo" | PDF, "¿Qué hacemos?" | OK |
| 172 | "Cada estación cambia el movimiento." | Paráfrasis de PDF "alternar patrones de movimiento" | Pierde su término: COPY-1 |
| 176 | "Una vuelta del circuito, por ejemplo" | B ("circuito de estaciones"), PDF ("por ejemplo") | OK |
| 178-182 | Sentadillas, Empujes, Tracciones, Core, Aeróbico | PDF, la misma lista y en el mismo orden | OK |
| 178-182 | Levantar, Empujar, Tirar, Estabilizar | carrusel del 05/02/2026 ("empujar, tirar, levantar, estabilizar") | OK |
| 182 | "Moverte" | No es un verbo de la lista del carrusel. Es un rótulo de la estación aeróbica, no una afirmación | OK |
| 178-179 | "Con mancuernas" · "Press con mancuernas" | fotograma `DbUtD7_j4uj_f008s` (visto: sentadilla con press de mancuernas) | OK |
| 180 | "Remo con TRX" | fotogramas `DUa7Xy0DthX_f024s` (visto), `DXvBvnKDg29_f016s` y `DbUtD7_j4uj_f042s` | OK |
| 181 | "Con la pelota medicinal" | fotograma `DWpl7tBNP0R_f004s` (visto) | OK |
| 182 | "Saltos, cubierta y maza" | fotogramas `DXvBvnKDg29_f014s` y `DbUtD7_j4uj_f034s` (`INDICE.md`) | OK |
| 183 | "Y otra vuelta" | Ninguna explícita | Confirmar: COPY-6 |
| 185 | "mantenés un buen nivel de esfuerzo sin generar fatiga excesiva" | PDF, textual | OK |
| 185 | "sin terminar destruido" | R28 | OK |
| 185 | "Como cada estación trabaja otra parte del cuerpo" | **Ninguna** | **COPY-1** |
| 189 | alt de la clase | fotograma `DWpl7tBNP0R_f004s` | **Describe lo que quedó afuera: COPY-4** |
| 190 | "Una clase en el cuartel: cada uno en su estación, al mismo tiempo." | la foto (visto) | OK |
| 193 | "7 personas como máximo por turno" | T | OK |
| 197 | "Es a propósito." | T ("El máximo de 7 es a propósito") | OK |
| 197 | "En grupos chicos hay supervisión constante, corrección técnica y adaptación de los ejercicios según tu nivel." | PDF, "Modalidad de trabajo"; "Grupos chicos" de las placas de 2026 | OK |
| 209 | "Elegís un turno y venís 2 veces por semana." | B, T | OK |
| 209 | "…combinar con algo más suave, como caminar o andar en bicicleta." | PDF ("caminata, bicicleta, etc.") | OK. Gramática: COPY-15 |
| 215-219 | los tres turnos; máximo 7 por turno | T | OK |
| 223 | $35.000 por mes | T | OK |
| 224 | "Valores de octubre 2026." | Supuesto (`fuentes.md`: "Asumir octubre 2026; confirmar con Nicolás") | COPY-5 y COPY-11 |
| 226-229 | 2 clases por semana, planificación del entrenamiento, seguimiento técnico, adaptación de los ejercicios según tu nivel | T, PDF | OK |
| 231 | "La clase de prueba es gratis. Empezás a pagar desde la segunda clase." | T | OK |
| 235-236 | "Un plan para hacer por tu cuenta. Personalizado: running, fuerza o lo que necesites." | T, B | OK |
| 238-239 | $10.000 extra por mes si ya entrenás; $25.000 por mes solo el plan | T | OK |
| 255-256 | Nicolás Guido Valle, Profesor en Educación Física y licenciado en Alto Rendimiento Deportivo | T, CV | OK |
| 257 | preparador físico de las inferiores de Nuevo Globito | CV (2022 – actualidad) | OK. Ambigüedad: COPY-7 |
| 257 | da clases en escuelas de la zona desde 2017 | CV | OK |
| 257 | "En el espacio planifica los entrenamientos y corrige la técnica de cada uno." | PDF ("planificación del entrenamiento", "corrección técnica"), R28 ("corregir tu técnica"), T (es el espacio de Nicolás) | OK (síntesis, no textual) |
| 261 | 2022 – hoy, PF de fútbol, 8.ª, 7.ª, 6.ª y 5.ª, Club Atlético Nuevo Globito | CV | OK |
| 262 | 2017 – hoy, profesor de Educación Física, "en todos los niveles y en el CEF" | CV ("…de la educación obligatoria y CEF") | Recorte que agranda: COPY-8 |
| 263 | 2025 – hoy, equipo de conducción del CEF n.º 198, Secretario | CV ("Secretario de educación… Parte del equipo de conducción del CEF n° 198"); D | OK. Confirmar: COPY-5 |
| 264 | 2021 – 2022, sala de fuerza y clases de funcional, "Proyecto propio, junto a otros colegas" | CV ("Otros trabajos de entrenador. Propio asociado con otros colegas. Sala de entrenamiento de fuerza y clases de funcional, 2021 - 2022") | OK |
| 265 | 2020 – 2022, PF de rugby, M12, M14 y M16, Tacuara Rugby Club | CV | OK |
| 270 | 2023, licenciado en Alto Rendimiento Deportivo, Universidad de San Pablo-Tucumán | CV (año), diploma (nombre), D (Pablo confirmó 2023) | OK |
| 271 | 2020, diplomado «Preparador físico deportivo», Asociación Natatio Argentina | CV | OK |
| 272 | 2017, Profesor en Educación Física, Instituto Santa Rosa | CV | OK |
| 273 | 2025, tercer dan de karate Goju-Ryu, Traditional Okinawan Goju-Ryu Karate-Do Federation | CV | OK |
| 279-290 | 12 cursos | CV | OK. Detalles: COPY-13 |
| 301 | "No hace falta que estés en forma para arrancar." | R28, textual | OK |
| 302 | "Vení a una clase de prueba para conocer cómo trabajamos." | PDF ("Podés venir a una clase de prueba para conocer cómo trabajamos") | OK |
| 302 | "Es gratis: la reservás por WhatsApp y empezás a pagar desde la segunda clase." | T | OK |
| 304 | "¿Preferís llamar? 2345-402547" | T (el número); que atienda llamadas no está confirmado | COPY-5 |
| 307 | alt de "Dónde estamos" | fotograma `DUa7Xy0DthX_f024s` | OK |
| 310 | Cuartel de Bomberos, Calle 21 Nº 739, entre 8 y 9, Veinticinco de Mayo (CP 6660), Buenos Aires | T | OK. Corte de línea: COPY-12 |
| 312, 328 | "Cómo llegar" a Google Maps | `INDICE.md` (enlace probado) | OK |
| 324 | "Entrenamiento funcional en grupos de máximo 7 personas, en 25 de Mayo." | T | OK |
| 326 | "WhatsApp 2345-402547" | T | OK |
| 330 | © Espacio Funcional 25 · Prof. Nicolás Guido Valle · Cuartel de Bomberos, calle 21 Nº 739, Veinticinco de Mayo | T | OK |

## Mensajes prellenados de WhatsApp (decodificados)

| Dónde | Texto | Revisión |
|---|---|---|
| Encabezado, menú, portada, bloque final, pie y barra fija (7 enlaces) | «Hola, Nicolás. Vi la página de Espacio Funcional 25 y quiero reservar la clase de prueba gratis. ¿Qué turno tenés libre?» | Voseo, tildes y signos de apertura bien. No promete nada que no esté en `T`. Va a `wa.me/5492345402547`. |
| "Consultar por el plan" | «Hola, Nicolás. Vi la página de Espacio Funcional 25 y quiero consultar por el plan complemento.» | Bien. |

## Texto alternativo de cada imagen

| Imagen (vista con Read) | alt | Qué se ve | Estado |
|---|---|---|---|
| `portada-movil-716` y `portada-compu-640` | Nicolás Valle le muestra un ejercicio a una alumna en el Cuartel de Bomberos, con las autobombas estacionadas atrás. | Nicolás con los codos arriba, mostrando el movimiento; la alumna lo copia con una bolsa. Atrás, una autobomba roja, un camión rojo al fondo, una camioneta roja y dos utilitarios blancos. | OK |
| `clase-568` | …un alumno hace remo con TRX, una alumna apoya las manos en una pelota medicinal y otra hace una estocada con mancuerna. | Remo con TRX y una alumna en cuatro apoyos con una mano en la pelota. La de la estocada no está. | **COPY-4** |
| `profe-596` | Nicolás Valle con el buzo de Espacio Funcional 25 y una pelota de ejercicio naranja, en el cuartel. | Buzo negro con el logo bordado y una pelota suiza naranja. Que es el cuartel lo dice `INDICE.md` (todos los fotogramas de 2026 son de ahí). | OK |
| `donde-716` | Una alumna hace remo con TRX en el salón del cuartel, debajo del letrero de Bomberos Voluntarios. | TRX delante del letrero "BOMBEROS VOLUNTA…". | OK |
| `og.jpg` | og:image:alt (ver la tabla de arriba) | Logo, "Espacio Funcional 25", la bajada, la cinta "Clase de prueba gratis" y la foto de la portada. | OK |
| `logo-80`, `logo-72` y `avatar-104` | `""` | Al lado está el nombre escrito. | OK |

`aria-label`: "Secciones", "Contacto", "Escribir por WhatsApp" y "Abrir el menú" / "Cerrar el menú" (los cambia el JS). Están bien y con voseo. La banda y el sello tienen `aria-hidden`, y lo que dicen ya está en el texto ("gratis" figura en el botón).

## Ortografía, signos y voseo: lo que se revisó y está bien

- **Voseo parejo** en todo el sitio: reservá, reservala, vení, elegís, venís, podés, entrenás, pagás, empezás, mantenés, sostenés, preferís, tenés. No hay ni un tuteo.
- **Tildes:** sin errores en el texto propio (Dónde, Cómo, Aeróbico, Técnica, menú, Nicolás, Atlético, Atlántida…). Las de dos apellidos del CV están en COPY-13.
- **Signos:**
  - ¿? de apertura en "¿Preferís llamar?" y en el mensaje de WhatsApp;
  - «» en el diplomado y en el og:image:alt;
  - – en los rangos de años (5 veces);
  - "8.ª, 7.ª, 6.ª y 5.ª" bien abreviados;
  - "Nº" y "n.º": COPY-12.
- **Números y unidades:** "18 a 19 h", "19 a 20 h", "7 a 8 h", "18 y 19 h", "7 h", "$35.000", "$10.000", "$25.000", "(CP 6660)". Son coherentes.
- **Nombres propios bien escritos:** Nuevo Globito, Club Atlético Nuevo Globito, Tacuara Rugby Club, Universidad de San Pablo-Tucumán, Goju-Ryu, Karate-Do, Asociación Natatio Argentina, Instituto Santa Rosa, Unión Argentina de Rugby.

## Capturas

| Archivo | Qué muestra |
|---|---|
| `copy/01-movil-390x844-pliegue.jpg` | Primera pantalla en el celular: qué, dónde, cuánto, horarios, gratis y desde la segunda clase |
| `copy/02-movil-360x740-pliegue.jpg` | Lo mismo a 360: "gratis" sola en la segunda línea del botón (COPY-9) |
| `copy/03-movil-390-sin-js-datos.jpg` | "Cuota / Ver / por mes" sin JS (COPY-10) |
| `copy/04-movil-360-bloque-final.jpg` | Botón del bloque final a 360 (COPY-9) |
| `copy/05-movil-360-barra-fija.jpg` | Barra fija a 360 (COPY-9) |
| `copy/06-movil-360-antetitulo-profe.jpg`, `copy/06-movil-390-antetitulo-profe.jpg` | El disco tapa "El profe" (COPY-3) |
| `copy/07-movil-390-zoom-el-profe-tapado.png` | Zoom del rótulo tapado, a 3x (COPY-3) |
| `copy/08-clase-recorte-vs-fotograma.jpg` | Fotograma original con la caja del recorte, al lado de la foto publicada (COPY-4) |
| `copy/09-compu-1366x768-pliegue.jpg` | Primera pantalla en la compu |
| `copy/10-movil-360-boton-con-balance-prueba.jpg` | El arreglo de COPY-9 probado |
| `copy/11-movil-360-el-profe-arreglo-probado.png` | El arreglo de COPY-3 probado |
| `copy/12-movil-390-cortes-trayectoria.jpg` | "CEF / n.º 198" y "San Pablo- / Tucumán" partidos (COPY-12); orden de los años (COPY-14) |
| `copy/13-movil-390-cortes-direccion.jpg` | "Buenos / Aires" partido en la dirección (COPY-12) |
