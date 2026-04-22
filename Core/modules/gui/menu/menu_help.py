import wx


def build_help_menu(menu):
    menu.Append(wx.ID_ANY, "Documentation")
    menu.Append(wx.ID_ANY, "Shortcuts")
    menu.Append(wx.ID_ANY, "About")
    
