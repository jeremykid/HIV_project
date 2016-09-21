from HIV_point import Point
from calculate_trimer_coordinates import distance,rotate120,rotate240
import math

import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

global R_radius

def rotate(degree, point_x, point_y):
    radians = math.radians(degree)
    x = point_x.x - point_y.x
    y = point_x.y - point_y.y
    temp_x = x*math.cos(radians) - y*math.sin(radians)
    temp_y = x*math.sin(radians) + y*math.cos(radians)
    return Point(temp_x+point_y.x,temp_y+point_y.y,point_y.z)

def plot():
    f = open("points","r")
    content = f.read().splitlines()
    point_1_list = content[0].split()
    Point_1 = Point(float(point_1_list[0]),float(point_1_list[1]),float(point_1_list[2]),int(point_1_list[3]))
    Point_1.setFather(1)
    Point_1.editIndex(1)
    old_point_2_list = content[1].split()
    old_Point_2 = Point(float(old_point_2_list[0]),float(old_point_2_list[1]),float(old_point_2_list[2]),int(old_point_2_list[3]))
    global R_radius
    R_radius =  Point_1.z
    d_radius =  distance(old_Point_2,Point_1)
    Point_2 = Point(d_radius,0,R_radius,2)
    Point_3 = rotate120(Point_2,Point_1)
    Point_4 = rotate240(Point_2,Point_1)
    Point_2.setFather(1)
    Point_3.setFather(1)
    Point_4.setFather(1)
    Point_2.editIndex(2)
    Point_3.editIndex(3)
    Point_4.editIndex(4)


    index_list = []
    for i in content:
        index_list.append(int(i.split()[3]))
       
    dict_points = {
            1:Point_1,
            2:Point_2,
            3:Point_3,
            4:Point_4,
            }

    for i in dict_points.keys():
        index_list.remove(i)

    index_list.reverse()
    while index_list:
        temp = index_list.pop()  # 1,2,5,6
        if temp%2:
            temp_father = (temp-1)/2
            temp_grandfather = dict_points[temp_father].getFather()
            dict_points[temp] = rotate(120,dict_points[temp_grandfather],dict_points[temp_father])
            
        else:
            temp_father = (temp-2)/2
            temp_grandfather = dict_points[temp_father].getFather()
            dict_points[temp] = rotate(240,dict_points[temp_grandfather],dict_points[temp_father])

        dict_points[temp].setFather(temp_father)
        dict_points[temp].editIndex(temp)
        # global R_radius
        dict_points[temp].z = R_radius


    T_x_points_array = []
    T_y_points_array = []
    w = open("points_2D","w")
    for i in sorted(dict_points.keys()):
        w.write(str(dict_points[i]))
        w.write("\n")
        temp_father = dict_points[i].getFather()
        T_x_points_array.append(dict_points[temp_father])
        T_y_points_array.append(dict_points[i])
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # linesPlot.drawLines(T_x_points_array,T_y_points_array)

    for i in range(len(T_y_points_array)):
        ax.plot([T_x_points_array[i].x,T_y_points_array[i].x],\
                [T_x_points_array[i].y,T_y_points_array[i].y],\
                zs = [T_x_points_array[i].z,T_y_points_array[i].z],\
                c = "b")
    plt.savefig('lines_plot_2D.png')
    plt.show()
    # print 'stop'
        # print (index_list)



if __name__ == '__main__':
    plot()