def garden_operations(operation_number: int) -> int | Exception:
    print(f"Testing operation {operation_number}...")
    try:
        if operation_number == 0:
            int("abc")
        if operation_number == 1:
            1 / 0
        if operation_number == 2:
            with open("false_path") as f:
                print(f)
        if operation_number == 3:
            "abc" + 10
        else:
            print("Operation completed successfully")

    except (
        ValueError, ZeroDivisionError, FileNotFoundError, TypeError
            ) as err:
        print(f"{err.__class__.__name__}: {err}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        garden_operations(i)
    print("\nAll error types tested successfully!")
