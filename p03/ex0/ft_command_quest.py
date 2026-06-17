import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argv: list[str] = sys.argv
    nb_args: int = len(argv)
    if (nb_args - 1 == 0):
        print("No arguments provided!")
    else:
        i: int = 0
        for arg in argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {nb_args}")
