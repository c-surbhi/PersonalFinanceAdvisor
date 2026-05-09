class BaseAgent:
    def __init__(self, name):
        self.name = name

    def process(self, query, context=None):
        """Process the query and return a response."""
        raise NotImplementedError("Subclasses must implement process method.")