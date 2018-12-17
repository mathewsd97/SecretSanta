# SecretSanta

A script that takes the data from santas.txt and randomly assigns Secret Santa to everyone.
The script takes into account any restrictions with the pairings, such as ensuring a couple doesnt draw eachother.

INSTRUCTIONS:
1. Enter the data to the 'santas.txt' file in the format "Name:Email:Pairing,Restrictions"
	- ensure that individuals in the pairing restrictions are separated by commas
	- currently need to include each self in the restriction to ensure you do not get paired to yourself
2. Edit the 'introduction.txt' 'body.txt' and 'closing.txt' files to customize the message to email to all participants
3. Edit line 81 in secret_santa.py and enter the subject line of the emails you are going to send
4. Edit line 82 in secret_santa.py and enter the email you want to send the emails from
5. Edit line 92 in secret_santa.py and enter the username and password of the email account you want to send emails from
6. Run the script and the emails will be sent!