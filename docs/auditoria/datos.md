# Auditoría de datos · Espacio Funcional 25

10/10/2026 · sitio en `http://127.0.0.1:8802/` (commit `c8960e6`) · fuente de verdad: `espacio-funcional-25/TAREAS.md`, sección "Datos del negocio" · capturas en `docs/auditoria/datos/`

## Resumen

Todos los datos del negocio están bien: los tres turnos, el máximo de 7, la cuota y lo que incluye, el plan complemento con sus dos precios, la clase de prueba, la dirección con CP, el teléfono, el Instagram, los 8 links de WhatsApp, el `tel:` y el link de Maps. No hay datos inventados ni viejos (ni el 6:30 del PDF) en el HTML, el JSON-LD ni la imagen OG. El dominio es el mismo en los 9 lugares donde aparece. Existen todos los archivos que referencia el HTML y los `width`/`height` de cada imagen coinciden con la proporción del archivo.

No hay hallazgos graves. Hay uno medio: **la cuota de la portada depende de `main.js`**. Sin JS, o mientras el script no llegó (red móvil lenta), la portada dice "Cuota · Ver · por mes". Los otros seis son menores: el JSON-LD sin JS, la vigencia en las ofertas, el formato de `streetAddress`, el @ del Instagram, el README que falta y un `alt` que describe a alguien que quedó fuera del recorte.

## 1. Dato por dato

Las líneas son de `index.html`. "Final" quiere decir el JSON-LD después de que corre `main.js`, leído con Playwright.

