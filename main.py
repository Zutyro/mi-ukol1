import numpy as np
import matplotlib.pyplot as plt
import random


def sphere(k):
    x_list = []
    for i in range(k):
        x_list.append(np.linspace(-5.12, 5.12, 500))
    # x_mesh = (np.meshgrid(*x_list))
    # suma = 0
    # for x in x_mesh:
    #     suma = suma + (x ** 2)
    # y = suma
    # 3D plotting for visualization
    # ax = plt.axes(projection='3d')
    # ax.plot_surface(x_mesh[0], x_mesh[1], y)
    # plt.show()
    lowest_records = [[100, 0]]
    lowest_coords = []
    for i in range(k*10000):
        coords = []
        suma = 0
        for x in x_list:
            coords.append(random.choice(x))
        for x in coords:
            suma = suma + (x ** 2)
        y = suma
        if lowest_records[len(lowest_records)-1][0] > y:
            lowest_records.append([y,i+1])
            lowest_coords = coords
    lowest_records_swapped = np.swapaxes(lowest_records,0,1)
    plt.title(f'Sphere in {k}D (maxFES = {k*10000})\nBest solution: {lowest_records[len(lowest_records)-1][0]}, in: \n{[float(i) for i in lowest_coords]}')
    plt.plot(lowest_records_swapped[1],lowest_records_swapped[0],drawstyle="steps-post")
    plt.show()


sphere(20)