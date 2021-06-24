# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import json
import os
import datetime


class ServerAPI:
    def __init__(self):
        with open('API/Command.json', 'r') as JsonParsing:
            self.CommandJson = json.load(JsonParsing)

        # Get environment variable
        self.SenderEmailAddress = os.environ.get("SENDER_EMAIL_ADDR")
        self.SenderEmailPassword = os.environ.get("SENDER_EMAIL_PW")
        self.ReceiverEmailAddress = os.environ.get("RECEIVER_EMAIL_ADDR")
        self.DiscordWebhookUrl = os.environ.get("DISCORD_WEBHOOK_ID")
        self.BackupPath = os.environ.get("BACKUP_PATH")

        # Get DateTime
        self.DateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.Date = datetime.datetime.now().strftime('%Y-%m-%d')

    def MailReportCredential(self):
        """
        :return: json
        """
        return {
            "sender": self.SenderEmailAddress,
            "sender-password": self.SenderEmailPassword,
            "receiver": self.ReceiverEmailAddress
        }

    def ExecuteCommand(self, Command=None):
        """
        :type Command: str
        """
        return os.popen(self.CommandJson[Command]).read()

    def DiscordReportCredential(self):
        return self.DiscordWebhookUrl

    def ReturnDate(self):
        return self.Date

    def ReturnDateTime(self):
        return self.DateTime

    def ReturnBackupPath(self):
        return self.BackupPath