| # | Dato | Qué dice el sitio (dónde) | Qué dice TAREAS.md | Estado |
|---|---|---|---|---|
| 1 | Turno 1 | "Lunes y jueves · 18 a 19 h" (l. 215). Portada: "Tarde · 18 y 19 h · lunes y jueves" (l. 109). JSON-LD: Monday y Thursday, 18:00–20:00 (l. 49, une los turnos 1 y 2) | Lunes y jueves 18 a 19 h | OK |
| 2 | Turno 2 | "Lunes y jueves · 19 a 20 h" (l. 216). Portada: ídem fila 1 | Lunes y jueves 19 a 20 h | OK |
| 3 | Turno 3 | "Martes y viernes · 7 a 8 h" (l. 217). Portada: "Mañana · 7 h · martes y viernes" (l. 110). JSON-LD: Tuesday y Friday, 07:00–08:00 (l. 50) | Martes y viernes 7 a 8 h | OK |
| 4 | 2 clases por semana, se elige un turno | "Elegís un turno y venís 2 veces por semana" (l. 209); "2 clases por semana" (l. 226). La clase dura una hora (l. 172), igual que los turnos | 2 clases por semana | OK |
| 5 | Máximo 7 por turno | meta description y og:description (l. 7 y 15), portada (l. 102), banda (l. 135), "7 personas como máximo por turno" (l. 193), "Máximo 7 personas por turno." (l. 219), pie (l. 324), JSON-LD `description` | Máximo 7 personas por turno | OK |
| 6 | Por qué 7 | "Es a propósito. En grupos chicos hay supervisión constante, corrección técnica y adaptación de los ejercicios según tu nivel." (l. 197) | A propósito, semipersonalizado, para que cada uno haga bien los ejercicios | OK |
| 7 | Cuota | `<strong id="precio-cuota">$35.000</strong>` "por mes" (l. 223, único lugar). Portada: la copia el JS y Playwright lee "$35.000". JSON-LD final: `price: 35000`, `priceCurrency: ARS`, `unitText: mes` y `priceRange: "$35.000 por mes (valores de octubre 2026)"` | $35.000 por mes | OK con JS. **Sin JS: "Ver" en la portada y nada de precio en el JSON-LD** (DAT-1, DAT-2) |
| 8 | Vigencia del precio | "Valores de octubre 2026." (l. 224, `#precio-vigencia`). JSON-LD final: solo dentro del texto de `priceRange` | (brief: mostrar de qué mes es) | OK en la página. En las ofertas no está (DAT-3) |
| 9 | Qué incluye la cuota | "2 clases por semana", "Planificación del entrenamiento", "Seguimiento técnico", "Adaptación de los ejercicios según tu nivel" (l. 226–229) | 2 clases por semana, planificación, seguimiento técnico y adaptación según nivel | OK |
| 10 | Plan complemento: qué es | "Un plan para hacer por tu cuenta" / "Personalizado: running, fuerza o lo que necesites." (l. 235–236) | Personalizado, de lo que necesite: running, fuerza, etc. | OK |
| 11 | Plan complemento para alumnos | "Si ya entrenás en el espacio · $10.000 · extra por mes" (l. 238). JSON-LD final: "Plan complemento para quienes entrenan en el espacio", 10000 ARS por mes | $10.000 extra por mes si ya entrena en el espacio | OK |
| 12 | Plan solo | "Solo el plan, sin venir a las clases · $25.000 · por mes" (l. 239). JSON-LD final: "Plan personalizado, sin las clases", 25000 ARS por mes | $25.000 por mes si no hace funcional | OK |
| 13 | Clase de prueba gratis | Botones "Reservá tu clase de prueba gratis" (l. 84, 104, 303, 335); sello "$0 · Clase de prueba · gratis" (l. 118–119); "La clase de prueba es gratis." (l. 231); bloque final (l. 302); meta y og:description; imagen OG ("Clase de prueba gratis"); JSON-LD final: oferta "Clase de prueba", `price: 0` | Gratis | OK |
| 14 | Se reserva por WhatsApp | "Te abre WhatsApp." (l. 105); "la reservás por WhatsApp" (l. 302); todos los botones de reserva van a wa.me | Se reserva por WhatsApp | OK |
| 15 | Se paga desde la segunda | "Pagás recién desde la segunda clase." (l. 105); "Empezás a pagar desde la segunda clase." (l. 231); "empezás a pagar desde la segunda clase" (l. 302) | Empieza a pagar desde la segunda clase | OK |
| 16 | Dirección | "Cuartel de Bomberos · Calle 21 Nº 739, entre 8 y 9" (l. 310). Portada: "calle 21 Nº 739, entre 8 y 9." (l. 102). Pie: "Cuartel de Bomberos, calle 21 Nº 739, Veinticinco de Mayo" (l. 330, abreviado sin entrecalles ni CP). JSON-LD: `streetAddress: "Calle 21 Nº 739, entre 8 y 9 (Cuartel de Bomberos)"` | Cuartel de Bomberos, Calle 21 Nº 739 e/ 8 y 9 | OK. El formato del `streetAddress` es mejorable (DAT-4) |
| 17 | Localidad, CP, provincia | "Veinticinco de Mayo (CP 6660), Buenos Aires" (l. 310). JSON-LD: `addressLocality: Veinticinco de Mayo`, `postalCode: 6660`, `addressRegion: Buenos Aires`, `addressCountry: AR` | Veinticinco de Mayo (CP 6660), Buenos Aires | OK |
| 18 | Teléfono visible | "¿Preferís llamar? 2345-402547" (l. 304); "WhatsApp 2345-402547" (l. 326) | 2345-402547 | OK |
| 19 | `tel:` | `tel:+5492345402547` (l. 304, único) | 2345-402547 → +54 9 2345 402547 | OK |
| 20 | Teléfono en JSON-LD | `"+54 9 2345 40-2547"` | ídem | OK |
| 21 | Número de WhatsApp | `wa.me/5492345402547` en los 8 links (l. 84, 86, 87, 104, 241, 303, 326, 335). No hay ninguno con `542345402547` ni con `api.whatsapp.com` | 2345-402547 (y `INDICE.md`: usar `5492345402547`) | OK |
| 22 | Texto de WhatsApp: reserva (7 links) | "Hola, Nicolás. Vi la página de Espacio Funcional 25 y quiero reservar la clase de prueba gratis. ¿Qué turno tenés libre?" | — | OK: está bien codificado (tildes, ¿ y ?) |
| 23 | Texto de WhatsApp: plan (l. 241) | "Hola, Nicolás. Vi la página de Espacio Funcional 25 y quiero consultar por el plan complemento." | — | OK |
| 24 | Instagram | `https://www.instagram.com/espaciofuncional25/` (l. 313, 327) y JSON-LD `sameAs` | @espaciofuncional25 | OK el link. **El @ no aparece escrito en ningún lado** (DAT-5) |
| 25 | Cómo llegar (Maps) | `https://www.google.com/maps/dir/?api=1&destination=-35.4387213%2C-60.1711055` (l. 312, 328) | Coordenadas del Cuartel de Bomberos Voluntarios (`INDICE.md`): −35.4387213, −60.1711055 | OK, es el link que `INDICE.md` da como probado |
| 26 | geo y hasMap | `geo: -35.4387213, -60.1711055`; `hasMap: maps.google.com/?cid=8828057531265068567` (la ficha del cuartel, como dice `INDICE.md`) | ídem | OK |
| 27 | Profe | "Nicolás Guido Valle" / "Profesor en Educación Física y licenciado en Alto Rendimiento Deportivo" (l. 255–256); pie "Prof. Nicolás Guido Valle"; og:description "Prof. Nicolás Valle"; JSON-LD "Prof. Nicolás Guido Valle" | Prof. Nicolás Guido Valle, Lic. en Alto Rendimiento Deportivo | OK |
| 28 | Imagen OG (`assets/img/og.jpg`, 1200×630, la miré) | "Espacio Funcional 25 / Entrenamiento funcional en 25 de Mayo / Clase de prueba gratis", con el logo y la foto de Nicolás con una alumna en el cuartel. Sin precios ni horarios | — | OK. El `og:image:alt` (l. 20) describe bien la imagen |

