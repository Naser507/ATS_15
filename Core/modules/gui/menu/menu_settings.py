import wx


def build_settings_menu(menu):
    menu.Append(wx.ID_ANY, "Audio Device")
    menu.Append(wx.ID_ANY, "Theme")
    menu.Append(wx.ID_ANY, "Paths")
    menu.Append(wx.ID_ANY, "Keybindings")
