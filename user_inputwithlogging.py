# user input
# uses the command "input()" (no commas)

import webbrowser
import logging

logging.basicConfig(
    filename="login_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

name = input("Enter your username: ").strip()
if not name:
    logging.warning("Login failed - empty username entered")
    print("That's not a valid username (for more information visit www.system.com)")
    input("Press enter to exit")
    exit()

with open("banned_words_userinput.txt", "r", encoding="utf-8") as f:
    BANNED_WORDS = [line.strip() for line in f if line.strip()]

if any(bad_word.lower() in name.lower() for bad_word in BANNED_WORDS):
    logging.warning(f"Login failed - inappropriate username attempted: '{name}'")
    print("That's not an appropriate username.")
    input("Press Enter to exit...")
    exit()

SYSTEM_PASSWORD = "systemsoft123"
userinput = input("Enter the password you were given (for more information visit www.system.com):")
if userinput != SYSTEM_PASSWORD:
    logging.warning(f"Login failed - wrong password entered by username: '{name}'")
    print("That's not a valid password (for more information visit www.system.com)")
    input("Press enter to exit")
    exit()

try:
    age = int(input("Enter your age: "))
except ValueError:
    logging.warning(f"Login failed - non-numeric age entered by username: '{name}'")
    print("Please enter a valid age (for more information visit www.system.com)")
    input("Press enter to exit")
    exit()

if age < 18:
    logging.warning(f"Login failed - age too low ({age}) for username: '{name}'")
    print("You need to be 18 years old or older to sign in (for more information visit www.system.com)")
    input("Press enter to exit")
    exit()

elif age > 122:
    logging.warning(f"Login failed - unrealistic age ({age}) for username: '{name}'")
    print("Please enter a realistic age (for more information visit www.system.com)")
    input("Press enter to exit")
    exit()

else:
    logging.info(f"Login successful - username: '{name}', age: {age}")
    print(f"{name} logged in")
    webbrowser.open("https://hackertyper.net/")

input("Press Enter to continue...")