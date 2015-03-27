#Boa:Dialog:Dialog1

import wx
import Frame1
import pickle
import hashlib


def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1STATICTEXT1, 
 wxID_DIALOG1STATICTEXT2, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1TEXTCTRL1, 
 wxID_DIALOG1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(500, 308), size=wx.Size(361, 248),
              style=wx.DEFAULT_DIALOG_STYLE, title='Dialog1')
        self.SetClientSize(wx.Size(345, 210))
        self.Bind(wx.EVT_CLOSE, self.OnDialog1Close)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'\u8bf7\u5148\u767b\u5f55', name='staticText1',
              parent=self, pos=wx.Point(136, 40), size=wx.Size(48, 13),
              style=0)

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label=u'\u7528\u6237\u540d\uff1a', name='staticText2',
              parent=self, pos=wx.Point(40, 80), size=wx.Size(48, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3,
              label=u'\u5bc6\u7801\uff1a', name='staticText3', parent=self,
              pos=wx.Point(51, 120), size=wx.Size(36, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(104, 80), size=wx.Size(184, 21),
              style=0, value=u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_DIALOG1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(104, 120), size=wx.Size(184, 21),
              style=wx.TE_PASSWORD, value=u'')

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label=u'\u767b\u5f55',
              name='button1', parent=self, pos=wx.Point(128, 160),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        username = self.textCtrl1.GetValue()
        password = self.textCtrl2.GetValue()
        s = open("key.dat").read()
        accounts = pickle.loads(s)
        md5p = accounts.get(username, "")
        if hashlib.md5(password).hexdigest() == md5p:            
            Frame1.create(None).Show()
            self.Destroy()
        else:
            wx.MessageBox("Password is error!")
        event.Skip()

    def OnDialog1Close(self, event):
        self.Destroy()
        event.Skip()
