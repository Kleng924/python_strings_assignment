# Objective:
# The aim of this assignment is to create an interactive help desk bot that processes user queries 
# and responds appropriately for a SaaS application.

# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands 
# (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

assistance = input("Please select one: (help/issue/contact support)")

if assistance == "help":
    print("what can I help you with?")
elif assistance == "issue":
    print("let's figure out the problem.")
elif assistance == "contact support":
    print("please dial 1-800-SUPPORT")

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login",
# "performance", "error", etc. Print out the category of the issue for the support team.

assistance_2 = input("Please select one: (help/issue/contact support)")
issues = input("Please select the issue: (login/performance/error)")

if assistance_2 == "issue":
    if issues == "login":
        print("Please click on forgot password.")
    elif issues == "performance":
        print("Please check your internet connection.")
    elif issues == "error":
        print("Please click on refresh button.")
    

