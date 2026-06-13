#!/usr/bin/python3

def input_temperature(temp_str: str) -> int | ValueError:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C")
    return temp


def test_temperature() -> int:
    print("=== Garden Temperature ===")
    input: str = '25'
    print(f"Input data is '{input}'")
    try:
        temp: int | ValueError = input_temperature(input)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(err)
    input = 'abc'
    print(f"\nInput data is '{input}'")
    try:
        temp = input_temperature(input)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature err: {err}\n")
    input = "100"
    print(f"\nInput data is '{input}'")
    try:
        temp = input_temperature(input)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature err: {err}\n")
    input = "-40"
    print(f"\nInput data is '{input}'")
    try:
        temp = input_temperature(input)
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature err: {err}\n")
    print("All tests completed - program didn't crash!")
    return (0)


if __name__ == "__main__":
    t = test_temperature()
