#!/usr/bin/env python
# Class autogenerated from ./allocalizationproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALLocalization(object):
    def __init__(self):
        self.proxy = ALProxy("ALLocalization")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def clear(self, pDirectory):
        """Delete all panoramas in a directory.

        :param str pDirectory: Name of the directory
        :returns int: 
        """
        return self.proxy.clear(pDirectory)

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

    def getCurrentPanoramaDescriptor(self):
        """Get some information about the current panorama.

        :returns AL::ALValue: 
        """
        return self.proxy.getCurrentPanoramaDescriptor()

    def getFrame(self, arg1, arg2):
        """Get a frame buffer.

        :param int arg1: arg
        :param str arg2: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getFrame(arg1, arg2)

    def getMessageFromErrorCode(self, arg1):
        """

        :param int arg1: arg
        :returns str: 
        """
        return self.proxy.getMessageFromErrorCode(arg1)

    def getMethodHelp(self, methodName):
        """Retrieves a method's description.

        :param str methodName: The name of the method.
        :returns AL::ALValue: A structure containing the method's description.
        """
        return self.proxy.getMethodHelp(methodName)

    def getMethodList(self):
        """Retrieves the module's method list.

        :returns std::vector<std::string>: An array of method names.
        """
        return self.proxy.getMethodList()

    def getModuleHelp(self):
        """Retrieves the module's description.

        :returns AL::ALValue: A structure describing the module.
        """
        return self.proxy.getModuleHelp()

    def getRobotOrientation(self):
        """Get the robot orientation.

        :returns AL::ALValue: 
        """
        return self.proxy.getRobotOrientation()

    def getRobotOrientation(self, arg1):
        """Get the robot orientation.

        :param bool arg1: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getRobotOrientation(arg1)

    def getRobotPosition(self):
        """Get the robot position in world navigation.

        :returns std::vector<float>: 
        """
        return self.proxy.getRobotPosition()

    def getRobotPosition(self, arg1):
        """Get the robot position in world navigation.

        :param bool arg1: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getRobotPosition(arg1)

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def goToHome(self):
        """Go to the robot home.

        :returns int: 
        """
        return self.proxy.goToHome()

    def goToPosition(self, arg1):
        """Go to a given position.

        :param std::vector<float> arg1: arg
        :returns int: 
        """
        return self.proxy.goToPosition(arg1)

    def isDataAvailable(self):
        """

        :returns bool: 
        """
        return self.proxy.isDataAvailable()

    def isInCurrentHome(self):
        """Is the robot in its home?

        :returns bool: 
        """
        return self.proxy.isInCurrentHome()

    def isInGivenZone(self, arg1, arg2, arg3, arg4):
        """

        :param float arg1: arg
        :param float arg2: arg
        :param float arg3: arg
        :param float arg4: arg
        :returns AL::ALValue: 
        """
        return self.proxy.isInGivenZone(arg1, arg2, arg3, arg4)

    def isRelocalizationRequired(self):
        """

        :returns bool: 
        """
        return self.proxy.isRelocalizationRequired()

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

    def learnHome(self):
        """Learn the robot home.

        :returns int: 
        """
        return self.proxy.learnHome()

    def load(self, pDirectory):
        """Loads panoramas from a directory in the default one.

        :param str pDirectory: Name of the directory
        :returns int: 
        """
        return self.proxy.load(pDirectory)

    def pCall(self):
        """NAOqi1 pCall method.

        :returns AL::ALValue: 
        """
        return self.proxy.pCall()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    def save(self, pDirectory):
        """Save the temporary panoramas in a directory from the default one.

        :param str pDirectory: Name of the directory
        :returns int: 
        """
        return self.proxy.save(pDirectory)

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def stopAll(self):
        """Stop all robot movements.
        """
        return self.proxy.stopAll()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()

    def wait(self, id, timeoutPeriod):
        """Wait for the end of a long running method that was called using 'post'

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :param int timeoutPeriod: The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero.
        :returns bool: True if the timeout period terminated. False if the method returned.
        """
        return self.proxy.wait(id, timeoutPeriod)