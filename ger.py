#!/usr/local/bin/python3
import sys
import time

args = sys.argv
del args[0]
x = 0
if not args[0] == '--help':
	program = open(args[0], 'r+').read().split('\n')
	lines = len(program)
	ger_stack = []
	next_line = program[x + 1]

	# A class used for making exception
	class WHAT(Exception):
		pass
	
	def ger_push(what_push):
		ger_stack.append(what_push)
	
	def ger_pop():
		ger_stack.pop()
	
	#### Note:
	# x += 1
	# skips a line
	####
	
	# Run commands
	while x < lines:
		if program[x] == 'ger':
			try:
				if program[x + 1] == '(newline)':
					print('\n', end = '')
				elif program[x + 1] == '(space)':
					print(' ', end = '')
				else:
					print(program[x + 1], end = '')
				x += 1
			except:
				raise WHAT('UNEXPECTED END OF FILE!!!')
		elif program[x] == 'GER':
			ger_push(str(input()))
		elif program[x] == 'Ger':
			print(ger_stack[len(ger_stack) - 1], end = '')
			ger_pop()
		elif program[x] == 'gEr':
			try:
				ger_push(next_line)
			except:
				# End of file when something else needed
				raise WHAT('UNEXPECTED END OF FILE!!!')
		elif program[x] == 'geR':
			time.sleep(int(next_line))
			x += 1
		elif program[x] == 'ge r':
			# Does truth-machine thing
			if int(ger_stack[len(ger_stack) - 1]) == 1:
				while True:
					print(1)
			print(0)
			ger_pop()
		elif program[x] == 'GEr':
			sys.exit('GEr INSTRUCTION DETECTED!!!!')
		elif program[x] == '':
			pass
		else:
			# Error thing
			
			raise WHAT(f'GER: SYNTAX ERROR: {program[x]} AT LINE {x + 1}!!!')
		x += 1

else:
	print('Usage: python3 ger.py <file>')
	print('Version: 1.3.1')
