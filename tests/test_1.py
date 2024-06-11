import task_manager
from lib import task_list
import io
import time
from contextlib import redirect_stdout


def test_hello():
    tl = task_list.TaskList()
    with io.StringIO() as buf, redirect_stdout(buf):
        task_manager.handle_command("add -t Task One -d description", tl)
        output = buf.getvalue()
        assert output == "Task added successfully.\n"
