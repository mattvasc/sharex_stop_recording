import time
import sys
from datetime import timedelta, datetime

try:
	import keyboard
except ImportError:
	print("\n\nkeyboard library needed to run, please install with the command: pip install keyboard\n\n")
	sys.exit(1)

if len(sys.argv) != 2:
	print("\n\nWrong usage, correct syntax: python ssr.py <MINUTES>\n\n")
	sys.exit(1)
	
minutes = 0
try:
	minutes = int(sys.argv[1])
except:
	print("\n\nPlease input a valid number for <MINUTES> parameter\n\n")
	sys.exit(1)
print("\n\nEstimate time to stop: {}\n\n".format(datetime.now() + timedelta(minutes=minutes)))

while minutes > 0:
	print("Going to wait {} minutes before press shift + print_screen".format(minutes), end="\r")
	time.sleep(60)
	minutes = minutes - 1
	
print("\n\nSending keystroke!!")
keyboard.press_and_release("shift+print_screen")
print("\n\nDone. Credits: @mattvasc")

sys.exit(0)
