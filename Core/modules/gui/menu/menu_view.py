import wx


def build_view_menu(menu):
    menu.Append(wx.ID_ANY, "Toggle Waveform")
    menu.Append(wx.ID_ANY, "DSP Chain Inspector")
    menu.Append(wx.ID_ANY, "Console / Logs")
    menu.Append(wx.ID_ANY, "Full Screen")
    menu.Append(wx.ID_ANY, "Reset Layout")
