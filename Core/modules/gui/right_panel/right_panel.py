import wx

# RIGHT PANEL MODULE
# Main workspace area (waveform / visualization / future DSP view)
'''
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

'''

import wx


class RightPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Main layout for dynamic content
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        # Track current loaded content
        self.current_content = None

    def load_content(self, content_panel):
        """
        Replaces current content with new content
        """

        # Remove old content if exists
        if self.current_content:
            self.sizer.Detach(self.current_content)
            self.current_content.Destroy()

        # Add new content
        if content_panel:
            self.current_content = content_panel
            self.sizer.Add(self.current_content, 1, wx.EXPAND)

        # Refresh layout
        self.Layout()


def create_right_panel(parent):
    return RightPanel(parent)

    