# ! /usr/bin/python3.8
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

import datetime
from Report import SendServerStatusforDiscord
from xml.etree.ElementTree import Element, dump
from Server_Status import HostServerStatus, DockerServerStatus
import os


def ServerStatus():
    HostServer = HostServerStatus().Memory_Used(), HostServerStatus().Storage_Used()
    DockerServer = DockerServerStatus().Container_ID_Name(), DockerServerStatus().Container_Network()
    print(HostServer)
    print(DockerServer)


def XMLReWriter():
    pass


def ExecuteCommand(Command):
    return os.system(Command)


if __name__ == '__main__':
    ServerStatus()
    """
    Web-hook URL 
        LSH : 838953823451480134/xPbLNRqT-Rg4k_H7a3kQJUQsRHx8X8yvh3Hl3-auxDIJLScML-GdKhI9ncsHiUxiNsvG 
        LOGOS : 840869197374291968/avpWEpIJNXhYO9XfIHw0-KzD7DCD_bkV3ALW2AjW1DxxE7fO5p5jVnoFGc7Yib51Ad3q 
    """

    """
        DateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        DiscordReport = SendServerStatusforDiscord(
        WebHook_URL="838953823451480134/xPbLNRqT-Rg4k_H7a3kQJUQsRHx8X8yvh3Hl3-auxDIJLScML-GdKhI9ncsHiUxiNsvG",
        Response="200",
        Report_Title="Server die",
        Date=DateTime,
        Message=f"Container ID : {container()}, Container Name : {container()}",
        ServerStatusCode="500",
        Error_Point="DB server",
        Error_Log="Demon not restarted"
        )

        DiscordReport.SendDiscordMessage()
    """
