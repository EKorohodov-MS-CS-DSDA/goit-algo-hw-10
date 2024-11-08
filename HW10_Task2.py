import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def draw_plot(a, b):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


def monte_carlo_simulation(f, a, b, num_experiments):
    x = np.random.uniform(a, b, num_experiments)
    y = np.random.uniform(0, f(b), num_experiments)

    ratio = np.sum(y <= f(x)) / num_experiments

    integral = (b - a) * f(b) * ratio

    return integral


def main():
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    draw_plot(a, b)

    result, error = spi.quad(f, a, b)

    tests = [10, 100, 1000, 10000, 100000, 1000000]
    for i in tests:
        print(f"Інтеграл за методом Монте-Карло({i}): {monte_carlo_simulation(f, a, b, i)}")
    print("Інтеграл: ", result, error)


if __name__ == '__main__':
    main()
