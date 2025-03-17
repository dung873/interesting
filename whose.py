# whose.py

def greet(name="World"):
    """
    向指定名称打招呼，默认向"World"打招呼。

    :param name: 要打招呼的名称，默认为"World"
    :type name: str
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet()