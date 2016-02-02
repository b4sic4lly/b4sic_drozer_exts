from xml.dom import minidom
from xml.etree import ElementTree

from drozer import android
from drozer.modules import common, Module
from drozer.modules.common import loader
import time
from drozer.console.session import Session, DebugSession
from drozer.connector import ServerConnector


class Receiver():
    def __init__(self, name, permission):
        self.name = name
        self.permission = permission
        self.intentfilters = []
        
    def __str__(self):
        result = self.name + ", Permission: " + self.permission + "\n"
        for intent in self.intentfilters:
            result += str(intent)
        
        return result
        
class IntentFilter():
    def __init__(self, actions):
        self.actions = actions
    
    def __str__(self):
        result = ""
        for action in self.actions:
            result += "\t\t" + action + "\n"
            
        return result

class DrozerConnection(Module, common.Filters, common.IntentFilter, common.PackageManager):

    def getmanifest(self, packagename):
        return self.getAndroidManifest(packagename)
    
    def __init__(self, tag):
        self.connect()
        self.tag = tag
    
    def logdebug(self, message):
        log = self.klass("android.util.Log")
        log.d(self.tag, message)
    
    def connect(self):
        arg=ServerConnectorArgs()      
        
        self.server = ServerConnector(arg, None)
        
        devices = self.server.listDevices().system_response.devices
        
        if len(devices) == 1:
            device = devices[0].id
        
        response = self.server.startSession(device, None)
               
        session_id = response.system_response.session_id
        session = Session(self.server, session_id, arg)
        
        Module.__init__(self, session)


    def sendintent(self, action, packagename, componentname, extras):
        intent = android.Intent(action=action ,component=(packagename, componentname))
        
        intent.extras = []
        for extra in extras:
            intent.extras.append(extra)
        
        
        self.getContext().sendBroadcast(intent.buildIn(self))
    
    def get_exported_receiver_by_name(self, packagename, name):
        receivers = self.get_exported_receivers(packagename)
        for receiver in receivers:
            if receiver.name == name:
                return receiver
            
        return None 
    
    def testfunc(self):
        bundle = self.new("android.os.Bundle")
        
        b = bytearray()
        
        testarr = ["test", "bla"]
        bundle.putStringArray("pdus", testarr)
        
        # Define service endpoint and parameters
                
        binding = self.getBinding(self.debugcurpackage, "com.androihelm.antivirus.receivers.SMSMonitor")
        binding.setBundle(bundle)
        binding.setObjFormat("bundleAsObj")
        
        # Send message and receive reply
        binding.sendBroadcast()
    
    def get_packages(self):
        result = []
        for package in self.packageManager().getPackages(common.PackageManager.GET_PERMISSIONS | common.PackageManager.GET_CONFIGURATIONS | common.PackageManager.GET_GIDS | common.PackageManager.GET_SHARED_LIBRARY_FILES):
            application = package.applicationInfo
            newpackagename = str(application.packageName)
            
            if newpackagename.startswith("com.google") == False and newpackagename.startswith("com.android") == False:  
                result.append(newpackagename)
        
        return result
    
    def send_service_msg(self, packagename, servicename, what, arg1, arg2, timeout):
        binder = self.getBinding(packagename, servicename)
        result = binder.send_message((what, arg1, arg2), timeout)
        
        response_message = None
        
        if result:
            response_message = binder.getMessage();
            response_bundle = binder.getData();
            
        return response_message
    
    def get_exported_receivers(self, packagename):
        damanifest = self.getmanifest(packagename)

        newdamanifest = ""
        for char in damanifest:
            if ord(char) > 20 and ord(char) < 127:
                newdamanifest += char
        
        damanifest = newdamanifest
        
        dom = minidom.parseString(damanifest)
        receiverlist = []
        
        for receiver in dom.getElementsByTagName('receiver'):  # visit every node <bar />
            if receiver.getAttribute("exported") == "true" or receiver.getAttribute("exported") == "":
                receivername = receiver.getAttribute("name")
                
                newreceiver = Receiver(receivername,receiver.getAttribute("permission"))
                receiverlist.append(newreceiver)
                
                intentfilters = receiver.getElementsByTagName("intent-filter")
                for intentfilter in intentfilters:
                    newintentfilter = IntentFilter([])
                    newreceiver.intentfilters.append(newintentfilter)
                    
                    actions = intentfilter.getElementsByTagName("action")
                    for action in actions:
                        newintentfilter.actions.append(action.getAttribute("name"))
                        
        return receiverlist
    
    def get_exported_services(self):
        pass
        
class ServerConnectorArgs():
    def __init__(self):
        self.accept_certificate=False
        self.command = 'connect'
        self.debug = False
        self.device = None
        self.file = []
        self.no_color=False
        self.onecmd= ''
        self.password = False
        self.server = None
        self.ssl = False

    