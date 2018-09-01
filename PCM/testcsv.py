import csv


f = open("ayushbansal323@gmail.com.csv")
reader = csv.reader(f)
for m_id,Sender,Subject,Date,Snippet,Message_body in reader:
	print(Date)
