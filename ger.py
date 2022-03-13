#!/usr/local/bin/python3
import sys
args = sys.argv
del args[0]
x = 0
program = open(args[0], 'r+').read().split('\n')
lines = len(program)
ger_var = 'A default string (you or the creator did something wrong)'
next_line = program[x + 1]

# A class used for making exception
class WHAT(Exception):
	pass

# Run commands
while x < lines:
	if program[x] == 'ger':
		print(next_line)
	elif program[x] == 'GER':
		ger_var = input()
	elif program[x] == 'Ger':
		print(ger_var)
	elif program[x] == 'gEr':
		ger_var = next_line
	else:
		raise WHAT('WHAT IS THAT (unknown instruction)??')
	x += 1
