# -*- coding:utf-8 -*-
# Copyright 2021. LOGOS - Cryptography Application Lab. all rights reserved.
# Made by LOGOS - Lee Sang-Hyeon.

from api import ServerAPI


class HostServerStatus:
    def __init__(self):
        self.api = ServerAPI()
        self.CMDType = ["memory"]
        self.UsedType = ["usage"]
        self.CMDName = ["MemoryUsed", "StorageUsed"]

    def Memory_Used(self):
        return self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0], CMDName=self.CMDName[0])

    def Storage_Used(self):
        return self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0], CMDName=self.CMDName[1])


class DockerServerStatus:
    def __init__(self):
        self.api = ServerAPI()
        self.CMDType = ["docker-inspect"]
        self.UsedType = ["docker-container"]
        self.CMDName = ["container-id", "container-name", "container-health-check", "container-time"]

    def Container_Info(self):
        return {
            "Container-ID": self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0],
                                                    CMDName=self.CMDName[0]),
            "Container-NAME": self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0],
                                                      CMDName=self.CMDName[1]),
            "Container-Health-Check": self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0],
                                                              CMDName=self.CMDName[2]),
            "Container-TIME": self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0],
                                                      CMDName=self.CMDName[3])
        }
