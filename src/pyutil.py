import wx
import chobopowreutilpanel

'''
Start  : 2019.04.01
Update : 
'''

SW_TITLE = "ChoboPowerUtil v0.0617b1"

class ChoboPowerUtilFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(ChoboPowerUtilFrame, self).__init__(*args, **kw)
        self.Bind(wx.EVT_CLOSE, self.onCloseApp)

        ctrl_Q_Id = wx.NewIdRef()
        self.Bind(wx.EVT_MENU, self.onClose, id=ctrl_Q_Id)

        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('Q'), ctrl_Q_Id )])
        self.SetAcceleratorTable(accel_tbl)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = chobopowreutilpanel.ChoboPowerUtilPanel(self)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def onClose(self, event):
        self.Close()

    def onCloseApp(self, event):
        self.Destroy()


def main(): 
    app = wx.App()
    frm = ChoboPowerUtilFrame(None, title=SW_TITLE, size=(600,600))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()