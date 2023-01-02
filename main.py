from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos('todos.txt')

        todos.append(todo)

        write_todos(todos, 'todos.txt')

    elif user_action.startswith("show"):

        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}- {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos('todos.txt')
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos, 'todos.txt')
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos('todos.txt')

            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos, 'todos.txt')

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("No item with that number.")

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid.")

print("Bye!")
