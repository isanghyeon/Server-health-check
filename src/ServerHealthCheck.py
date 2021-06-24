# ! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

"""
    This script checks the health of the docker server and sends it to the administrator.

    How to use...
        1. Define administrator mail. - ContactMailAddress.json (path : /root/Contact/ContactMailAddress.json)
        2. Define this script in the crontab scheduler. - crontab (path : /etc/crontab or cmd : crontab -e)
        3.
        4.
        5.
"""

from Report import SendServerStatusforDiscord
from api import ServerAPI

if __name__ == '__main__':
    DiscordReport = SendServerStatusforDiscord(
        WebHook_URL=ServerAPI().DiscordReportCredential(),
        Report_Title="Container failed restarted",
        Report_Status="Good",
        Report_Date=ServerAPI().ReturnDateTime(),
        Container_ID=ServerAPI().ExecuteCommand("get-container-id"),
        Container_Name=ServerAPI().ExecuteCommand("get-container-name"),
        Container_Status_Code=ServerAPI().ExecuteCommand("get-container-status"),
        Container_Failed_Time=ServerAPI().ExecuteCommand("get-container-exited-time"),
        Backup_Container_ID=ServerAPI().ExecuteCommand("get-backup-container-id") + ServerAPI().ExecuteCommand(
            "get-container-id"),
        Backup_Container_Date=ServerAPI().ExecuteCommand("get-backup-container-date") + ServerAPI().ReturnDate(),
        Backup_Path=ServerAPI().ReturnBackupPath(),
        Backup_File_Name=ServerAPI().ExecuteCommand("get-backup-file-name") + ServerAPI().ExecuteCommand(
            "get-backup-container-id") + ServerAPI().ExecuteCommand(
            "get-container-id") + "_" + ServerAPI().ExecuteCommand(
            "get-backup-container-date") + ServerAPI().ReturnDate()
    )
    DiscordReport.SendDiscordMessage()
