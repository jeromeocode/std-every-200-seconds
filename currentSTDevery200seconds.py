import os
import csv
import statistics
import pdb
from numpy import genfromtxt

array1=[]

#change the filename to a chosen file and make sure that file is in the same folder as this python program
file='LT30minThermal.csv'

with open(file) as csvfile:
				#changed the format of csv so that they have a header (change skip_header to 0 if there are no headers)
				dataReader = genfromtxt(file, delimiter=',', skip_header=1)

				for row in dataReader:
					array1.append(row[1])

					#row[1] contains the current data
					if round(row[0])%200 == 0 and len(array1) > 10:

						#prints the last time point in the array with the stdev beside it
						print(row[0], statistics.stdev(array1))
						
						array1=[]