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
            if ("note" in btn):
                continue
            if ("color" in btn) == False:
                btn["color"] = [204, 204, 204]
            if len(btn["function"]) == 0:
                self.makeLabel(urlMngBtnBox, btn["name"])
            else:
                self.makeButton(urlMngBtnBox, btn["name"], btn["function"], btn["color"])

        sizer.Add(urlMngBtnBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        ##
        self.SetSizer(sizer)
        self.SetAutoLayout(True)

    def OnButtonFunction001(self, evt):
        print ("OnButtonFunction001")

    def makeLabel(self, labelBox, labelName):
        label_id = wx.NewIdRef()
        tmpLabel = wx.StaticText(self, id=label_id, label=labelName, size=(580,25))
        labelBox.Add(tmpLabel, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

    def makeButton(self, btnBox, btnName, btnCmd, btnColor):
        btnId = wx.NewIdRef()
        tmpBtn = wx.Button(self, btnId, btnName, size=(580,25))
        tmpBtn.SetBackgroundColour(wx.Colour(btnColor[0], btnColor[1], btnColor[2]))
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