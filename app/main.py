import sys
from enum import StrEnum

class Command(StrEnum):
    EXIT = 'exit'
    ECHO = 'echo'
    TYPE = 'type'

BUILTIN_COMMANDS = { member.value for member in Command }

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        if command == Command.EXIT:
            break
        elif len(command) >= 4 and command[:4] == Command.ECHO:
            first_space_pos = command.find(" ")
            echo_args = "" if first_space_pos == -1 else command[first_space_pos + 1:]
            sys.stdout.write(echo_args + "\n")
        elif len(command) >= 4 and command[:4] == Command.TYPE:
            first_space_pos = command.find(" ")
            type_arg = "" if first_space_pos == -1 else command[first_space_pos + 1:]
            if type_arg in BUILTIN_COMMANDS:
                sys.stdout.write("{} is a shell builtin\n".format(type_arg))
            else:
                sys.stdout.write("{}: not found\n".format(type_arg))
        else:
            sys.stdout.write("{}: command not found\n".format(command))

"""
TODO: explain this Python idiom
"""
if __name__ == "__main__":
    main()
