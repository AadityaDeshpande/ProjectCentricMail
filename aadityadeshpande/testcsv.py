import csv


f = open("1998shrikantgadekar@gmail.com.csv")
reader = csv.reader(f)
for m_id,Sender,Subject,Date,Snippet,Message_body in reader:
	#print("title: ",Subject)
	print("BODY:",Message_body)
	
