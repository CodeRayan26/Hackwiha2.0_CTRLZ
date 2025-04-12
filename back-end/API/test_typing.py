from typing import Optional

def test_func(arg: Optional[str]):
    print(f"Argument: {arg}")

test_func("Hello")
test_func(None)