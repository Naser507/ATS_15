import wx


def build_dsp_menu(menu):
    # Keep flat for now (we’ll group later as you planned)

    menu.Append(wx.ID_ANY, "Add Transformer")
    menu.Append(wx.ID_ANY, "Bypass All")
    menu.Append(wx.ID_ANY, "Clear Chain")
    menu.Append(wx.ID_ANY, "Engine Stats")
    menu.Append(wx.ID_ANY, "Buffer Settings")
