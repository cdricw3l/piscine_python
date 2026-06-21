import sys
import typing


if __name__ == "__main__":
    args: list[str] =  sys.argv
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{args[1]}'\n---")
            fd: typing.IO = open(args[1])
            line = fd.read()
            print("")
            print(line)
            fd.close()
            print(f"\nFile '{args[1]}' closed.\n---")
        except (FileNotFoundError,PermissionError) as e:
            print(f"Error opening file '{args[1]}': {e}")

        