import datetime as dt
import random
import smtplib  # class used for sending emails

now = dt.datetime.now()
day = now.weekday()

# Determines whether the current day is Monday
if day == 0:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()  # creates a list of quotes
    random_quote = quotes_list[random.randint(0, len(quotes_list))]  # randomly chooses quote

''' 
Sets up the email
'''
my_email = "h68355132@gmail.com"
password = "ejcl rwnj ttqm ljge"

with smtplib.SMTP("smtp.gmail.com") as connection:  # works like a file
    connection.starttls()  # helps secure the connection
    connection.login(user=my_email, password=password)  # this logins in to the email account
    connection.sendmail(
        from_addr=my_email,
        to_addrs="harpercolins@yahoo.com",
        msg=f"Subject:Motivational Quote\n\n{random_quote}"
    )

