import csv
from Projectcentricmail.PCM.caller import gmail_read


f = open("../PCM/1998shrikantgadekar@gmail.com.csv")
reader = csv.reader(f)
for m_id,Sender,Subject,Date,Snippet,Message_body in reader:
	print(Date)
