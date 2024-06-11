from lib.task_list import TaskList
from lib.task import Task
import sys
# comments


def main():
    tl = TaskList()
    print("Welcome to the Task Manager Application:")
    print('type "help" for a list of commands\n')
    # tl.addTask("Task 1", "Need to do x, y, and z")
    while True:
        command = input()
        handle_command(command, tl)
    task = Task(
        "Task 2",
        "This is some longer text that will fill more of a line in the terminal. Lets see how it displays.....",
    )

    task.markComplete()
    tl.addTaskT(task)
    print(tl.length())
    print(tl)


def handle_command(command, tl):
    if command in ["quit", "q", "Q"]:
        sys.exit()
    elif command == "help":
        print("Valid commands include:")
        print("\tquit - exit program")
        print("\tdisplay - display tasks")
        print("\tadd -t <title> -d <description> - add a task")
        print("\tcomplete <id> - mark a task as completed")
    elif command == "display":
        # Assuming you have a function called displayTasks() that prints the tasks
        print(tl)
    elif command.startswith("add"):
        parts = command.split()
        if len(parts) < 6 or "-t" not in parts or "-d" not in parts:
            print(
                "Invalid command. Please provide both title and description using -t and -d tags."
            )
        else:
            title_index = parts.index("-t") + 1
            description_index = parts.index("-d") + 1
            if title_index >= len(parts) or description_index >= len(parts):
                print(
                    "Invalid command. Please provide both title and description using -t and -d tags."
                )
            else:
                # Extract title
                title_parts = []
                i = title_index
                while i < len(parts) and parts[i] != "-d":
                    title_parts.append(parts[i])
                    i += 1
                title = " ".join(title_parts)

                # Extract description
                description_parts = []
                i = description_index
                while i < len(parts) and (parts[i] != "-t" or parts[i] != "-t"):
                    description_parts.append(parts[i])
                    i += 1
                description = " ".join(description_parts)

                # Assuming you have a function called addTask() that adds the task
                tl.addTask(title, description)
                print("Task added successfully.")
    # elif command.startswith("complete"):
    #     # Assuming the user input for marking a task completed is in the format "complete id"
    #     parts = command.split(maxsplit=1)
    #     if len(parts) < 2:
    #         print("Invalid command. Please provide the id of the task.")
    #     else:
    #         task_id = parts[1]
    #         # Assuming you have a function called markTaskCompleted() that marks the task as completed
    #         markTaskCompleted(task_id)
    #         print("Task marked as completed.")
    else:
        print("Invalid command. Type 'help' for a list of valid commands.")


if __name__ == "__main__":
    main()
