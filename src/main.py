from control_system import SpacecraftControl

control = SpacecraftControl()
print(control.execute_command("NAVIGATE", "(10, 20)"))
print(control.execute_command("COMMUNICATE", "Hello, Earth!"))