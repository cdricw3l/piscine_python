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
def power_validator(min_power: int) -> Callable:
    def validator(func: Callable):
        @wraps(func)
        # *args is a tuple of all argument passed to the fonction
        def wrapper(*args):
            if args[2] < min_power:
                return "Insufficient power for this spell"
            return func(*args)
        return wrapper
    return validator



def retry_spell(max_attempts: int) -> Callable:
    def retry(func):
        func.retry = 0
        @wraps(func)    
        def wrapper(*args, **kwargs):
            try:
                print(args)
                func(args[0])
                print("Waaaaaaagh spelled !")
            except Exception as e:
                if func.retry == max_attempts:
                    print(f"Spell casting failed after {max_attempts} attempts")
                else:
                    print(f"Spell failed, retrying... (attempt {func.retry + 1}/{max_attempts})")
                    func.retry += 1
                    wrapper(args, kwargs)
        return wrapper
    return retry
            

class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    @power_validator(20)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"{spell_name} as a power {power}"


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

def power_validator_test(power: int):
    mage: MageGuild = MageGuild()
    print(mage.cast_spell("hello", power))

@retry_spell(3)
def max_retry(mode: int):
    if mode == 0:
        raise Exception
    else:
        pass
        

if __name__ == "__main__":
    #spell_timer_test()
    #power_validator_test(21)
    max_retry(0)
    #max_retry(1)

    