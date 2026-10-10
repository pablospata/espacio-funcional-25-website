def lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def L(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
def ratio(a, b):
    la, lb = sorted((L(a), L(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)
pairs = [
 ('#000000', '#FF7B02', 'texto negro sobre naranja'),
 ('#FFFFFF', '#FF7B02', 'blanco sobre naranja (prohibido)'),
 ('#FF7B02', '#FFFFFF', 'naranja sobre blanco (prohibido para texto)'),
 ('#000000', '#FFFFFF', 'negro sobre blanco'),
 ('#000000', '#F2F2F2', 'negro sobre cal'),
 ('#545454', '#FFFFFF', 'gris sobre blanco'),
 ('#545454', '#F2F2F2', 'gris sobre cal'),
 ('#FFFFFF', '#000000', 'blanco sobre negro'),
 ('#FF7B02', '#000000', 'naranja sobre negro'),
 ('#BDBDBD', '#000000', 'gris claro sobre negro (pie)'),
 ('#2B2B2B', '#FF7B02', 'hover negro claro sobre naranja (fondo de boton)'),
 ('#FFFFFF', '#2B2B2B', 'blanco sobre hover'),
 ('#3A3A3A', '#FF7B02', 'linea gris oscura sobre naranja'),
 ('#F2F2F2', '#FFFFFF', 'cal vs blanco (solo separacion)'),
 ('#000000', '#FFB370', 'negro sobre naranja claro'),
]
for a, b, n in pairs:
    r = ratio(a, b)
    nivel = 'AAA' if r >= 7 else 'AA' if r >= 4.5 else 'AA grande/UI' if r >= 3 else 'NO PASA'
    print(f'{a} sobre {b}: {r:5.2f}:1  {nivel:13s} {n}')
