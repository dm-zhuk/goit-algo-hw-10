"""
1. Обчисліть значення інтеграла функції за допомогою методу Монте-Карло: знайдіть площу під графіком.
2. Перевірте правильність розрахунків, щоб підтвердити точність методу Монте-Карло, шляхом порівняння отриманого результату та аналітичних розрахунків або результату виконання функції quad. Зробіть висновки.
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


# Визначення функції
def f(x):
    return x**2


# Межі інтегрування
a = 0
b = 2
y_max = f(b)

# Обчислення аналітичного інтеграла
result, error = sp.integrate.quad(f, a, b)
print("Аналітичний інтеграл:", result)

# Метод Монте-Карло
N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, y_max, N)

# Площа під кривою
under_curve = y_random < f(x_random)
area_MC = (b - a) * y_max
integral_MC = area_MC * np.sum(under_curve) / N

print("Інтеграл за методом Монте-Карло:", integral_MC)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b, 100)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Додавання випадкових точок
ax.scatter(x_random, y_random, color="yellow", s=1, alpha=0.5, label="Випадкові точки")

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()
