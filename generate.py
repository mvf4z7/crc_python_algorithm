from sys import stdin
from utilities import mod2_div

error_message = "\n\nThis script takes one argument, which is the binary frame that is to be CRC encoded."
error_message += "\nThis argument may be piped through the use of echo or can be entered after"
error_message += "the script is run.\nIf you choose the latter, press ctrl-D to end std input after"
error_message += "pressing enter.\n\nExample:  echo 1000101001 | python generate.py"

piped_input = stdin.readlines()
if len(piped_input) > 1:
	raise ValueError(error_message)

piped_input = piped_input[0].replace("\n", "")

for char in piped_input:
	if char != "0" and char != "1":
		raise ValueError(error_message)

FRAME = piped_input
GENERATOR = "100000100110000010001110110110111"
#GENERATOR = "10011"

generator_degree = len(GENERATOR) - 1
FRAME = FRAME + ("0" * generator_degree)

division = mod2_div(FRAME, GENERATOR)

tx = bin(int(FRAME, 2) ^ int(division["remainder"],2))[2:]
print tx


