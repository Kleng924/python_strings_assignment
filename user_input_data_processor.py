# Objective:
# The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

user_name = str(input("whats your full name?"))
full_name = len(user_name)

print(full_name)

if len(user_name) >=2:
    print(f"Hello, {user_name}")
elif len(user_name) <=2:
    print("error")


# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. 
# The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, 
# and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.


import re

def check_password_complexity(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'\d', password):
        return "Password must contain at least one number."
    return "Password meets the complexity requirements."

password = "C0dingT3mple"
print(check_password_complexity(password))

import re

def check_password_complexity(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'\d', password):
        return "Password must contain at least one number."
    return "Password meets the complexity requirements."

password_2 = "codingtemple"
print(check_password_complexity(password_2))


# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format

import re

def standardize_email(email):
    email = email.strip().lower()
    email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    if re.match(email_regex, email):
        return email
    else:
        raise ValueError(f"Invalid email format: {email}")
    
emails = [" EXAMPLE@DOMAIN.COM ", "user.name+tag@sub.domain.com", "InavalidEmail@domain", 
          "AnotherExample@DOMAIN.com"]

standardized_emails = []

for email in emails:
    try:
        standardized_emails.append(standardize_email(email))
    except ValueError as e:
        print(e)

print(standardized_emails)
