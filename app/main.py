import sys, os, re, subprocess
from enum import StrEnum

class Command(StrEnum):
    EXIT = 'exit'
    ECHO = 'echo'
    TYPE = 'type'
    PWD = 'pwd'
    CD = 'cd'

BUILTIN_COMMANDS = { member.value for member in Command }

def main():
    while True:
        sys.stdout.write("$ ")
        user_input = input()

        if re.match(rf"^{Command.EXIT}$", user_input):
            break
        elif re.match(rf"^{Command.ECHO}.*$", user_input):
            first_space_pos = user_input.find(" ")
            echo_args = "" if first_space_pos == -1 else user_input[first_space_pos + 1:]
            sys.stdout.write(echo_args + "\n")
        elif re.match(rf"^{Command.TYPE}.*$", user_input):
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
        elif re.match(rf"^{Command.PWD}$", user_input):
            sys.stdout.write(f"{os.getcwd()}\n")
        elif re.match(rf"^{Command.CD}(\s(\S)*)?$", user_input):
            first_space_pos = user_input.find(" ")
            target_dir = "" if first_space_pos == -1 else user_input[first_space_pos + 1:]
            if os.path.exists(target_dir):
                os.chdir(os.path.realpath(target_dir))
            else:
                sys.stdout.write(f"cd: {target_dir}: No such file or directory\n")
        elif re.match(rf"^(\S)+(\s(\S))*", user_input):
            args = user_input.split(" ")
            command = args[0]
            does_command_exist = False
            path_dirs = os.getenv("PATH").split(os.pathsep)
            for path_dir in path_dirs:
                command_path = os.path.join(path_dir, command)
                if not os.path.exists(command_path):
                    continue
                if not os.access(command_path, os.X_OK):
                    continue
                does_command_exist = True
                command_args = args if len(args) > 1 else [command]
                subprocess.run([*command_args])
                break
            if not does_command_exist:
                sys.stdout.write(f"{user_input}: command not found\n")
        else:
            sys.stdout.write(f"{user_input}: command not found\n")
"""
TODO: explain this Python idiom
"""
if __name__ == "__main__":
    main()
