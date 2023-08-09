Feature: Acceptance testing

    Scenario: Adding a task
        Given the To-Do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks
        Given the following tasks are in the to-do list
        | Title     | Description     | Due Date   | Priority |
        | Task 1    | Description 1  | 2023-08-15 | High     |
        | Task 2    | Description 2  | 2023-08-20 | Medium   |
        When I list the tasks
        Then I should see the following tasks in the output
        | Title     | Description     | Due Date   | Priority | Status    |
        | Task 1    | Description 1  | 2023-08-15 | High     | Not Done  |
        | Task 2    | Description 2  | 2023-08-20 | Medium   | Not Done  |


    Scenario: Mark a task as completed
        Given an empty to-do list
        When I add a new task with title "Task 1", description "Description 1", due date "2023-08-15", and priority "High"
        And I mark task 1 as completed
        Then task 1 should be marked as completed in the output


    Scenario: Clear all tasks
        Given the following tasks are in the to-do list
        | Title       | Description     | Due Date     | Priority |
        | Task 1      | Description 1  | 2023-08-15   | High     |
        | Task 2      | Description 2  | 2023-08-20   | Medium   |
        When I clear the to-do list
        Then the to-do list should be empty in the output

    Scenario: Delete the first task
        Given the following tasks are in the to-do list
        | Title       | Description     | Due Date     | Priority |
        | Task 1      | Description 1  | 2023-08-15   | High     |
        | Task 2      | Description 2  | 2023-08-20   | Medium   |
        When I delete the first task
        Then task 1 should be deleted from the list in the output

    


    

  

