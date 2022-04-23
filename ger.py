#!/usr/local/bin/python3
from ast import arg
from inspect import signature
import string
import sys
import time
import re

args = sys.argv
del args[0]
x = 0

if len(args) == 0 or args[0] == '--help':
    print('Usage: python3 ger.py <file>')
    print('Version: 1.6.0')
    exit()

program = open(args[0], 'r+').read().split('\n')
lines = len(program)
ger_stack = []
next_line = program[x + 1]

def err(error):
    print(f'GER: {error}')
    exit()

instructions = {}
def instruction(func):
    def inner():
        global x
        argcount = len(signature(func).parameters)
        args = []
        argnum = 1

        while argnum <= argcount:
            try:
                args.append(program[x + argnum])
            except IndexError:
                err(f'UNEXPECTED END OF FILE FOR INSTRUCTION {program[x]}')

            argnum += 1

        x += argcount
        func(*args)
    

    instructions[func.__name__] = inner
    return inner


########################
# IMPORTANT            #
# WHERE MOST CODE GOES #
########################
@instruction
def ger(text):
    text = text.split("; ")[1]
    global x
    if not text.startswith("; "):
        err(f'INVALID INPUT OF "ger". Did you forget to put "; " at the start? ({x + 1})')
    elif text == 'insert_newline':
        print('\n', end='')
    elif text == 'insert_space':
        print(' ', end='')
    else:
        text = text.split("; ")[1]
        print(text, end='')


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
        ger_push(program[x + 1].split('; ', )[1])
        x += 1
    except:
        # End of file when something else needed
        err(f'UNEXPECTED END OF FILE!!! {program[x]} AT LINE {x + 1}!!!')

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
# IMPORTANT            #
# WHERE MOST CODE GOES #
########################

def ger_push(what_push: str):
    ger_stack.append(what_push)

def ger_pop():
    ger_stack.pop()

def runCode():
    ignore = program[x].startswith('COMMENT: ') or program[x].replace(' ', '') == ''

    if (ignore): return
    if (not program[x] in instructions.keys()):
        err(
            f'SYNTAX ERROR: WHAT IS "{program[x]}"??? THE ERROR IS AT LINE {x + 1}!!!'
        )
    instructions[program[x]]()

while x < lines: 
    runCode()
    x += 1
