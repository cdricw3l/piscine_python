import typing
import sys

if __name__ == "__main__":
    print(sys.stdin.fileno())
    print(sys.stdout.fileno())
    fd: typing.IO = open(sys.stdin.fileno(), 'r')
    print(fd.isatty())