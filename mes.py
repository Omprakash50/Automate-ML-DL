import smtplib as s
op=s.SMTP("smtp.gmail.com",587)
op.starttls()
op.login("omprakash.21910935@viit.ac.in","Sukhiom@1710")
subject="Good news"
boby="Congratulation your model trigger more then 90% accuracy"
message="Subject:{}\n\n{}".format(subject,boby)
listOfAddress=["choudharyomprakash147@gmail.com"]
op.sendmail("choudharyomprakash",listOfAddress,message)
op.quit()
Hee
