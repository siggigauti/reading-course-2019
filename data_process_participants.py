import csv

data = []

with open('data.csv', 'r') as csvfile:
	cvsreader = csv.reader(csvfile, delimiter=',')
	for row in cvsreader:
		data.append(row)

data = data[1:] # Remove the questions
data_answers = [] # Only answers
users = []
for item in data:
	users.append(item[1])
	data_answers.append(item[1:])

data_answers = [x for x in data_answers if x[4]] #Remove responses with no ECTS info
data_answers = [x for x in data_answers if int(x[4]) >= 60] # Only those with 60 or more credits completed
data_answers = [x for x in data_answers if x[10] == 'Yes'] # Remove those with no knowledge of UML
print(len(data_answers))
data_professionals = [x for x in data_answers if x[5] == 'Yes']
data_no_professionals = [x for x in data_answers if x[5] == 'No']
data_confident_above8_uml_read = [x for x in data_answers if int(x[11]) >= 8]
data_confident_below8_uml_read = [x for x in data_answers if int(x[11]) < 8]
data_confident_above7_uml_write = [x for x in data_answers if int(x[12]) >= 7]
data_confident_below7_uml_write = [x for x in data_answers if int(x[12]) < 7]


data_confident_read_write = [x for x in data_confident_above8_uml_read if int(x[12]) >= 7]
data_not_confident_read_write = [x for x in data_confident_below8_uml_read if int(x[12]) <7]
print(len(data_confident_read_write)) # Canditates
print(len(data_not_confident_read_write)) # Candidates

print("Candidates for 'expert' group, must select 4-5")
for item in data_confident_read_write:
	print(item[0])

print("Candidates for 'amateur' group, must select 4-5")
for item in data_not_confident_read_write:
	print(item[0])
