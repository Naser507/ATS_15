import wx

def load(parent):
    panel = wx.Panel(parent)

    sizer = wx.BoxSizer(wx.VERTICAL)

    title = wx.StaticText(panel, label="New Project")
    desc = wx.StaticText(panel, label="This is a dummy New Project screen.")

    sizer.Add(title, 0, wx.ALL, 10)
    sizer.Add(desc, 0, wx.ALL, 10)

    panel.SetSizer(sizer)

    return panel