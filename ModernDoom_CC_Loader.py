import keyboard
import time
import json
import logging
import os


logging.basicConfig(
    filename='log.log',
    filemode='w',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

json_path = "commands.json"
json_backup = """{
    "command_example": [
        "(command) (value)",
        "g_fov 120 (will set fov to 120)",
        "!DO NOT ADD A COMMA TO THE LAST COMMAND IT WILL BREAK!"
    ],

    "commands": [

    ]
}"""

if not os.path.exists(json_path):
    try:
        with open(json_path, 'w') as f:
            f.write(json_backup)
        
        logging.warning(f"{json_path} not found. A default template was created.")
        print(f"{json_path} created. Please fill in your commands and run the script again\n\nThis windows will auto close in 10 seconds. Press \"ctrl+C\" to keep it open")
        time.sleep(10)
        exit(0)
    
    except Exception as e:
        logging.error(f"Failed to create {json_path}: {e}")
        print(f"Error creating {json_path}. Check the .log file for details\n\nThis windows will auto close in 10 seconds. Press \"ctrl+C\" to keep it open")
        time.sleep(10)
        exit(1)

logging.info("Started Loading Commands from commands.json")
try:
    with open('commands.json', 'r') as f:
        data = json.load(f)
        commands = data.get("commands", [])

    if not commands:
        print("No commands found in Commands.json! Please add some then re-run this program!\n\nThis windows will auto close in 10 seconds. Press \"ctrl+C\" to keep it open")
        print("\nDon't konw how to add commands? Check the github - https://github.com/Chimkins/ModernDoom-CC-Loader")
        logging.info("No commands found")
        time.sleep(10)
        exit(1)
    logging.info(f"Loaded {commands} commands(s) from commands.json")

except Exception as e:
    logging.error(f"Failed to load commands: {e}")
    print("Error loading JSON file. Check the .log file for details.")
    exit(1)


print("Please switch to the game window and press \"x\" to start the program...")

keyboard.wait('x')
logging.info("Started command input")

try:
    keyboard.send('`')
    time.sleep(0.3)

    for cmd in commands:
        keyboard.write(cmd)
        keyboard.send('enter')
        logging.info(f"Sent command: {cmd}")
        time.sleep(0.3)

    logging.info("All commands sent successfully.")

except Exception as e:
    logging.error(f"Error during command execution: {e}")
    print("An error occurred. Check the.log file for details.")

keyboard.send("`")
print("\nConsole commands ran Successfully!\n\nThis windows will auto close in 10 seconds. Press \"ctrl+C\" to keep it open")
print("\nDid something go wrong? Check the .log file to see what happend!")
time.sleep(10)
exit(1)
