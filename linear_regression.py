import sys
import numpy as np
from pathlib import Path


def file_len(fc):
	rows_in_file = 0
	for line in fc:
		token = line.split(' ')
		if token[0] != '@attribute' and token[0] != '@relation' and token[0].rstrip() != '@data':
			rows_in_file = rows_in_file + 1
	return rows_in_file


def main(argv):
	# Read file and append instances to instance list
	fc = Path(argv[0]).read_text()
	fc = [row for row in ''.join(fc).split('\n') if row != '']
	rows_in_file = file_len(fc)
	
	nr_of_attributes = 0
	data_counter = 0
	relation = ''

	for line in fc:
		token = line.split(' ')
		if token[0] == "@attribute":
			nr_of_attributes = nr_of_attributes + 1
		elif token[0] == "@relation":
			relation = token[1]
		elif token[0].rstrip() == "@data":
			data = [[0 for x in range(nr_of_attributes)] for y in range(rows_in_file)] # TODO: Change to numpy
			data = [np.zeros(nr_of_attributes) for _ in range(rows_in_file)] # TODO: Change to numpy
		else:
			token = token[0].split(",")
			data[data_counter][0] = float(token[0])
			data[data_counter][1] = float(token[1])
			data_counter += 1

	x_sum = y_sum = 0
	for row in data:
		x_sum += row[0]
		y_sum += row[1]

	print(f'x sum: {x_sum}')
	print(f'y sum: {y_sum}')

	x_mean = x_sum / data_counter
	y_mean = y_sum / data_counter

	print(f'x mean: {x_mean}')
	print(f'y mean: {y_mean}')

	xx_deviation = yy_deviation = xy_deviation = 0
	for row in data:
		if row[0] != 0 and row[1] != 0:
			x_deviation = (row[0] - x_mean)
			y_deviation = (row[1] - y_mean)
			xy_deviation += x_deviation * y_deviation
			xx_deviation += x_deviation * x_deviation
			yy_deviation += y_deviation * y_deviation

	xy_deviation = xy_deviation / (data_counter - 1)
	xx_deviation = xx_deviation / (data_counter - 1)
	yy_deviation = yy_deviation / (data_counter - 1)

	b = xy_deviation / xx_deviation
	a = y_mean - b * x_mean
	
	correlation = xy_deviation / ((yy_deviation * xx_deviation) ** 0.5)

	print(f'Y = {str(a)} + {str(b)}x')
	print(f'Correlation coefficient: {correlation}')

	return 0


if __name__ == "__main__":
	main(sys.argv[1:])
