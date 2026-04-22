import wx


def build_file_menu(menu):
    # Simple flat structure (as you chose)

    menu.Append(wx.ID_ANY, "New Project")
    menu.Append(wx.ID_ANY, "Open Project")
    menu.Append(wx.ID_ANY, "Import Audio")
    menu.Append(wx.ID_ANY, "Export Render")
    menu.Append(wx.ID_ANY, "Recent Files")
    menu.AppendSeparator()
    menu.Append(wx.ID_EXIT, "Exit") 

    