
# Importing library
import pandas as pd
import plotly.graph_objects as go
import smtplib, ssl
import json
from pretty_html_table import build_table
from win10toast_click import ToastNotifier
import email.encoders as enc
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

SOURCE_NODE = './sourceNode/'
DESTINATION_NODE = './destinationNode/'
toast = ToastNotifier()
status = False


# Pull the data from source and data manipulation
def get_data():
    data = pd.read_csv(SOURCE_NODE + 'us-500.csv')
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(['first_name', 'company_name', 'city', 'zip', 'phone1', 'email']),
                    fill_color='lightgreen',
                    align='left'),
        cells=dict(values=[data.first_name, data.company_name, data.city, data.zip, data.phone1, data.email],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.update_layout(title_text='Data - 16th July 2022', height=700, width=1000, font=dict(size=12),
                      title_x=0.5, title_y=0.9, )

    fig.write_html(DESTINATION_NODE + 'output.html')

    df = data[['company_name', 'city', 'zip', 'phone1', 'email']].head()
    outputs = build_table(df, 'blue_light')
    files = 'output.html'
    return outputs, files


# Send email with configurations
def send_mail(body, file_name, sender_id, sender_pass, receiver_id, cc_person, bcc_person):
    try:
        message = MIMEMultipart()

        # Make below address configuration as per requirements
        to = receiver_id
        cc = cc_person
        bcc = bcc_person
        to_address = [to] + cc + bcc
        message['Subject'] = 'Client "US-NVA133A" Data on 16th July 2022'
        message['From'] = sender_id
        # message['To'] = receiver

        # Email body
        text1 = '''\
        Hi Team,
    
        Good Morning, Please find below US client dummy data.
        '''
        text2 = '''\
            Thanks,
            Alan Walkies
            Team Lead, NSEXT-85 Group,
            Head Quarter II, Asia Division, Mumbai.
            '''
        html1 = '''\
        <html>
            <body>
                <h4> PFA for more details - US-NVA133A </h3>
            </body><br><br>
        <html>'''

        part1 = MIMEText(text1, 'plain')
        part2 = MIMEText(text2, 'plain')
        part3 = MIMEText(html1, 'html')

        body_content = body

        # Email body contents arrangement
        message.attach(part1)
        message.attach(MIMEText(body_content, "html"))
        message.attach(part3)
        message.attach(part2)

        # Email attachment
        with open(DESTINATION_NODE + file_name, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        enc.encode_base64(part)
        part.add_header('Content-Disposition',
                        f'attachment; filename={file_name}')
        message.attach(part)
        msg_body = message.as_string()

        # Email configuration setup
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
        server.login(sender_id, sender_pass)



        server.sendmail(sender_id, to_address, msg_body)
        server.quit()
        return True

    except Exception:
        return False


# Get credentials from a config file
content = open("credentials.json")
config = json.load(content)
sender_id = config['from']
sender_pass = config['pass']
receiver_id = config['to']
cc_person = config['cc']
bcc_person = config['bcc']

output, file = get_data()
status = send_mail(output, file, sender_id, sender_pass, receiver_id, cc_person, bcc_person)


# Notification pop-up
if status is True:
    toast.show_toast('Automation Email Notifier',
                     'The report has been send via email successfully. Please check the mails.',
                     duration=4,
                     callback_on_click='')
else:
    toast.show_toast('Automation Email Notifier',
                     'Error appears in email report. Please check the files / credentials.',
                     duration=4,
                     callback_on_click='')

