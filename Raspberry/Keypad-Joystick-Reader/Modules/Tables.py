#import dependencies
from prettytable import PrettyTable
from .Utilities import frange

def createTable(functions: list, variables: list, start: list, stop: list, step: list):
	#initialize variables
	header = []
	rows = []

	equationsID = []
	equations = []
	substitutedEquations = []

	points = []
	results = []

	variablesRange = []

	tablePoints = 1 # set to be added and let range() continue one more time 

	#create table object
	table = PrettyTable()

	#assign variables values
	equationNumber = len(functions)
	variableNumber = len(variables)

	

	#prepare lists
	for variable in range(0, variableNumber):
		points.append([])

		#and get variables range
		varRange = (stop[variable] - start[variable]) / step[variable]
		variablesRange.append(int(varRange))

	#find the variable with the greatest range diference, as it will be the table number of rows (points)
	tablePoints += max(variablesRange)

	#prepare rows and substituted equations list(with tablePoints as reference)
	for row in range(0, tablePoints):
		rows.append([])
		substitutedEquations.append([])
		results.append([])
	


	#get the points that equations will be evaluated

	for i in range(0, variableNumber):
		try:
			for p in frange(start[i], stop[i], step[i]):
				points[i].append(p)
		
		#if there are no values for certain veriable, use the ones of the first variable
		except:
			for p in frange(start[0], stop[0], step[0]):
				points[i].append(p)


	#separe equationID and equation from functions  
	for function in functions:
		func = function.split("=")
		equationsID.append(func[0])
		equations.append(func[1])

	#substitute variables in equations for their real values
	for equation in range(0, equationNumber):
		for point in range(0, tablePoints):
			replacedEquation = equations[equation]
			for variable in range(0, variableNumber):
				replacedEquation = replacedEquation.replace(variables[variable], str(points[variable][point]))
			substitutedEquations[point].append(replacedEquation)

	#evaluate each equation in substitutedEquations and store the result in results
	for equation in range(0, equationNumber):
		for row in range(0, tablePoints):
			try:
				results[row].append(str(eval(substitutedEquations[row][equation])))

			#if theres any error store "ERROR"
			except:
				results[row].append("ERROR")
			
	#build rows list with results list and variables values(points list)
	for row in range(0, tablePoints):
		for i in range(0, (variableNumber + equationNumber)):
			if (i < variableNumber):
				rows[row].append(points[i][row])
			else:
				rows[row].append(results[row][(i - variableNumber)])


	#build table header
	for i in range(0, (variableNumber + equationNumber)):
		if (i < variableNumber):
			header.append(variables[i])
		else:
			header.append(equationsID[(i - variableNumber)])


	#set table header
	table.field_names = header

	#set table rows
	table.add_rows(rows)


	#return table in string format
	return table.get_string()