
import calculate_trimer_coordinates
import csv

def input_variable():
	minRadius = float(input('Input the Min Radius: '))
	maxRadius = float(input('Input the Max Radius: '))
	interval = float(input('Input the interval: '))
	option = raw_input('Do you want to use default r = 52.0769942809? (y or n): ')

	if option == 'y':
		r = 52.0769942809
	else:
		r = float(input('Input the r: '))


	with open('relationship_between_R&number_of_trimers.csv', 'w') as csvfile:
	    fieldnames = ['Radius', 'number_of_trimers']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writeheader()
	    while (minRadius<=maxRadius):
			number_of_trimers = calculate_trimer_coordinates.algorithm(minRadius,r,False)
			print number_of_trimers
			writer.writerow({'Radius': minRadius, 'number_of_trimers': number_of_trimers})
			minRadius+=interval

if __name__ == '__main__':
	input_variable()