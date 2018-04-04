import os
import csv
import statistics
import pdb
from numpy import genfromtxt

array1=[]

file='LT30minThermal.csv'
with open(file) as csvfile:
				#changed the format of csv so that they have a header
				dataReader = genfromtxt(file, delimiter=',', skip_header=1)
				for row in dataReader:
					array1.append(row[1])
					#row[1] contains the current data
					if round(row[0])%200 == 0 and len(array1) > 10:
						print(row[0], statistics.stdev(array1))
						array1=[]
