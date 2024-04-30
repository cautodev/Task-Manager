from .task import Task


class TaskList:
    tasks = {}
    id = 0

    def __init__(self) -> None:
        pass

    def addTask(self, label="", description=""):
        self.tasks[self.id] = Task(label, description)
        self.id += 1

    def addTaskT(self, task: Task):
        self.tasks[self.id] = task
        self.id += 1

    def length(self):
        return len(self.tasks)

    def __str__(self):
        string = ""
        string += "Tasks:\n"
        string += "===============================\n\n"

        for t in self.tasks:
            string += "{}".format(t)
            string += "\n\n"

        return string
