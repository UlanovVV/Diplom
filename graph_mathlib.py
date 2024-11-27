import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import IndexLocator


# Создание линейных графиков в нескольких координатных осях
f, ax = plt.subplots(2, 2)
f.set_size_inches(14, 10)
f.set_facecolor("#6780D5")
ax[0, 0].plot(np.random.randn(10), 'r:s')
ax[0, 0].grid()
ax[0, 1].plot(np.random.randn(10), '-.*')
ax[0, 1].grid()
ax[1, 0].plot(np.random.randn(5), 'y--')
ax[1, 0].grid()
ax[1, 1].plot(np.random.randn(20), color='#E32BB9', alpha=0.5)
ax[1, 1].grid()
ax[1, 1].set(facecolor='#EAE481')
ax[1, 1].xaxis.set_major_locator(IndexLocator(base=1, offset=0))
plt.show()


# Создание гистограммы

f2 = plt.figure(figsize=(14, 10))
ax = f2.add_subplot()
x = np.arange(12)
y1 = np.random.randint(3, 20, len(x))
y2 = np.random.randint(5, 25, len(x))
w = 0.2
f2.suptitle('Создание гистограммы', size='20')
ax.set_xlabel('0x', size='14')
ax.set_ylabel('0y', size='14')
ax.bar(x - w/2, y1, width=w, label='data1')
ax.bar(x + w/2, y2, width=w, label='data2')
ax.grid(which='major', color='#2D1F2A', linewidth=1)
ax.legend()
plt.show()


# Создание трехмерного графика

f3 = plt.figure(figsize=(14, 10))
ax_3d = f3.add_subplot(projection='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
ax_3d.scatter(x, y, z, color='g')
ax_3d.set_xlabel('x', size='14')
ax_3d.set_ylabel('y', size='14')
ax_3d.set_zlabel('z', size='14')
plt.show()


# Создание круговой диаграммы

plt.figure(figsize=(10, 10))
vals = [168.1, 130.6, 74.4, 77.4, 61.5, 238]
color = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', ]
exp = [0.3, 0.2, 0, 0, 0, 0.1]
labels = ['KIA', 'Hyundai', 'Toyota', 'Volkswagen', 'Skoda', 'Остальные']
plt.pie(vals, labels=labels, autopct='%.1f%%', startangle=90, colors=color, explode=exp)
plt.title('Топ по продажам автомобилей в 2019 году', fontsize=16)
plt.axis('equal')
plt.show()


# Создание диаграммы уровней

f4, ax = plt.subplots()
x = np.random.randn(6)
y = np.random.randn(6)
z = x**2 + y**2
d = ax.tricontour(x, y, z)
d.clabel(colors='black')
plt.show()


# Создание анимационного графика

def update_cos(frame, line, x):
    line.set_ydata(np.cos(x + frame))
    return [line]


f5, ax = plt.subplots()

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)

line, = ax.plot(x, y)

phasa = np.arange(0, 4*np.pi, 0.1)

animation = FuncAnimation(
    f5,
    func=update_cos,
    frames=phasa,
    fargs=(line, x),
    interval=30,
    repeat=True)

plt.show()
