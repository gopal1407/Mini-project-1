
def display_menu():
    print("Welcome to the To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!\n")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{idx}. {task['task']} - {status}")
    print()

# Function to mark a task as complete
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task '{tasks[task_number - 1]['task']}' marked as complete.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

# Main function to run the application
def run_app():
    tasks = []  # List to store tasks
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

# Run the To-Do List application
if __name__ == "__main__":
    run_app()

    #Task3

# Function to display the main menu
def display_menu():
    print("\nWelcome to the To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Function to add a task
def add_task(tasks):
    task_title = input("Enter the task title: ").strip()
    if task_title:  # Ensure that the user doesn't enter an empty title
        tasks.append({"title": task_title, "status": "Incomplete"})
        print(f"Task '{task_title}' added successfully!\n")
    else:
        print("Task title cannot be empty. Please try again.\n")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} - {task['status']}")
    print()

# Function to mark a task as complete
def mark_task_complete(tasks):
    if not tasks:
        print("No tasks available to mark as complete.\n")
        return
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Complete"
            print(f"Task '{tasks[task_number - 1]['title']}' marked as complete.\n")
        else:
            print("Invalid task number. Please choose a valid task.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

# Function to delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.\n")
        return
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' deleted successfully.\n")
        else:
            print("Invalid task number. Please choose a valid task.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

# Function to get valid user choice from the menu
def get_user_choice():
    while True:
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please select a valid option (1-5).\n")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 5.\n")

# Main function to run the application
def run_app():
    tasks = []  # List to store tasks
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            mark_task_complete(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("Goodbye!")
            break

# Run the To-Do List application
if __name__ == "__main__":
    run_app()

    #Task4

def display_menu():
    print("\nWelcome to the To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Function to add a task
def add_task(tasks):
    try:
        task_title = input("Enter the task title: ").strip()
        if not task_title:
            raise ValueError("Task title cannot be empty.")  # Custom error if title is empty
        tasks.append({"title": task_title, "status": "Incomplete"})
        print(f"Task '{task_title}' added successfully!\n")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while adding the task: {e}")
    finally:
        print("Attempt to add task completed.\n")

# Function to view all tasks
def view_tasks(tasks):
    try:
        if not tasks:
            raise ValueError("No tasks available.")
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} - {task['status']}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while viewing tasks: {e}")
    finally:
        print("Attempt to view tasks completed.\n")

# Function to mark a task as complete
def mark_task_complete(tasks):
    try:
        if not tasks:
            raise ValueError("No tasks available to mark as complete.")
        view_tasks(tasks)
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Complete"
            print(f"Task '{tasks[task_number - 1]['title']}' marked as complete.\n")
        else:
            raise ValueError("Invalid task number.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while marking the task: {e}")
    finally:
        print("Attempt to mark task completed.\n")

# Function to delete a task
def delete_task(tasks):
    try:
        if not tasks:
            raise ValueError("No tasks available to delete.")
        view_tasks(tasks)
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' deleted successfully.\n")
        else:
            raise ValueError("Invalid task number.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while deleting the task: {e}")
    finally:
        print("Attempt to delete task completed.\n")

# Function to get valid user choice from the menu
def get_user_choice():
    while True:
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= 5:
                return choice
            else:
                raise ValueError("Invalid choice. Please select a valid option (1-5).")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while getting user choice: {e}")
        finally:
            print("Attempt to get user choice completed.\n")

# Main function to run the application
def run_app():
    tasks = []  # List to store tasks
    while True:
        display_menu()
        choice = get_user_choice()

        try:
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                raise ValueError("Invalid choice. Please select a valid option (1-5).")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Main loop completed.\n")

# Run the To-Do List application
if __name__ == "__main__":
    try:
        run_app()
    except Exception as e:
        print(f"An unexpected error occurred in the application: {e}")
    finally:
        print("Application has ended.")

        #Task 5

def display_menu():
    """
    Display the main menu of the To-Do List Application.

    This function shows a set of options for the user to choose from.
    """
    print("\nWelcome to the To-Do List App!\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks):
    """
    Add a new task to the To-Do list.

    Args:
        tasks (list): The list of tasks to which the new task will be added.

    This function prompts the user for a task title and appends it to the list.
    """
    try:
        task_title = input("Enter the task title: ").strip()
        if not task_title:
            raise ValueError("Task title cannot be empty.")  # Raise error if empty title is entered
        tasks.append({"title": task_title, "status": "Incomplete"})
        print(f"Task '{task_title}' added successfully!\n")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Attempt to add task completed.\n")

def view_tasks(tasks):
    """
    Display all the tasks in the To-Do list.

    Args:
        tasks (list): The list of tasks to be displayed.

    This function shows the list of tasks with their titles and statuses.
    """
    try:
        if not tasks:
            raise ValueError("No tasks available.")  # Raise error if the task list is empty
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} - {task['status']}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Attempt to view tasks completed.\n")

def mark_task_complete(tasks):
    """
    Mark a specific task as complete.

    Args:
        tasks (list): The list of tasks to be updated.

    This function allows the user to select a task and mark it as 'Complete'.
    """
    try:
        if not tasks:
            raise ValueError("No tasks available to mark as complete.")
        view_tasks(tasks)
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Complete"
            print(f"Task '{tasks[task_number - 1]['title']}' marked as complete.\n")
        else:
            raise ValueError("Invalid task number.")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Attempt to mark task completed.\n")

def delete_task(tasks):
    """
    Delete a specific task from the To-Do list.

    Args:
        tasks (list): The list of tasks from which the user can delete a task.

    This function allows the user to delete a task by selecting its number.
    """
    try:
        if not tasks:
            raise ValueError("No tasks available to delete.")
        view_tasks(tasks)
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' deleted successfully.\n")
        else:
            raise ValueError("Invalid task number.")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Attempt to delete task completed.\n")

def get_user_choice():
    """
    Prompt the user to choose an option from the menu.

    Returns:
        int: The user's menu choice (1-5).
    
    This function ensures the user selects a valid menu option.
    """
    while True:
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= 5:
                return choice
            else:
                raise ValueError("Invalid choice. Please select a valid option (1-5).")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Attempt to get user choice completed.\n")

def run_app():
    """
    Run the main loop of the To-Do List Application.
    """
    tasks = []  # List to store tasks
    while True:
        try:
            display_menu()
            choice = get_user_choice()

            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                raise ValueError("Invalid choice. Please select a valid option (1-5).")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Main loop completed.\n")  # This will always run, even if there's an exception

#Task 6

def view_tasks(tasks):
    """
    Display all the tasks in the To-Do list.
    """
    if not tasks:
        print("No tasks available.")
        return
def get_user_choice():
    """
    Prompt the user to choose an option from the menu.
    """
    while True:
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please select a valid option (1-5).")
        except ValueError:
            print("Please enter a number between 1 and 5.")

def mark_task_complete(tasks):
    """
    Mark a specific task as complete.
    """
    if not tasks:
        print("No tasks available to mark as complete.")
        return
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Complete"
            print(f"Task '{tasks[task_number - 1]['title']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

def add_task(tasks):
    """
    Add a new task to the To-Do list.
    """
    task_title = input("Enter the task title: ").strip()
    if not task_title:
        print("Error: Task title cannot be empty.")
        return
    tasks.append({"title": task_title, "status": "Incomplete"})
    print(f"Task '{task_title}' added successfully.")


