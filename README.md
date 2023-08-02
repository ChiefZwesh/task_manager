# Task Management System

The Task Management System is a Python script that allows users to manage tasks, including registering users, adding tasks, viewing tasks, generating reports, displaying statistics, and exiting the program. The script utilizes text files to store user information and task data.

## Prerequisites

Before running the script, ensure you have Python installed on your system.

## Usage

1. Run the script using Python:

   ```bash
   python task_management.py
   ```

2. The script will present the main menu with the following options:

   - `r` - Register a new user (Admin only).
   - `a` - Add a new task.
   - `va` - View all tasks.
   - `vm` - View tasks assigned to the current user.
   - `gr` - Generate reports (Admin only).
   - `ds` - Display statistics (Admin only).
   - `e` - Exit the program.

3. Choose an option from the menu by typing the corresponding letter.

4. Depending on the selected option, the script will prompt for additional information or display relevant information based on the user's input.

## Data Storage

- User data is stored in the `user.txt` file, with each line containing the username and password separated by a comma (`,`).

- Task data is stored in the `tasks.txt` file, with each line representing a task and containing the username, task title, task description, task creation date, due date, and completion status separated by commas (`,`).

## Note

- Only the `admin` user can register new users and generate reports.
- For the due date of the task, use the format `DD-MM-YYYY`.
- When marking a task as complete or editing a task, enter the corresponding task number as displayed in the task list.

## Disclaimer

This script is for educational and informational purposes only. It provides basic task management functionalities and may not cover all aspects of a complete task management system. Always verify results and adapt the script as per your specific requirements.

## License

This script is open-source and licensed under the [MIT License](LICENSE).

Feel free to modify, distribute, and use the script as per the terms of the MIT License.

---
*Disclaimer: The author and the script contributors are not responsible for any losses or damages incurred while using this script. Use it at your own risk.*
