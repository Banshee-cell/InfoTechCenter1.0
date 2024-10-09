import sys  # Importing the sys module for system-specific parameters and functions
import time  # Importing the time module to use time-related functions

# Welcome message for the user
print("\nWelcome to InfoTechCenter V1.0\n")

# Initialize counters for the boot process
x = 0  # Counter for booting iterations
ellipsis = 0  # Counter for the ellipsis effect

# Loop to simulate the system booting process
while x != 20:
    x += 1  # Increment the boot counter
    # Create a booting message with an ellipsis effect
    message = "InfoTech Center System Booting" + "." * ellipsis
    ellipsis += 1  # Increment the ellipsis counter
    sys.stdout.write("\r" + message)  # Overwrite the current line with the message
    time.sleep(0.5)  # Pause for half a second

    # Reset ellipsis counter after reaching 4 dots
    if ellipsis == 4:
        ellipsis = 0

    # Check if the boot process is complete
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")
