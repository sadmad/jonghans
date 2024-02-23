import pyfiglet
import subprocess
import os

# Generate ASCII art
ascii_art = pyfiglet.figlet_format("Junghans", font="slant")

# Save to a file
filename = "junghans_art.txt"
with open(filename, "w") as file:
    file.write(ascii_art)