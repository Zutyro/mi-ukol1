import numpy as np
import matplotlib.pyplot as plt
import random


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
    print(lowest_coords_concated)
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

# trid(20)
# sphere(5)