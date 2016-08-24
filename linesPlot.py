
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def drawLines(T_x_points_array,T_y_points_array):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    with open("lines") as f:
        content = f.read().splitlines()
        count = 0
        for i in content:
            line_list = i.split(' ')
            count += 1

            try:
                ax.plot([float(line_list[0]), float(line_list[4])],\
                    [float(line_list[1]),float(line_list[5])],\
                    zs=[float(line_list[2]),float(line_list[6])],\
                    c = "r")
            except:
                print count

    for i in range(len(T_y_points_array)):
        ax.plot([T_x_points_array[i].x,T_y_points_array[i].x],\
                [T_x_points_array[i].y,T_y_points_array[i].y],\
                zs = [T_x_points_array[i].z,T_y_points_array[i].z],\
                c = "b")
    plt.savefig('lines.png')
    plt.show()
