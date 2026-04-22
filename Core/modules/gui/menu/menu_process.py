import wx


def build_process_menu(menu):
    menu.Append(wx.ID_ANY, "Normalize")
    menu.Append(wx.ID_ANY, "Reverse")
    menu.Append(wx.ID_ANY, "Resample")
    menu.Append(wx.ID_ANY, "Silence Trim")
