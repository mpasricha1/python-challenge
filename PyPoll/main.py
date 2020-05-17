import csv 
import os 

csv_path = os.path.join('Resources', 'election_data.csv')

def printToScreen(candidateList, totalVotes, winner):
	print('')
	print('---')
	print('Election Results')
	print('---------------------')
	print('Total Votes: ' + str(totalVotes))
	print('---------------------')
	for i in candidateList:
		print(i['name'] + ': ' + str(i['Percentage']) + '% ' + str(i['voteCount']))
	print('---------------------')
	print('Winner: ' + str(winner))
	print('---------------------')
	print('---')

def printToFile(printList):
	output_file = os.path.join('Resources', 'Election_output.csv')
	with open(output_file,'w', newline='') as dataFile:
		writer = csv.writer(dataFile)
		writer.writerow(['Name', 'Vote Count', 'Percentage'])
		for i in printList:
			wName = i['name']
			wVotes = i['voteCount']
			wPcent = i['Percentage']
			wList = [wName, wVotes,wPcent]
			writer.writerow(wList)

def findTotalVote(candidateList):
	tVotes  = 0
	for i in candidateList:
		tVotes += i['voteCount']
	return tVotes

def findWinner(candidateList):
	winnerTotal = candidateList[0]['voteCount']
	winnerName = candidateList[0]['name']
	for i in candidateList:
		if i['voteCount'] > winnerTotal:
			winnerTotal = i['voteCount']
			winnerName = i['name']
	return winnerName

def findPercentageOfVote(candidateList,totalVotes):
	for i in candidateList: 
		pVote = (i['voteCount'] / totalVotes) * 100
		i["Percentage"] = int(pVote)
	return candidateList
	
def parseFile(csv_path):
	cList = []
	with open(csv_path) as csvFile:
			csvReader = csv.reader(csvFile, delimiter=',')
			next(csvReader,None)
			for row in csvReader: 
				candidateFound = False
				if len(cList) == 0:
					candidate = {'name': row[2], 'voteCount': 1}
					cList.append(candidate)
				for i in cList:
					if row[2] == i['name']:
						i['voteCount'] += 1 
						candidateFound = True
						break		
				if candidateFound == False:
					candidate = {'name': row[2], 'voteCount': 1}
					cList.append(candidate)
	return cList


candidateList = parseFile(csv_path)	
totalVotes = findTotalVote(candidateList)
candidateList = findPercentageOfVote(candidateList,totalVotes)
winner = findWinner(candidateList)
printToScreen(candidateList, totalVotes, winner)
printToFile(candidateList)
		

