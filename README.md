# Espacio Funcional 25 · sitio

13/10/2026 · Nicolás revisó el texto y dio el OK; el cupo pasó de 7 a 9 por turno; dominio comprado: `espaciofuncional25.com` · **publicado el 14/10/2026 en https://espaciofuncional25.com** (Hostinger)

Sitio de una sola página de Espacio Funcional 25, el entrenamiento funcional del Prof. Nicolás Guido Valle en el Cuartel de Bomberos de 25 de Mayo. Su trabajo: que alguien de 25 de Mayo que llega desde Instagram o WhatsApp entienda en segundos qué es, dónde queda, cuánto sale y en qué horarios hay clase, y que reserve la clase de prueba gratis por WhatsApp.

## Qué hay

- `index.html`: la página. Encabezado, portada, El enfoque, Cómo es la clase, Turnos y cuota, El profe, clase de prueba y Dónde estamos, pie y botón fijo de WhatsApp en el celular.
- `css/style.css` y `js/main.js`: sin dependencias. El CSS está escrito desde el celular (360–390 px) y se amplía en 600 y 1024 px.
- `assets/img/`: fotogramas reales de los reels de Instagram, recortados y con corrección de color (`docs/imagenes.md`). **Ninguna imagen es generada.** `og.jpg` es una composición con el logo real, texto y una foto real.
- `assets/fonts/`: Barlow y Barlow Semi Condensed (woff2 de @fontsource 5.3.0, licencia OFL).
- `docs/` (no se publica: `.htaccess` devuelve 404 y `robots.txt` la excluye):
  - `diseno.md` y `diseno/`: el diseño aprobado por Pablo y su maqueta.
  - `plan.md`: el plan v0. El diseño y la lista de decisiones de ese plan quedaron viejos; lo vigente es `diseno.md` y este README.
  - `imagenes.md`, `relevamiento/` y `fotos-instagram/INDICE.md`. Las fotos originales de Instagram quedan solo en local, fuera de git, porque hay alumnos y menores.
  - `herramientas/`: `capturas.py`, `contraste.py` e `imagenes.py`.
  - `auditoria/`: las cinco auditorías del 10/10/2026 (celular, compu, copy, datos, accesibilidad y rendimiento) y `correcciones.md`, con lo que se hizo con cada hallazgo.
- `.github/workflows/pages.yml`: vista previa en GitHub Pages, sin `docs/` ni este README. El sitio definitivo va en Hostinger.

## Cómo se publica

El sitio vive en el plan Cloud Startup del Hostinger de Pablo, como sitio PHP/HTML de `espaciofuncional25.com` (dominio y DNS en el mismo Hostinger). hPanel → el sitio → Avanzado → Git está conectado con este repo (rama `main`, a `public_html`) y tiene la **implementación automática** activada: cada push a `main` se publica solo, igual que la vista previa. Si algo no se actualiza, ahí está el botón "Redeploy".

Se publica el repo entero, incluidos `docs/` y este README: el `.htaccess` los devuelve como 404 (verificado el 14/10/2026: `docs/`, `README.md` y `.github/` dan 404, `.git/` da 403, http y www redirigen con 301 a https sin www).

## Cómo verlo

Vista previa: https://pablospata.github.io/espacio-funcional-25-website/ (se actualiza sola con cada push a `main`; no publica `docs/` ni este README). La imagen para compartir apunta al dominio definitivo, así que en la vista previa no aparece al pasar el link por WhatsApp.

En local:

```sh
python -m http.server 8802 --bind 127.0.0.1
```

Abrir http://127.0.0.1:8802/.

## Cómo cambiar la cuota

El precio está en **un solo lugar**: `index.html`, bloque "Turnos y cuota" (tiene el comentario "los precios están acá").

- `#precio-cuota` ($35.000), `#precio-complemento` ($10.000) y `#precio-solo-plan` ($25.000).
- `#precio-vigencia`: el texto que se ve ("octubre de 2026") y `data-desde`, el primer día de ese mes en formato `AAAA-MM-DD` (hoy `2026-10-01`).

Lo demás se copia solo:

- La cuota de los datos de la portada la copia el script corto del final de `index.html`, sin esperar a `main.js`. Sin JavaScript, la portada dice "Cuota · Ver · más abajo" y el link lleva a la cuota.
- El JSON-LD (`ExerciseGym`) lo completa `main.js`: `priceRange` y las cuatro ofertas de `makesOffer`, con `validFrom` tomado de `data-desde`. **El JSON-LD que está escrito en el HTML no tiene precio**, a propósito, para no tener el precio en dos lugares. Google ejecuta el JS y toma la versión completa. Un validador que no ejecuta JS lo va a ver sin precio. Cuando se publique, revisarlo con la Prueba de resultados enriquecidos de Google, que sí ejecuta el JS.

## Dominio

`espaciofuncional25.com`, comprado por Pablo el 13/10/2026. Aparece en 9 lugares:

- `index.html`: `canonical` (línea 10), `og:url` (16), `og:image` (17) y, en el JSON-LD, `@id`, `url`, `image` y `logo` (31 y 34–36).
- `robots.txt` (línea `Sitemap`) y `sitemap.xml` (`loc`).

El `.htaccess` no escribe el dominio: redirige a https y sin www con el host que llegue.

## Cupo

