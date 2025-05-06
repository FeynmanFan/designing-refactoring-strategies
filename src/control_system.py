class SpacecraftControl:
    def execute_command(self, command_type, data):
        if command_type == "NAVIGATE":
            return f"Navigating to coordinates: {data}"
        elif command_type == "COMMUNICATE":
            return f"Sending message: {data}"
        elif command_type == "DIAGNOSTIC":
            return f"Running diagnostics: {data}"
        else:
            raise NotImplementedError(f"Unknown command: {command_type}")