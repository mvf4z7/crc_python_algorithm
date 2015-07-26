
The input frame should be echoed to the generate.py program. The output from generate can be directly verified through the verify.py program or first altered through the alter.py program.

An example of how the programs should be run is below. This example is taken from page 114 in the textbook. As stated in the project instructions, the 32 bit ethernet generator was used, so this example will only run if the variable GENERATOR on line 20 of the generate.py file is commented out, and line 21 is uncommented.


Example:
echo 1101011111 | python generate.py | python alter.py 1 | python verify.py