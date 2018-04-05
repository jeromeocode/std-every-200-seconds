# std-every-200-seconds

This is used to calculate sample standard deviation in 200s intervals in the csv file. With this you can view how the stdev changes over time instead of calculating total deviation.

## How to use it

- Take this python file and place it in the same folder as the CSV file you are calcualting the stdev from.
- Change the code to replace the file varible to the filename of your choice.

```python
#change the filename to a chosen file and make sure that file is in the same folder as this python program
file='LT30minThermal.csv'
```

- It will then output the the time interval and the stdev of the data in that time interval