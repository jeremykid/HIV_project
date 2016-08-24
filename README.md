# Anbor

Anbor is an open source, python based code and HIV-trimers' plot and caculate tool to help biology researcher to plot the HIV cell with different radius.

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
