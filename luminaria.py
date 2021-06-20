from utils import *
import numpy as np

import argparse

argument_parser = argparse.ArgumentParser()

argument_parser.add_argument("--h", default=24)
argument_parser.add_argument("--d", default=4)
argument_parser.add_argument("--x", default=30)
argument_parser.add_argument("--y", default=20)
argument_parser.add_argument("--z", default=-10)

args = argument_parser.parse_args()

h, d = args.h, args.d
x, y, z = args.x, args.y, args.z

hC = int(2*h/3)
hB = int(h/3)

union = Union()

difference = Difference()

# Raio do cilindro maior menos o raio do menor
OFFSET_RAIO_CILINDROS = 0.5

difference.add_objects([
    Cylinder(
        (x, y + hB, z),
        (x, y + hC, z),
        d
    ),
    Cylinder(
        (x, y + hB - 1, z),
        (x, y + hC + 1, z),
        (d - OFFSET_RAIO_CILINDROS)
    ),
])

# Angulo entre um buraco e outro
theta = 2*(np.pi)/10

# Centro do primeiro buraco
vector = np.array([0, d - OFFSET_RAIO_CILINDROS / 2])

# Matriz de rotação para o centro dos buracos
rot = np.array([[np.cos(theta),-np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Altura dos buracos de cima
y1 = y + hC - ((hC - hB)/4)

sphere = Sphere(
    (x, y1, z + vector[1]),
    OFFSET_RAIO_CILINDROS
)

difference.add_object(sphere)

for i in range(9):
    vector = rot.dot(vector)

    sphere = Sphere(
        (x + vector[0], y1, z + vector[1]),
        OFFSET_RAIO_CILINDROS
    )

    difference.add_object(sphere)

vector = rot.dot(vector)
# Altura dos buracos do meio
y2 = y + hC - (2*(hC - hB)/4)

for i in range(9):
    vector = rot.dot(vector)

    sphere = Sphere(
        (x + vector[0], y2, z + vector[1]),
        OFFSET_RAIO_CILINDROS
    )

    difference.add_object(sphere)

vector = rot.dot(vector)
# Altura dos buracos mais de baixo
y3 = y + hC - (3*(hC - hB)/4)

for i in range(9):
    vector = rot.dot(vector)

    sphere = Sphere(
        (x + vector[0], y3, z + vector[1]),
        OFFSET_RAIO_CILINDROS
    )

    difference.add_object(sphere)

union.add_object(difference)

# Criação da base da parte de cima da luminária e o cabo

# Razão entre o raio da parte de cima da luminária e do cabo
RAZAO_LUMINARIA_CABO = 1/6
# Tamanho da base da luminária
TAMANHO_BASE_LUMINARIA = 1

union.add_objects([
    Cylinder(
        (x, y + hB + .25 , z),
        (x, y + hB + .75, z),
        (d - OFFSET_RAIO_CILINDROS)
    ),
    Cylinder(
        (x, y + TAMANHO_BASE_LUMINARIA, z),
        (x, y + hB - .25 , z),
        (d * (RAZAO_LUMINARIA_CABO))
    )
])

intersection = Intersection()

# Razão entre o raio da base e o da luminária
RAZAO_LUMINARIA_BASE = 2/3
# Relação entre a esfera e o cilindro para obtermos a forma desejada
o = np.sqrt((d) ** 2 - (2 * d / 3) ** 2)

intersection.add_objects([
    Cylinder(
        (x, y, z),
        (x, y + TAMANHO_BASE_LUMINARIA, z),
        (RAZAO_LUMINARIA_BASE * d)
    ),
    Sphere(
        (x, y - o + TAMANHO_BASE_LUMINARIA, z),
        d
    )
])

union.add_object(intersection)
union.show_object()
