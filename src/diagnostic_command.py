import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.base_command import Command

class DiagnosticCommand(Command):
    def execute(self, data):
        return f"Running diagnostics: {data}"