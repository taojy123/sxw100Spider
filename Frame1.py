#Boa:Frame:Frame1

import wx
import spider

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(615, 328), size=wx.Size(400, 250),
              style=wx.DEFAULT_FRAME_STYLE, title=u'SXW100')
        self.SetClientSize(wx.Size(384, 212))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 212),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'\u9009\u62e9\u6587\u4ef6', name='button1',
              parent=self.panel1, pos=wx.Point(56, 24), size=wx.Size(136, 32),
              style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label=u'\u5f00\u59cb\u8fd0\u884c', name='button2',
              parent=self.panel1, pos=wx.Point(56, 144), size=wx.Size(136, 32),
              style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=u'-',
              name='staticText1', parent=self.panel1, pos=wx.Point(56, 96),
              size=wx.Size(272, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        input_file_name = wx.FileSelector("Open", wildcard="*.xls")
        if input_file_name:
            self.staticText1.SetLabel(input_file_name)
        event.Skip()

    def OnButton2Button(self, event):
        input_file_name = self.staticText1.GetLabel()
        if input_file_name and input_file_name != "-":
            spider.get_data(input_file_name)
            wx.MessageBox("Finish!")
        event.Skip()
