import sys

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break
        sys.stdout.write("{}: command not found\n".format(command))

"""
TODO: explain this Python idiom
"""
if __name__ == "__main__":
    main()
