import sys


def main():
    sys.stdout.write("$ ")
 
    command = input()
    sys.stdout.write("{}: command not found".format(command))

"""
TODO: explain this Python idiom
"""
if __name__ == "__main__":
    main()
