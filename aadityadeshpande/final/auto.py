import csv
import re

def is_spam(mail):	
	'''
	for j in range(0,len(mail)):
	 for i in mail:	  
	  mail[j] = i.strip('\n')
	  mail[j] = i.strip('\t')
	  mail[j] = i.strip()  	  
	  mail[j] = i.replace('\n','')
	  mail[j] = i.replace('\t','')
	'''
	pattern = r"^http:"
	
	spam_words = ['free','paid','discount','price','off','cheap','trade','.inc','limited','exchange','xchange','flat','latest','new','999','available','lose','win','loss','sale','sponser','income','dob','loan','earn','money','login','gold','silver','100000','spin','hurry','advertisement','smartpicks',]
	
	sensitive_words = ['password','credit','loan','debit','username','e-mail','g-mail','click','address','phone','limited','privacy','policy','delivery','free','discount','99','99%','sponser','loan','bank','details','pin','otp','subscribe','www.','enter','voucher','vouchers','gmail','email','$','antivirus','+','years','interested','chatting','chatting!','profile',]

	# encrypted words for profanity filter
	alp = "abcdefghijklmnopqrstuvwxyz*"
	w1 = alp[18]+alp[4]+alp[23]
	w2 = alp[15]+alp[14]+alp[17]+alp[13]
	w3 = alp[23]+alp[23]+alp[23]
	w4 = alp[13]+alp[20]+alp[3]+alp[4]
	w5 = alp[1]+alp[14]+alp[14]+alp[1]
	w6 = alp[21]+alp[0]+alp[6]+alp[4]+alp[13]+alp[0]
	w7 = alp[21]+alp[0]+alp[6]+alp[8]+alp[13]+alp[0]
	w8 = alp[1]+alp[20]+alp[19]+alp[19]
	w9 = alp[15]+alp[4]+alp[13]+alp[8]+alp[18]
	w10 = alp[7]+alp[14]+alp[13]+alp[4]+alp[24]+alp[12]+alp[14]+alp[14]+alp[13]
	w11 = alp[26]
	w12 = alp[7]+alp[14]+alp[19]+alp[8]+alp[19]+alp[18]     
	prof = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12]

	#sure_shot spam words that occure only in spam mails
	sure_shot = [ ] 

	spam_score = 0 
	# spam score ,if it increases higher than the normal then mail will be marked as spam

	#mail = str(input("Enter mail here : "))
	#mail = mail.lower()
	con = 0 #counter to change condition

	# empty message detection
	if mail == "" :
	    con = 1
	    return(True)
	    

	# For cyrillic characters -
	c = "ёяшертыуиопющэъасдфгчйкльжзхцвбнмЁЯШЕРТЫУИОПЮЩЭЪАСДФГЧЙКЛЬЖЗХЦВБНМ"
	if con == 0:
	    for char in c:
	     if char in mail:
	      return(True)
		    

	# profantity filter
	if con == 0:
	    for word in prof:
	     if word in mail:
              return(True)
		   

	# for sureshot words in email   
	if con== 0:
	     for word in sure_shot:
	      if word in mail:
	       return(True) 
		                
		      
	# for sensative words
	if con == 0:
	    for word in sensitive_words:
	     if word in mail:
               spam_score +=1         #0.5   
	     break                

	# for spam score       
	for word in spam_words:
	    if word in mail:
	     spam_score +=2        #1
               
                
        #pattern matching for a non secure links
	if con== 0:
	     for word in mail:
	      if re.match(pattern,word):
	       spam_score +=5
	
	#Calculations for spam       
	
	spam_level = 100*(spam_score/len(mail))
		            
	# for final decision 
	if con == 0:
	    if spam_level >= 10:
	     return(True)
	    
	    else:
	     return(False)

	
def main():
 csv.field_size_limit(100000000)
 cnt=0
 scn=0
 f = open("sunnyakhandare5618@gmail.com.csv")
 reader = csv.reader(f)
 for m_id,Sender,Subject,Date,Snippet,Message_body in reader:
  
  mail = Subject+Snippet+Message_body
  mail = mail.lower()  
  mail = mail.replace('\n',' ')
  mail = mail.replace('\t',' ')
  mail = mail.split(' ')
 
  #print(mail)
  if (is_spam(mail)):
   print("--------------------------------------------------------------")
   print(m_id," YES it is a spam")
   cnt+=1
   scn+=1
  else:
   print(m_id," NO it is not a spam")
   scn+=1
  if(is_spam(mail)):
   print(mail)
   print("--------------------------------------------------------------")    
#returns false when a normal mail
#returns true when a spam mail
 print("total no of spams are: ",cnt)
 print("Scanned number of mails",scn)	
if __name__=='__main__':
 main() 	
