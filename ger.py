#!/usr/local/bin/python3
import sys
import time
import re

args = sys.argv
del args[0]
x = 0

if len(args) == 0 or args[0] == '--help':
    print('Usage: python3 ger.py <file>')
    print('Version: 2.0.0')
    exit()

program = open(args[0], 'r+').read().split('\n')
lines = len(program)
ger_stack = []
next_line = program[x + 1]

instructions = {}

# A class used for making exception
def err(error):
    print(f'GER: {error}')
    exit()

def ger_push(what_push: str):
    ger_stack.append(what_push)

def ger_pop():
    ger_stack.pop()

def instruction(func):  
    if program[x] == func.__name__:
        instructions[func.__name__] = func

    return func

def runCode():
    global x
    if not program[x] in instructions.keys() and program[x]:
        err(
            f'SYNTAX ERROR: WHAT IS "{program[x]}"??? THE ERROR IS AT LINE {x + 1}!!!'
        )
        
    for intruction in instructions.values():
        intruction()


#############
# Note:
# x += 1
# skips a line
#############

# Interprets the code
def interpret():
    global x
    if program[x].startswith('COMMENT: ') or program[x] == '':
        pass

    runCode()

    x += 1


########################
# IMPORTANT
# WHERE MOST CODE GOES 
########################
@instruction
def ger():
    global x

    try:
        str_array = re.split('; ', program[x + 1])
    except IndexError:
        str_array = ['', '']

    try:
        if str_array[1] == 'insert_newline':
            print('\n', end='')
        elif str_array[1] == 'insert_space':
            print(' ', end='')
        else:
            print(str_array[1], end='')
        x += 1
    except:
        err('UNEXPECTED END OF FILE!!!')

@instruction
def GER():
    ger_push(str(input()))

@instruction
def Ger():
    print(ger_stack[len(ger_stack) - 1], end='')
    ger_pop()

@instruction
def gEr():
    try:
        ger_push(next_line)
    except:
        # End of file when something else needed
        err('UNEXPECTED END OF FILE!!!')

@instruction
def geR():
    time.sleep(int(next_line))
    x += 1

@instruction
def ge_r():
    # Does truth-machine thing
    if int(ger_stack[len(ger_stack) - 1]) == 1:
        while True:
            print(1)
    print(0)
    ger_pop()
########################
# IMPORTANT
# WHERE MOST CODE GOES 
########################


# Interprets every line
while x < lines: interpret()