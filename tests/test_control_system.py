import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.control_system import SpacecraftControl
import pytest

def test_navigate_command():
    control = SpacecraftControl()
    result = control.execute_command("NAVIGATE", "(10, 20)")
    assert result == "Navigating to coordinates: (10, 20)"

def test_communicate_command():
    control = SpacecraftControl()
    result = control.execute_command("COMMUNICATE", "Hello, Earth!")
    assert result == "Sending message: Hello, Earth!"

def test_diagnostic_command():
    control = SpacecraftControl()
    result = control.execute_command("DIAGNOSTIC", "System check")
    assert result == "Running diagnostics: System check"

def test_invalid_command_raises_error():
    control = SpacecraftControl()
    with pytest.raises(NotImplementedError, match="Unknown command: INVALID"):
        control.execute_command("INVALID", "No data")