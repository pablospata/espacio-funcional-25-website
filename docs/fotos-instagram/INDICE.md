# Fotos de Instagram: índice y clasificación

Relevado el 09/10/2026 desde [@espaciofuncional25](https://www.instagram.com/espaciofuncional25/). Hay autorización de Nicolás para usar las fotos. Esta carpeta está en `docs/`, que no se publica.

## Resumen

- **64 publicaciones**, todas bajadas: 81 imágenes (portadas de reels incluidas) y 17 fotogramas sacados de los reels de 2026.
- **Clasificación de las 81:** 32 clase, 6 espacio, 6 Nicolás, 27 flyer, 10 otro.
- **El problema:** casi todo lo de 2018 a 2022 es de otra etapa del espacio: otros profes y otros lugares (Laguna Las Mulitas, un gimnasio de musculación, el Club Atlético Sportivo). **Del Cuartel de Bomberos solo hay material de 2026**, y las fotos de 2026 tienen texto quemado encima (son placas o portadas de reels). Las imágenes limpias del lugar actual salen de los **fotogramas de los reels**, a 716×1274 px como máximo.
- **Para el sitio conviene pedirle a Nicolás** los videos o fotos originales del celular (sin texto y en más resolución) y el permiso de los alumnos que se reconocen.

## Perfil (09/10/2026)

- **Nombre de usuario:** espaciofuncional25. **Categoría:** Entrenador. Subtítulo: "Centro de entrenamiento".
- **Números:** 64 publicaciones, 1.707 seguidores, 633 seguidos.
- **Bio:**
  > Prof. Nicolás Valle | Lic. Alto Rendimiento
  > Entrenamiento funcional
  > Grupos semi-personalizados
  > Fuerza y resistencia
  > 📩 Reserva tu clase de prueba
- **Ubicación en el perfil:** Cuartel de Bomberos Voluntarios, 25 De Mayo, Buenos Aires, Argentina 6660.
- **Links de la bio (3):**
  - "WhatsApp": `wa.link/ea2jy3` → `api.whatsapp.com/send?phone=542345402547` con el texto "Escribime y....¡Empecemos a entrenar! 🏃🏻🏋🏻". Usa el número **sin el 9** (ver WhatsApp, más abajo).
  - "Formación profesional": un archivo de Google Drive.
  - "Información y Aranceles": un documento de Google Docs.
- **Historias destacadas (6):** TESTIMONIOS, HORARIOS, TRAYECTORIA, ALUMNOS, INFO 2026, RUTINAS. No las abrí: verlas deja registro de visita y, además, no se pueden bajar sin la sesión. "HORARIOS" e "INFO 2026" pueden tener horarios viejos (ver Textos de las placas).
- **Fijados:** tres reels (07/03, 05/10 y 23/03/2026).

## Cómo se bajaron

- **Datos de las publicaciones** (código, fecha, tipo, carrusel, leyendas): de la consulta que hace la propia página del perfil, leída en Chrome con la sesión del usuario.
- **Imágenes:** la extensión de Chrome bloquea las URL firmadas de Instagram, así que las bajé con `curl` desde la página pública de cada publicación, abierta sin sesión en Chrome headless. Es la misma imagen a la máxima resolución que ofrece Instagram (por ejemplo, 1440×1800 en el carrusel de 2026).
- **Formato:** Instagram sirve las fotos de 2021 a 2026 en **WebP** y las portadas de reels y las fotos viejas en JPG. Dejé la extensión real (`.webp` o `.jpg`) en vez de renombrar todo a `.jpg`. Son los originales tal como los da Instagram: no están procesados.
- **Nombre:** `AAAA-MM-DD_<código>_<n>`, con la fecha de publicación en hora argentina. La publicación es `https://www.instagram.com/p/<código>/`.
- **Fotogramas** (`fotogramas-reels/`): los saqué con ffmpeg de los videos de los reels de 2026, a 716×1274 (lo máximo que da Instagram sin sesión). El sufijo `_fNNNs` es el segundo del reel. No son originales: son cuadros del video, sin retocar.
- **Verificación:** las 81 imágenes y los 17 fotogramas abren bien con Pillow. Las dimensiones están en las tablas.
- **Hojas de contacto:** `hoja-contacto-1.jpg` a `-3.jpg` (las 81) y `fotogramas-reels/hoja-contacto-1.jpg`.

## Historia de la cuenta (lo que muestran las publicaciones)

- La marca existe desde el 29/10/2018 (placa "Cumplimos 3 años" del 29/10/2021). La crearon dos profes de Educación Física que no son Nicolás.
- De 2018 a 2021 entrenaban al aire libre y en el club de pesca de Laguna Las Mulitas. En 2021 y 2022 daban musculación en un gimnasio, y desde marzo de 2022 funcional en el Club Atlético Sportivo (calle 9).
- El 27/07/2022 se presenta a Nicolás como profe nuevo de "fuerza y acondicionamiento", desde el 1/8/2022.
- No hay publicaciones entre el 30/12/2022 y el 05/02/2026. Desde febrero de 2026, todo es en el Cuartel de Bomberos y la cuenta habla con la voz de Nicolás.
- Para el sitio: **no usar fotos de antes de 2026 como "el lugar"**, porque muestran otros espacios. Si se quiere contar la historia, es una pregunta para Nicolás.

## Las 81 imágenes

Clases: clase (gente entrenando), espacio (lugar o equipamiento), nicolas (el profe), flyer (placa con texto), otro. En "Caras" se indica si se reconoce a alumnos.

| Archivo | Publicación | Clase | Descripción | Caras | Calidad | Tamaño y orientación | Uso en el sitio |
|---|---|---|---|---|---|---|---|
| 2018-10-19_BpHsQ9mFbf-_1.jpg | foto | otro | Logo anterior, en negro, sobre un campo verde | no | media | 1056×1056 cuadrada | no (logo viejo) |
| 2019-01-04_BsN-hG-AiF5_1.jpg | foto | clase | Grupo de unas 11 personas posando de noche al aire libre (etapa anterior) | sí | baja: noche, ruido | 1080×1080 cuadrada | no |
| 2020-08-10_CDueNIwArDC_1.jpg | video (portada) | clase | Arquero entrenando al aire libre, en blanco y negro | sí | baja | 480×600 vertical | no |
| 2020-09-14_CFIxC4jglLP_1.jpg | video (portada) | clase | Persona haciendo flexiones en un salón con ventanales; marca de agua de una app | no | baja | 640×640 cuadrada | no |
| 2021-01-08_CJykIKULYOM_1.jpg | carrusel | otro | "Antes" de un alumno, con texto encima (testimonio) | sí | media | 1272×1590 vertical | no (testimonio) |
| 2021-01-08_CJykIKULYOM_2.jpg | carrusel | otro | Captura de la historia de un alumno en un gimnasio | sí | media | 1206×1507 vertical | no |
| 2021-05-27_CPY8vSmrBHl_1.jpg | foto | flyer | Placa "Clases por WhatsApp", de la pandemia | no | — | 1080×1080 cuadrada | no |
| 2021-05-28_CPa4_qNABEE_1.jpg | reel (portada) | clase | Rutina en casa: persona en el pasto, con franjas negras | no | baja | 720×1600 vertical | no |
| 2021-05-30_CPgu-8ULzwj_1.jpg | foto | flyer | Placa "Calentamiento y elongación" | no | — | 1080×1080 cuadrada | no |
| 2021-05-31_CPimXzugw0n_1.jpg | reel (portada) | clase | Rutina en casa al aire libre, con franjas negras | no | baja | 720×1600 vertical | no |
| 2021-06-17_CQPUV5OLFW2_1.jpg | foto | flyer | Ilustración de auriculares con mancuernas | no | — | 1080×1080 cuadrada | no |
| 2021-06-25_CQj1r4tAiQv_1.jpg | reel (portada) | clase | Persona con barbijo junto a unas vallas, en un salón con ventanales | no | baja | 720×1600 vertical | no |
| 2021-07-20_CRjWEisr5Se_1.jpg | foto | otro | Los dos profes fundadores de la etapa anterior (no es Nicolás) | — | buena | 960×1200 vertical | no |
| 2021-07-22_CRpb3D8AqOz_1.jpg | reel (portada) | otro | Cuadro negro vacío | no | — | 720×1280 vertical | no |
| 2021-08-25_CTBI-NhLq9S_1.jpg | foto | flyer | Placa "Sorteo" | no | — | 1080×1080 cuadrada | no |
| 2021-09-17_CT7RTMOL_4Y_1.jpg | foto | flyer | Placa "Feliz día del profesor" | no | — | 1080×1080 cuadrada | no |
| 2021-09-20_CUD_uGOgRol_1.jpg | reel (portada) | clase | Dos personas con una cubierta y un minitramp, en un salón con ventanales | parcial | baja | 720×1280 vertical | no |
| 2021-09-29_CUaJdY-Lbkz_1.webp | foto | clase | Alumno con barbijo en una máquina de un gimnasio de musculación | parcial | media | 1080×1350 vertical | no (otro lugar) |
| 2021-10-06_CUsJipELihU_1.webp | carrusel | espacio | Sala de musculación vacía (otro gimnasio, no es el lugar actual) | no | media | 868×1085 vertical | no |
| 2021-10-06_CUsJipELihU_2.webp | carrusel | espacio | Ídem: máquinas de musculación | no | media | 868×1085 vertical | no |
| 2021-10-06_CUsJipELihU_3.webp | carrusel | espacio | Ídem | no | media | 868×1085 vertical | no |
| 2021-10-06_CUsJipELihU_4.webp | carrusel | espacio | Ídem | no | media | 868×1085 vertical | no |
| 2021-10-29_CVnfBtbrHMJ_1.jpg | foto | flyer | Placa "29 de octubre: hoy cumplimos 3 años" | no | — | 1080×1080 cuadrada | no (dato: arranque el 29/10/2018) |
| 2021-11-05_CV6ZDQKrQTE_1.jpg | foto | otro | Certificado de un curso de otro profe, con su nombre | — | media | 828×625 horizontal | no (datos personales) |
| 2021-11-28_CW1eDZ3rwdi_1.jpg | foto | flyer | Placa "Mala postura" | no | — | 1080×1080 cuadrada | no |
| 2021-12-04_CXEA4fBLaFg_1.jpg | carrusel | otro | Antes y después de un alumno en ropa interior, con captura de chat | sí | media | 1080×1080 cuadrada | no |
| 2021-12-04_CXEA4fBLaFg_2.jpg | carrusel | otro | Ídem, otra composición | sí | media | 1080×1080 cuadrada | no |
| 2021-12-10_CXUeGgdg_K2_1.jpg | reel (portada) | flyer | Placa negra "Funcional training" | no | — | 480×854 vertical | no |
| 2021-12-22_CXygQ4wL08O_1.jpg | foto | espacio | Sala de musculación vacía, otro lugar | no | media | 1080×1350 vertical | no |
| 2021-12-29_CYFa0Z7L3xk_1.jpg | foto | otro | Detalle de unos pies en una máquina | no | media | 899×1124 vertical | no |
| 2022-02-25_CaavsEsLKrU_1.webp | foto | flyer | Placa "Mismo equipo, nuevo lugar" con mancuernas naranjas | no | — | 1080×1080 cuadrada | no |
| 2022-03-01_CalFh1uLx1v_1.webp | foto | flyer | Placa "Nuevo espacio: Club Atlético Sportivo" | no | — | 1080×1080 cuadrada | no |
| 2022-03-03_CaqNcTDrZDs_1.webp | carrusel | flyer | Placa de horarios de funcional 2022 | no | — | 1080×1080 cuadrada | no |
| 2022-03-03_CaqNcTDrZDs_2.webp | carrusel | flyer | Placa de horarios de musculación 2022 | no | — | 1080×1080 cuadrada | no |
| 2022-03-14_CbFqIMtLYmK_1.webp | foto | clase | Clase de la mañana en el salón del club, con contraluz | chicas | media | 1080×810 horizontal | no (otro lugar) |
| 2022-03-30_CbvvZVTLo7N_1.webp | foto | clase | Alumna en una máquina de musculación | sí | media | 1080×1350 vertical | no |
| 2022-04-01_Cb06MBYLpWn_1.webp | carrusel | clase | Alumna en una máquina de musculación | sí | media | 1080×1350 vertical | no |
| 2022-04-01_Cb06MBYLpWn_2.webp | carrusel | clase | Alumna con barra en una máquina | sí | media | 1080×1350 vertical | no |
| 2022-04-20_Cck7ouXr0IF_1.webp | foto | clase | Clase de las 8 en el club, con sol de costado | chicas | media | 1080×808 horizontal | no |
| 2022-05-03_CdHUQSTAZ7y_1.jpg | reel (portada) | clase | Persona de espaldas con el texto "Funcional training" | no | baja | 480×854 vertical | no |
| 2022-06-22_CfHJnKlLfLG_1.webp | foto | clase | Alumna en TRX en el club | sí | buena | 1080×1350 vertical | no (otro lugar) |
| 2022-06-30_Cfby4GsLBKX_1.webp | carrusel | clase | Preparación física de un equipo de básquet: estaciones con kettlebells, cajón y barra | sí | buena | 768×960 vertical | solo como referencia de estaciones (otro lugar) |
| 2022-06-30_Cfby4GsLBKX_2.webp | carrusel | clase | Ídem: estocada con kettlebell | sí | buena | 768×960 vertical | ídem |
| 2022-06-30_Cfby4GsLBKX_3.webp | carrusel | clase | Ídem: grupo en estaciones | sí | buena | 768×960 vertical | ídem |
| 2022-07-08_CfwZlFDL0dv_1.webp | foto | clase | Clase en el club con cajones y conos | chicas | media | 1080×810 horizontal | no |
| 2022-07-13_Cf9P5B_rnZZ_1.webp | foto | flyer | Placa de sorteo del día del amigo | no | — | 1080×1080 cuadrada | no |
| 2022-07-22_CgVSpJhraAx_1.webp | foto | flyer | Placa "Nueva disciplina: fuerza y acondicionamiento" | no | — | 1080×1080 cuadrada | no |
| 2022-07-27_CgiLZd_rLr2_1.webp | foto | nicolas (alta: la leyenda le da la bienvenida a "Nico" y lo etiqueta) | Retrato de Nicolás sonriendo, de brazos cruzados, con fondo de ladrillo; abajo, franja naranja con el logo viejo y su usuario | — | buena | 1080×1080 cuadrada | el profe (alternativa, es de 2022): recortar por encima de la franja, unos 1080×900 |
| 2022-08-11_ChIxD5eLnzv_1.webp | foto | flyer | Placa de horarios 2022 | no | — | 1080×1080 cuadrada | no |
| 2022-08-18_ChZ8jljAFJW_1.jpg | reel (portada) | espacio | Pared con el logo viejo y un TRX, en el club | no | baja | 480×854 vertical | no |
| 2022-08-22_ChlFLw9rTGz_1.webp | foto | clase | Clase en el club con colchonetas | chicas | media | 1080×810 horizontal | no |
| 2022-08-25_ChswrG2LjZ7_1.jpg | carrusel | clase | Foto grupal de un equipo juvenil de hockey con los profes | sí (menores) | buena | 1440×1080 horizontal | no (menores) |
| 2022-08-25_ChswrG2LjZ7_2.jpg | carrusel | clase | Una jugadora haciendo un test | sí | media | 771×581 horizontal | no |
| 2022-08-25_ChswrG2LjZ7_3.jpg | carrusel (video) | nicolas (media-alta, por la cara) | Nicolás sentado en un banco con el celular, durante los tests | parcial | baja | 480×360 horizontal | no |
| 2022-09-01_Ch-xq9FrVcK_1.webp | foto | clase | Clase en el club: ejercicios en el piso y con cajón | parcial | media | 1080×1350 vertical | no |
| 2022-09-19_CisRrB-rzpZ_1.webp | foto | flyer | Placa "Centro de entrenamiento: funcional, fuerza y adaptación" | no | — | 1080×1350 vertical | no |
| 2022-09-22_Ci02vVJguXh_1.jpg | reel (portada) | clase | Clase en el club con escalera de coordinación | parcial | baja | 480×854 vertical | no |
| 2022-10-27_CkOL012L4Q0_1.webp | foto | flyer | Placa "Descuentos para socios" del club | no | — | 1080×1350 vertical | no |
| 2022-11-11_Ck0063wLzRW_1.webp | foto | clase | Clase en el club con cubierta, cajón y TRX | parcial | media | 1080×1318 vertical | no |
| 2022-12-02_Clq1tRgrUgW_1.webp | foto | flyer | Placa "Nuevos horarios" del verano 2022 | no | — | 1080×1350 vertical | no |
| 2022-12-09_Cl84vg9rPrr_1.webp | foto | clase | Alumna en TRX, con una franja naranja con logo y usuario | sí | buena | 1080×1350 vertical | no (otro lugar) |
| 2022-12-14_CmJ1J9xA9iH_1.jpg | reel (portada) | clase | Alumna en TRX con una franja naranja | sí | baja | 480×854 vertical | no |
| 2022-12-16_CmO6n5tLhnt_1.webp | foto | otro | Antes y después del cuerpo de una alumna (testimonio) | sí | media | 720×815 vertical | no |
| 2022-12-30_CmzALxeBpoF_1.jpg | reel (portada) | clase | Alumna haciendo sentadilla sobre una cubierta, con franjas negras | parcial | baja | 480×854 vertical | no |
| 2026-02-05_DUYdWLijiB-_1.webp | carrusel | flyer | Placa "Espacio Funcional 25 – 2026" con el logo, sobre una foto desenfocada del salón | no | buena como placa | 1440×1800 vertical | no |
| 2026-02-05_DUYdWLijiB-_2.webp | carrusel | flyer | "¿Por qué entrenar funcional y no 'solo hacer ejercicio'?"; de fondo, el salón con el letrero de Bomberos Voluntarios, desenfocado | parcial | buena como placa | 1440×1800 vertical | no |
| 2026-02-05_DUYdWLijiB-_3.webp | carrusel | flyer | Placa sobre la fuerza (texto abajo) | no | — | 1440×1800 vertical | no |
| 2026-02-05_DUYdWLijiB-_4.webp | carrusel | flyer | Placa sobre la resistencia | no | — | 1440×1800 vertical | no |
| 2026-02-05_DUYdWLijiB-_5.webp | carrusel | flyer | Placa sobre la coordinación | no | — | 1440×1800 vertical | no |
| 2026-02-05_DUYdWLijiB-_6.webp | carrusel | flyer | Placa sobre el estímulo y el tiempo | no | — | 1440×1800 vertical | no |
| 2026-02-05_DUYdWLijiB-_7.webp | carrusel | flyer | Placa de horarios: martes y viernes de 6:30 a 7:30 (horario viejo) | no | — | 1440×1800 vertical | no |
| 2026-02-06_DUa7Xy0DthX_1.jpg | reel (portada) | flyer | Placa "Espacio Funcional 25 – 2026 – 25 de Mayo" | no | — | 640×1138 vertical | no |
| 2026-02-12_DUq1IOwkvz9_1.jpg | reel (portada) | clase | En blanco y negro: alumna lanzando una pelota medicinal, con pesas y colchoneta; salpicaduras y degradé naranja de edición | parcial (cara movida) | media: blanco y negro, movida | 1080×1920 vertical | fondo de sección con tratamiento; recorte 4:5 desde arriba (y 0–1350) |
| 2026-02-18_DU6d9Qdjrnu_1.jpg | reel (portada) | clase | Alumna en estocada con mancuernas, con el texto "Es hacer algo por vos" encima | sí | media | 1080×1920 vertical | no (texto quemado) |
| 2026-03-07_DVmf_99jhOi_1.jpg | reel (portada) | clase | Alumna con una pelota sobre la cabeza y el texto "Resumen de la semana" | sí | media-baja | 540×960 vertical | no |
| 2026-03-23_DWPee4shkru_1.jpg | reel (portada) | nicolas (alta) | Nicolás en primer plano en el salón, con el logo grande y texto | — | baja | 540×960 vertical | no |
| 2026-04-02_DWpl7tBNP0R_1.jpg | reel (portada) | nicolas (alta) | Miniatura diseñada: Nicolás y un grupo de alumnos, con el texto "Lo más importante para una clase de funcional" | sí | media | 540×960 vertical | no |
| 2026-04-29_DXvBvnKDg29_1.jpg | reel (portada) | clase | Alumna con pelota medicinal en el salón y el texto "¿Buscando tu mejor versión?" | parcial | media-baja | 540×960 vertical | no |
| 2026-07-28_DbUtD7_j4uj_1.jpg | reel (portada) | nicolas (alta: en el reel dice "Soy Nicolás Valle") | Nicolás con el buzo de la marca y una pelota naranja, con el texto "Entrenamiento funcional de alta intensidad" | — | buena | 1088×1936 vertical | no por el texto; el mismo plano, limpio, está en los fotogramas (f024s) |
| 2026-07-30_Dbbmv_gCadM_1.jpg | reel (portada) | nicolas (alta) | Miniatura diseñada con Nicolás y un montaje, con el texto "El verdadero rol del entrenamiento" | — | media | 1076×1920 vertical | no |
| 2026-10-05_DeIqw8-kez9_1.jpg | reel (portada) | flyer | Placa "¿Pensando en empezar entrenamiento funcional?" | no | — | 1080×1920 vertical | no |

## Fotogramas de los reels de 2026 (`fotogramas-reels/`)

Todos son del Cuartel de Bomberos, de 716×1274 y verticales. Casi todos tienen el logo chico arriba a la izquierda, y algunos tienen subtítulos o texto abajo. El recorte sugerido (en px del fotograma) deja eso afuera.

| Archivo | Clase | Descripción | Caras | Calidad | Uso y recorte |
|---|---|---|---|---|---|
| 2026-02-06_DUa7Xy0DthX_f000s.jpg | clase | Hombre de remera azul (probablemente Nicolás, confianza media) golpeando una cubierta con una maza | movida | media | alternativa; y 150–1000 |
| 2026-02-06_DUa7Xy0DthX_f020s.jpg | nicolas (media: no hay leyenda, pero coincide con su cara en otros reels) | El mismo hombre de remera azul con desplazamientos entre conos; sin texto ni logo | — | media | el profe en acción; 4:5, y 50–950 |
| 2026-02-06_DUa7Xy0DthX_f024s.jpg | espacio y clase | Alumna en TRX debajo del letrero "BOMBEROS VOLUNTARIOS"; salón amplio, sin texto ni logo | parcial (de perfil) | media-buena | dónde estamos; 4:5, y 150–1050 |
| 2026-02-06_DUa7Xy0DthX_f040s.jpg | espacio | Skipping delante de la camioneta roja de los bomberos (probablemente Nicolás, cara movida) | no | media | dónde estamos; y 100–950 |
| 2026-03-23_DWPee4shkru_f000s.jpg | nicolas (alta) | Nicolás grabándose en el salón, con el logo grande y subtítulo | — | baja | no |
| 2026-04-02_DWpl7tBNP0R_f002s.jpg | clase | Alumno en TRX y alumna con una pesa; logo chico y degradé abajo | parcial | media | alternativa; y 200–1000 |
| 2026-04-02_DWpl7tBNP0R_f004s.jpg | clase | **Circuito:** cuatro personas en estaciones distintas (estocada con mancuerna, pelotas en el piso, TRX), con la camioneta de Bomberos al fondo | parcial (de perfil o de espalda) | media-buena | cómo es la clase; y 200–1000 (716×800) |
| 2026-04-02_DWpl7tBNP0R_f006s.jpg | nicolas (alta) | Primer plano de Nicolás con remera azul, hablando a cámara; subtítulo abajo | — | media | el profe (alternativa); x 160–716, y 0–700 |
| 2026-04-29_DXvBvnKDg29_f014s.jpg | espacio y clase | Alumno saltando sobre una cubierta debajo de las letras "VOLUNTARIOS 25 DE MAYO"; texto abajo | parcial | media | dónde estamos; y 200–880 |
| 2026-04-29_DXvBvnKDg29_f016s.jpg | clase y espacio | Alumna en TRX, otra persona detrás, autobomba y camioneta de Bomberos al fondo; texto abajo | sí | media-buena | cómo es la clase o dónde estamos; y 200–890 |
| 2026-07-28_DbUtD7_j4uj_f008s.jpg | clase y espacio | Salón con "VOLUNTARIOS 25 DE MAYO": una alumna en la cubierta y otra con mancuernas (dos estaciones a la vez); subtítulo abajo | parcial | media-buena | estaciones o dónde estamos; y 170–900 |
| 2026-07-28_DbUtD7_j4uj_f018s.jpg | nicolas (alta) y clase | Nicolás mostrándole un movimiento a una alumna en el garage del cuartel, con autobombas detrás; subtítulo abajo | sí (la alumna) | media-buena | portada en celular o supervisión; y 180–940 |
| 2026-07-28_DbUtD7_j4uj_f024s.jpg | nicolas (alta) | Nicolás con el buzo negro de la marca y la pelota naranja, sin subtítulo | — | buena para su tamaño | **el profe**; 4:5, y 200–1095 |
| 2026-07-28_DbUtD7_j4uj_f026s.jpg | clase | Pasillo largo del cuartel: una alumna en TRX al fondo y otra con una bolsa al hombro | sí | media-buena | cómo es la clase; y 170–800 |
| 2026-07-28_DbUtD7_j4uj_f034s.jpg | clase | Alumno golpeando una cubierta con una maza, junto a la escalera; subtítulo | parcial | media | alternativa; y 150–850 |
| 2026-07-28_DbUtD7_j4uj_f042s.jpg | clase y espacio | Alumna en TRX con la camioneta de Bomberos al fondo; subtítulo | sí | media-buena | alternativa a la f016s de DXvBvnKDg29; y 130–940 |
| 2026-07-30_Dbbmv_gCadM_f016s.jpg | nicolas (alta) | Nicolás de cuerpo entero hablando, con el buzo de la marca y un rodillo naranja; subtítulo abajo | — | buena | el profe (alternativa); y 0–1090 |

## Textos de las placas y reels de 2026 (la voz de Nicolás)

Sirven para el copy y para controlar datos, no como imágenes.

- **Reel del 28/07/2026 (DbUtD7_j4uj), reconstruido a partir de los subtítulos** (puede faltar alguna palabra):
  > Sentís que querés empezar a moverte por salud o cambiar tu cuerpo, pero el gimnasio tradicional te aburre o te da miedo no saber por dónde empezar. No te preocupes. Lo más fácil para un entrenador es simplemente agotarte hasta dejarte sin aire. Lo difícil y lo que de verdad importa es lograr que quieras volver cada semana sin lastimarte entrenando. Soy Nicolás Valle, profesor de Educación Física y licenciado en alto rendimiento, y en Espacio Funcional veinticinco trabajamos con intervalos de alta intensidad en grupos reducidos. Esto nos permite acompañarte de cerca, corregir tu técnica y adaptar cada ejercicio a tu nivel, tengas o no experiencia previa. Combinamos fuerza y cardio con movilidad en estaciones pensadas para que entrenes de forma eficiente, ganes salud y veas resultados reales sin terminar destruido. No hace falta que estés en forma para arrancar. Escribinos por privado o WhatsApp y reservá tu clase de prueba para venir a conocer una forma diferente de entrenar.

  Es la idea central del brief ("Que quieras volver"), dicha por él. Al final, la placa: "Lunes y jueves 18 y 19 hs / Martes y viernes 7 hs / Reservá tu clase de prueba". **Coincide con `TAREAS.md`.**
- **Reel del 05/10/2026 (DeIqw8-kez9, fijado):** "No necesitás experiencia previa. Los ejercicios se adaptan al nivel de cada persona." / "Trabajamos fuerza y resistencia combinando ejercicios de diferentes patrones de movimiento." / "Las clases son en grupos reducidos. Esto permite corregir técnica y adaptar ejercicios." / "El objetivo no es solo cansarse. Buscamos entrenamientos exigentes pero sostenibles en el tiempo." / "Podés venir a una clase de prueba para conocer cómo trabajamos." / "Si querés más información escribime por MD o WhatsApp."
- **Reel del 02/04/2026 (DWpl7tBNP0R):** a "¿qué es lo más importante para dar una clase?" responde "la conexión con los alumnos, que ellos te respeten, que te quieran" (en tono de humor).
- **Reel del 30/07/2026 (Dbbmv_gCadM):** explica estímulo, descanso y supercompensación: "Entrenar fuerte es la mitad de la ecuación. La otra es darle el tiempo a tu biología…"
- **Carrusel del 05/02/2026:** "¿Por qué entrenar funcional y no 'solo hacer ejercicio'?" / "Mejora la fuerza real, la que usás todos los días: empujar, tirar, levantar, estabilizar." / "Aumenta la resistencia combinando fuerza y cardio en el mismo entrenamiento." / "Mejora la coordinación y el control corporal. Menos lesiones, más eficiencia al moverte." / "Más estímulo en menos tiempo. Entrenamientos intensos, dinámicos y bien planificados."
- **Otras frases de 2026:** "Entrenamiento con criterio", "Grupos chicos", "Primera clase de prueba, cupos limitados", "Fuerza, resistencia y comunidad", "Entrenamiento real para la vida diaria", "¡Te esperamos! Entrenamientos en el Cuartel de Bomberos".
- **Cómo fueron cambiando los horarios en 2026** (vale `TAREAS.md`):
  - feb.: martes y viernes de 6:30 a 7:30;
  - 18/02: se suma el turno tarde, lunes y jueves a las 18;
  - abr.: lunes y jueves 18, martes y viernes 6:30;
  - 29/04: martes y viernes a las 7;
  - jul.: lunes y jueves 18 y 19, martes y viernes 7.
- **"Personalizados: consultar"** aparece en varias placas de 2026. No está en `TAREAS.md`: queda como pregunta.

## TOP para el sitio

Las 12 son del Cuartel de Bomberos, salvo la 10. Los fotogramas son de 716 px de ancho: alcanzan para el celular (unos 360 px de CSS a 2x) y para columnas en la compu, pero no para una foto a todo el ancho de una pantalla grande.

1. **`fotogramas-reels/2026-07-28_DbUtD7_j4uj_f024s.jpg`: el profe.** Nicolás identificado sin dudas (el reel dice "Soy Nicolás Valle"). Tiene el buzo con el logo y la pelota naranja, que repite el color de la marca, y no tiene subtítulo. Recorte 4:5, y 200–1095.
2. **`fotogramas-reels/2026-04-02_DWpl7tBNP0R_f004s.jpg`: cómo es la clase.** Es la única imagen que muestra el circuito, con cuatro personas en estaciones distintas a la vez y la camioneta de Bomberos al fondo. Las caras se ven de perfil o de espalda. Recorte y 200–1000.
3. **`fotogramas-reels/2026-07-28_DbUtD7_j4uj_f018s.jpg`: portada en el celular o supervisión.** Muestra al profe corrigiendo a una alumna adentro del cuartel, con autobombas: se entiende qué es y dónde queda. Se reconoce a la alumna, así que hace falta permiso. Recorte y 180–940.
4. **`fotogramas-reels/2026-07-28_DbUtD7_j4uj_f008s.jpg`: estaciones y lugar.** Dos estaciones en simultáneo debajo de "VOLUNTARIOS 25 DE MAYO". Recorte y 170–900.
5. **`fotogramas-reels/2026-02-06_DUa7Xy0DthX_f024s.jpg`: dónde estamos.** El letrero "BOMBEROS VOLUNTARIOS" bien legible y la imagen sin ningún texto agregado. Recorte 4:5, y 150–1050.
6. **`fotogramas-reels/2026-02-06_DUa7Xy0DthX_f040s.jpg`: dónde estamos.** La camioneta roja de los bomberos detrás: no hay manera más clara de decir "en el cuartel". Recorte y 100–950.
7. **`fotogramas-reels/2026-04-29_DXvBvnKDg29_f016s.jpg`: cómo es la clase.** TRX con la autobomba y la camioneta de Bomberos al fondo, y otra persona acompañando. Recorte y 200–890.
8. **`fotogramas-reels/2026-04-29_DXvBvnKDg29_f014s.jpg`: dónde estamos (alternativa).** Salto sobre una cubierta debajo del letrero. Recorte y 200–880.
9. **`fotogramas-reels/2026-07-30_Dbbmv_gCadM_f016s.jpg`: el profe (alternativa).** Nicolás de cuerpo entero con el buzo de la marca. Recorte y 0–1090, sin el subtítulo.
10. **`2022-07-27_CgiLZd_rLr2_1.webp`: el profe (la más nítida, 1080 px).** Retrato sonriendo, pero es de 2022 y el fondo no es el espacio. Recorte por encima de la franja naranja.
11. **`fotogramas-reels/2026-07-28_DbUtD7_j4uj_f026s.jpg`: cómo es la clase.** El pasillo largo del cuartel con dos estaciones. Recorte y 170–800.
12. **Imagen para compartir (1200×630):** no hay ninguna foto horizontal del cuartel que sirva. Propuesta: campo naranja con el logo y el texto, más una franja con la n.º 1 a 630 px de alto (unos 354 px de ancho, achicada, sin agrandar).

## Preguntas para Nicolás (fotos)

- ¿Nos pasás los videos o fotos originales de los reels de 2026, sin texto y en la resolución del celular? Sobre todo los del 28/07, 06/02, 02/04 y 29/04.
- ¿Tenés permiso de los alumnos que se reconocen (TOP 3, 7 y 11) o preferís fotos donde no se vean caras?
- ¿Tenés una foto de la entrada del cuartel? En Instagram no hay ninguna.
- La cuenta muestra una etapa anterior, desde 2018, con otros profes y en otros lugares. ¿Querés que el sitio la cuente o arrancamos en 2026 en el cuartel?
- En las placas de 2026 aparece "Personalizados: consultar". ¿Seguís dando entrenamiento personalizado aparte del plan complemento?
- La bio y las destacadas "HORARIOS" e "INFO 2026" pueden tener horarios viejos (6:30). Conviene revisarlas, y cambiar el link de WhatsApp de la bio al número con el 9.

## Privacidad

- Hay fotos de antes y después del cuerpo de alumnos y fotos de menores (el equipo de hockey de 2022). No van al sitio.
- Si el repo se sube a un GitHub público, **conviene no versionar `docs/fotos-instagram/`** (agregarla al `.gitignore`). Aunque `docs/` no se publique en el hosting, en el repo quedarían a la vista las fotos de alumnos.

## Otros datos verificados el 09/10/2026

**WhatsApp**

| Prueba | Resultado |
|---|---|
| `web.whatsapp.com/send?phone=5492345402547` | Abre el chat con **+54 9 2345 40-2547**, que tiene foto de perfil: la cuenta existe. |
| `web.whatsapp.com/send?phone=542345402547` | Abre **el mismo chat**: WhatsApp Web lo normaliza a +54 9 2345 40-2547. |
| `wa.me/5492345402547` | La página dice "Chatea en WhatsApp con el +54 9 2345 40-2547". |
| `wa.me/542345402547` | La página dice "Chatea en WhatsApp con el +54 2345 40-2547" (sin el 9). |

- **Usar `https://wa.me/5492345402547`**, con `?text=` si se quiere un mensaje inicial. Es el formato internacional de un celular argentino (+54 9, el área sin 0 y el número sin 15). Abre el chat directo y la página intermedia muestra el número bien.
- El formato sin 9 funciona solo si WhatsApp lo corrige, cosa que hizo en WhatsApp Web. No lo probé en un celular.

**Google Maps**

- La búsqueda "Bomberos Voluntarios 25 de Mayo, Calle 21 739, Veinticinco de Mayo, Buenos Aires" lleva a la ficha **"Bomberos Voluntarios"** (parque de bomberos):
  - dirección: C. 21 739, B6660DOO Veinticinco de Mayo, Provincia de Buenos Aires;
  - plus code: HR6H+GH;
  - abierto las 24 horas;
  - el teléfono que figura es el del cuartel, no el del espacio.
- **Coordenadas:** −35.4387213, −60.1711055.
- **Coincide con lo esperado:** en el mapa, el pin está sobre la calle 21, entre la 9 y la 8. Una cuadra al norte, cerca de la calle 22, aparece otro punto, "Estación de Bomberos": no hay que usar ese.
- **"Cómo llegar"** (probado, lleva a esa ficha): `https://www.google.com/maps/dir/?api=1&destination=-35.4387213%2C-60.1711055`. Con texto también funciona: `https://www.google.com/maps/dir/?api=1&destination=Bomberos+Voluntarios%2C+Calle+21+739%2C+Veinticinco+de+Mayo%2C+Buenos+Aires`.
- **Ficha** (probada): `https://maps.google.com/?cid=8828057531265068567`. Es la del cuartel, no la del espacio: cuando Nicolás tenga su Perfil de Empresa, se cambia.
- **Mapa embebido sin clave** (probado dentro de un iframe; fuera de un iframe muestra un aviso): `https://www.google.com/maps?q=-35.4387213,-60.1711055&z=17&output=embed`, con `loading="lazy"`.
