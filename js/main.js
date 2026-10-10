/* Espacio Funcional 25 · sin dependencias */
(function () {
  'use strict';

  /* ---------- menú del celular ---------- */
  var cabecera = document.getElementById('cabecera');
  var boton = cabecera && cabecera.querySelector('.menu-boton');
  var menu = document.getElementById('menu');
  function menuAbierto() { return !!cabecera && cabecera.classList.contains('menu-abierto'); }

  function abrirMenu(abrir) {
    cabecera.classList.toggle('menu-abierto', abrir);
    boton.setAttribute('aria-expanded', String(abrir));
    boton.setAttribute('aria-label', abrir ? 'Cerrar el menú' : 'Abrir el menú');
    actualizarBarra();
  }
  if (boton && menu) {
    boton.addEventListener('click', function () {
      abrirMenu(boton.getAttribute('aria-expanded') !== 'true');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) abrirMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menuAbierto()) {
        abrirMenu(false);
        boton.focus();
      }
    });
    /* un toque fuera del panel y del botón lo cierra, también en la marca */
    document.addEventListener('click', function (e) {
      if (menuAbierto() && !menu.contains(e.target) && !boton.contains(e.target)) abrirMenu(false);
    });
    /* con teclado: cuando el foco sale del encabezado, se cierra */
    cabecera.addEventListener('focusout', function (e) {
      if (menuAbierto() && e.relatedTarget && !cabecera.contains(e.relatedTarget)) abrirMenu(false);
    });
  }

  /* ---------- precios: la fuente única es la sección "Turnos y cuota" del HTML ---------- */
  function texto(id) {
    var el = document.getElementById(id);
    return el ? el.textContent.trim() : '';
  }
  function numero(t) {
    return Number(t.replace(/\D/g, '')) || 0;
  }
  /* la cuota de la portada la copia el script chico del final de index.html, sin esperar a este archivo */
  var cuota = texto('precio-cuota');
  var vigencia = texto('precio-vigencia');
  var vigenciaEl = document.getElementById('precio-vigencia');
  var desde = vigenciaEl ? vigenciaEl.getAttribute('data-desde') : '';

  var ld = document.getElementById('datos-negocio');
  if (ld && cuota) {
    try {
      var datos = JSON.parse(ld.textContent);
      var oferta = function (nombre, monto, porMes) {
        var o = { '@type': 'Offer', name: nombre, price: monto, priceCurrency: 'ARS' };
        if (desde) o.validFrom = desde;
        if (porMes) o.priceSpecification = { '@type': 'UnitPriceSpecification', price: monto, priceCurrency: 'ARS', unitCode: 'MON', unitText: 'mes' };
        return o;
      };
      datos.priceRange = cuota + ' por mes (valores de ' + vigencia + ')';
      datos.makesOffer = [
        oferta('Clase de prueba', 0),
        oferta('Cuota mensual: 2 clases por semana', numero(cuota), true),
        oferta('Plan complemento para quienes entrenan en el espacio', numero(texto('precio-complemento')), true),
        oferta('Plan complemento, solo el plan (sin las clases)', numero(texto('precio-solo-plan')), true)
      ];
      ld.textContent = JSON.stringify(datos);
    } catch (err) { /* si el JSON-LD no se puede leer, queda el original */ }
  }

  /* ---------- la bolita que recorre el circuito ---------- */
  var pista = document.querySelector('.pista');
  function medirPista() {
    if (!pista) return;
    var paradas = pista.querySelectorAll(':scope > li');
    var horizontal = getComputedStyle(pista).display === 'grid';
    var x0 = paradas[0].offsetLeft;
    var y0 = paradas[0].offsetTop;
    for (var i = 1; i < paradas.length; i++) {
      pista.style.setProperty('--d' + i, (horizontal ? paradas[i].offsetLeft - x0 : paradas[i].offsetTop - y0) + 'px');
    }
  }
  medirPista();
  window.addEventListener('resize', medirPista);
  // una vuelta cada vez que la pista entra en pantalla (dura 5 s: no hace falta botón de pausa)
  if (pista && 'IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) { medirPista(); pista.classList.add('corriendo'); }
        else pista.classList.remove('corriendo');
      });
    }, { threshold: 0.6 }).observe(pista);
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(medirPista);

  /* ---------- botón fijo del celular: aparece apenas el de la portada empieza a salir de la pantalla y se
     esconde solo mientras el del bloque final se ve entero, así siempre hay un botón de WhatsApp a la vista ---------- */
  var barra = document.getElementById('barra');
  var ctaPortada = document.getElementById('cta-portada');
  var ctaFinal = document.getElementById('cta-final');
  function actualizarBarra() {
    if (!barra || !ctaPortada) return;
    /* si el menú quedó abierto y se bajó con el dedo hasta perderlo de vista, se cierra */
    if (menuAbierto() && menu && menu.getBoundingClientRect().bottom < 0) { abrirMenu(false); return; }
    var pasada = ctaPortada.getBoundingClientRect().top < 0;
    var enFinal = false;
    if (ctaFinal) {
      var r = ctaFinal.getBoundingClientRect();
      enFinal = r.top >= 0 && r.bottom <= window.innerHeight;
    }
    barra.classList.toggle('visible', pasada && !enFinal && !menuAbierto());
  }
  window.addEventListener('scroll', actualizarBarra, { passive: true });
  window.addEventListener('resize', actualizarBarra);
  actualizarBarra();

  /* ---------- año del pie ---------- */
  var anio = document.getElementById('anio');
  if (anio) anio.textContent = String(new Date().getFullYear());
})();
