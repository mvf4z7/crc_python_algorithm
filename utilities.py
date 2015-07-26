def mod2_div(dividend, divisor):
	"""
	Parameters should be string representations of
	binary numbers.
	"""
	quotient = ""
	remainder = ""

	operand1 = dividend[:len(divisor)]
	idx = len(divisor)
	while(True):
		operand2 = divisor
		if(len(operand1) < len(divisor)):
			operand2 = "0" * len(divisor)
			quotient += "0"
		else:
			quotient += "1"

		xor_result = bin(int(operand1, 2) ^ int(operand2, 2))[2:]

		if(idx + 1 > len(dividend)):
			remainder = xor_result
			break

		operand1 = xor_result + dividend[idx]
		idx += 1

	return {
		"quotient": quotient,
		"remainder": remainder
	}

def flip_bit(bit):
	"""
	The bit parameter should be a string that
	is a 0 or 1.
	"""

	if type(bit) != str:
		raise TypeError("The input parameter should be of string type.")

	if bit != "0" and bit != "1":
		raise ValueError("The parameter should be a 0 or 1, encoded as a string")

	if bit == "0":
		return "1"
	else:
		return "0"


if __name__ == "__main__":

	"""
	A small test for the mod2_div function.  The numbers are taken 
	from the example on page 214 of the book.
	"""

	frame = "11010111110000"
	generator = "10011"

	result = mod2_div(frame, generator)

	print "quotient: %s" % result["quotient"]
	print "remainder: %s" % result["remainder"]
	print ""

	tx = "11010111110010"
	generator = "10011"

	result = mod2_div(tx, generator)

	print "quotient: %s" % result["quotient"]
	print "remainder: %s" % result["remainder"]

