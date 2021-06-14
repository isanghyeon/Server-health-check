# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

import json
import os


class ServerAPI:
    def __init__(self):
        with open('API/ReportCredential.json', 'r') as JsonParsing:
            self.ReportCredential = json.load(JsonParsing)

        with open('API/Command.json', 'r') as JsonParsing:
            self.Command = json.load(JsonParsing)

    def MailReportCredential(self):
        """
        :return: json
        """
        return {
            "sender": self.ReportCredential["Credential"]["send"]["E-mail-Address"],
            "sender-password": self.ReportCredential["Credential"]["send"]["E-mail-Password"],
            "receiver": self.ReportCredential["Credential"]["receive"]
        }

    def ExecuteCommand(self, CMDType=None, UsedType=None, CMDName=None):
        """
        :type CMDType: str
        :type UsedType: str
        :type CMDName: str
        :return: json
        """
        if CMDType is None or UsedType is None or CMDName is None:
            return {
                    "CMDType": None,
                    "UsedType": None,
                    "CMDName": None,
                    "Command": None
            }

        return {
            "CMDType": CMDType,
            "UsedType": UsedType,
            "CMDName": CMDName,
            "Command": self.Command[CMDType][UsedType][CMDName]
        }