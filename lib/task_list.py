from .task import Task


class TaskList:
    id = 0

    def __init__(self):
        self.id = 0
        self.tasks = {}

    def addTask(self, label="", description=""):
        self.tasks[self.id] = Task(label, description)
        self.id += 1

    def markTaskCompleted(self, id):
        self.tasks[id].markComplete()

    def addTaskT(self, task: Task):
        self.tasks[self.id] = task
        self.id += 1

    def length(self):
        return len(self.tasks)

    def __str__(self):
        string = "\n"
        string += "Tasks:\n"
        string += "===============================\n\n"

        for t in self.tasks:
            string += "{} - {}".format(t, self.tasks[t])
            string += "\n\n"

        return string