**Máximo 9 por turno** (Nicolás, 13/10/2026; antes decía 7). Está en la descripción, `og:description` y el JSON-LD, en la bajada de la portada, la banda negra, el bloque del número grande (con 9 figuritas), la nota de los turnos y el pie.

## Decisiones tomadas sin Nicolás

Nicolás revisó el texto el 13/10/2026 y dio el OK a todo. Lo único que cambió fue el cupo (de 7 a 9).

1. **Titular: «Entrená acompañado.»**, elegido por Pablo. Reemplazó a «Que quieras volver.», que no se entendía sin el contexto de la idea de Nicolás.
2. **La cita de El enfoque está reconstruida** a partir de los subtítulos del reel del 28/07/2026, que puede tener palabras de menos, y va firmada "Nicolás Valle · Profe de Espacio Funcional 25". Dice: «Lo más fácil para un entrenador: Agotarte hasta dejarte sin aire. Lo difícil, y lo que de verdad importa: Que quieras volver cada semana, sin lastimarte entrenando.»
3. **"Valores de octubre de 2026."** El mes del precio es un supuesto. En el JSON-LD figura como `validFrom: 2026-10-01`.
4. **"¿Preferís llamar? 2345-402547"**, con `tel:+5492345402547`. No se sabe si ese número atiende llamadas o solo WhatsApp.
5. **"Y otra vuelta"** al final del circuito. Ninguna fuente dice que en la clase se repita el circuito. Si no se repite, el rótulo pasa a ser «Y la estación siguiente».
6. **El circuito es un ejemplo** ("Una vuelta del circuito, por ejemplo"). Tiene las cinco estaciones del PDF en el mismo orden y el material que se ve en los reels: sentadillas con mancuernas, press con mancuernas, remo con TRX, core con la pelota medicinal, y saltos, cubierta y maza.
7. **La trayectoria completa del CV**, que pidió Pablo: "Equipo de conducción del CEF Nº 198 · Secretario" (2025 – hoy), la docencia "en todos los niveles de la educación obligatoria, y en el CEF" y la lista de cursos (el seminario de obesidad y el de RCP, a la vista en Formación). Quedan afuera los dos años de Medicina y los cursos de gestión educativa. La licenciatura va con 2023, que confirmó Pablo (el diploma es de marzo de 2024).
8. **La bio** termina con «En el espacio planifica los entrenamientos, adapta cada ejercicio a tu nivel y corrige la técnica de cada uno.». Es una síntesis del PDF y del reel, no una frase textual suya.
9. **El mensaje central es que te cuida**, igual que en el plan del Instagram: en El enfoque van tres promesas («Sabe lo que hace», «Te adapta», «Te cuida: no entrenás solo, te mira, te corrige la técnica y se fija que estés bien; la salud va primero»), la portada dice «con cada ejercicio adaptado a tu nivel» y el bloque del 7 dice «así el profe te ve a vos». Sale de lo que Pablo cuenta que remarca Nicolás y del PDF («esfuerzo adaptado», «progresión gradual», «técnica correcta»). En Formación quedan a la vista el seminario de ejercicio para personas con obesidad y el curso de RCP.
10. **La bolita del circuito da una sola vuelta de 5 segundos** cada vez que la pista entra en pantalla, y con «reducir movimiento» no se mueve (WCAG 2.2.2; antes daba vueltas sin fin, hallazgo A11Y-9).
11. **"Pablo Añon" y "Emiliano Gonzalez"** van sin tilde, como en el CV.
12. **El WhatsApp va con el 9** (`wa.me/5492345402547`), y el mensaje prellenado es «Hola, Nicolás. Vi la página de Espacio Funcional 25 y quiero reservar la clase de prueba gratis. ¿Qué turno tenés libre?». Así se sabe de dónde vino cada uno. Falta probarlo en un celular.
13. **Hay fotos de alumnos que se reconocen** en la portada, en Cómo es la clase y en Dónde estamos. Se usan con la autorización de Nicolás para las fotos de Instagram.
14. **No hay mapa embebido**: solo el botón "Cómo llegar", que abre la ficha del cuartel en Google Maps. Cuando Nicolás tenga su Perfil de Empresa, hay que cambiar `hasMap` en el JSON-LD.
15. **No se dice cuántos lugares quedan por turno**, porque habría que actualizarlo cada vez.

## Decisiones de Pablo (de las auditorías)

Tres cosas medidas en las auditorías que tocan algo que Pablo aprobó o pidió. Por eso no se cambiaron. El detalle está en `docs/auditoria/correcciones.md`.

- **Precargar Barlow 400 y 600** (A11Y-4). En 4G lento, el primer pantallazo salta 39 px cuando llegan esas fuentes (CLS 0,086–0,090). Con la precarga, el salto queda en 0 y el LCP baja medio segundo. El brief pide precargar solo la fuente del titular.
- **Logos con pérdida** (A11Y-12). Calidad 90 y alfa al 100 ahorran unos 8,5 KB del primer pantallazo. `docs/imagenes.md` eligió "sin pérdida" a propósito.
- **Fotos más nítidas en pantallas de alta densidad** (PC-12). Hacen falta los videos originales de los reels o fotos de 1080 px o más: pedírselos a Nicolás.

## Qué falta

- Probar en un celular que `wa.me/5492345402547` abra el chat bien.
- Dar de alta el Perfil de Empresa en Google Maps y poner el link del sitio en la bio de Instagram.
