import numpy as np

x, y, z = tuple(map(float, input().split()))
point_init = x0, y0, z0 = tuple(map(float, input().split()))

TAMANHO_CAPA = .3
LARGURA_BEIRADA = .5
ANGULO_ROTACAO = -45

def add_box(point_init, point_end, *atributes):
    print("\tbox {{ <{}, {}, {}>, <{}, {}, {}> {}}} ".format(*point_init, *point_end, ''.join(atributes)))

def make_rotation(center_position, angle):
    print("\ttranslate <{}, {}, {}>".format(*(-center_position)))
    print("\trotate <0, {}, 0>".format(angle))
    print("\ttranslate <{}, {}, {}>".format(*center_position))

print("union {")

add_box(point_init, (x0 + x, y0 + TAMANHO_CAPA, z0 + z))
add_box(point_init, (x0 + LARGURA_BEIRADA, y0 + y, z0 + z))
add_box((x0, y0 + y, z0), (x0 + x, y0 + y - TAMANHO_CAPA, z0 + z))

center_position = np.array([x0 + x/2, y0 + y/2, z0 + z/2])
make_rotation(center_position, ANGULO_ROTACAO)

print("\tpigment {Brown}")
print("}")

print("union {")
OFFSET_PAGINA = .1
TAMANHO_PAGINA = .1
init_point_pages = np.array((x0 + offset_pagina, y0 + tamanho_capa + tamanho_pagina, z0))

for i_pagina in range(2, 15):
    end_point_pages = np.array((x0 + x - OFFSET_PAGINA, y0 + TAMANHO_CAPA + i_pagina * TAMANHO_PAGINA, z0 + z))
    if i_pagina % 2:
        add_box(init_point_pages, end_point_pages, 'pigment {White}')
    else:
        add_box(init_point_pages, end_point_pages, 'pigment {Gray}')
    init_point_pages[1] = end_point_pages[1]

print("}")

