import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

x = np.linspace(0, 2 * np.pi, 200)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

fig = plt.figure(figsize=(2, 2), facecolor='lightskyblue', layout='constrained')
fig.suptitle('Figure')
ax = fig.add_subplot()
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')

row = int(1080)
col = int(1920)

# Defining the top, bottom, left and right margins for
# For the red square
Rrow1 = int(0.25*row)
Rrow2 = int(0.5*row)
Rcol1 = int(0.25*col)
Rcol2 = int(0.75*col)

# For the white square
Wrow1 = int(0.5*row)
Wrow2 = int(0.75*row)
Wcol1 = int(0.25*col)
Wcol2 = int(0.75*col)

Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
for i in range(Rrow1, Rrow2):
    for j in range(Rcol1, Rcol2):
        Gambar[i, j, 0] = 255

for i in range(Wrow1, Wrow2):
    for j in range(Wcol1, Wcol2):
        Gambar[i, j, :] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

x = np.linspace(0, 2 * np.pi, 200)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

fig = plt.figure(figsize=(2, 2), facecolor='lightskyblue', layout='constrained')
fig.suptitle('Figure')
ax = fig.add_subplot()
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')

row = int(1080)
col = int(1920)

# Defining the top, bottom, left and right margins for
# For the red square
Rrow1 = int(0.25*row)
Rrow2 = int(0.5*row)
Rcol1 = int(0.25*col)
Rcol2 = int(0.75*col)

# For the white square
Wrow1 = int(0.5*row)
Wrow2 = int(0.75*row)
Wcol1 = int(0.25*col)
Wcol2 = int(0.75*col)

Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
for i in range(Rrow1, Rrow2):
    for j in range(Rcol1, Rcol2):
        Gambar[i, j, 0] = 255

for i in range(Wrow1, Wrow2):
    for j in range(Wcol1, Wcol2):
        Gambar[i, j, :] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()v