from datetime import datetime
import logging 
import csv 
import os


printList = []
csv_path = os.path.join('Resources','budget_data.csv')
logging.basicConfig(filename=('Error_log_' + datetime.now().strftime('%Y-%d-%m') + '.txt'),level=logging.INFO)

def printToScreen(printList):
	print('')
	print('---')
	print('Financial Analysis')
	print('-----------------------------')
	print('Total Months: ' + str(printList[0]))
	print('Total Net Profit/Loss:' + str(printList[1]))
	print('Average Change: ' + str(printList[2]))
	print('Greatest Increase in Profit: ' + str(printList[3]) + ' ' + str(printList[4]))
	print('Greatest Descrease In Losses: ' + str(printList[5]) + ' ' + str(printList[6]))

def printToFile(printList):
	output_file = os.path.join('analysis', 'budget_output.txt')
	with open(output_file,'w', newline= '') as dataFile:
		writer = csv.writer(dataFile)
		writer.writerow(['Total Months', 'Profit/Loss', 'Average Change', 'Greatest Increase Date', 'Greatest Increase', 'Greatest Descrease Date', 'Greatest Decrease'])
		writer.writerow(printList)

def printError():
	print('')
	print('No Data In File')
	cont = input('Reload file press (y)es to continue: ').lower()
	if(cont == 'y' or cont == 'yes'):
		validateAndExecute()

def parseFile(csv_path):
	totalMonths = 0
	netProLoss = 0
	avrProLoss = 0
	greatestIncrease = 0
	greatestDecrease = 0
	increaseDate = '' 
	decreaseDate = '' 
	with open(csv_path) as csvFile:
		csvReader = csv.reader(csvFile, delimiter=',')
		next(csvReader,None)
		for row in csvReader: 
			totalMonths += 1 
			netProLoss += int(row[1])
			avrProLoss = netProLoss/totalMonths
			if int(row[1]) > int(greatestIncrease):
				increaseDate = row[0]
				greatestIncrease = row[1]
			if int(row[1]) < int(greatestDecrease):
				decreaseDate = row[0] 
				greatestDecrease = row[1]
		printList.extend([totalMonths,netProLoss,avrProLoss,increaseDate,greatestIncrease,decreaseDate,greatestDecrease])
	return printList

def validateAndExecute():
	try:	 
		printList = parseFile(csv_path)
	except Exception as e:
			print('No Data in File')
			logging.error(datetime.now().strftime("%Y-%m-%d-%d-%H:%M:%S") + ' :: No Data In File')
			printError()
	else:
		printToScreen(printList)
		printToFile(printList)

validateAndExecute()