**Trayectoria del profe contra el CV** (`NICOLÁS gUIDO VALLE (3).pdf`): coinciden Nuevo Globito 2022–hoy (8.ª, 7.ª, 6.ª y 5.ª), docente desde 2017 en el sistema provincial, secretario del CEF n.º 198 desde 2025, la sala de fuerza propia de 2021–2022, Tacuara M12/M14/M16 de 2020–2022, la licenciatura de 2023 en la Univ. de San Pablo-Tucumán, el diplomado de la Asociación Natatio de 2020, el profesorado de 2017 en el Instituto Santa Rosa, el 3.er dan de 2025 y los 12 cursos con sus años. No aparece ningún domicilio ni dato personal.

**Fuera del alcance de esta auditoría (para copy):** los ejemplos del circuito ("Press con mancuernas", "Con la pelota medicinal", "Saltos, cubierta y maza", l. 178–182) salen de lo que se ve en los reels y llevan un "por ejemplo" adelante. Ni el PDF ni `TAREAS.md` los nombran. Conviene que Nicolás los confirme.

## 2. Precio en un solo lugar

- `grep -rnE "35\.000|35000|10\.000|25\.000"` en todo el repo, salvo `docs/` y `.git`: hay **3 resultados, todos en el bloque "Turnos y cuota" de `index.html`** (l. 223, 238 y 239). Tampoco hay variantes como "35 mil", "35,000", "10000" o "25000".
- `js/main.js` no tiene ningún precio escrito. Los lee del DOM: `texto('precio-cuota')`, `texto('precio-complemento')`, `texto('precio-solo-plan')` y `texto('precio-vigencia')` (l. 42–43 y 60–62).
- La imagen OG no tiene precio (la miré), así que no hay que regenerarla cuando cambie la cuota.
- **Con JS** (Playwright, 390×844): la portada muestra "Cuota · $35.000 · por mes" (captura `02-datos-portada-con-js.png`). El JSON-LD final tiene las 4 ofertas con 0, 35000, 10000 y 25000 ARS, y `priceRange` con "valores de octubre 2026".
- **Sin JS** (`java_script_enabled=False`): la portada muestra "Cuota · **Ver** · por mes" (`06-portada-390-sin-js.png`, `07-datos-portada-sin-js.png`). El JSON-LD queda sin `priceRange` ni `makesOffer`.
- **Con JS lento:** retuve `main.js` con `page.route` sin contestarlo. Con `readyState` en `interactive`, la página ya estaba pintada y decía "Ver" (`08-portada-390-main-js-demorado.png`). Cuando liberé el script pasó a "$35.000".

## 3. JSON-LD

