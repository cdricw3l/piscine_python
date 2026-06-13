#!/usr/bin/python3

def input_temperature(temp_str: str) -> int | Exception:
    temp: int = int(temp_str)
    return temp

def test_temperature() -> Exception | None:
    print("=== Garden Temperature ===")
    input:str = '25'
    print(f"Input data is '{input}'")
    try:
        temp_1: int = input_temperature(input)
        print(f"Temperature is now {temp_1}°C")
    except TypeError as err:
        print(err)
    input:str = 'abc'
    print(f"\nInput data is '{input}'")
    try:
        temp_2: int = input_temperature(input)
        print(f"Temperature is now {temp_2}°C")
    except ValueError as err:
        print(f"Caught input_temperature err: {err}\n")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    t = test_temperature()
    print(type(t))