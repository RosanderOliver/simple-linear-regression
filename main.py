import sys

import subprocess

def file_len(fname):
	p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	res = p.communicate()
	if p.returncode != 0:
		raise IOError(err)
	res = str(res[0])
	rows = int(res.split(" ")[0])
	return rows


def main(argv):
	#Read file and append instances to instance list
	file = open(argv[0])
	rowsInFile = file_len(argv[0])
	
	nrOfAttributes = 0
	relation = ""
	dataCounter = 0

	for line in file:
		token = line.split(" ")
		if token[0] == "@attribute":
			nrOfAttributes = nrOfAttributes + 1
		elif token[0] == "@relation":
			relation = token[1]
		elif token[0].rstrip() == "@data":
			data = [[0 for x in range(nrOfAttributes)] for y in range (rowsInFile)]
		elif token[0] != "\n":
			token = token[0].split(",")
			data[dataCounter][0] = float(token[0])	
			data[dataCounter][1] = float(token[1])			
			dataCounter = dataCounter + 1

 
	xSum = 0
	ySum = 0
	
	for row in data:
		xSum += row[0]
		ySum += row[1]

	print "x sum: " + str(xSum)
	print "y sum: " + str(ySum)

	xMean = xSum / dataCounter
	yMean = ySum / dataCounter

	print "x mean: " + str(xMean)
	print "y mean: " + str(yMean)

	xxDeviation = 0
	yyDeviation = 0
	xyDeviation = 0
	for row in data:
		if row[0] != 0 and row[1] != 0:
			tempx = (row[0] - xMean)
			tempy = (row[1] - yMean)
			xyDeviation += tempx * tempy
			xxDeviation += tempx*tempx
			yyDeviation += tempy*tempy

	xyDeviation = xyDeviation / (dataCounter - 1)
	xxDeviation = xxDeviation / (dataCounter - 1)
	yyDeviation = yyDeviation / (dataCounter -1)

	
	b = xyDeviation/xxDeviation
	a = yMean - b*xMean
	
	corr = xyDeviation / ((yyDeviation*xxDeviation) ** 0.5)

	print "Y = " + str(a) + " + " + str(b) + "x"
	print "Correlation coefficent: " + str(corr)	



	return 0


if __name__ == "__main__":
	main(sys.argv[1:])
