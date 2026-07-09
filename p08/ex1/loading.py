from importlib import util, metadata
import sys

try:
    import pandas as pd  # type: ignore[import-untyped]
except (ImportError, ImportWarning):
    pass
try:
    import numpy as np  # type: ignore[import-not-found]
except (ImportError, ImportWarning):
    pass
try:
    import matplotlib.pyplot as plt  # type: ignore[import-not-found]
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


def venv_instruction() -> None:
    print(f"{Color_line.YELLOW}"
          "python -m venv \x1B[3m<environement-name>\x1B[0m")
    print(f"{Color_line.YELLOW}source matrix_env/bin/activate # On Unix")
    print(f"matrix_env\\Scripts\\activate # On Windows{Color_line.RESET}\n")


def get_plot_color(key: str) -> str | None:
    match key:
        case '< 100':
            return 'bo'
        case '101/200':
            return 'ro'
        case '201/300':
            return 'go'
        case '301/400':
            return 'yo'
        case '401/500':
            return 'co'
    return None


def get_pie_color(key: str) -> str | None:
    match key:
        case '< 100':
            return 'blue'
        case '101/200':
            return 'red'
        case '201/300':
            return 'green'
        case '301/400':
            return 'yellow'
        case '401/500':
            return 'cyan'
    return None


def create_data_set() -> None:

    arr: np.typing.NDArray = np.random.randint(
        low=0, high=500, size=(1, 1000)).round(2)
    print("\nAnalyzing Matrix data...")
    frame = pd.DataFrame({"value": arr[0]})
    sets: dict[str, pd.DataFrame] = {
        '< 100': frame.query('value <= 100'),
        '101/200': frame.query('value > 100 and value <= 200'),
        '201/300': frame.query('value > 200 and value <= 300'),
        '301/400': frame.query('value > 300 and value <= 400'),
        '401/500': frame.query('value > 400 and value <= 500'),
    }
    print("Processing 1000 data points...")
    fig, ax = plt.subplots(2)
    pie: list[int] = [len(list(sets[x]['value'])) for x in sets]
    label: list[str] = [x for x in sets]
    color: list[str | None] = [get_pie_color(x) for x in sets]

    ax[1].set_xlabel('distribution index')
    ax[1].set_ylabel('distribution value')
    for x in sets:
        ax[0].pie(pie, labels=label, colors=color, autopct='%1.1f%%')
        ax[1].plot(sets[x], get_plot_color(x))
        ax[1].plot(sets[x], get_plot_color(x))
    try:
        print("Generating visualization.")
        plt.savefig("matrix_analysis.png")
    except Exception as e:
        print(e)


def check_dependancy(dependencys: dict[str, str]) -> bool:
    print("Checking dependencies:")
    is_complete: bool = True
    for dependency in dependencys:
        dependency = dependency.strip()
        if util.find_spec(dependency) is not None:
            version = metadata.version(dependency)
            print(f"{Color_line.GREEN}[OK] "
                  f"{dependency}{Color_line.RESET} ({version}) - "
                  f"{dependencys[dependency]} ready")
        else:
            is_complete = False
            print(f"{Color_line.RED}[NOK] {dependency}{Color_line.RESET}")
    if is_complete is False:
        if sys.base_prefix == sys.prefix:
            print(f"\n{Color_line.RED}Your are not in "
                  "a python virtual environment"
                  f"\nFollow the instructions below "
                  f"to install a Python virtual environment."
                  f"{Color_line.RESET}")
            venv_instruction()
        print(f"\nDependance installation instruction:\n"
              f"{Color_line.YELLOW}pip install -r "
              f"requirements.txt{Color_line.RESET}")
        print(f" or\n{Color_line.YELLOW}poetry install{Color_line.RESET}")

    return is_complete


if __name__ == "__main__":

    print("\nLOADING STATUS: Loading programs...\n")
    check: bool = check_dependancy({'pandas': 'Data manipulation',
                                    'numpy': 'Numerical computation',
                                    'matplotlib': 'Visualization'})
    if check is True:
        create_data_set()
