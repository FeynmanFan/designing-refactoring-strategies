import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.navigate_command import NavigateCommand
from src.communicate_command import CommunicateCommand
from src.diagnostic_command import DiagnosticCommand

class SpacecraftControl:
    def __init__(self):
        self.commands = {
            "NAVIGATE": NavigateCommand(), 
            "COMMUNICATE": CommunicateCommand(), 
            "DIAGNOSTIC": DiagnosticCommand()
        }

    def execute_command(self, command_type, data):
        command = self.commands.get(command_type)
        if command != None:
            return command.execute(data)

        raise NotImplementedError(f"Unknown command: {command_type}")