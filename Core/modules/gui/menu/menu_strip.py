import wx
from Core.modules.gui.menu.menu_file import build_file_menu
from Core.modules.gui.menu.menu_view import build_view_menu
from Core.modules.gui.menu.menu_dsp import build_dsp_menu
from Core.modules.gui.menu.menu_process import build_process_menu
from Core.modules.gui.menu.menu_converter import build_converter_menu
from Core.modules.gui.menu.menu_settings import build_settings_menu
from Core.modules.gui.menu.menu_help import build_help_menu



def create_menu_bar(frame):
    menu_bar = wx.MenuBar()

    # Create empty menus (no items yet)
    menus = {
        "File": wx.Menu(),
        "View": wx.Menu(),
        "DSP": wx.Menu(),
        "Process": wx.Menu(),
        "Settings": wx.Menu(),
        "Converter": wx.Menu(),
        "Help": wx.Menu(),
    }

    build_file_menu(menus["File"])
    build_view_menu(menus["View"])
    build_dsp_menu(menus["DSP"])
    build_process_menu(menus["Process"])
    build_converter_menu(menus["Converter"])
    build_settings_menu(menus["Settings"])
    build_help_menu(menus["Help"])


    # Attach menus to menu bar
    for name, menu in menus.items():
        menu_bar.Append(menu, name)

    # Store reference in frame (for future modular loading)
    frame.menus = menus

    return menu_bar