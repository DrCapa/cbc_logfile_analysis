# Cbc logfile analysis
Given is a short analysis and plot function for Cbc logfiles. The script works for the standard logfile format of the Cbc solver version 2.9.7. 

The project includes
* analysis_cbc_logfile.py: contains the analysis function,
* input folder: with some logfiles to test,
* example.py: an example how to use the function.

Currently there are two parts:

1. You will get a summary for all logfiles in the input folder. Of course it is posibile to extend or modify the selected kpi. Finally you will get an overview of your kpi to compare the results of the logfiles. You can set the optional argument **`summary=False`** if you don't need a summary.
2. Additional it is possible to plot the convergence behavior of every logfile since the number of founded solutions is greater than one. You can activate this feature by setting the optional argument **`plot=True`**.

The function generates an output folder for the summary excel file and a subfolder for the plots