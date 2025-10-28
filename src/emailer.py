import smtplib
from email.mime.text import MIMEText


def send_email(to, content):
    user_acct = "INSERT_YOUR_EMAIL_HERE@gmail.com"
    app_pw = "INSERT_YOUR_APP_PW_HERE"

    msg = MIMEText(content)
    msg['Subject'] = "Your Secret Santa Assignment"
    msg['From'] = user_acct
    msg["To"] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(user_acct, app_pw)
        smtp_server.sendmail(user_acct, to, msg.as_string())
    print("Message sent!")


def email_results(matches, participants):
    for participant in participants:
        participant_name = participant[0]
        participant_email = participant[1]

        assignment = [i for i in matches if i[0] == participant_name]
        assignee = assignment[0][1]

        send_email(participant_email, f"Your Secret Santa assignee is {assignee}. Keep it secret! Keep it safe!")