- Es JSON válido: se parsea igual con JS y sin JS. `@type: ExerciseGym`, `@id` y `@context` correctos.
- `address` es un `PostalAddress` completo (calle, localidad, región, CP y país).
- `openingHoursSpecification` es coherente con los turnos: lunes y jueves de 18:00 a 20:00 (los dos turnos de la tarde juntos) y martes y viernes de 07:00 a 08:00.
- `sameAs` apunta al Instagram. `geo` coincide con `INDICE.md`.
- `url`, `image`, `logo` y `@id` son absolutas y del mismo dominio. `logo-120.png` mide 120×120 y existe.
- `telephone` está en formato internacional.
- Precio: lo agrega el JS (ver DAT-2 y DAT-3).

## 4. Dominio

| Lugar | Valor | Estado |
|---|---|---|
| canonical (l. 10) | `https://espaciofuncional25.com.ar/` | OK |
| og:url (l. 16) | `https://espaciofuncional25.com.ar/` | OK |
| og:image (l. 17) | `https://espaciofuncional25.com.ar/assets/img/og.jpg` | OK |
| JSON-LD `@id`, `url`, `image`, `logo` (l. 31, 34–36) | `https://espaciofuncional25.com.ar/…` | OK |
| robots.txt (l. 4) | `Sitemap: https://espaciofuncional25.com.ar/sitemap.xml` | OK |
| sitemap.xml (l. 3) | `https://espaciofuncional25.com.ar/` (lastmod 2026-10-09) | OK |
| .htaccess | no escribe el dominio (redirige a https sin www con `%{HTTP_HOST}`) | OK |

No aparece ningún otro dominio propio. Los demás hosts que hay son wa.me, instagram.com, google.com/maps, schema.org, sitemaps.org, w3.org (dentro de los SVG en `data:` del CSS) y github.com/sil.org (en `assets/fonts/OFL.txt`). Si se pasa a `.com`, hay que cambiar esos 9 lugares; el README tendría que decirlo (DAT-6).

## 5. Archivos referenciados y proporciones

Revisé todos los `src`, `srcset`, `href` de íconos, el preload, el CSS, el JS y las 5 fuentes del CSS: existen todos. Con JS, Playwright no registró errores de consola ni requests con respuesta 400 o más.

| Elemento | Atributos | Archivo(s) | Proporción | Estado |
|---|---|---|---|---|
| logo de la cabecera (l. 73) | 40×40, `srcset` 2x/3x | logo-80.webp 80×80, logo-120.webp 120×120 | 1:1 | OK |
| portada, `<source>` de compu (l. 123) | 640×800 | portada-compu-480 480×600, -640 640×800 | 0,8 | OK |
| portada, `<img>` (l. 124) | 716×537 | portada-movil-400 400×300, -716 716×537 | 1,333 | OK |
| firma (l. 160) | 52×52 | avatar-104 104×104, -156 156×156 | 1:1 | OK |
| clase (l. 189) | 568×426 | clase-400 400×300, -568 568×426 | 1,333 | OK |
| profe (l. 251) | 596×745 | profe-400 400×500, -596 596×745 | 0,8 | OK |
| dónde (l. 307) | 716×448 | donde-400 400×250 (1,600), -716 716×448 (1,598) | ≈1,6 | OK (0,1 % de diferencia) |
| pie (l. 323) | 36×36 | logo-72.webp 72×72 | 1:1 | OK |
| favicon.ico (l. 22) | `sizes="any"` | ICO de 16, 32 y 48 px | — | OK |
| favicon-32.png (l. 23) | 32×32 | 32×32 | — | OK |
| apple-touch-icon (l. 24) | — | 180×180 | — | OK |
| preload (l. 25) | barlow-sc-700.woff2 | existe (23 KB) | — | OK |
| og:image (l. 17–19) | 1200×630 | og.jpg 1200×630 | — | OK |

Hay dos archivos que nada referencia: `assets/img/logo-80.png` y `assets/img/logo-72.png`. No rompen nada; se pueden borrar o dejar.

## 6. Hallazgos

### DAT-1 · media · La cuota de la portada dice "Ver" sin JS o mientras `main.js` no llegó

