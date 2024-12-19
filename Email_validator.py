import re

def validate_email(email):
    """
    Validates if the given string is a valid email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Define a regex pattern for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use regex to validate the email
    return bool(re.match(email_pattern, email))

# Prompt the user for an email address
email_input = input("Enter an email address to validate: ")

# Validate the email and provide feedback
if validate_email(email_input):
    print(f"'{email_input}' is a valid email address!")
else:
    print(f"'{email_input}' is NOT a valid email address.")
