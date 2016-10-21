import ssl
import atexit
import json
from pyVim.connect import SmartConnect, Disconnect


def readConfig(configPath):
    return json.load(open(configPath, "r+"))


class ConnectDetails:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password


class DConnecter:
    def __init__(self, connectionDetails=None):
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self.context.verify_mode = ssl.CERT_NONE
        self.connectionDetails = connectionDetails

    def connect(self):
        si = SmartConnect(host=self.connectionDetails.host,
                          user=self.connectionDetails.user,
                          pwd=self.connectionDetails.password,
                          port=int(self.connectionDetails.port),
                          sslContext=self.context)
        if not si:
            print("Could not connect to the specified host using specified username and password")
            return -1
        print("Connected to host : {0}".format(self.connectionDetails.host))
        atexit.register(Disconnect, si)
        return si
