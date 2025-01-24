# college-management-system-using-python-nogui
The College Management Application System simplifies college operations by allowing users to register, log in, manage student records, track fees, add faculty, and manage faculty salaries. It provides an efficient way to handle administrative tasks and ensures secure access and data management.
The College Management Application System is a comprehensive software solution designed to streamline the administration of a college or educational institution. It offers a user-friendly interface that allows administrators and staff to manage essential functions efficiently. Below is a description of its key features:

1. **User Registration & Login**: New users, such as administrators or faculty, can register and create accounts. Once registered, users can log into the system with secure credentials for access to various features.

2. **Student Management**: Administrators can easily add new students to the system, storing essential information such as personal details, enrollment status, course registrations, and more. The system also allows the modification or removal of student records as needed.

3. **Student Record Management**: The system enables administrators to maintain and update detailed student records, including academic performance, attendance, grades, and progress reports. This provides a centralized location for tracking student information.

4. **Fee Management**: The system simplifies the management of student fees by allowing administrators to add and track fee payments, issue receipts, generate outstanding balances, and set reminders for upcoming payments.

5. **Faculty Management**: Administrators can add and manage faculty profiles, including personal information, subjects taught, and course assignments. The system allows for easy updates and maintenance of faculty data.

6. **Faculty Salary Management**: The application provides a feature to manage faculty salaries, including calculating pay based on teaching load, deductions, bonuses, and generating payslips. It ensures transparency and accuracy in salary distribution.

7. **Exit**: Users can securely log out of the system at any time to protect their information and ensure secure access control.

This system improves operational efficiency, reduces manual work, and provides a seamless way to manage both student and faculty-related tasks within an educational institution.

## Features
User-friendly interface with easy-to-navigate modules. </br>
MySQL Database integration for secure data storage. </br>
Modular code structure for easy maintenance and scalability. </br>

## Prerequisites 
Before running the project, ensure you have the following installed:</br>

Python (version 3.6 or higher) </br>
MySQL Server (version 5.7 or higher) </br>
## Required Python libraries: 
mysql-connector-python </br>
Any additional libraries listed in requirements.txt

## How to Download, Install, and Run the Python Program
1. Clone the Repository: </br>
git clone https://github.com/yourusername/college-management-system.git </br>
cd college-management-system </br>

2. Set Up the MySQL Database </br>
Open MySQL Workbench or your preferred MySQL client. </br>
Create a new database: </br>
CREATE DATABASE college_management;</br>

Import the provided SQL file (database.sql) into the newly created database: </br>
mysql -u username -p college_management < database.sql </br>
Replace username with your MySQL username. </br>

3. Configure Database Connection </br>
Open the file where the MySQL connection is configured (e.g., config.py). </br>
Update the database credentials: </br> 
DB_HOST = 'localhost' </br>
DB_USER = 'your_mysql_username' </br>
DB_PASSWORD = 'your_mysql_password' </br>
DB_NAME = 'college_management' </br>


4. Run the Application </br>
Start the application using the following command: </br>
python main.py </br>


5. Explore the System </br>
Follow the on-screen instructions to navigate the modules: </br>

Add, edit, or delete students and teachers. </br>
Log and track expenses. </br>

