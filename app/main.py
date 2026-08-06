import sys, os
from enum import StrEnum

class Command(StrEnum):
    EXIT = 'exit'
    ECHO = 'echo'
    TYPE = 'type'

BUILTIN_COMMANDS = { member.value for member in Command }

def main():
    while True:
        sys.stdout.write("$ ")
        user_input = input()

        if user_input == Command.EXIT:
            break
        elif len(user_input) >= 4 and user_input[:4] == Command.ECHO:
            first_space_pos = user_input.find(" ")
            echo_args = "" if first_space_pos == -1 else user_input[first_space_pos + 1:]
            sys.stdout.write(echo_args + "\n")
        elif len(user_input) >= 4 and user_input[:4] == Command.TYPE:
            first_space_pos = user_input.find(" ")
            command = "" if first_space_pos == -1 else user_input[first_space_pos + 1:]

            if command in BUILTIN_COMMANDS:
                sys.stdout.write("{} is a shell builtin\n".format(command))
                continue

            does_command_exist = False
            path_dirs = os.getenv("PATH").split(os.pathsep)
            for path_dir in path_dirs:
                command_path = os.path.join(path_dir, command)
                if not os.path.exists(command_path):
                    continue
                if not os.access(command_path, os.X_OK):
                    continue
                does_command_exist = True
                sys.stdout.write("{} is {}\n".format(command, command_path))
                break

            if not does_command_exist:
                sys.stdout.write("{}: not found\n".format(command))
        else:
            sys.stdout.write("{}: command not found\n".format(user_input))

"""
TODO: explain this Python idiom
"""
if __name__ == "__main__":
    main()
