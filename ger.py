#!/usr/local/bin/python3
import sys
import time

args = sys.argv
del args[0]
x = 0
if not args[0] == '-h':
	program = open(args[0], 'r+').read().split('\n')
	lines = len(program)
	ger_var = None
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
		elif program[x] == "geR":
			time.sleep(int(next_line))
			x += 1
		else:
			# Just-A-Unity-Dev made most of this error except capitalization
			raise WHAT(f'GERRRRR: SYNTAX EERROR, UNKNOWN INSTRUCTION AT LINE {x}!!!!!! AAAAAAAAAAA')
		x += 1

else:
	print('Usage: ger <file>')
	print('Version: 1.0.2')
