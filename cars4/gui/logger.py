import csv


class Logger:

	def __init__(self, outputFile, maze):
		self.maze = maze
		self.csvWriter = csv.writer(outputFile)

		self.stepCount = 0;



	# BaseMaze's __str__ outputs newlines which is a delimeter for csv, needs its own output formatter
	def formatMaze(self, maze):
		temp=""
		for b in maze.maze.maze:
	    		temp=temp+((str)(b))+";"
		return temp   
	

	def log(self, move):
		self.stepCount += 1
		print(self.stepCount, move)
		self.csvWriter.writerow([self.formatMaze(self.maze), str(move)])

