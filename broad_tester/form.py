# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class broadrectester_main
###########################################################################

class broadrectester_main ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BroadcastReceiver Tester", pos = wx.DefaultPosition, size = wx.Size( 938,318 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Package Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        combopackageChoices = []
        self.combopackage = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, combopackageChoices, 0 )
        self.combopackage.SetSelection( 0 )
        bSizer2.Add( self.combopackage, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.lblcategory = wx.StaticText( self, wx.ID_ANY, u"Broadcast Receiver", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblcategory.Wrap( -1 )
        bSizer2.Add( self.lblcategory, 0, wx.ALL, 5 )
        
        combobroadcastrecChoices = []
        self.combobroadcastrec = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, combobroadcastrecChoices, 0 )
        self.combobroadcastrec.SetSelection( 0 )
        bSizer2.Add( self.combobroadcastrec, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Action", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        comboactionChoices = []
        self.comboaction = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, comboactionChoices, 0 )
        self.comboaction.SetSelection( 0 )
        bSizer2.Add( self.comboaction, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.cmdsend = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.cmdsend, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Extras (<Type> <Key> <Value>)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtextras = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
        bSizer3.Add( self.txtextras, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass
    

