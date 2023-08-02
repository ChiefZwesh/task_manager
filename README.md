# Task_manager.py

Task_manager.py  allows users to manage tasks, including registering users, adding tasks, viewing tasks, generating reports, displaying statistics, and exiting the program. The script utilizes text files to store user information and task data.

## Prerequisites

Before running the script, ensure you have Docker and Docker Compose installed on your system.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your_username/task_manager.git
   cd task_manager
   ```

2. Build the Docker image:

   ```bash
   docker build -t task_management .
   ```

3. Run the Docker container:

   ```bash
   docker run -it task_management python task_manager.py
   ```

4. The script will present the main menu with the following options:

   - `r` - Register a new user (Admin only).
   - `a` - Add a new task.
   - `va` - View all tasks.
   - `vm` - View tasks assigned to the current user.
   - `gr` - Generate reports (Admin only).
   - `ds` - Display statistics (Admin only).
   - `e` - Exit the program.

5. Choose an option from the menu by typing the corresponding letter.

6. Depending on the selected option, the script will prompt for additional information or display relevant information based on the user's input.

## Data Storage

- User data is stored in the `user.txt` file, with each line containing the username and password separated by a comma (`,`).

- Task data is stored in the `tasks.txt` file, with each line representing a task and containing the username, task title, task description, task creation date, due date, and completion status separated by commas (`,`).

## Note

- Only the `admin` user can register new users and generate reports.
- For the due date of the task, use the format `DD-MM-YYYY`.
- When marking a task as complete or editing a task, enter the corresponding task number as displayed in the task list.

