#todos = []
#todos in first line because all the value form output will store in todos after completion of while loop
#not use because we read and write through case add

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
        to-do items.
        """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local
    # file = open('todos.txt', 'r')
    # todos = file.readiness()
    # file.close()


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write and to-do list in the next file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
