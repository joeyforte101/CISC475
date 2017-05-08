import math
import collections
import sys
import csv

def format():
	data_file = sys.argv[1]
	data = list(csv.reader(open(data_file)))
	flip_date = ""
	new_data = []
	for entry in data:
		flip_date = entry[1][5:] + "-" + entry[1][2:4] + "-" + entry[1][0] + " "
		if(len(entry[2]) == 1):
			flip_date = flip_date + "0" + entry[2] + ":"
		else:
			flip_date = flip_date + entry[2] + ":"
		if(len(entry[3]) == 1):
			flip_date = flip_date + "0" + entry[3] + ":"
		else:
			flip_date = flip_date + entry[3] + ":"
		if(len(entry[4]) == 1):
			flip_date = flip_date + "0" + entry[4]
		else:
			flip_date = flip_date + entry[4] 
		new_entry = []
		new_entry.append(entry[0])
		new_entry.append(flip_date)
		new_entry.append(entry[5])
		new_entry.append(entry[6])
		new_entry.append(entry[7])
		new_entry.append(entry[8])
		new_entry.append(entry[9])
		new_entry.append(entry[10][:-1])
		new_data.append(new_entry)
	with open("data.csv","wb") as f:
		writer = csv.writer(f)
		writer.writerows(new_data)

format()