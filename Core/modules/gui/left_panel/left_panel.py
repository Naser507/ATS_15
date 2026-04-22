import wx

# LEFT PANEL MODULE
# Responsible ONLY for defining the left UI region

class LeftPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, style=wx.BORDER_SIMPLE)

        # This panel is intentionally EMPTY for now
        # Later we will load file tree / controls here
        
        # TEMP DEBUG VISIBILITY ONLY
        #self.SetBackgroundColour(wx.Colour(180, 180, 180))

        # DO NOT design UI manually
        # Let OS handle default appearance

        self._init_ui()

    def _init_ui(self):
        pass


def create_left_panel(parent):
    """
    Factory function so main_gui can load this module cleanly
    """
    return LeftPanel(parent)

