# validation.py
import re

def validate_name(name):
    if not name or not name.strip():
        return False, "Name cannot be empty."
    if not re.match(r"^[a-zA-Z\s]+$", name):
        return False, "Name must contain only letters and spaces."
    return True, ""

def validate_roll_no(roll_no, cursor):
    if not roll_no or not roll_no.strip():
        return False, "Roll number cannot be empty."
    cursor.execute("SELECT roll_no FROM students WHERE roll_no = %s", (roll_no,))
    if cursor.fetchone():
        return False, "Roll number already exists."
    return True, ""

def validate_email(email, cursor):
    if not email or not email.strip():
        return True, ""  # Email is optional
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False, "Invalid email format."
    cursor.execute("SELECT email FROM students WHERE email = %s", (email,))
    if cursor.fetchone():
        return False, "Email already exists."
    return True, ""

def validate_phone(phone):
    if not phone or not phone.strip():
        return True, ""  # Phone is optional
    if not re.match(r"^\d{10}$", phone):
        return False, "Phone number must be 10 digits."
    return True, ""

def validate_marks(marks):
    try:
        marks = int(marks)
        if 0 <= marks <= 100:
            return True, ""
        return False, "Marks must be between 0 and 100."
    except ValueError:
        return False, "Marks must be a valid number."