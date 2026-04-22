import wx

# RIGHT PANEL MODULE
# Main workspace area (waveform / visualization / future DSP view)

class RightPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, style=wx.BORDER_SIMPLE)

        # EMPTY BY DESIGN
        # No UI elements yet
        # No styling
        # No layout logic

        # TEMP DEBUG VISIBILITY ONLY
        #self.SetBackgroundColour(wx.Colour(200, 200, 200))

        self._init_ui()

    def _init_ui(self):
        pass


def create_right_panel(parent):
    """
    Factory function for modular loading
    """
    return RightPanel(parent)