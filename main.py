import numpy as np
import matplotlib.pyplot as plt


def sphere(k):
    X = []
    for i in range(k):
        X.append(np.linspace(-5.12,5.12,10000))
    x1,x2 = np.meshgrid(X[0],X[1])
    suma = 0
    for x in X:
        suma = suma + x**2
    y = suma
    ax = plt.axes(projection='3d')
    ax.plot3D(x1,x2,y)
    plt.show()
    print(y)



sphere(2)