import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import poisson
import numpy as np


def ud_function(a, b, x):
    return (x - a) / (b - a) if a <= x < b else 0 if x < a else 1


def ud_density(a, b, x):
    return 1 / (b - a) if a <= x <= b else 0


def possion_function(x, mu):
    poisson.cdf(x, mu)
    return poisson.cdf(x, mu)


def possion_density(x, mu):
    return poisson.pmf(x, mu)

def draw_possion(x, y_function, y_density, name):
    fig, axs = plt.subplots(ncols=2, figsize=(10, 5))

    fig.suptitle(name)
    axs[0].plot(x, y_function, 'bo', color='blue', ms=4)
    axs[1].vlines(x, 0, y_density, color='blue', lw=4, alpha=0.5)

    axs[0].set_xlabel('x')
    axs[0].set_ylabel('F(x)')

    axs[1].set_xlabel('x')
    axs[1].set_ylabel('f(x)')

    axs[0].grid(True)
    axs[1].grid(True)
    plt.show()


def draw_graphics(x, y_function, y_density, name):
    fig, axs = plt.subplots(ncols=2, figsize=(10, 5))

    fig.suptitle(name)
    axs[0].plot(x, y_function, color='blue')
    axs[1].plot(x, y_density, color='blue')

    axs[0].set_xlabel('x')
    axs[0].set_ylabel('F(x)')

    axs[1].set_xlabel('x')
    axs[1].set_ylabel('f(x)')

    axs[0].grid(True)
    axs[1].grid(True)
    plt.show()


def main():
    # a = float(input("Input a: "))
    # b = float(input("Input b: "))
    a = 1
    b = 10
    delta = b - a
    x = np.arange(a - delta / 2, b + delta / 2, 0.001)
    y_function = [ud_function(a, b, _x) for _x in x]
    y_density = [ud_density(a, b, _x) for _x in x]
    draw_graphics(x, y_function, y_density, 'Равномерное распределение')

    # mu = float(input("Input mu: "))
    mu = 5
    x = np.linspace(poisson.ppf(0.01, mu), poisson.ppf(0.90, mu))
    y_function = possion_function(x, mu)
    y_density = possion_density(x, mu)

    draw_possion(x, y_function, y_density, 'Пуасонновоское распределение')


if __name__ == '__main__':
    main()


# sns.distplot(np.random.uniform(0, 10, size=100), hist=False)
# sns.distplot(np.random.poisson(lam=1, size=1000), hist=False, label='poisson')