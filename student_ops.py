# student_ops.py
from db_config import get_db_connection
from validation import validate_name, validate_roll_no, validate_email, validate_phone

def add_student():
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        name = input("Enter student name: ")
        is_valid, msg = validate_name(name)
        if not is_valid:
            print(msg)
            return

        roll_no = input("Enter roll number: ")
        is_valid, msg = validate_roll_no(roll_no, cursor)
        if not is_valid:
            print(msg)
            return

        email = input("Enter email (optional, press Enter to skip): ")
        is_valid, msg = validate_email(email, cursor)
        if not is_valid:
            print(msg)
            return

        phone = input("Enter phone number (optional, press Enter to skip): ")
        is_valid, msg = validate_phone(phone)
        if not is_valid:
            print(msg)
            return

        cursor.execute(
            "INSERT INTO students (name, roll_no, email, phone) VALUES (%s, %s, %s, %s)",
            (name, roll_no, email or None, phone or None)
        )
        connection.commit()
        print("Student added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def view_students():
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT student_id, name, roll_no, email, phone FROM students")
        students = cursor.fetchall()
        if not students:
            print("No students found.")
            return
        print("\nStudent List:")
        print("ID | Name | Roll No | Email | Phone")
        print("-" * 50)
        for student in students:
            print(f"{student[0]} | {student[1]} | {student[2]} | {student[3] or 'N/A'} | {student[4] or 'N/A'}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def update_student():
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        student_id = input("Enter student ID to update: ")
        cursor.execute("SELECT student_id FROM students WHERE student_id = %s", (student_id,))
        if not cursor.fetchone():
            print("Student ID not found.")
            return

        name = input("Enter new name (press Enter to skip): ")
        if name:
            is_valid, msg = validate_name(name)
            if not is_valid:
                print(msg)
                return
            cursor.execute("UPDATE students SET name = %s WHERE student_id = %s", (name, student_id))

        email = input("Enter new email (press Enter to skip): ")
        if email:
            is_valid, msg = validate_email(email, cursor)
            if not is_valid:
                print(msg)
                return
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (email, student_id))

        phone = input("Enter new phone (press Enter to skip): ")
        if phone:
            is_valid, msg = validate_phone(phone)
            if not is_valid:
                print(msg)
                return
            cursor.execute("UPDATE students SET phone = %s WHERE student_id = %s", (phone, student_id))

        connection.commit()
        print("Student updated successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def delete_student():
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        student_id = input("Enter student ID to delete: ")
        cursor.execute("SELECT student_id FROM students WHERE student_id = %s", (student_id,))
        if not cursor.fetchone():
            print("Student ID not found.")
            return

        cursor.execute("DELETE FROM results WHERE student_id = %s", (student_id,))
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        connection.commit()
        print("Student and their results deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()