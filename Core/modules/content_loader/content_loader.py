# Content Loader (bridge layer between GUI and content modules)
# GUI should NEVER directly access contents/

class ContentLoader:
    def __init__(self):
        # In future: register content modules here
        self.registry = {}

    def register(self, name, module):
        """
        Register a content module
        """
        self.registry[name] = module

    def get(self, name):
        """
        Fetch content module by name
        """
        return self.registry.get(name, None)