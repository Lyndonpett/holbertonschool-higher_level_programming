#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argLength = (len(sys.argv) - 1)

    if argLength == 0:
        print("{:d} arguments.".format(0, sys.argv[argLength]))

    if argLength == 1:
        print("{:d} argument:".format(1))

    if argLength > 1:
        print("{:d} arguments:".format(argLength))

    for i in range(1, (argLength + 1)):
        print("{:d}: {}".format(i, sys.argv[i]))
