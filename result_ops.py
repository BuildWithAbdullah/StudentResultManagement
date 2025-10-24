# result_ops.py
from db_config import get_db_connection
from validation import validate_marks

def add_result():
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        student_id = input("Enter student ID: ")
        cursor.execute("SELECT student_id FROM students WHERE student_id = %s", (student_id,))
        if not cursor.fetchone():
            print("Student ID not found.")
            return

        subject = input("Enter subject name: ")
        if not subject or not subject.strip():
            print("Subject cannot be empty.")
            return

        marks = input("Enter marks (0-100): ")
        is_valid, msg = validate_marks(marks)
        if not is_valid:
            print(msg)
            return
        marks = int(marks)
        grade = 'A' if marks >= 80 else 'B' if marks >= 60 else 'C' if marks >= 40 else 'F'

        cursor.execute(
            "INSERT INTO results (student_id, subject, marks, grade) VALUES (%s, %s, %s, %s)",
            (student_id, subject, marks, grade)
        )
        connection.commit()
        print("Result added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def view_results():
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        student_id = input("Enter student ID to view results (press Enter for all): ")
        if student_id:
            cursor.execute(
                "SELECT s.name, r.subject, r.marks, r.grade FROM results r JOIN students s ON r.student_id = s.student_id WHERE r.student_id = %s",
                (student_id,)
            )
        else:
            cursor.execute(
                "SELECT s.name, r.subject, r.marks, r.grade FROM results r JOIN students s ON r.student_id = s.student_id"
            )
        results = cursor.fetchall()
        if not results:
            print("No results found.")
            return
        print("\nResult List:")
        print("Student Name | Subject | Marks | Grade")
        print("-" * 50)
        for result in results:
            print(f"{result[0]} | {result[1]} | {result[2]} | {result[3]}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def update_result():
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        result_id = input("Enter result ID to update: ")
        cursor.execute("SELECT result_id FROM results WHERE result_id = %s", (result_id,))
        if not cursor.fetchone():
            print("Result ID not found.")
            return

        marks = input("Enter new marks (0-100): ")
        is_valid, msg = validate_marks(marks)
        if not is_valid:
            print(msg)
            return
        marks = int(marks)
        grade = 'A' if marks >= 80 else 'B' if marks >= 60 else 'C' if marks >= 40 else 'F'

        cursor.execute(
            "UPDATE results SET marks = %s, grade = %s WHERE result_id = %s",
            (marks, grade, result_id)
        )
        connection.commit()
        print("Result updated successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

def delete_result():
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()
    try:
        result_id = input("Enter result ID to delete: ")
        cursor.execute("SELECT result_id FROM results WHERE result_id = %s", (result_id,))
        if not cursor.fetchone():
            print("Result ID not found.")
            return

        cursor.execute("DELETE FROM results WHERE result_id = %s", (result_id,))
        connection.commit()
        print("Result deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()