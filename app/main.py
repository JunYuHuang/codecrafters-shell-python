import sys

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        if command == "exit":
            break
        elif len(command) >= 4 and command[:4] == "echo":
            first_space_pos = command.find(" ")
            echo_args = "" if first_space_pos == -1 else command[first_space_pos + 1:]
            sys.stdout.write(echo_args + "\n")
        else:
            sys.stdout.write("{}: command not found\n".format(command))

"""
TODO: explain this Python idiom
"""
if __name__ == "__main__":
    main()
