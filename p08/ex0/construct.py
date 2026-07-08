import sys
import site


def interpreter() -> str | None:
    path: str = sys.executable
    python: str = path.split('/')[len(path.split('/')) - 1]
    if python == 'python':
        return f"{sys.executable}{sys.version_info[0]}.{sys.version_info[1]}"
    elif python == "python3":
        return f"{sys.executable}.{sys.version_info[1]}"
    return None


def get_vitual_env() -> str:
    path: str = sys.prefix
    venv: str = path.split("/")[len(path.split("/")) - 1]
    return venv


def instruction() -> None:
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")


if __name__ == "__main__":
    if sys.base_prefix == sys.prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {interpreter()}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment")
        print("The machines can see everything you install.\n")
        instruction()
        print("Then run this program again")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {interpreter()}")
        print(f"Virtual Environment: {get_vitual_env()}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")