- **Dónde:** `index.html` l. 108, `<a href="#turnos" data-copia="cuota">Ver</a><small>por mes</small>`; `js/main.js` l. 42–46.
- **Problema:** el dato de la portada que responde "cuánto sale" depende de un script externo con `defer`. Mientras no llega, la portada ya está pintada y dice "Cuota · Ver · por mes". "Ver por mes" no se entiende, y el "Ver" no parece un link: tiene el color del texto (`rgb(23, 24, 26)`), `text-decoration: none` y el mismo tamaño que "$35.000". Para alguien con datos móviles flojos en 25 de Mayo, lo primero que ve es eso, y después el texto cambia.
- **Evidencia:** `docs/auditoria/datos/07-datos-portada-sin-js.png` (sin JS) y `08-portada-390-main-js-demorado.png` (con `main.js` retenido: `readyState` en `interactive` y el texto "Ver"). Con JS: `02-datos-portada-con-js.png`.
- **Arreglo:**
  1. Sacar las 4 líneas que copian la cuota (`main.js` l. 42–46) a un `<script>` inline al final del `<body>`, antes de `<script src="js/main.js" defer>`. Así el precio sigue leyéndose del bloque "Turnos y cuota" (no se escribe en ningún otro lado), pero se copia sin esperar la red.
  2. Que la versión sin JS se lea bien: `<a href="#turnos" data-copia="cuota">Ver</a><small data-copia-nota>en Turnos y cuota</small>`, y que el mismo script cambie la nota por "por mes" cuando copia el precio. Si no, como mínimo, subrayar el link mientras dice "Ver".

### DAT-2 · menor · Sin JS, el JSON-LD no tiene precio

- **Dónde:** `index.html` l. 27–54 y `js/main.js` l. 48–66.
- **Problema:** el brief pide "JSON-LD `ExerciseGym` con … precio". `priceRange` y `makesOffer` los agrega el JS, así que un lector que no ejecuta JS (validadores, algunas herramientas de SEO, buscadores que no renderizan) ve el `ExerciseGym` sin ningún precio. Google sí renderiza JS y toma el JSON-LD final.
- **Evidencia:** sin JS, las claves son `@context, @type, @id, name, description, url, image, logo, telephone, address, geo, hasMap, openingHoursSpecification, sameAs`, sin `priceRange` ni `makesOffer`. Con JS están las 4 ofertas (ver sección 2).
- **Arreglo:** mantener el diseño (escribir el precio en el JSON-LD estático lo pondría en dos lugares) y dejarlo anotado en el README: "el precio del JSON-LD lo completa `main.js` a partir del bloque Turnos y cuota". Cuando se publique, verificarlo con la Prueba de resultados enriquecidos de Google, que renderiza JS.

### DAT-3 · menor · Las ofertas del JSON-LD no llevan la vigencia

- **Dónde:** `js/main.js` l. 52–63.
- **Problema:** "octubre 2026" aparece solo en el texto libre de `priceRange`. Las 4 `Offer` no tienen fecha, así que para un buscador el precio no tiene vigencia. Además, `UnitPriceSpecification` usa solo `unitText: "mes"`, que no es un código que se pueda leer de forma estándar.
- **Evidencia:** JSON-LD final leído con Playwright: cada oferta tiene solo `name`, `price`, `priceCurrency` y `priceSpecification{price, priceCurrency, unitText}`.
- **Arreglo:** en el mismo bloque del HTML, `<span id="precio-vigencia" data-desde="2026-10-01">octubre 2026</span>`. En `oferta()`, agregar `validFrom: document.getElementById('precio-vigencia').dataset.desde` y, en la `priceSpecification`, `unitCode: 'MON'`. Sigue sin haber precios en el JS y la fecha se cambia en el mismo lugar que el precio.

### DAT-4 · menor · `streetAddress` mezcla la calle con las entrecalles y el nombre del lugar

