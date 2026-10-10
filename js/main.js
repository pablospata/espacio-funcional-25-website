/* Espacio Funcional 25 · sin dependencias */
(function () {
  'use strict';

  /* ---------- menú del celular ---------- */
  var cabecera = document.getElementById('cabecera');
  var boton = cabecera && cabecera.querySelector('.menu-boton');
  var menu = document.getElementById('menu');

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
      if (e.key === 'Escape' && cabecera.classList.contains('menu-abierto')) {
        abrirMenu(false);
        boton.focus();
      }
    });
    document.addEventListener('click', function (e) {
      if (cabecera.classList.contains('menu-abierto') && !cabecera.contains(e.target)) abrirMenu(false);
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
  var cuota = texto('precio-cuota');
  var vigencia = texto('precio-vigencia');
  document.querySelectorAll('[data-copia="cuota"]').forEach(function (el) {
    if (cuota) el.textContent = cuota;
  });

  var ld = document.getElementById('datos-negocio');
  if (ld && cuota) {
    try {
      var datos = JSON.parse(ld.textContent);
      var oferta = function (nombre, monto, unidad) {
        var o = { '@type': 'Offer', name: nombre, price: monto, priceCurrency: 'ARS' };
        if (unidad) o.priceSpecification = { '@type': 'UnitPriceSpecification', price: monto, priceCurrency: 'ARS', unitText: unidad };
        return o;
      };
      datos.priceRange = cuota + ' por mes (valores de ' + vigencia + ')';
      datos.makesOffer = [
        oferta('Clase de prueba', 0),
        oferta('Cuota mensual: 2 clases por semana', numero(cuota), 'mes'),
        oferta('Plan complemento para quienes entrenan en el espacio', numero(texto('precio-complemento')), 'mes'),
        oferta('Plan personalizado, sin las clases', numero(texto('precio-solo-plan')), 'mes')
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
      pista.style.setProperty('--p' + i, horizontal
        ? 'calc(' + (paradas[i].offsetLeft - x0) + 'px + .125rem)'
        : 'calc(' + (paradas[i].offsetTop - y0) + 'px + .3125rem)');
    }
  }
  medirPista();
  window.addEventListener('resize', medirPista);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(medirPista);

  /* ---------- botón fijo del celular: aparece al pasar el de la portada, se esconde en el bloque final ---------- */
  var barra = document.getElementById('barra');
  var ctaPortada = document.getElementById('cta-portada');
  var final = document.getElementById('prueba');
  function actualizarBarra() {
    if (!barra || !ctaPortada || !final) return;
    var pasada = ctaPortada.getBoundingClientRect().bottom < 0;
    var r = final.getBoundingClientRect();
    var enFinal = r.top < window.innerHeight && r.bottom > 0;
    var menuAbierto = cabecera && cabecera.classList.contains('menu-abierto');
    barra.classList.toggle('visible', pasada && !enFinal && !menuAbierto);
  }
  window.addEventListener('scroll', actualizarBarra, { passive: true });
  window.addEventListener('resize', actualizarBarra);
  actualizarBarra();

  /* ---------- año del pie ---------- */
  var anio = document.getElementById('anio');
  if (anio) anio.textContent = String(new Date().getFullYear());
})();
