# To solve this mission you must use the SendGrid API
# It all starts with your first email. Let’s try to send one.
#
# Your mission is to create a function that sends a welcome email to a user.
# The function gets two arguments: email and the name of the user.
#
# Subject of the email should be "Welcome" and body simply "Hi {name}" ({name} should be replaced by a user's name)
#
# Input: Two arguments: email and a username.
#
# Output: None. You should send an email. You don’t need to return anything.


import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content

API_KEY = "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"
SUBJECT = "Welcome"
BODY = "Hi {name}"

sg = sendgrid.SendGridAPIClient(API_KEY)


def send_email(email, name):
    global API_KEY
    global SUBJECT
    global BODY

    BODY = "Hi {}".format(name)

    message = Mail(
        from_email='serik@bk.ru',
        to_emails=email,
        subject=SUBJECT,
    )

    message.content = Content('text/plain', BODY)
    try:
        sg = sendgrid.SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
