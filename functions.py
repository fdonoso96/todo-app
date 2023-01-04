def get_todos(filepath="todos.txt"):
    """ Read a text file and return list of`
    to-do items.
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write to-do item list in the text file."""
    with open(filepath,'w') as file_local:
        file_local.writelines(todos_arg)


def test_function():
    print("This is a git test function part 2")


if __name__ == "__main__":
    print("A")

