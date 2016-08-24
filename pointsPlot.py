from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def drawPoints(T_points_array):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    index_array = []
    for i in T_points_array:
        index_array.append(i.index)

    f = open("out","r")
    content = f.read().splitlines()
    x = []
    y = []
    z = []
    T_x = []
    T_y = []
    T_z = []

    for i in content:
        point_list = i.split()
        try:
            if int(point_list[3]) not in index_array:

                x.append(float(point_list[0]))
                y.append(float(point_list[1]))
                z.append(float(point_list[2]))
        except:
            print i
    ax.scatter(x, y, z, c='r', marker='o')

    for i in T_points_array:
        T_x.append(i.x)
        T_y.append(i.y)
        T_z.append(i.z)

    ax.scatter(T_x, T_y, T_z, c='b', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.savefig('points.png')
    plt.show()
