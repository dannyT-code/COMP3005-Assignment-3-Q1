import psycopg2

#Connect to database
connection = psycopg2.connect(database="ASS3", user="postgres", password="postgres")
cursor = connection.cursor()

#Retrieves and displays all records from the students table.
def getAllStudents(): 
    try:
        cursor.execute("SELECT * FROM students")
        print(cursor.fetchall())
    except:
        print("Error fetching data")

#Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        connection.commit()
    except psycopg2.errors.UniqueViolation:
        print("Email already exists")
    except:
        print("Other error with adding student")

#Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    try: 
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        connection.commit()
    except psycopg2.errors.UniqueViolation:
        print("Email already exists")
    except:
        print("Other error with updating email")

#Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    try:
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        connection.commit()
    except:
        print("Error deleting student")

#Code for user to interact with the database using the above functions
def main():
    while(True):
        chosenOption = input("1. Get all students \n2. Add a student \n3. Update a student's email \n4. Delete a student \n5. Exit\n")
        
        if chosenOption == "1":
            getAllStudents()
        elif chosenOption == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date: ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif chosenOption == "3":
            student_id = input("Enter student id: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif chosenOption == "4":
            student_id = input("Enter student id: ")
            deleteStudent(student_id)
        elif chosenOption == "5":
            break
    
    #Closed when user exits
    cursor.close()
    connection.close()
main()