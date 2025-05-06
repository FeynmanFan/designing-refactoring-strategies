from base_command import Command

class NavigateCommand(Command):
    def execute(self, data):
        return f"Navigating to coordinates: {data}"