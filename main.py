import numpy as np
import matplotlib.pyplot as plt
import random

from scipy.optimize import rosen


def sphere(k):
    x_list = []
    for i in range(k):
        x_list.append(np.linspace(-5.12, 5.12, 500))
    ### Vizualizace
    # x_mesh = (np.meshgrid(*x_list))
    # suma = 0
    # for x in x_mesh:
    #     suma = suma + (x ** 2)
    # y = suma
    # ax = plt.axes(projection='3d')
    # ax.plot_surface(x_mesh[0], x_mesh[1], y)
    # plt.show()
    lowest_records = []
    lowest_coords = []
    for i in range(k*10000):
        coords = []
        suma = 0
        for x in x_list:
            coords.append(random.choice(x))
        for x in coords:
            suma = suma + (x ** 2)
        y = suma
        if i == 0:
            lowest_records.append([y,i+1])
        if lowest_records[len(lowest_records)-1][0] > y:
            lowest_records.append([y,i+1])
            lowest_coords = coords
    lowest_records_swapped = np.swapaxes(lowest_records,0,1)
    lowest_coords_concated = ''
    for i,coord in enumerate(lowest_coords):
        if i%5 == 0 and i!=0:
            lowest_coords_concated = lowest_coords_concated + '\n'
        lowest_coords_concated = lowest_coords_concated + str(coord) + ', '
    plt.title(f'Sphere in {k}D (maxFES = {k*10000})\nBest solution: {lowest_records[len(lowest_records)-1][0]}'
              f', in: \n{lowest_coords_concated}')
    plt.plot(lowest_records_swapped[1],lowest_records_swapped[0],drawstyle="steps-post")
    plt.show()

def trid(k):
    x_list = []
    for i in range(k):
        x_list.append(np.linspace(-k**2, k**2, 500))
    # # Vizualizace
    # x_mesh = (np.meshgrid(*x_list))
    # suma1,suma2 = 0,0
    # for i,x in enumerate(x_mesh):
    #     suma1 = suma1 + (x - 1)**2
    #     if i > 0:
    #         suma2 = x*x_list[i-1]
    # y = suma1-suma2
    # ax = plt.axes(projection='3d')
    # ax.plot_surface(x_mesh[0], x_mesh[1], y)
    # plt.show()
    lowest_records = []
    lowest_coords = []
    for i in range(k*10000):
        coords = []
        suma1,suma2 = 0,0
        for x in x_list:
            coords.append(random.choice(x))
        for j,x in enumerate(coords):
            suma1 = suma1 + (x - 1)**2
            if j > 0:
                suma2 = suma2 + x*coords[j-1]
        y = suma1-suma2
        if i == 0:
            lowest_records.append([y,i+1])
        if lowest_records[len(lowest_records)-1][0] > y:
            lowest_records.append([y,i+1])
            lowest_coords = coords
    lowest_records_swapped = np.swapaxes(lowest_records,0,1)
    lowest_coords_concated = ''
    for i,coord in enumerate(lowest_coords):
        if i%5 == 0 and i!=0:
            lowest_coords_concated = lowest_coords_concated + '\n'
        lowest_coords_concated = lowest_coords_concated + str(coord) + ', '
    plt.title(f'Trid in {k}D (maxFES = {k*10000})\nBest solution: {lowest_records[len(lowest_records)-1][0]}'
              f', in: \n{lowest_coords_concated}')
    plt.plot(lowest_records_swapped[1],lowest_records_swapped[0],drawstyle="steps-post")
    plt.show()

def schwefel(k):
    x_list = []
    for i in range(k):
        x_list.append(np.linspace(-500, 500, 500))
    # # Vizualizace
    # x_mesh = (np.meshgrid(*x_list))
    # suma1 = 0
    # for x in x_mesh:
    #     suma1 = suma1 + x * np.sin(np.sqrt(np.abs(x)))
    # y = 418.9829*k - suma1
    # ax = plt.axes(projection='3d')
    # ax.plot_surface(x_mesh[0], x_mesh[1], y)
    # plt.show()
    lowest_records = []
    lowest_coords = []
    for i in range(k * 10000):
        coords = []
        suma1 = 0
        for x in x_list:
            coords.append(random.choice(x))
        for x in coords:
            suma1 = suma1 + x * np.sin(np.sqrt(np.abs(x)))
        y = 418.9829*k - suma1
        if i == 0:
            lowest_records.append([y, i + 1])
        if lowest_records[len(lowest_records) - 1][0] > y:
            lowest_records.append([y, i + 1])
            lowest_coords = coords
    lowest_records_swapped = np.swapaxes(lowest_records, 0, 1)
    lowest_coords_concated = ''
    for i, coord in enumerate(lowest_coords):
        if i % 5 == 0 and i != 0:
            lowest_coords_concated = lowest_coords_concated + '\n'
        lowest_coords_concated = lowest_coords_concated + str(coord) + ', '
    plt.title(f'Schwefel in {k}D (maxFES = {k * 10000})\nBest solution: {lowest_records[len(lowest_records) - 1][0]}'
              f', in: \n{lowest_coords_concated}')
    plt.plot(lowest_records_swapped[1], lowest_records_swapped[0], drawstyle="steps-post")
    plt.show()

