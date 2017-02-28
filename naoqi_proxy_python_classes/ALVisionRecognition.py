#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alvisionrecognitionproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALVisionRecognition(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALVisionRecognition")

    def changeDatabase(self, databasePath, databaseName):
        """By default the database has the name "database" and is on the robot in /home/nao/naoqi/share/naoqi/vision/visionrecognition/current/ folder. This bound method allows to choose both another name and another folder for the database.

        :param str databasePath: Absolute path of the database on the robot, or "" to set default path.
        :param str databaseName: Name of the database (without extension), or "" to set default database name.
        :returns bool: True if the operation succeded, false otherwise.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.changeDatabase(databasePath, databaseName)

    def getActiveCamera(self):
        """Gets extractor active camera

        :returns int: Id of the current active camera of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getActiveCamera()

    def getCurrentPeriod(self):
        """Gets the current period.

        :returns int: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getCurrentPeriod()

    def getCurrentPrecision(self):
        """Gets the current precision.

        :returns float: Precision of the extractor.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getCurrentPrecision()

    def getEventList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getEventList()

    def getFrameRate(self):
        """Gets extractor framerate

        :returns int: Current value of the framerate of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getFrameRate()

    def getMemoryKeyList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getMemoryKeyList()

    def getMyPeriod(self, name):
        """Gets the period for a specific subscription.

        :param str name: Name of the module which has subscribed.
        :returns int: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getMyPeriod(name)

    def getMyPrecision(self, name):
        """Gets the precision for a specific subscription.

        :param str name: name of the module which has subscribed
        :returns float: precision of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getMyPrecision(name)

    def getOutputNames(self):
        """Get the list of values updated in ALMemory.

        :returns std::vector<std::string>: Array of values updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getOutputNames()

    def getParam(self, paramName):
        """Get some vision recognition parameters.

        :param str paramName: The name of the parameter to get. "db_path" and "db_name" can be used.
        :returns AL::ALValue: Value of the parameter as a string for "db_path" and "db_name"
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getParam(paramName)

    def getResolution(self):
        """Gets extractor resolution

        :returns int: Current value of the resolution of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getResolution()

    def getSubscribersInfo(self):
        """Gets the parameters given by the module.

        :returns AL::ALValue: Array of names and parameters of all subscribers.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.getSubscribersInfo()

    def isPaused(self):
        """Gets extractor pause status

        :returns bool: True if the extractor is paused, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.isPaused()

    def isProcessing(self):
        """Gets extractor running status

        :returns bool: True if the extractor is currently processing images, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.isProcessing()

    def pause(self, paused):
        """Changes the pause status of the extractor

        :param bool paused: New pause satus
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.pause(paused)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.ping()

    def setActiveCamera(self, cameraId):
        """Sets extractor active camera

        :param int cameraId: Id of the camera that will become the active camera
        :returns bool: True if the update succeeded, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.setActiveCamera(cameraId)

    def setFrameRate(self, subscriberName, framerate):
        """Sets the extractor framerate for a chosen subscriber

        :param str subscriberName: Name of the subcriber
        :param int framerate: New framerate
        :returns bool: True if the update succeeded, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.setFrameRate(subscriberName, framerate)

    def setFrameRate2(self, framerate):
        """Sets the extractor framerate for all the subscribers

        :param int framerate: New framerate
        :returns bool: True if the update succeeded, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.setFrameRate(framerate)

    def setParam(self, paramName, paramValue):
        """Set vision recognition parameters (deprecated in 1.22)

        :param str paramName: Name of the parameter to be changed. Only "resolution" can be used.
        :param AL::ALValue paramValue: Value of the resolution as an integer: 0(QQVGA) 1(QVGA) 2(VGA)
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.setParam(paramName, paramValue)

    def setParameter(self, paramName, value):
        """DEPRECATED: Sets pause and resolution

        :param str paramName: Name of the parameter to set
        :param AL::ALValue value: New value
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.setParameter(paramName, value)

    def setResolution(self, resolution):
        """Sets extractor resolution

        :param int resolution: New resolution
        :returns bool: True if the update succeeded, False if not
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.setResolution(resolution)

    def subscribe(self, name, period, precision):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        :param int period: Refresh period (in milliseconds) if relevant.
        :param float precision: Precision of the extractor if relevant.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.subscribe(name, period, precision)

    def subscribe2(self, name):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.subscribe(name)

    def unsubscribe(self, name):
        """Unsubscribes from the extractor.

        :param str name: Name of the module which had subscribed.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.unsubscribe(name)

    def updatePeriod(self, name, period):
        """Updates the period if relevant.

        :param str name: Name of the module which has subscribed.
        :param int period: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.updatePeriod(name, period)

    def updatePrecision(self, name, precision):
        """Updates the precision if relevant.

        :param str name: Name of the module which has subscribed.
        :param float precision: Precision of the extractor.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.updatePrecision(name, precision)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALVisionRecognition")
        return self.proxy.version()
