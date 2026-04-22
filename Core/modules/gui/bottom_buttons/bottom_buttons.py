import wx

# BOTTOM BUTTONS MODULE
# Future area for Save / Run / Stop controls

class BottomButtons(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetMinSize((-1, 50))

        # EMPTY PLACEHOLDER ONLY
        # No buttons yet
        # No styling
        # OS handles appearance
        # TEMP DEBUG VISIBILITY ONLY
        #self.SetBackgroundColour(wx.Colour(150, 150, 150))

        self._init_ui()

    def _init_ui(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Spacer pushes buttons to the right
        sizer.AddStretchSpacer()

        # Buttons (OS decides look)
        save_btn = wx.Button(self, label="Run")
        run_btn = wx.Button(self, label="Save")

        # Add buttons to layout
        sizer.Add(save_btn, 0, wx.ALL, 5)
        sizer.Add(run_btn, 0, wx.ALL, 5)

        self.SetSizer(sizer)


def create_bottom_buttons(parent):
    """
    Factory function for modular loading
    """
    return BottomButtons(parent)