def dixonprice(k):
    x_list = []
    for i in range(k):
        x_list.append(np.linspace(-10, 10, 500))
    # # Vizualizace
    # x_mesh = (np.meshgrid(*x_list))
    # suma1 = 0
    # for i,x in enumerate(x_mesh):
    #     if i == 0:
    #         continue
    #     suma1 = suma1 + (i+1) * (2*(x**2) - x_mesh[i-1])**2
    # y = (x_mesh[0]-1)**2 + suma1
    # ax = plt.axes(projection='3d')
    # ax.plot_surface(x_mesh[0], x_mesh[1], y)
    # plt.show()
    lowest_records = []
    lowest_coords = []
    for i in range(k * 10000):
        coords = []
        suma1 = 0
        for x in x_list:
            coords.append(random.choice(x))
        for j, x in enumerate(coords):
            if j == 0:
                continue
            suma1 = suma1 + (j + 1) * (2 * (x ** 2) - coords[j - 1]) ** 2
        y = (coords[0]-1)**2 + suma1
        if i == 0:
            lowest_records.append([y, i + 1])
        if lowest_records[len(lowest_records) - 1][0] > y:
            lowest_records.append([y, i + 1])
            lowest_coords = coords
    lowest_records_swapped = np.swapaxes(lowest_records, 0, 1)
    lowest_coords_concated = ''
    for i, coord in enumerate(lowest_coords):
        if i % 5 == 0 and i != 0:
            lowest_coords_concated = lowest_coords_concated + '\n'
        lowest_coords_concated = lowest_coords_concated + str(coord) + ', '
    plt.title(f'Dixon-price in {k}D (maxFES = {k * 10000})\nBest solution: {lowest_records[len(lowest_records) - 1][0]}'
              f', in: \n{lowest_coords_concated}')
    plt.plot(lowest_records_swapped[1], lowest_records_swapped[0], drawstyle="steps-post")
    plt.show()

def rosenbrock(k):
    x_list = []
    for i in range(k):
        x_list.append(np.linspace(-10, 10, 500))
    # # Vizualizace
    # x_mesh = (np.meshgrid(*x_list))
    # suma1 = 0
    # for i,x in enumerate(x_mesh):
    #     if i == len(x_mesh)-1:
    #         continue
    #     suma1 = suma1 + (100*(x_mesh[i+1]-x**2)**2 + (x-1)**2)
    # y = suma1
    # ax = plt.axes(projection='3d')
    # ax.plot_surface(x_mesh[0], x_mesh[1], y)
    # plt.show()
    lowest_records = []
    lowest_coords = []
    for i in range(k * 10000):
        coords = []
        suma1 = 0
        for x in x_list:
            coords.append(random.choice(x))
        for j, x in enumerate(coords):
            if j == len(coords) - 1:
                continue
            suma1 = suma1 + (100 * (coords[j + 1] - x ** 2) ** 2 + (x - 1) ** 2)
        y = suma1
        if i == 0:
            lowest_records.append([y, i + 1])
        if lowest_records[len(lowest_records) - 1][0] > y:
            lowest_records.append([y, i + 1])
            lowest_coords = coords
    lowest_records_swapped = np.swapaxes(lowest_records, 0, 1)
    lowest_coords_concated = ''
    for i, coord in enumerate(lowest_coords):
        if i % 5 == 0 and i != 0:
            lowest_coords_concated = lowest_coords_concated + '\n'
        lowest_coords_concated = lowest_coords_concated + str(coord) + ', '
    plt.title(f'Rosenbrock in {k}D (maxFES = {k * 10000})\nBest solution: {lowest_records[len(lowest_records) - 1][0]}'
              f', in: \n{lowest_coords_concated}')
    plt.plot(lowest_records_swapped[1], lowest_records_swapped[0], drawstyle="steps-post")
    plt.show()

trid(5)
trid(10)
trid(20)
sphere(5)
sphere(10)
sphere(20)
schwefel(5)
schwefel(10)
schwefel(20)
dixonprice(5)
dixonprice(10)
dixonprice(20)
rosenbrock(5)
rosenbrock(10)
rosenbrock(20)