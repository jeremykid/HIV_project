# Anbor

Anbor is an open source, python based code and HIV-trimers' plot and caculate tool to help biology researcher to plot the HIV cell with different radius.

## Setup requirement of environment of Anbor
The matplotlib and 


## How to use the Anbor?
There is two parts of Anbor.

1. Use Anbor to caculate the trimers' coordinates in that format

0 0 632.1911456 1
52.0328031384 0 630.046214156 2
-26.0164015692 45.0617293479 630.046214156 3
...

Means
X axis | Y axis | Z axis | Index (Trace the roots)
--- | --- | --- | ---
0 | 0 | 632.1911456 | 1
52.0328031384 | 0 | 630.046214156 | 2

2. Use Anbor to plot the trimer-center by matplotlib

```command line
python caculate_trimer_coordinates.py 
Type the R: 632.1911456      
There are 1067 points.
There are 12 T_points.
1 - show and save the lines plot
2 - show and save the points model
3 - quit
```

3. Use Anbor to plot the trimer by PyMOL api
```command line
python pymol_plot_trimer.py 
The default filename is points.
Input file name:
your_input_file_name
Eg: R.pdb or R.pse
Input output file name:
your_output_file_name
```

4. Use Anbor to find the relationship between the radius and the number of trimers
```
Input the Min Radius: <<Your minimum Radius>>
Input the Max Radius: <<Your maximum Radius>>
Input the interval: <<Your step>>
Do you want to use default r = 52.0769942809? (y or n): n
Input the r: <<Your distance between two trimers>>
```
You will find the results in relationship_between_R&number_of_trimers.csv