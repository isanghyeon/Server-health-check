# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import smtplib
from email.mime.text import MIMEText
from api import *
from discord_webhook import DiscordWebhook


class SendServerStatusforDiscord:
    """
        Report for Server Status
        Discord Bot Token: "N/A"
        Web Hook URL: "N/A"
    """

    def __init__(self, WebHook_URL, **kwargs):
        """
        Init Report for Server Status
        :param WebHook_URL: LOGOS discord channel web-hook url
        :type WebHook_URL: str
        """

        self.webhook_url = WebHook_URL
        self.Report_Status = kwargs.get("Report_Status")
        self.Report_Date = kwargs.get("Report_Date")
        self.Report_Title = kwargs.get("Report_Title")

        self.Container_ID = kwargs.get("Container_ID")
        self.Container_Name = kwargs.get("Container_Name")
        self.Container_Status_Code = kwargs.get("Container_Status_Code")
        self.Container_Failed_Time = kwargs.get("Container_Failed_Time")

        self.Backup_Container_ID = kwargs.get("Backup_Container_ID")
        self.Backup_Container_Date = kwargs.get("Backup_Container_Date")

        self.Backup_Path = kwargs.get("Backup_Path")
        self.Backup_File_Name = kwargs.get("Backup_File_Name")

        self.Report_Message = f"""
**----------------------------------------------------------------------**
**LOGOS Server health check**

`Report Title : {self.Report_Title}`
`Report Status :  {self.Report_Status}`
`Report Date : {self.Report_Date}`

**> container information**
`- Container ID : {self.Container_ID}`
`- Container Name : {self.Container_Name}`
`- Container Status Code : {self.Container_Status_Code}`
`- Container Failed Time : {self.Container_Failed_Time}`

**> used information**
`- Backup Container ID : {self.Backup_Container_ID}`
`- Backup Container Date : {self.Backup_Container_Date}`

**> backups information**
`- Backup Path : {self.Backup_Path}`
`- Backup File Name : {self.Backup_File_Name}`
**----------------------------------------------------------------------**
        """

        self.webhook = DiscordWebhook(
            url=self.webhook_url,
            content=self.Report_Message
        )

    def SendDiscordMessage(self):
        return self.webhook.execute()


class SendServerStatusforMail:
    def __init__(
            self, ServerName="",
            Title="LOGOS Server Health",
            Date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            Message=None,
            Status=None
    ):
        self.ServerName = ServerName
        self.Title = Title
        self.Message = Message
        self.Status = Status
        self.date = Date

        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
        self.msg = MIMEText(self.Message)

        self.sender = list()
        self.receive = None

    def Sender_Receiver_MailCredential(self):
        self.sender = ServerAPI().MailReportCredential()
        return self.sender

    def SendMail(self):
        self.smtp.ehlo()  # say Hello
        self.smtp.starttls()  # TLS 사용시 필요
        self.smtp.login(self.Sender_Receiver_MailCredential()[0], self.Sender_Receiver_MailCredential()[1])

        self.msg['Subject'] = self.Title
        self.msg['To'] = self.Sender_Receiver_MailCredential()[2]

        self.smtp.sendmail(self.Sender_Receiver_MailCredential()[0], self.Sender_Receiver_MailCredential()[2],
                           self.msg.as_string())
        self.smtp.quit()
