import wx
from Core.modules.gui.menu.menu_strip import create_menu_bar

# GUI ORCHESTRATOR ONLY
# This file does NOT build UI elements.
# It only loads and assembles modules.


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="ATS_15", size=(900, 600))
        self.SetMinSize((700, 500))

        # Root window container
        self.panel = wx.Panel(self)

        # Build layout
        self._build_layout()

        # Load menu system
        self.SetMenuBar(create_menu_bar(self))

        self.Show()

    def _build_layout(self):
        """
        Assembles all GUI modules (no logic, no styling)
        """

        # Import modules (lazy loading)
        from Core.modules.gui.left_panel.left_panel import create_left_panel
        from Core.modules.gui.right_panel.right_panel import create_right_panel
        from Core.modules.gui.bottom_buttons.bottom_buttons import create_bottom_buttons

        # Create main vertical layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create modules
        #left = create_left_panel(self.panel)
        #right = create_right_panel(self.panel)
        #bottom = create_bottom_buttons(self.panel)

        # Create splitter
        #splitter = wx.SplitterWindow(self.panel)
        splitter = wx.SplitterWindow(self.panel)

        left = create_left_panel(splitter)
        right = create_right_panel(splitter)

        bottom = create_bottom_buttons(self.panel)




        splitter.SplitVertically(left, right, 250)

        # Set minimum sizes
        left.SetMinSize((200, -1))
        right.SetMinSize((300, -1))
        splitter.SetMinimumPaneSize(150)

        # Add to layout
        main_sizer.Add(splitter, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(bottom, 0, wx.EXPAND)

        # Apply layout
        self.panel.SetSizer(main_sizer)


def run_app():
    app = wx.App(False)
    MainFrame()
    app.MainLoop()