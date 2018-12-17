#all imports
import smtplib  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText                    
from email.mime.application import MIMEApplication
from os.path import basename
import email
import email.mime.application
import random

class SecretSanta:
    def __init__(self, name, email, invalid_matches):
        self.name = name
        self.email = email
        self.invalid_matches = invalid_matches

def assign(santa, santasList):
    if (len(santasList) == 1):
        return santasList[0]

    current = random.choice(santasList)
    try:
        santa.invalid_matches.index(current.name)
        #current is invalid
        santasList.remove(current)
        return assign(santa, santasList)
        
    except:
        #current is valid
        return current
        

def main():
    # get all secret santa data from file
    with open("santas.txt", "r") as santaFile:
        secret_santas = []
        for line in santaFile:
            secret_santas.append(line.strip('\n'))

    # instantiate SecretSanta objects
    santas = []
    receviers = []
    for person in secret_santas:
        name = person.split(':')[0]
        email = person.split(':')[1]
        invalids = person.split(':')[2].split(',')
        currentSanta = SecretSanta(name, email, invalids)
        santas.append(currentSanta)
        receviers.append(currentSanta)

    for santa in santas:
        temp = []
        for x in receviers:
            temp.append(x)

        assignedPerson = assign(santa, temp)
        for x in receviers:
            if (x.name == assignedPerson.name):
                receviers.remove(x)
                
        print ("sending email to " + santa.name + "...")
        # send email to inform secret santa
        sendEmail(santa, assignedPerson)

def sendEmail(santa, receipent):
    intro = open("introduction.txt", "r")
    body = open("body.txt", "r")
    closing = open("closing.txt", "r")
    backup = open("backup2018.txt", "a")

    html = intro.read() + santa.name + "\n" + body.read() + receipent.name + "\n" + closing.read()
    backup.write(santa.name + " -> " + receipent.name + "\n")
    thebody= MIMEText(html)
    intro.close()
    body.close()
    closing.close()
    backup.close()

    #attach picture an html to the body
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Secret Santa!" #email subject
    msg['From'] = "example@gmail.com" #from email
    msg.attach(thebody)

    #connect to server
    s = smtplib.SMTP()
    s.connect('smtp.gmail.com',587) #gmail portal
    s.starttls()

    #send email
    msg['To'] = santa.email
    s.login('example@gmail.com','password') #login information
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

print ("Welcome to Secret Santa! \n")
input ("Make sure your santas.txt file is up to date. \nIf you are ready to start press ENTER.\n")
main()
