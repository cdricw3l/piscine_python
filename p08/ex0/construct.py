import sys
import site

def venv_instruction() -> None:
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.prefix}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment")
        print("The machines can see everything you install.\n")
        venv_instruction()
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {site.getusersitepackages()}")
        print(f"Environment Path: {sys.exec_prefix}")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")
        # print(f"Environment Path: {sys.base_exec_prefix}")

    