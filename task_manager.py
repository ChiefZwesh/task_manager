#=====importing libraries===========
import datetime

#====Login Section====
with open('user.txt', "r") as f:
    user_data = f.readlines()
    
# Create a dictionary to store the usernames and passwords
users = {}
for line in user_data:
    # Split each line into username and password
    username, password = line.strip().split(",")
    # Remove leading and trailing whitespace from username and password
    username = username.strip()
    password = password.strip()
    # Add the username and password to the dictionary
    users[username] = password

while True:
    # Prompt the user to enter their username and password
    username = input("Enter your username: ")
    print()
    password = input("Enter your password: ")                                                                                                               
    # Check if the username is in the dictionary
    if username in users:
        # Check if the password matches the one in the dictionary
        if users[username] == password:
            print("Login successful!")
            print()
            # Set the current user to the logged in user
            current_user = username
            break
    print("Incorrect username or password. Please try again.")
    print()
    
#====Execution functions====
def reg_user():
    # Ensure that only the admin user can add new users
    if current_user == 'admin':
        # Create an empty list to store the existing usernames
        existing_usernames = []
        # Loop through each line in the user.txt file
        with open('user.txt', 'r') as f:
            for line in f:
                # Split the line at the comma to get the username
                username = line.strip().split(",")[0]
                # Append the username to the list of existing usernames
                existing_usernames.append(username)
        
        while True:
            # Request input for a new username
            new_username = input("Enter a new username: ")
            # Check if the new username is already in the list of existing usernames
            if new_username in existing_usernames:
                print("That username is already taken. Please choose a different one.")
            else:
                break
        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm password: ")
        
        # Check if the new password and confirmed password match
        if new_password == confirm_password:
            with open('user.txt', 'a') as user_file:
                user_file.write(f"{new_username},{new_password}\n")  
            print("New user added successfully!")
            # Update the users dictionary to include the new user
            users[new_username] = new_password
        else:
            print("Passwords do not match. Please try again.")
    else:
        print("Only the admin user can add new users.")

def add_task():
    # Prompt the user for information about the new task
    username = input("Enter the username of the person the task is assigned to: ")
    title = input("Enter the title of the task: ")
    description = input("Enter a description of the task: ")
    due_date_str = input("Enter the due date of the task (format: DD-MM-YYYY): ")
    # Parse the due date string into a datetime object
    due_date = datetime.datetime.strptime(due_date_str, '%d-%m-%Y')
    # Get the current date
    current_date = datetime.datetime.today().strftime('%d-%m-%Y')
    # Add status of task as "No" by default
    status = "No"
    # Write the task information to the file
    with open('tasks.txt', 'a') as f:
        f.write(f"{username}, {title}, {description}, {current_date}, {due_date.strftime('%d-%m-%Y')}, {status}\n")
    print('Success')


