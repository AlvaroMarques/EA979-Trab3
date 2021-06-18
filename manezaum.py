import numpy as np

stri = input("Deseja gerar uma luminária (s/n) ?\n")

if(stri == 's'):
	h, d = map(int, input("Altura e diametro da lampada respectivamente\n").split())
	x, y, z = map(int, input("Posição da lampada\n").split())

	hC = int(2*h/3)
	hB = int(h/3)

	print("union {")
	print("\tdifference {")
	print(f"\t\tcylinder {{\n\t\t\t<{x}, {y + hB}, {z}>, <{x}, {y + hC}, {z}>, {d}\n\t\t\t}}")
	print(f"\t\tcylinder {{\n\t\t\t<{x}, {y + hB - 1}, {z}>, <{x}, {y + hC + 1}, {z}>, {d - 0.5}\n\t\t\t}}")

	theta = 2*(np.pi)/10
	vector = np.array([0, d - 0.25])
	rot = np.array([[np.cos(theta),-np.sin(theta)], [np.sin(theta), np.cos(theta)]])
	y1 = y + hC - ((hC - hB)/4)
	print(f"\t\tsphere {{\n\t\t\t<{x}, {y1}, {z + vector[1]}>, 0.5\n\t\t\t}}")
	for i in range(9):
		vector = rot.dot(vector)
		print(f"\t\tsphere {{\n\t\t\t<{x + vector[0]}, {y1}, {z + vector[1]}>, 0.5\n\t\t\t}}")
	vector = rot.dot(vector)
	y2 = y + hC - (2*(hC - hB)/4)
	print(f"\t\tsphere {{\n\t\t\t<{x}, {y2}, {z + vector[1]}>, 0.5\n\t\t\t}}")
	for i in range(9):
		vector = rot.dot(vector)
		print(f"\t\tsphere {{\n\t\t\t<{x + vector[0]}, {y2}, {z + vector[1]}>, 0.5\n\t\t\t}}")
	vector = rot.dot(vector)
	y3 = y + hC - (3*(hC - hB)/4)
	print(f"\t\tsphere {{\n\t\t\t<{x}, {y3}, {z + vector[1]}>, 0.5\n\t\t\t}}")
	for i in range(9):
		vector = rot.dot(vector)
		print(f"\t\tsphere {{\n\t\t\t<{x + vector[0]}, {y3}, {z + vector[1]}>, 0.5\n\t\t\t}}")

	print("\t}")

	print(f"\tcylinder {{\n\t\t<{x}, {y + hB + 0.25}, {z}>, <{x}, {y + hB + 0.75}, {z}>, {d - 0.5}\n\t\t}}")
	print(f"\tcylinder {{\n\t\t<{x}, {y + 1}, {z}>, <{x}, {y + hB + 0.25}, {z}>, {d/6}\n\t\t}}")
	print("\tintersection {")

	o = np.sqrt((d)**2 - (2*d/3)**2)
	print(f"\t\tcylinder {{\n\t\t\t<{x}, {y}, {z}>, <{x}, {y + 1}, {z}>, {2*d/3}\n\t\t\t}}")
	print(f"\t\tsphere {{\n\t\t\t<{x}, {y - o + 0.5}, {z}>, {d}\n\t\t\t}}")
	print("\t}")

stri = input("Deseja gerar um cinzeiro (s/n) ?\n")

if(stri == 's'):
	h, d = map(int, input("Altura e diametro da cinzeiro respectivamente\n").split())
	x, y, z = map(int, input("Posição do cinzeiro\n").split())

	hC = int(3*h/5)
	hB = int(2*h/5)

	print("union {")
	print("\tmerge {")
	print("\t\tdifference {")
	print(f"\t\t\tcylinder {{\n\t\t\t\t<{x}, {y + hB}, {z}>, <{x}, {y + hC}, {z}>, {d}\n\t\t\t\t}}")
	print(f"\t\t\tcylinder {{\n\t\t\t\t<{x}, {y + hB + 0.2}, {z}>, <{x}, {y + hC + 1}, {z}>, {d - 0.75}\n\t\t\t\t}}")
	theta = 2*(np.pi)/4
	vector = np.array([0, d - 0.375])
	rot = np.array([[np.cos(theta),-np.sin(theta)], [np.sin(theta), np.cos(theta)]])
	yN = y + hC
	print(f"\t\t\tsphere {{\n\t\t\t\t<{x}, {yN}, {z + vector[1]}>, 0.5\n\t\t\t\t}}")
	for i in range(9):
		vector = rot.dot(vector)
		print(f"\t\t\tsphere {{\n\t\t\t\t<{x + vector[0]}, {yN}, {z + vector[1]}>, 0.5\n\t\t\t\t}}")
	print("\t\t}")
	print("\t\tdifference {")
	di = 1.2*d
	print(f"\t\t\tsphere {{\n\t\t\t\t<{x}, {(y + hB) - di + 0.18}, {z}>, {di}\n\t\t\t\t}}")
	print(f"\t\t\tcylinder {{\n\t\t\t\t<{x}, {(y + hB) - 2*di}, {z}>, <{x}, {y}, {z}>, {di}\n\t\t\t\t}}")
	print("\t\t}")
	print("\t}")
