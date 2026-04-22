import wx
from Core.modules.gui.menu.menu_strip import create_menu_bar

# GUI ORCHESTRATOR ONLY
# This file does NOT build UI elements.
# It only loads and assembles modules.

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="ATS_15", size=(900, 600))

        # Root window container
        self.panel = wx.Panel(self)

        # Placeholder: GUI modules will attach themselves here later
        self._build_layout()

        # Load menu system (already modular)
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

        # Create main vertical layout (left/right + bottom section)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Horizontal layout for left + right panels
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create modules
        left = create_left_panel(self.panel)
        right = create_right_panel(self.panel)
        bottom = create_bottom_buttons(self.panel)

        # Add left/right into top area
        top_sizer.Add(left, 1, wx.EXPAND | wx.ALL, 5)
        top_sizer.Add(right, 3, wx.EXPAND | wx.ALL, 5)

        # Assemble full layout
        main_sizer.Add(top_sizer, 1, wx.EXPAND)
        main_sizer.Add(bottom, 0, wx.EXPAND)

        # Attach to root panel
        self.panel.SetSizer(main_sizer)


def run_app():
    app = wx.App(False)
    MainFrame()
    app.MainLoop()