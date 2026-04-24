import wx


def create_left_panel(parent):
    """
    Creates the left panel with:
    - Scrollable container
    - Tree view (project structure)
    """

    # Root panel (this is what main_gui receives)
    panel = wx.Panel(parent)

    # Scrollable container (enables both scroll directions)
    scroll = wx.ScrolledWindow(panel, style=wx.VSCROLL | wx.HSCROLL)
    scroll.SetScrollRate(5, 5)

    # Tree control (project structure)
    tree = wx.TreeCtrl(scroll)

    # Dummy data (for testing)
    #root = tree.AddRoot("Project")
    #tree.AppendItem(root, "audio_1.wav")
    #tree.AppendItem(root, "audio_2.wav")
    #tree.ExpandAll()

    # Dummy data (for proper scroll testing)
    root = tree.AddRoot("Very_Long_Project_Name_For_Testing_Scrolling")

    # Simulate folders
    audio_folder = tree.AppendItem(root, "audio_files_with_long_names")
    converted_folder = tree.AppendItem(root, "converted_outputs_directory")
    results_folder = tree.AppendItem(root, "dsp_results_and_artifacts")

    # Add many items to force vertical scroll
    for i in range(30):
        tree.AppendItem(audio_folder, f"very_long_audio_filename_number_{i}_example.wav")

        # Add long names to force horizontal scroll
        tree.AppendItem(converted_folder, "extremely_long_converted_filename_example_output_version_final.wav")
        tree.AppendItem(results_folder, "very_long_dsp_result_file_name_with_extra_details.txt")

        tree.ExpandAll()




    # Layout inside scroll area
    scroll_sizer = wx.BoxSizer(wx.VERTICAL)
    scroll_sizer.Add(tree, 1, wx.EXPAND)
    scroll.SetSizer(scroll_sizer)

    # Layout for panel
    main_sizer = wx.BoxSizer(wx.VERTICAL)
    main_sizer.Add(scroll, 1, wx.EXPAND)
    panel.SetSizer(main_sizer)

    return panel
