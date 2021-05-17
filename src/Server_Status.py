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
        self.CMDType = ["network", "docker-inspect"]
        self.UsedType = ["network-interface", "docker-container"]
        self.CMDName = ["enp6s0", "docker0", "br-08c15f3adc22", "container-id", "container-name", "container-live"]

    def Container_ID_Name(self):
        return {
            "Container-ID": self.api.ExecuteCommand(CMDType=self.CMDType[1], UsedType=self.UsedType[1],
                                                    CMDName=self.CMDName[3]),
            "Container-NAME": self.api.ExecuteCommand(CMDType=self.CMDType[1], UsedType=self.UsedType[1],
                                                      CMDName=self.CMDName[4]),
            "live": self.api.ExecuteCommand(CMDType=self.CMDType[1], UsedType=self.UsedType[1],
                                            CMDName=self.CMDName[5])
        }

    def Container_Network(self):
        return {
            self.CMDName[0]: self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0],
                                                     CMDName=self.CMDName[0]),
            self.CMDName[1]: self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0],
                                                     CMDName=self.CMDName[1]),
            self.CMDName[2]: self.api.ExecuteCommand(CMDType=self.CMDType[0], UsedType=self.UsedType[0],
                                                     CMDName=self.CMDName[2])
        }
