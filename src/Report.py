# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import smtplib
import datetime
from email.mime.text import MIMEText
from api import *
from discord_webhook import DiscordWebhook


class XML_ReWrite:
    def __init__(self):
        pass


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
        :keyword Response: Server response message
        :keyword Report_Title: Server health check report title
        :keyword Date: Server health check report time
        :keyword Report_Message: report message
        :keyword ServerStatusCode: server status code
        :keyword Error_Point: error point
        :keyword Error_Log: error log
        """

        self.webhook_url = "https://discord.com/api/webhooks/" + WebHook_URL
        self.Response = kwargs.get("Response")
        self.Report_Title = kwargs.get("Report_Title")
        self.Report_Date = kwargs.get("Date")
        self.Message = kwargs.get("Message")
        self.ServerStatusCode = kwargs.get("ServerStatusCode")
        self.Error_Point = kwargs.get("Error_Point")
        self.Error_Log = kwargs.get("Error_Log")

        self.Report_Message = f"""
            Response: {self.Response} 
            Report Title:  {self.Report_Title} 
            Report Date:  {self.Report_Date} 
            Message:  {self.Message} 
            Server status: {self.ServerStatusCode} 
            Error point:  {self.Error_Point} 
            Error Log:  {self.Error_Log}
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
