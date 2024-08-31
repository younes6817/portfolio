import smtplib, ssl

host = "sedyounesmousavi1388@gmail.com"

port = 465

username = "sedyounesmousavi1388@gmail.com"

password = "1q2w3e4R5T@"

receiver = "sedyounesmousavi1388@gmail.com"

context = ssl.create_default_context()

message = """
Hi
How are you?
Bye!
"""


with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
