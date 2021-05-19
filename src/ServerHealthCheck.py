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

import datetime
from Report import SendServerStatusforDiscord
from Server_Status import HostServerStatus, DockerServerStatus
import os


def ExecuteCMD(Command):
    return os.popen(Command).read()


def ServerStatus(ServerType=None):
    if ServerType == "HostServer":
        HostServer = HostServerStatus().Memory_Used(), HostServerStatus().Storage_Used()

        for idx in range(len(HostServer)):
            Command = HostServer[idx]["Command"]
            Result = ExecuteCMD(Command)

    elif ServerType == "DockerServer":
        DockerServer = DockerServerStatus().Container_Info()

        for idx in DockerServer.keys():
            Command = DockerServer[idx]["Command"]
            Result = ExecuteCMD(Command)

    else:
        return "Error"


if __name__ == '__main__':
    import logging
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
    """ 
    Web-hook URL s
        LSH : 838953823451480134/xPbLNRqT-Rg4k_H7a3kQJUQsRHx8X8yvh3Hl3-auxDIJLScML-GdKhI9ncsHiUxiNsvG 
        LOGOS : 840869197374291968/avpWEpIJNXhYO9XfIHw0-KzD7DCD_bkV3ALW2AjW1DxxE7fO5p5jVnoFGc7Yib51Ad3q 
    """

    ServerStatus("DockerServer")

    DiscordReport = SendServerStatusforDiscord(
        WebHook_URL="838953823451480134/xPbLNRqT-Rg4k_H7a3kQJUQsRHx8X8yvh3Hl3-auxDIJLScML-GdKhI9ncsHiUxiNsvG",
        Response="200",
        Report_Title="Docker container down",
        Date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        Message=f"""\n{os.popen('df -h').read()}""",
        ServerStatusCode="500",
        Error_Point="DB server",
        Error_Log="Demon not restarted"
    )

    # DiscordReport.SendDiscordMessage()
