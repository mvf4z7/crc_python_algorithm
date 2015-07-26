from sys import argv, stdin
from utilities import flip_bit

error_message = "\n\nThis script takes two arguments. One argument should be a binary string "
error_message += "\nthat is piped in. The second argument is provided on the command line "
error_message += "\nand represents the index of the binary number that should be flipped, "
error_message += "\nstarting from the left with an index of 1." 
error_message += "\n\nExample:  echo 11010111110010 | python alter.py 3"

piped_input = stdin.readlines()
if len(piped_input) > 1:
	raise ValueError(error_message)

piped_input = piped_input[0].replace("\n", "")

for char in piped_input:
	if char != "0" and char != "1":
		raise ValueError(error_message)

if len(argv) != 2:
	raise ValueError(error_message)

idx = argv[1]
try:
	idx = int(idx)
except:
	raise ValueError(error_message)

valid_indexs = [num + 1 for num in xrange(len(piped_input))]
if idx not in valid_indexs:
	raise ValueError(error_message)

# Input index starts at 1
idx = idx - 1

# All input validated at this point
flipped_bit = flip_bit(piped_input[idx])
altered_input = piped_input[:idx] + flipped_bit + piped_input[idx+1:]

print altered_input
