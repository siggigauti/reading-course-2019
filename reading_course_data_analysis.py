import re
import csv
data = []
with open('data_2.csv', 'r') as f:
	data = f.readlines()

data1 = []
data = data[1:]
data = [x.split(',')[1:] for x in data]
participants = []
for i in data:
	data1.append([re.sub("\'|\"", "" , x) for x in i])
	#data1.append([x.replace(['"',"'"], "") for x in i])
	participants.append(re.sub("\'|\"", "" , i[0]))
data = data1
print(data[1])

data_1 = []
with open('data.csv', 'r') as csvfile:
	cvsreader = csv.reader(csvfile, delimiter=',')
	for row in cvsreader:
		data_1.append(row)

data_1_participants = []
data_1 = data_1[1:] # Remove the questions
#find participants
for q in data_1:
	if(any(item in q for item in participants)):
		data_1_participants.append(q)
print(data_1_participants)