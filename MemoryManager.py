class MemoryManager:

    def __init__(self):
        self.memory = None

    def store(self, value):
        self.memory = value

    def recall(self):
        return self.memory if self.memory else ""

    def clear(self):
        self.memory = None
