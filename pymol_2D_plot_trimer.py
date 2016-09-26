import pymol
from pymol import cmd 
from HIV_point import Point
import os
from calculate_trimer_coordinates import distance

pymol.finish_launching()

def main():
    print 'The default filename is points_2D.'
    fileName = raw_input('Input file name:')
    inputFile = open(fileName,'r')
    inputFileList = inputFile.read().splitlines()
    pointMap = {}
    for i in inputFileList:
        tempList = i.split()
        pointMap[int(tempList[3])] = Point(float(tempList[0]),float(tempList[1]),float(tempList[2]),int(tempList[3]))
    Radius = float(inputFileList[0].split()[2])
    # print (pointMap.keys())
    r = distance(pointMap[1],pointMap[2])

    print 'Eg: R.pdb or R.pse'
    outPutFile = raw_input('Input output file name:')

    # cmd.pseudoatom('center')

    # cmd.set('surface_mode', 1)
    # cmd.translate([0,0,0], 'center', camera=1)
    # cmd.ramp_new('test', 'center', [640, 646, 647], ['black', 'forest', 'green'])
    # cmd.set('surface_color', 'test', 't*')

    #Plot the first 4 trimer-center's coordinates.
    cmd.load('t1.pdb')
    cmd.create('t0', 't1')
    #first trimerIndex
    cmd.select('/t1/PSDO')
    # cmd.color('blue','t1')
    cmd.show('line', 't1')
    cmd.rotate ('z', -30, 't1', camera=1)
    cmd.translate([0,0,Radius],'t1',camera=1)
    my_dict = {'L':[]}
    cmd.iterate_state(1, '/'+tempTName+'/PSDO', 'L.append( (x,y,z) )', space=my_dict)
    cmd.translate([pointMap[i].x-my_dict['L'][0][0],pointMap[i].y-my_dict['L'][0][1],pointMap[i].z-my_dict['L'][0][2]],tempTName,camera=1)
    

    #second trimerIndex
    cmd.create('t2', 't1')
    # cmd.color('red', 't2')
    cmd.select('/t2/PSDO')
    # cmd.color('yellow', 't2')
    cmd.show('line', 't2')
    cmd.translate([r, 0, 0], 't2', camera=1)
    cmd.orient('t2')
    cmd.rotate('z', 60, 't2', camera=1)
    cmd.rotate('z', -30 )
    # this angle changes to bring involved pseudo atoms to horizontal positions
    # cmd.rotate('y', 4.726, 't2', camera=1)
    # cmd.rotate('x', 0.004, 't2', camera=1)
    # because we are rotating only one trimer, the 2 central pseudo atoms will not align. correction commands are:
    # cmd.translate([0, -0.0440605685747639, -2.14176156973178], 't2', camera=1)
    # cmd.alter('/t2//A', chain='D')
    # cmd.alter('/t2//B', chain='E')
    # cmd.alter('/t2//C', chain='F')

    # third trimerIndex
    cmd.create('t3','t2')
    cmd.select('/t3/PSDO')
    cmd.show('line','t3')
    cmd.origin('t1')
    cmd.rotate(pointMap[1].getCoordinate(),120,'t3',camera=1)

    # forth trimerIndex
    cmd.create('t4','t2')
    cmd.select('/t4/PSDO')
    cmd.show('line','t4')
    cmd.origin('t1')
    cmd.rotate(pointMap[1].getCoordinate(),240,'t4',camera=1)

    # According to the first 4 trimer-center coordinates, to plot the following trimers.
    keyList = pointMap.keys()
    keyList.sort()
    testCount = 1
    for i in keyList:
        if (i>4 and i <20):
            # testCount += 1
            tempTName = 't'+str(i)
            if (i%2)==1:
                tempTFatherName = 't'+str((i-1)/2)
                tempDegree = 120
            else:
                tempTFatherName = 't'+str((i-2)/2)
                tempDegree = 240
            tempTGrandFatherIndex = ((i-1)//2-1)//2
            if tempTGrandFatherIndex == 0:
                tempTGrandFatherIndex = 1
            tempTGrandFatherName = 't'+str(tempTGrandFatherIndex)
            cmd.create(tempTName,tempTGrandFatherName)
            cmd.select('/'+tempTName+'/PSDO')
            cmd.show('line',tempTName)
            cmd.origin(tempTFatherName)
            cmd.rotate(pointMap[(i-1)//2].getCoordinate(),tempDegree,tempTName,camera=1)
            my_dict = {'L':[]}
            cmd.iterate_state(1, '/'+tempTName+'/PSDO', 'L.append( (x,y,z) )', space=my_dict)
            cmd.translate([pointMap[i].x-my_dict['L'][0][0],pointMap[i].y-my_dict['L'][0][1],pointMap[i].z-my_dict['L'][0][2]],tempTName,camera=1)
            
    cmd.save(outPutFile)
main()