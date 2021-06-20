import numpy as np
import argparse

from utils import *

x, y, z = tuple(map(float, input().split()))
point_init = x0, y0, z0 = tuple(map(float, input().split()))

TAMANHO_CAPA = .3
LARGURA_BEIRADA = .5
ANGULO_ROTACAO = -45

main = Union()

main.add_object(Box(point_init, (x0 + x, y0 + TAMANHO_CAPA, z0 + z)))
main.add_object(Box(point_init, (x0 + LARGURA_BEIRADA, y0 + y, z0 + z)))
main.add_object(Box((x0, y0 + y, z0), (x0 + x, y0 + y - TAMANHO_CAPA, z0 + z)))

center_position = np.array([x0 + x/2, y0 + y/2, z0 + z/2])

main.add_rotation_y(ANGULO_ROTACAO, center_position)

pages = Union()

OFFSET_PAGINA = .1
TAMANHO_PAGINA = .1
init_point_pages = np.array((x0 + OFFSET_PAGINA, y0 + TAMANHO_CAPA + TAMANHO_PAGINA, z0))

numero_paginas = int((y - TAMANHO_CAPA * 2) / OFFSET_PAGINA)

for i_pagina in range(2, numero_paginas):
    end_point_pages = np.array((x0 + x - OFFSET_PAGINA, y0 + TAMANHO_CAPA + i_pagina * TAMANHO_PAGINA, z0 + z))
    page = Box(init_point_pages, end_point_pages)

    if i_pagina % 2:
        page.add_pigment('White')
        pages.add_object(page)
    else:
        page.add_pigment('Gray')
        pages.add_object(page)

    init_point_pages[1] = end_point_pages[1]

main.add_pigment('Brown')
main.add_object(pages)
main.show_object()
