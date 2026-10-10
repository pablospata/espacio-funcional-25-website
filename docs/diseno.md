# Diseño aprobado · Espacio Funcional 25

09/10/2026 · aprobado por Pablo sobre la maqueta `docs/diseno/index.html` (lorem ipsum) · el sitio real (`index.html`, `css/style.css`) es esa maqueta con el contenido de verdad

## Cómo se llegó

1. El plan v0 (`docs/plan.md`) proponía naranja como campo grande, bordes negros de 3 px, Big Shoulders Display 800 enorme y fotos en cajas con borde. Pablo: "Todo naranja el sitio?????" y "Está quedando muy horrible... errores muy básicos". Se frenó todo y se rehízo de cero con lorem ipsum.
2. Primera versión limpia (blanco, Barlow, tarjetas suaves): "muy MEHHH, falta algo que uno diga WOW".
3. Se sumaron los detalles con carácter (cinta del titular, sello "$0", chevrones, banda inclinada) y fotos en blanco y negro: "¿Por qué las fotos en blanco y negro? Muy feo... al fondo le falta decoración, es muy liso".
4. Fotos en color y fondos con textura (rombos y discos del logo): "Sí, ahora sí me gusta".

## Tokens

| Nombre | Valor | Uso |
|---|---|---|
| `--tinta` | `#17181A` | Texto, tarjeta del precio, pie, botón del bloque final |
| `--tinta-2` | `#3B3F45` | Texto secundario (10,6:1 sobre blanco) |
| `--gris` | `#5C626A` | Rótulos y notas (6,2:1 sobre blanco, 5,6:1 sobre `--niebla`) |
| `--linea` | `#E2E4E8` | Divisores |
| `--niebla` | `#F2F3F5` | Fondo de las secciones alternas |
| `--naranja` | `#FF7B02` | El del logo. Botones (con texto `--tinta`, 6,8:1), cinta del titular, sello, discos, chevrones, bloque final |

- Tipografía: **Barlow Semi Condensed** 600/700 para títulos y números, **Barlow** 400/500/600 para el texto. Barlow nació de la señalética vial de California: tiene el aire de cartel del logo (el rombo es una señal de tránsito) sin gritar, y se lee bien en todas las edades. Archivos woff2 de @fontsource 5.3.0 en `assets/fonts/`, licencia OFL. Se precarga solo `barlow-sc-700` (titular).
- Escala (celular → compu): h1 56 → 92 px; h2 34 → 52 px; texto 18 px; nada baja de 14 px.
- Radios de 18 px en fotos y tarjetas; botones redondeados (999 px) de 56 px de alto; sin bordes gruesos.

## Lo que la hace distinta

- **Cinta naranja** levemente torcida detrás de "volver." en el titular.
- **Sello circular "$0"** con "Clase de prueba · gratis · 25 de Mayo" alrededor, sobre la foto de la portada.
- **Franja de chevrones** naranja y negra, como la de atrás de las autobombas: borde de la foto de portada, tarjeta del precio y borde del bloque final.
- **Banda negra inclinada** entre la portada y el enfoque (fuerza, resistencia, técnica, continuidad, máximo 7 por turno, 25 de Mayo).
- **Fondos con las formas del logo**: disco naranja detrás de la foto de portada y de la del profe; tramas de rombos que se desvanecen (naranja en la portada y el profe, gris en las secciones grises, naranja oscuro en el bloque final); un anillo gris enorme en "Cómo es la clase".
- **El circuito como recorrido**: una línea naranja con una parada por estación (vertical en el celular, horizontal en la compu) y una bolita que la recorre, se detiene en cada estación y vuelve a empezar. Es el único movimiento de la página; con `prefers-reduced-motion` queda quieta.
- **El 7** grande con siete figuras de personas.

## Cambios del copy respecto del plan v0

- Titular: "Que quieras volver." con "Entrenamiento funcional en 25 de Mayo" como primera línea del `h1` (chica, con el punto naranja).
- Licenciatura con año 2023 (Pablo confirmó que terminó en 2023 y el diploma se emitió en marzo de 2024).
- El profe: por pedido de Pablo ("en el CV hay información importante para publicar"), además de la bio va la trayectoria completa: experiencia, formación y una lista desplegable de cursos. Quedan afuera los datos personales, los dos años de Medicina (pregunta para Nicolás) y los cursos de gestión educativa.
- Bloque final: el título es la frase de Nicolás del reel del 28/07/2026, "No hace falta que estés en forma para arrancar."
- Datos rápidos de la portada: cuota, turnos de la tarde (18 y 19 h, lunes y jueves) y de la mañana (7 h, martes y viernes).

## Ajustes después de las auditorías (10/10/2026)

Arreglos de defectos que no cambian el estilo aprobado (colores, tipografías, cinta, sello, chevrones, banda, tramas, discos, pista, fotos). El detalle de cada uno está en `docs/auditoria/correcciones.md`.

- **El profe, celular y tablet:** la foto deja abajo el lugar que ocupa el disco (`margin-bottom: 12.5%`), así el disco ya no tapa "El profe". **En la compu**, la foto queda fija mientras se lee la trayectoria (`position: sticky`) y se suelta al final.
- **Botón fijo:** aparece apenas el botón de la portada empieza a salir de la pantalla. Se esconde solo mientras el botón negro del bloque final se ve entero. Escondido, no recibe el foco.
- **Botones de reserva:** hasta 383 px de ancho tienen 16 px de relleno a los costados (en vez de 24). Así, a 360 px "Reservá tu clase de prueba gratis" entra en una línea. En pantallas más angostas, el texto se parte en dos renglones parejos.
- **Compu con ventana baja** (menos de 760 px de alto): la portada se compacta para que la cuota y los turnos entren en el primer pantallazo. El titular baja de 92 a 84 px y la foto, de 576 a 480 px de alto máximo.
- **Compu, otros:**
  - el encabezado es blanco opaco;
  - el menú no se parte en dos renglones;
  - las columnas de la pista son parejas y el título de cada estación se achica un poco entre 1024 y 1170 px;
  - la tarjeta de turnos reparte los horarios en su alto;
  - la tarjeta del 7 termina a la altura de la foto;
  - la banda se recorta solo a los costados;
  - el sello se acerca al centro entre 1024 y 1360 px;
  - en El enfoque, las dos columnas arrancan arriba.
- **Hover:** el naranja del hover pasa de `#F26F00` a `#E06500`, porque antes casi no se notaba. El texto tinta queda a 5,1:1. La cuota de la portada y "Cursos y capacitaciones" se subrayan con el hover.
- **La bolita** se mueve con `transform` en lugar de `top` y `left`. Se ve igual, pero ya no recalcula el layout en cada cuadro.
