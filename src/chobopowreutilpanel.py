import wx
import os
import loadcfg

class ChoboPowerUtilPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(ChoboPowerUtilPanel, self).__init__(*args, **kw)
        self.buttonList = loadcfg.LoadCfg("choboutil.cfg").load()
        self.drawUI()

    def drawUI(self):
        print ("ChoboUrlManagerPanel::drawUI")
        self.SetBackgroundColour('LIGHT GREY')
        sizer = wx.BoxSizer(wx.VERTICAL)

        ##
        urlMngBtnBox = wx.BoxSizer(wx.VERTICAL)

        for btn in self.buttonList:
            self.makeButton(urlMngBtnBox, btn["name"], btn["function"])

        sizer.Add(urlMngBtnBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        #self.makeFuntion("dir")()

        ##
        self.SetSizer(sizer)
        self.SetAutoLayout(True)

    def OnButtonFunction001(self, evt):
        print ("OnButtonFunction001")

    def makeButton(self, btnBox, btnName, btnCmd):
        tmpBtn = wx.Button(self, 10, btnName, size=(580,30))
        tmpBtn.Bind(wx.EVT_BUTTON, self.makeFuntion(btnCmd))
        btnBox.Add(tmpBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

    def makeFuntion(self, run_cmd):
        print ("makeFuntion")
        def function_(self):
            print (run_cmd)
            runCmd = "start " + run_cmd
            print (runCmd)
            os.system(runCmd)
        return function_