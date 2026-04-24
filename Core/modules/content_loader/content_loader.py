# Content Loader (bridge layer between GUI and content modules)
# GUI should NEVER directly access contents/

import importlib


def load_content(parent, path):
    """
    Dynamically loads a content module and returns its panel

    path example: "file.new_project"
    """

    try:
        module_path = f"Core.modules.contents.{path}"
        module = importlib.import_module(module_path)

        return module.load(parent)

    except Exception as e:
        print(f"[Content Loader Error] {e}")
        return None