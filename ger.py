#!/usr/local/bin/python3
import sys
import time
import re

args = sys.argv
del args[0]
x = 0

program = open(args[0], 'r+').read().split('\n')
lines = len(program)
ger_stack = []
next_line = program[x + 1]

instructions = {}


def instruction(func):
    instructions[func.__name__] = func
    return func


########################
# IMPORTANT            #
# WHERE MOST CODE GOES #
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
        err(f'UNEXPECTED END OF FILE!!! FOR {program[x]} AT LINE {x + 1}!!!')


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
        err(f'UNEXPECTED END OF FILE!!! FOR {program[x]} AT LINE {x + 1}!!!')


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


if len(args) == 0 or args[0] == '--help':
    print('Usage: python3 ger.py <file>')
    print('Version: 2.0.0')
    exit()

# A class used for making exception


def err(error):
    print(f'GER: {error}')
    exit()


def ger_push(what_push: str):
    ger_stack.append(what_push)


def ger_pop():
    ger_stack.pop()


def runCode():
    ignore = program[x].startswith(
        'COMMENT: ') or program[x].replace(' ', '') == ''

    if (ignore):
        return
    if program[x] not in instructions.keys():
        err(
            f'SYNTAX ERROR: WHAT IS "{program[x]}"??? THE ERROR IS AT LINE {x + 1}!!!'
        )
    instructions[program[x]]()


while x < lines:
    runCode()
    x += 1