def view_all():
    # Open the task.txt file in read mode
    with open('tasks.txt', 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Split the line at every comma and space
            task_info = line.strip().split(', ')
            # Print the task information in the specified format
            print(f"Task assigned to: {task_info[0]}")
            print(f"Task title: {task_info[1]}")
            print(f"Task description: {task_info[2]}")
            print(f"Task due date: {task_info[3]}")
            print(f"Task complete: {task_info[5]}")
            # Add a newline after each task for readability
            print()


def view_mine():
    with open('tasks.txt', 'r') as task_file:
        # Create a list to store the task information
        task_list = []
        # Loop through each line in the file
        for line in task_file:
            task_info = line.strip().split(', ')
            # Check if the username of the logged in user matches the username on the task
            if task_info[0] == current_user:
                task_list.append(task_info)
        # Check if any tasks were found for the current user
        if not task_list:
            print("No tasks found for the current user.")
            return
        # Print the task information in the desired format
        print("Tasks assigned to you:")
        for i, task in enumerate(task_list):
            print(f"{i+1}. Task: {task[1]}, Description: {task[2]}, Due Date: {task[3]}, Completed: {task[4]}")
        # Prompt the user to select a task
        task_selection = input("Enter the number of the task you would like to select (-1 to return to main menu): ")
        # If the user enters -1, return to the main menu
        if task_selection == '-1':
            return
        try:
            task_number = int(task_selection)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        # Check if the task number is within the range of available tasks
        if task_number < 1 or task_number > len(task_list):
            print("Invalid task number. Please enter a valid task number.")
            return
        # Get the selected task information
        selected_task = task_list[task_number - 1]
        # Prompt the user to select an action
        action_selection = input("Enter 'c' to mark the task as complete or 'e' to edit the task: ")
        # If the user selects 'c', mark the task as complete
        if action_selection == 'c':
            # Change the task complete status to 'Yes'
            selected_task[4] = 'Yes'
            # Write the updated task information to the file
            with open('tasks.txt', 'w') as task_file:
                for task in task_list:
            # Check if the task being written is the selected task
                    if task == selected_task:
                        task_file.write(', '.join(selected_task) + '\n')
                    else:
                        task_file.write(', '.join(task) + '\n')
            print("Task marked as complete.")
        # If the user selects 'e', edit the task
        # If the user selects 'e', edit the task
        elif action_selection == 'e':
            # Prompt the user for new information about the task
            new_title = input("Enter the new title for the task: ")
            new_description = input("Enter the new description for the task: ")
            new_due_date = input("Enter the new due date for the task (format: DD-MM-YYYY): ")
            # Update the task information with the new information
            selected_task[1] = new_title
            selected_task[2] = new_description
            selected_task[3] = new_due_date
            # Write the updated task information to the file
            with open('tasks.txt', 'w') as task_file:
                for task in task_list:
                    task_file.write(', '.join(task) + '\n')
            print("Task updated successfully.")


def generate_reports():
    if current_user == 'admin':
        with open('tasks.txt', 'r') as f:
            task_list = f.readlines()
        with open('user.txt', 'r') as f:
            user_list = f.readlines()
        num_users = len(user_list)
        total_tasks = len(task_list)
        
        completed_tasks = sum(task.split(',')[4].strip() == 'Yes' for task in task_list)
        incomplete_tasks = total_tasks - completed_tasks
        overdue_tasks = sum(datetime.datetime.strptime(task.split(',')[3].strip(), '%d-%m-%Y').date() < datetime.date.today() and task.split(',')[4].strip() == 'No' for task in task_list)

        with open('task_overview.txt', 'w') as f:
            f.write('Task Overview\n\n')
            f.write(f'Total number of tasks: {total_tasks}\n')
            f.write(f'Number of completed tasks: {completed_tasks}\n')
            f.write(f'Number of incomplete tasks: {incomplete_tasks}\n')
            f.write(f'Number of overdue tasks: {overdue_tasks}\n')
            f.write(f'Percentage of incomplete tasks: {incomplete_tasks / total_tasks * 100:.2f}%\n')
            f.write(f'Percentage of overdue tasks: {overdue_tasks / total_tasks * 100:.2f}%\n')
            
        with open('user_overview.txt', 'w') as f:
            f.write('User Overview\n\n')
            f.write(f'Total number of users: {num_users}\n')
            for user in user_list:
                username = user.split(',')[0]
                num_user_tasks = sum(task.split(',')[0] == username for task in task_list)
                percent_user_tasks = num_user_tasks / total_tasks * 100
                num_completed_tasks = sum(task.split(',')[4] == 'Yes\n' and task.split(',')[0] == username for task in task_list)
                percent_completed_tasks = num_completed_tasks / num_user_tasks * 100 if num_user_tasks > 0 else 0
                percent_incomplete_tasks = (num_user_tasks - num_completed_tasks) / num_user_tasks * 100 if num_user_tasks > 0 else 0
                percent_overdue_tasks = sum(datetime.datetime.strptime(task.split(',')[3].strip(), '%d-%m-%Y').date() < datetime.date.today() and task.split(',')[4].strip() == 'No' and task.split(',')[0] == username for task in task_list) / num_user_tasks * 100 if num_user_tasks > 0 else 0
                
                f.write(f'\n{username}\n')
                f.write(f'Total number of tasks assigned: {num_user_tasks}\n')
                f.write(f'Percentage of all tasks assigned: {percent_user_tasks:.2f}%\n')
                f.write(f'Percentage of tasks completed: {percent_completed_tasks:.2f}%\n')
                f.write(f'Percentage of tasks not completed: {percent_incomplete_tasks:.2f}%\n')
                f.write(f'Percentage of tasks overdue: {percent_overdue_tasks:.2f}%\n')
                
        print('Success')
    else:
        print('Restricted to Admin')


def display_statistics():
    if current_user == 'admin':
        try:
            with open('task_overview.txt', 'r') as f:
                task_overview = f.read()
            with open('user_overview.txt', 'r') as f:
                user_overview = f.read()
            print('-' * 50)
            print(task_overview)
            print('-' * 50)
            print(user_overview)
        except FileNotFoundError:
            print('No statistics available')
    else:
        print('Restricted to Admin')
    
def exit_program():
    print('Goodbye!!!')
    exit()
    
#====Menu Section====
while True:
#presenting the menu to the user and 
# making sure that the user input is coneverted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user (Admin Ony!)
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports (Admin Only!)
ds - display statistics (Admin Only!)
e - Exit
: ''').lower()
# Process the user's selection
    if menu == 'r':
        reg_user()
        print()
    elif menu == 'a':
        add_task()
        print()
    elif menu == 'va':
        view_all()
        print()
    elif menu == 'vm':
        view_mine()
        print()
    elif menu == 'gr':
        generate_reports()
        print()
    elif menu == 'ds':
        display_statistics()
        print()
    elif menu == 'e':
        exit_program()
        print()
    else:
        print("Invalid selection. Please try again.") 
        print()
#====End of Menu Section====