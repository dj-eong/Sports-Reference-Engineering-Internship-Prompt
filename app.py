import json

def convert_to_matrix(data):
	matrix = [['Tm']]
	i = 1
	for team in data:
		#fill out top row and left column with team
		matrix[0].append(team)
		matrix.append([team])
		
		#fill in team records
		for opp in data[team]:
			record = data[team][opp]
			if len(matrix[i]) == i:
				matrix[i].append(None)
			matrix[i].append(record['W'])
		i += 1
	return matrix

def print_matrix(matrix):
	for row in matrix:
		print(row)

# read json data and convert to dictionary/map
with open('file.json') as file:
	data = json.load(file)

	matrix = convert_to_matrix(data)
	print_matrix(matrix)