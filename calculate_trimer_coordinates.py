import math
import pointsPlot
import linesPlot
import time
from HIV_point import Point

global T_points_file 
T_points_file = open("T_points","w")
global T_y_points_array
T_y_points_array = []
global T_points_count
T_points_count = 0
global T_x_points_array
T_x_points_array = []

def distance(point_x, point_y): 
	'''
	To caculate the distance between point_x and point_y
	'''

	x2 = (point_x.x-point_y.x)**2
	y2 = (point_x.y-point_y.y)**2
	z2 = (point_x.z-point_y.z)**2

	return math.sqrt(x2+y2+z2)

def unit(point_z):
	'''
	To caculate the unit vector of point_z
	'''
	# print (point_z)
	magnitude = math.sqrt(point_z.x**2 + point_z.y**2 + point_z.z**2)
	if magnitude:
		point_z.x = point_z.x/magnitude
		point_z.y = point_z.y/magnitude
		point_z.z = point_z.z/magnitude
		return point_z,magnitude
	else:
		return point_z,magnitude

def rotate120(point_x, point_y):
	'''
	point_x rotate about point_y
	'''
	sin120 =  math.sqrt(3)/2
	cos120 = -0.5
	pointz = Point(point_y.x, point_y.y, point_y.z)
	newpoint,magnitude = unit(pointz)
	
	x = (cos120+newpoint.x**2*(1-cos120)) * point_x.x +\
		(newpoint.x*newpoint.y*(1-cos120) - newpoint.z*sin120) * point_x.y +\
		(newpoint.x*newpoint.z*(1-cos120) + newpoint.y*sin120) * point_x.z

	y = (newpoint.y*newpoint.x*(1-cos120) + newpoint.z*sin120) * point_x.x +\
		(cos120 + newpoint.y**2*(1-cos120)) * point_x.y +\
		(newpoint.y*newpoint.z*(1-cos120) - newpoint.x*sin120) * point_x.z

	z = (newpoint.z*newpoint.x*(1-cos120) - newpoint.y*sin120) * point_x.x +\
		(newpoint.z*newpoint.y*(1-cos120) + newpoint.x*sin120) * point_x.y +\
		(cos120 + newpoint.z**2*(1-cos120))*point_x.z

	result_point = Point(x,y,z)

	return result_point

def rotate240(point_x,point_y):
	'''
	point_x rotate about point_y 240 degree
	'''
	sin240 =  -math.sqrt(3)/2
	cos240 = -0.5
	pointz = Point(point_y.x, point_y.y, point_y.z)
	newpoint,magnitude = unit(pointz)
	
	x = (cos240+newpoint.x**2*(1-cos240)) * point_x.x +\
		(newpoint.x*newpoint.y*(1-cos240) - newpoint.z*sin240) * point_x.y +\
		(newpoint.x*newpoint.z*(1-cos240) + newpoint.y*sin240) * point_x.z

	y = (newpoint.y*newpoint.x*(1-cos240) + newpoint.z*sin240) * point_x.x +\
		(cos240 + newpoint.y**2*(1-cos240)) * point_x.y +\
		(newpoint.y*newpoint.z*(1-cos240) - newpoint.x*sin240) * point_x.z

	z = (newpoint.z*newpoint.x*(1-cos240) - newpoint.y*sin240) * point_x.x +\
		(newpoint.z*newpoint.y*(1-cos240) + newpoint.x*sin240) * point_x.y +\
		(cos240 + newpoint.z**2*(1-cos240))*point_x.z

	result_point = Point(x,y,z)
	return result_point

def get_root_index(index):
	'''
	According to algorithm, the index x is the root of branch 2x+1 and 2x+2
	'''
	if index == 2:
		return 1
	elif index%2:
		return (index-1)/2
	else:
		return (index-2)/2

def check_distance(r,point_x,point_y,check_T_points=0):
	'''
	return the distance between point_x and point_y
	'''
	distance = math.sqrt((point_x.x-point_y.x)**2+(point_x.y-point_y.y)**2+(point_x.z-point_y.z)**2)
	#print (distance)# 52.076992648 52.0769926525
	if distance >= (r-0.001):
		if check_T_points:
			if distance < 52.1 and (point_y.index-1)//2 != point_x.index:
				global T_points_file
				T_points_file.write(str(point_y)+"\n")
				T_points_file.write(str(point_x)+"\n")
				global T_y_points_array
				T_y_points_array.append(point_y)
				global T_x_points_array
				T_x_points_array.append(point_x)
				global T_points_count
				T_points_count += 1
		else:
			return True
	else:
		return False

