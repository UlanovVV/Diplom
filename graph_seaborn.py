import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")


# Создание линейных графиков

N = 50
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 8
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 8

sns.lineplot(x=random_x, y=random_y0, label='A', color='#E32BB9', linestyle='--')
sns.lineplot(x=random_x, y=random_y1, label='B', linewidth=4)
sns.lineplot(x=random_x, y=random_y2, label='C')
plt.legend()
plt.show()


# Создание гистограммы

penguins = sns.load_dataset("penguins")
sns.displot(penguins, x="flipper_length_mm", bins=20)
plt.show()


# Разделение по группам

sns.pairplot(data=penguins, hue='species')
plt.show()

# Создание диаграммы уровней

sns.displot(
    penguins, x="bill_length_mm", y="bill_depth_mm",
    kind="kde", rug=True, hue='species')
plt.show()


# Создание "Скрипичной" диаграммы
g = sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="violin", inner=None)
sns.swarmplot(data=penguins, x="species", y="bill_length_mm", color="k", size=2, ax=g.ax)
plt.show()