import time
from typing import Callable
from functools import wraps


class Color:
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    RESET: str = "\033[0m"



def spell_timer(func: Callable) -> Callable:
    
    @wraps(func)
    def time_mesurment():
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func()
        end = time.time()
        print(f"Spell completed in {round(end - start, 3)}")
        return result
    return time_mesurment


# !!! Need to undestand deeper: https://stackoverflow.com/questions/61233508/parameterized-decorators-in-python
def power_validator(min_power: int, i: int) -> Callable:
    def validator(func: Callable):
        @wraps(func)
        def check(*args):
            print(args)
            if args[0] < min_power:
                raise Exception("Insufficient power for this spell")
        return check
    return validator



# def retry_spell(max_attempts: int) -> Callable:
#     def retry(func):
#         @wraps()

class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def fireball(ex_simulation_time: int = 3.1568) -> str:
    time.sleep(ex_simulation_time)
    return "Fireball cast!"


def spell_timer_test():
    print(f"\n{Color.YELLOW}Testing spell timer...{Color.RESET}")
    try:
        # create a timer wrapper for fireball
        casting_fireball = spell_timer(fireball)
        result: str = casting_fireball()
        print(f"Result: {result}")
    except Exception as e:
        print(f"\n{Color.RED}{e.__class__.__name__}: {e}{Color.RESET}")

@power_validator(20,21)
def power_validator_test(power: int):
    pass
    
if __name__ == "__main__":
    #spell_timer_test()
    try:
        power_validator_test(20)
    except Exception as e:
        print(e)



    