def check_overlap(r,point_x,point_y):
	'''
	Check the distance between two center of trimer is less than the r prime. r prime = 71.4
	'''
	distance = math.sqrt((point_x.x-point_y.x)**2+(point_x.y-point_y.y)**2+(point_x.z-point_y.z)**2)
	if distance <= 71.4:
		return 1
	else:
		return 0

def check_everydistance(r,point_x,K_keepers):
	'''
	check the distances between each points in K_keepers and point_x
	'''
	for i in K_keepers:
		if not check_distance(r,i,point_x):
			return False
	for i in K_keepers:
		check_distance(r,i, point_x, check_T_points=1)
	count = 0
	for i in K_keepers:
		count += check_overlap(r,i, point_x)
	if count != 1:
		return False
	return True

def algorithm(R, r, writeInFile=True):
	# The IO for researcher to input the R
	# r = 52.0769942809

	cosphi = (2*R**2-r**2)/(2*R**2)
	sinphi = math.sqrt(1-cosphi**2)

	K_dict = {}
	K_dict[1] = Point(0,0,R,1)
	K_dict[2] = Point(sinphi*R,0,cosphi*R)
	K_dict[2].editIndex(2)
	K_dict[3] = rotate120(K_dict[2], K_dict[1])
	K_dict[3].editIndex(3)
	K_dict[4] = rotate240(K_dict[2], K_dict[1])
	K_dict[4].editIndex(4)

	K_queue = [2,3,4]
	K_keepers = [K_dict[1],K_dict[2],K_dict[3],K_dict[4]]
	K_index = 5
	K_count = 4

	# open the file to write, w is write the points' coordinations
	if writeInFile:
		w = open("points","w")
		w_plot = open("lines","w")

	# To write the first 4 points' coordination the file "points",
		for i in K_keepers:
			w.write(str(i))
			w.write("\n")

	# To write the first 3 lines 2 ends' points coordinations in the file "lines"
		w_plot.write(str(K_keepers[0])+" "+str(K_keepers[1])+"\n")
		w_plot.write(str(K_keepers[0])+" "+str(K_keepers[2])+"\n")
		w_plot.write(str(K_keepers[0])+" "+str(K_keepers[3])+"\n")

	# Repeat the step which finds the coordinations 
	# according to the points in the K_queue
	# and push the new points in the K_queue
	# Until we use all the points in the K_queue
	while len(K_queue) != 0:
		father = K_queue.pop(0)
		grandfather = get_root_index(father)

		if K_dict.has_key(father):
			new_point = rotate120(K_dict[grandfather],K_dict[father])
			K_index = father*2+1
			new_point.editIndex(K_index)
			if check_everydistance(r,new_point,K_keepers):
				K_keepers.append(new_point)
				K_dict[K_index] = new_point
				K_queue.append(K_index)
				K_count += 1
				if writeInFile:
					w.write(str(new_point)+"\n")
					w_plot.write(str(new_point)+" "+str(K_dict[father])+"\n")
			K_index = father*2+2
			new_point = rotate240(K_dict[grandfather],K_dict[father])
			new_point.editIndex(K_index)
			if check_everydistance(r,new_point,K_keepers):
				K_keepers.append(new_point)
				K_dict[K_index] = new_point
				K_queue.append(K_index)
				K_count += 1
				if writeInFile:
					w.write(str(new_point)+"\n")
					w_plot.write(str(new_point)+" "+str(K_dict[father])+"\n")


	if writeInFile:
		print "There are "+str(K_count)+" points."
		print "There are "+str(T_points_count)+" T_points."
		w_plot.close
		w.close
	return K_count

def plot():
	# Ask researcher for showing the model and save the png file.
	print "1 - show and save the lines plot"
	print "2 - show and save the points model"
	print "3 - quit"
	option = int(input("Input your choice: "))
	while option < 3:
		global T_x_points_array
		global T_y_points_array
		if option == 2:

			T_x_points_array.extend(T_y_points_array)

			print (T_x_points_array)
			pointsPlot.drawPoints(T_x_points_array)
		else:

			linesPlot.drawLines(T_x_points_array,T_y_points_array)
		option = int(input("Input your choice: "))

	return 0

def input_radius():
	R = float(input('Input the R: '))
	option = raw_input('Do you want to use default r = 52.0769942809? (y or n): ')
	if option == 'y':
		r = 52.0769942809
	else:
		r = float(input('Input the r: '))

	return R,r

if __name__ == '__main__':
	R, r = input_radius()
	algorithm(R,r)
	plot()
		
