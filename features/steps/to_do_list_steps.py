from behave import *

from to_do_list import Task, ToDoListManager

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    # Set the to-do list as an empty list
    global to_do_list
    to_do_list = []
# Step 2: When the user adds a task "Buy groceries"
@when('the user adds a task "{task}"')
def step_impl(context, task):
    # Add the task to the to-do list
    global to_do_list
    to_do_list.append(task)
# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    # Check if the task is in the to-do list
    assert task in to_do_list, f'Task "{task}" not found in the to-do list'


@given("the following tasks are in the to-do list")
def step_given_tasks(context):
    context.todo_list = ToDoListManager()
    for row in context.table:
        task = Task(row["Title"], row["Description"], row["Due Date"], row["Priority"])
        context.todo_list.add_task(task)

@when("I list the tasks")
def step_list_tasks(context):
    context.output = []
    import io
    import sys
    sys.stdout = io.StringIO()
    context.todo_list.list_tasks()
    sys.stdout.seek(0)
    context.output = sys.stdout.read().strip().split('\n')

@then("I should see the following tasks in the output")
def step_check_output(context):
    expected_output = context.table
    assert context.output == context.output


@given("an empty to-do list")
def step_empty_todo_list(context):
    context.todo_list = ToDoListManager()

@when('I add a new task with title "{title}", description "{description}", due date "{due_date}", and priority "{priority}"')
def step_add_task(context, title, description, due_date, priority):
    task = Task(title, description, due_date, priority)
    context.todo_list.add_task(task)

@when(u'I mark task {task_index} as completed')
def step_mark_task_as_completed(context, task_index):
    task_index = int(task_index)
    context.todo_list.mark_task_completed(task_index)

@then(u'task {task_index} should be marked as completed in the output')
def step_check_task_marked_as_completed(context, task_index):
    task_index = int(task_index)
    output_lines = context.output
    task_line = output_lines[task_index - 1]
    assert "Marked 'Task 1' as completed!" in task_line

def step_given_tasks(context):
    context.todo_list = ToDoListManager()
    for row in context.table:
        task = Task(row["Title"], row["Description"], row["Due Date"], row["Priority"])
        context.todo_list.add_task(task)

@when("I clear the to-do list")
def step_clear_todo_list(context):
    context.todo_list.clear_tasks()

@then("the to-do list should be empty in the output")
def step_check_empty_todo_list(context):
    assert not context.todo_list.tasks


@when("I delete the first task")
def step_delete_first_task(context):
    context.deleted_task_title = context.todo_list.tasks[0].title
    context.todo_list.delete_first_task()

@then("task 1 should be deleted from the list in the output")
def step_check_task_deleted(context):
    assert context.deleted_task_title not in [task.title for task in context.todo_list.tasks]

