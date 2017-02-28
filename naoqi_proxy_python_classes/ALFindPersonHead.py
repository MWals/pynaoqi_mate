#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alfindpersonheadproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALFindPersonHead(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALFindPersonHead")

    def getTrackingDistance(self):
        """Gets the distance (in meters) for the tracking

        :returns float: Current tracking distance (in meters)
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.getTrackingDistance()

    def getVerticalOffset(self):
        """Sets the value of vertical offset (in meters) for the blob tracker

        :returns float: Current vertical offset of the blob tracker
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.getVerticalOffset()

    def isSearching(self):
        """Tells if the module is running or not.

        :returns bool: True if the module is running, False if not.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.isSearching()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.ping()

    def setTrackingDistance(self, distance):
        """Sets the distance (in meters) for the tracking

        :param float distance: New value (in meters)
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.setTrackingDistance(distance)

    def setVerticalOffset(self, value):
        """Sets the value of vertical offset (in meters) for the blob tracker

        :param float value: New vertical offset (in meters), added if positive, substracted if negative
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.setVerticalOffset(value)

    def startSearch(self):
        """Starts the module's process, the events are then raised.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.startSearch()

    def stopSearch(self):
        """Stops the module's process, the events are not raised anymore.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.stopSearch()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALFindPersonHead")
        return self.proxy.version()