- **Dónde:** `index.html` l. 40.
- **Problema:** `"Calle 21 Nº 739, entre 8 y 9 (Cuartel de Bomberos)"`. La ficha de Maps del cuartel es "C. 21 739, B6660DOO" (`INDICE.md`). Un `streetAddress` con paréntesis, "Nº" y entrecalles es más difícil de cruzar con esa ficha y con el Perfil de Empresa que se va a dar de alta.
- **Evidencia:** l. 40 del HTML; `docs/fotos-instagram/INDICE.md`, sección Google Maps.
- **Arreglo:** `"streetAddress": "Calle 21 739"`. "Entre 8 y 9" y "Cuartel de Bomberos" ya están en la página y en `description`. La dirección visible queda como está.

### DAT-5 · menor · El usuario de Instagram no aparece escrito

- **Dónde:** l. 313 (botón "Instagram") y l. 327 (pie, "Instagram").
- **Problema:** `TAREAS.md` da "@espaciofuncional25", pero el sitio solo dice "Instagram". Quien quiera buscarlo en la app, recordarlo o pasárselo a alguien no tiene el usuario. El link anda bien.
- **Evidencia:** `grep "@espaciofuncional25"` en `index.html` y en el texto visible (Playwright): 0 resultados. Captura `05-pie-390.png`.
- **Arreglo:** en el pie, que el link diga "Instagram @espaciofuncional25", igual que "WhatsApp 2345-402547" al lado. El botón de "Dónde estamos" puede quedar como está.

### DAT-6 · menor · No existe el README que el HTML y el brief mencionan

- **Dónde:** raíz del repo; `index.html` l. 9 ("ver README").
- **Problema:** no hay `README.md`. El brief pide anotar ahí el dominio como pendiente (`.com.ar` o `.com`), y el comentario del HTML manda a leerlo. Tampoco queda escrito en ningún lado del repo dónde se cambia el precio, que es lo que más se va a tocar.
- **Evidencia:** `ls README*` en la raíz: "No such file or directory". El `.htaccess` ya bloquea `/README.md`.
- **Arreglo:** crear `README.md` con:
  - dominio pendiente, con los 9 lugares a cambiar (canonical, og:url, og:image, JSON-LD `@id`/`url`/`image`/`logo`, robots.txt y sitemap.xml);
  - "para cambiar la cuota: `index.html`, bloque Turnos y cuota, `#precio-cuota`, `#precio-complemento`, `#precio-solo-plan` y `#precio-vigencia`; el resto se copia solo";
  - la nota de DAT-2.

### DAT-7 · menor · El `alt` de la foto de la clase describe a alguien que no se ve

- **Dónde:** `index.html` l. 189 (`clase-568.webp` y `clase-400.webp`).
- **Problema:** el `alt` dice "…y otra hace una estocada con mancuerna", pero en el recorte esa persona quedó cortada contra el borde izquierdo: solo se ven un pedazo de brazo arriba y una rodilla abajo. Se ven bien el alumno en TRX y la alumna con la mano en la pelota.
- **Evidencia:** miré `assets/img/clase-568.webp` (568×426).
- **Arreglo:** "Una clase en el cuartel: un alumno hace remo con TRX y una alumna apoya la mano en una pelota medicinal, con la camioneta de Bomberos al fondo." O recortar la foto para que entre la estocada.

## 7. Capturas (`docs/auditoria/datos/`)

- `01-portada-390-con-js.png`: portada a 390×844 (DPR 2), con la cuota copiada.
- `02-datos-portada-con-js.png`: los tres datos de la portada con JS.
- `03-turnos-390.png`: bloque "Turnos y cuota" entero.
- `04-final-donde-390.png`: clase de prueba, teléfono y dirección.
- `05-pie-390.png`: pie.
- `06-portada-390-sin-js.png` y `07-datos-portada-sin-js.png`: sin JS, "Cuota · Ver · por mes".
- `08-portada-390-main-js-demorado.png`: con `main.js` retenido, la página pintada con "Ver".
- `09-portada-1366-con-js.png`: portada en compu.

En `03` y `04`, la barra fija de WhatsApp aparece encima del contenido porque Playwright desplaza la página para sacar la captura de cada elemento. Lo medí aparte: con `#prueba` o `#donde` en pantalla, la barra no tiene la clase `visible`. No es un defecto de esta auditoría.

Scripts usados (scratchpad): `datos_pw.py` (con y sin JS, JSON-LD final, imágenes, consola y red), `datos_lento.py` (`main.js` retenido) y `barra.py`.
