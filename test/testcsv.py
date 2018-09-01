import csv


f = open("CSV_NAME.csv")
reader = csv.reader(f)
for Sender,Subject,Date,Snippet,Message_body in reader:
	print(Date)
