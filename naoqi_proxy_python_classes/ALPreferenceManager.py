#!/usr/bin/env python
# Class autogenerated from ./alpreferencemanagerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALPreferenceManager(object):
    def __init__(self):
        self.proxy = ALProxy("ALPreferenceManager")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

    def getDomainList(self):
        """Get available preferences domain

        :returns std::vector<std::string>: a list containing all the available domain names
        """
        return self.proxy.getDomainList()

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

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def getValue(self, domain, setting):
        """Get specified preference

        :param str domain: Preference domain
        :param str setting: Preference setting
        :returns AL::ALValue: corresponding preferences value
        """
        return self.proxy.getValue(domain, setting)

    def getValueList(self, domain):
        """Get preferences names and values for a given domain

        :param str domain: Preference domain
        :returns std::vector<std::vector<AL::ALValue> >: a list of preferences names and values associated to the domain
        """
        return self.proxy.getValueList(domain)

    def importPrefFile(self, domain, applicationName, filename, override):
        """Import a preferences XML file

        :param str domain: Preference domain: all preferences values found in XML file will be imported in that domain.
        :param str applicationName: Application name: will be used to search for preference file on disk (in location of type <configurationdirectory>/applicationName/filename).
        :param str filename: Preference XML filename
        :param bool override: Set this to true if you want to override preferences that already exist with preferences in imported XML file
        """
        return self.proxy.importPrefFile(domain, applicationName, filename, override)

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

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

    def removeDomainValues(self, domain):
        """Remove an entire preference domain

        :param str domain: Preference domain
        """
        return self.proxy.removeDomainValues(domain)

    def removeValue(self, domain, setting):
        """Remove specified preference

        :param str domain: Preference domain
        :param str setting: Preference setting
        """
        return self.proxy.removeValue(domain, setting)

    def setValue(self, domain, setting, value):
        """Set specified preference

        :param str domain: Preference domain
        :param str setting: Preference setting
        :param AL::ALValue value: Preference value
        """
        return self.proxy.setValue(domain, setting, value)

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def update(self):
        """Synchronizes local preferences with preferences stored on a server.
        """
        return self.proxy.update()

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