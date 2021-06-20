import numpy as np
from utils import *

h, d = map(int, input().split())
x, y, z = map(int, input().split())

hC = int(3*h/5)
hB = int(2*h/5)

union = Union()

merge = Merge()
union.add_object(merge)

difference = Difference()
merge.add_object(difference)

OFFSET_ALTURA_CILINDROS = 1
OFFSET_RAIO_CILINDROS = .75

difference.add_objects([
    Cylinder(
        start_point=(x, y+hB, z),
        end_point=(x, y+hC, z),
        radius=d
    ),
    Cylinder(
        start_point=(x, y+hB, z),
        end_point=(x, y+hC + OFFSET_ALTURA_CILINDROS, z),
        radius=(d - OFFSET_RAIO_CILINDROS)
    )
])

# Angulo entre os buracos 
theta = 2*(np.pi)/4
# Centro do primeiro buraco
vector = np.array([0, d - 0.375])
# Matriz de rotação dos buracos
rot = np.array([[np.cos(theta),-np.sin(theta)], [np.sin(theta), np.cos(theta)]])
# Altura dos buracos
yN = y + hC

RAIO_BURACO = .5

difference.add_object(
    Sphere(
        center=(x, yN, z+vector[1]),
        radius=RAIO_BURACO
    )
)

for i in range(3):
    vector = rot.dot(vector)
    difference.add_object(
        Sphere(
            center=(x, yN, z+vector[1]),
            radius=RAIO_BURACO
        )
    )


difference_base = Difference()

RAZAO_DIM_BASE = 1.2
diametro_base = RAZAO_DIM_BASE * d
AJUSTE = .18

difference_base.add_objects([
    Sphere(
        center=(x, y+hB - diametro_base + AJUSTE, z),
        radius=diametro_base
    ),
    Cylinder(
        start_point=(x, y + hB - 2*diametro_base, z),
        end_point=(x, y, z),
        radius=diametro_base
    )
])
merge.add_object(difference_base)
union.show_object()
