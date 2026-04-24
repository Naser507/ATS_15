import wx


def build_file_menu(menu, frame):
    # Create menu items
    new_project = menu.Append(wx.ID_ANY, "New Project")
    open_project = menu.Append(wx.ID_ANY, "Open Project")
    import_audio = menu.Append(wx.ID_ANY, "Import Audio")
    export_render = menu.Append(wx.ID_ANY, "Export Render")
    recent_files = menu.Append(wx.ID_ANY, "Recent Files")

    menu.AppendSeparator()
    exit_item = menu.Append(wx.ID_EXIT, "Exit")

    # Disable all except New Project
    open_project.Enable(False)
    import_audio.Enable(False)
    export_render.Enable(False)
    recent_files.Enable(False)

    # Bind New Project action
    from Core.modules.content_loader.content_loader import load_content

    def on_new_project(event):
        content = load_content(frame.right_panel, "file.new_project")
        if content:
            frame.right_panel.load_content(content)

    frame.Bind(wx.EVT_MENU, on_new_project, new_project)

    # Exit binding (good practice)
    frame.Bind(wx.EVT_MENU, lambda e: frame.Close(), exit_item)