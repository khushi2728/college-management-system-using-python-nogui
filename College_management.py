import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
        )
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

try:
    mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print("Something went wrong: {}" .format(err))

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS COLLEGE_DB")
    mycursor.execute("use COLLEGE_DB")

    user_table = "CREATE TABLE IF NOT EXISTS REGISTER_USER (FIRSTNAME VARCHAR(60), LASTNAME VARCHAR(60), EMAIL_ID VARCHAR(60), USERNAME VARCHAR(60), PASSWORD VARCHAR(60))"
    mycursor.execute(user_table)

except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

try:
    student_table = "CREATE TABLE IF NOT EXISTS STUDENTS (ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(60), COURSE VARCHAR(60), FEES INT)"
    mycursor.execute(student_table)
    
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))


try:
    faculty_table = "CREATE TABLE IF NOT EXISTS FACULTIES (ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(60),SUBJECT VARCHAR(60), SALARY INT)"
    mycursor.execute(faculty_table)

except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
 

def register_Newuser():
    print("\n\n\n\t\t********* REGISTER NEW USER *********\n\n\n")
    fn = input("\t\tEnter your firstname : ")
    ln = input("\t\tEnter your lastname : ")
    email = input("\t\tEnter your E-mail id : ")
    user_name = input("\t\tEnter your username : ")
    password = input("\t\tEnter password : ")

    res_tb_qry = "INSERT INTO REGISTER_USER (FIRSTNAME, LASTNAME, EMAIL_ID, USERNAME, PASSWORD) VALUES (%s, %s, %s, %s, %s)"
    res_tb_val = (fn , ln , email , user_name , password)

    mycursor.execute(res_tb_qry, res_tb_val)
    mydb.commit()



    print("\n\t\t\t ********* NEW REGISTRATION SUCCESSFUL **********\n\n\n")


def login_user():
    print("\n\n\n\t\t********* LOGIN *********\n\n\n")
    username = input("\t\t\tEnter your username : ")
    password = input("\t\t\tEnter your password : ")

    mycursor.execute("SELECT * FROM REGISTER_USER WHERE USERNAME=%s AND PASSWORD=%s", (username, password))
    user = mycursor.fetchone()

    if user:
        print(f"\n\t\tWelcome, {user[1]} {user[2]}!\n\n")
    else:
        print("\n\t\t\tInvalid!!! Please try again.\n\n")


def admission_student():
    print("\n\t\t********* ADIMISSION OF STUDENT *********\n\n")
    name = input("Enter student name: ")
    course = input("Enter course: ")

    query = "INSERT INTO STUDENTS (NAME, COURSE) VALUES (%s, %s)"
    mycursor.execute(query, (name, course))
    mydb.commit()

    print("\nStudent added Successfully!!\n")


def manage_record():
    print("\n\t\t********* STUDENT RECORDS *********\n\n")
    mycursor.execute("SELECT * FROM STUDENTS")
    students = mycursor.fetchall()

    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Course: {student[2]}, Fees: {student[3]}")


def manage_fees():
    print("\n\t\t********* MANAGE FEES *********\n\n")
    student_id = int(input("Enter student ID: "))
    amount = float(input("Enter fees amount to pay: "))

    mycursor.execute("UPDATE STUDENTS SET FEES = FEES + %s WHERE ID = %s", (amount, student_id))
    mydb.commit()

    print("\nFees updated successfully!\n")


def recruit_faculty():
    print("\n\t\t********* ADD NEW FACULTY *********\n\n")
    name = input("Enter faculty name: ")
    subject = input("Enter subject: ")

    query = "INSERT INTO FACULTIES (NAME, SUBJECT) VALUES (%s, %s)"
    mycursor.execute(query, (name, subject))
    mydb.commit()

    print("\nFaculty added successfully!\n")


def manage_faculty_salary():
    print("\n\t\t********* MANAGE FACULTY SALARY *********\n\n")
    faculty_id = int(input("Enter faculty ID: "))
    salary = float(input("Enter salary amount to pay: "))

    mycursor.execute("UPDATE FACULTIES SET SALARY = SALARY + %s WHERE ID = %s", (salary, faculty_id))
    mydb.commit()

    print("\nSalary updated successfully!\n")




loop_con = True

while(loop_con):
    print("\n\n\n\t\t********* COLLEGE MANAGEMENT SYSTEM *********\n\n\n")
    print("\t\t1. Register a New User\n")
    print("\t\t2. Login\n")
    print("\t\t3. Add Student\n")
    print("\t\t4. Manage Student Records\n")
    print("\t\t5. Manage Fees\n")
    print("\t\t6. Add Faculty\n")
    print("\t\t7. Manage Faculty Salary\n")
    print("\t\t8. Exit\n")

    main_choice = int(input("Enter your choice: "))

    if main_choice == 1:
        register_Newuser()
    elif main_choice == 2:
        login_user()
    elif main_choice == 3:
        admission_student()
    elif main_choice == 4:
        manage_record()
    elif main_choice == 5:
        manage_fees()
    elif main_choice == 6:
        recruit_faculty()
    elif main_choice == 7:
        manage_faculty_salary()
    elif main_choice == 8:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

    end_choice = input("Do you want to continue (y/n): ").lower()
    if end_choice == 'n':
        loop_con = False




    

    

    

