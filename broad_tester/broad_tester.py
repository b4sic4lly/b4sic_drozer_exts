# import drozer util
import sys
sys.path.append('../')

import wx
from form import broadrectester_main
from drozerutil import DrozerConnection

class MainFrame(broadrectester_main):
    
    
    
    def __init__(self,parent):
        broadrectester_main.__init__(self,parent)
        self.cmdsend.Bind( wx.EVT_BUTTON, self.send )
        self.combobroadcastrec.Bind(wx.EVT_CHOICE, self.changebroadcastreceiver)
        self.combopackage.Bind(wx.EVT_CHOICE, self.changepackage)
        
        try:
            self.drozercon = DrozerConnection("Broadcast Receiver Tester")
        except:
            self.Info("Could not connect to Drozer Client. Drozer Client started and port forwarded?")
        self.packagelist = self.drozercon.get_packages()
        
        for package in self.packagelist:
            self.combopackage.Append(package)

    
    def changepackage(self, event):
        self.combobroadcastrec.Clear()
        for rec in self.drozercon.get_exported_receivers(self.combopackage.GetStringSelection()):
            self.combobroadcastrec.Append(rec.name)
    
    def send(self, event):
        
        extrastext = self.txtextras.GetValue()
        extraslist = []
        for line in extrastext.split("\n"):
            if len(line) > 3:
                linesplit = line.split(" ")
                if len(linesplit) == 3:
                    extraslist.append((str(linesplit[0]), str(linesplit[1]), str(linesplit[2])))
                else:
                    self.Info("Extras malformed")
                    return
        
                
        self.drozercon.sendintent(self.comboaction.GetStringSelection(), self.combopackage.GetStringSelection(), self.combobroadcastrec.GetStringSelection(), extraslist)
    
    
    def changebroadcastreceiver(self, event):
        selreceiver = self.combobroadcastrec.GetStringSelection()
        
        if selreceiver != "":
            cureceiver = self.drozercon.get_exported_receiver_by_name(self.combopackage.GetStringSelection(), selreceiver)
            
            # fill action combo box
            self.comboaction.Clear()
            for intent in cureceiver.intentfilters:
                for action in intent.actions:
                    self.comboaction.Append(action)
                    
    
    def Info(self, message, caption = 'BroadcastReceiverTester'):
        dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
            
        
app = wx.App(False)

frame = MainFrame(None)
frame.Show(True)
app.MainLoop()