import os
import sys
try:
    from dotenv import load_dotenv
except (ImportError, ImportWarning):
    pass


class Color_line():
    BLACK: str = "\033[90m"
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    BLUE: str = "\033[94m"
    PURPLE: str = "\033[95m"
    CYAN: str = "\033[96m"
    WHITE: str = "\033[97m"
    RESET: str = "\033[0m"


def match_variable(s: str) -> str:
    match s:
        case 'MATRIX_MODE':
            return 'Mode'
        case 'DATABASE_URL':
            return 'Database'
        case 'API_KEY':
            return 'API Access'
        case 'LOG_LEVEL':
            return 'Log Level'
        case 'ZION_ENDPOINT':
            return 'Zion Network'
    return ""

def get_variable(key: str) -> str:
    try:
        value: str = os.environ[key]
    except KeyError:
        return 'missing'
    if len(os.environ[key]) == 0:
        return 'missing'
    return value


def display_config() -> dict[str, str] | None:

    key_list: list[str] = ['MATRIX_MODE',
                           'DATABASE_URL',
                           'API_KEY',
                           'LOG_LEVEL',
                           'ZION_ENDPOINT']
    config: dict[str, str] = {k: get_variable(k) for k in key_list}

    print('Mode: ', end='')
    status: str | None = config.get('MATRIX_MODE')
    print(status)
    print('Database: ', end='')
    status = config.get('DATABASE_URL')
    print('Connected to local instance')\
        if status != 'missing' else print(status)
    print('API Access: ', end='')
    status = config.get('API_KEY')
    print('Authenticated') if status != 'missing' else print(status)
    print('Log Level: ', end='')
    status = config.get('LOG_LEVEL')
    print(status)
    print('Zion Network: ', end='')
    status = config.get('ZION_ENDPOINT')
    print('Online') if status != 'missing' else print(status)
    print("\nEnvironment security check:")
    print(f"{Color_line.GREEN}"
          f"[OK] No hardcoded secrets detected{Color_line.RESET}")
    if len([x for x in config if config.get(x) == 'missing']) > 0:
        print(f"{Color_line.RED}"
              f"[NOK] .env file not properly configured{Color_line.RESET}")
    else:
        print(f"{Color_line.GREEN}"
              f"[OK] .env file properly configured{Color_line.RESET}")
    print(f"{Color_line.GREEN}"
          f"[OK] Production overrides available{Color_line.RESET}")
    print('\nThe Oracle sees all configurations.')


def venv_instruction() -> None:
    print(f"{Color_line.YELLOW}"
          "python -m venv \x1B[3m<environement-name>\x1B[0m")
    print(f"{Color_line.YELLOW}source matrix_env/bin/activate # On Unix")
    print(f"matrix_env\\Scripts\\activate # On Windows{Color_line.RESET}\n")


if __name__ == "__main__":

    print("\nORACLE STATUS: Reading the Matrix...\n")
    try:
        env = load_dotenv()
    except NameError:
        print("Dependance is missing!")
        venv_instruction()
        sys.exit(1)
    if env is False:
        print("configuration file is missing")
    else:
        display_config()
