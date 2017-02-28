#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/almemorywatcherproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALMemoryWatcher(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALMemoryWatcher")

    def addListener(self, name, interval):
        """add an ALMemory key to the list of keys to listen to

        :param str name: the complete name of the ALMemory key
        :param int interval: interval of time the system should wait before retrieving this key value again
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.addListener(name, interval)

    def addListener2(self, name):
        """add an ALMemory key to the list of keys to listen to

        :param str name: the complete name of the ALMemory key
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.addListener(name)

    def addListeners(self, listNames, interval):
        """add a list of ALMemory keys to the list of keys to listen

        :param std::vector<std::string> listNames: the vector of complete names of ALMemory keys
        :param int interval: interval of time the system should wait before retrieving this key value again
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.addListeners(listNames, interval)

    def addListeners2(self, listNames):
        """add a list of ALMemory keys to the list of keys to listen

        :param std::vector<std::string> listNames: the vector of complete names of ALMemory keys
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.addListeners(listNames)

    def clearBuffer(self):
        """remove all buffered data.                                           The list of keys listened to keeps unchanged.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.clearBuffer()

    def getData(self):
        """return an ALValue containing all buffered data                                       since the last call of getData().

        :returns AL::ALValue: The complete array of all buffered data
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.getData()

    def isWatching(self):
        """tells whether keys are watched and data being gathered.

        :returns bool: true if keys are being watched.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.isWatching()

    def listeners(self):
        """get the list of listened ALMemory keys

        :returns std::vector<std::string>: a list of ALMemory keys
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.listeners()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.ping()

    def removeAllListeners(self):
        """remove all keys listened to
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.removeAllListeners()

    def removeListener(self, name):
        """remove a key from the list to listen to

        :param str name: the name of the key to stop to listen
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.removeListener(name)

    def removeListeners(self, listNames):
        """remove a list of key from the list to listen

        :param std::vector<std::string> listNames: the vector of names of key to stop to listen
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.removeListeners(listNames)

    def setPeriodMs(self, period):
        """edit "period" value between two buffering.

        :param int period: the new period (in ms) to apply.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.setPeriodMs(period)

    def startWatching(self, period):
        """start listening to selected keys from ALMemory

        :param int period: the time between two listen of ALMemory keys, in milliseconds.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.startWatching(period)

    def stopWatching(self):
        """stop listening selected keys from ALMemory.                                    List of listened keys and associated buffers keep unchanged.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.stopWatching()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALMemoryWatcher")
        return self.proxy.version()
