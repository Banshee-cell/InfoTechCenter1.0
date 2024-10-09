import sys  # Importing the sys module for system-specific parameters and functions
import time  # Importing the time module to use time-related functionsimport sys  # Importing the sys module for system-specific parameters and functions
import time  # Importing the time module to use time-related functions

# ANSI escape codes for colors
class TextColors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RESET = '\033[0m'  # Reset color

# Welcome message for the user
print(f"\n{TextColors.CYAN}Welcome to InfoTechCenter V1.0{TextColors.RESET}\n")

# Initialize counters for the boot process
x = 0  # Counter for booting iterations
ellipsis = 0  # Counter for the ellipsis effect

# Loop to simulate the system booting process
while x != 20:
    x += 1  # Increment the boot counter
    # Create a booting message with an ellipsis effect and cyan color
    message = f"{TextColors.CYAN}InfoTech Center System Booting" + "." * ellipsis + f"{TextColors.RESET}"
    ellipsis += 1  # Increment the ellipsis counter
    sys.stdout.write("\r" + message)  # Overwrite the current line with the message
    time.sleep(0.5)  # Pause for half a second

    # Reset ellipsis counter after reaching 4 dots
    if ellipsis == 4:
        ellipsis = 0

    # Check if the boot process is complete
    if x == 20:

        # Green color for the final success message
        print(f"\n\n{TextColors.GREEN}Operating System Booted Up - Retina Scanned - Access Granted{TextColors.RESET}")
   
