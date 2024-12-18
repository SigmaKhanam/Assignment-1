# Python File I/O and JSON Handling: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Example 1: Writing to a Text File
'''
with open('data/example.txt', 'w') as file:
    file.write("Hello, Python developers!\n")
    file.write("Welcome to file I/O operations.")
'''
# Example 2: Reading from a Text File
'''
with open('data/example.txt', 'r') as file:
    content = file.read() # readlines(), readlines()
    print(content)
'''
# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

import csv

# Example 3: Writing to a CSV File
'''
with open('data/example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 28, "New York"])
    writer.writerow(["Bob", 22, "Los Angeles"])
    writer.writerow(["Carol", 24, "Chicago"])
'''
# Example 4: Reading from a CSV File
'''
with open('data/example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''

# Section 3: JSON Data
# --------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.

import json

# Example 5: Writing JSON to a File
'''
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('data/data.json', 'w') as file:
    json.dump(data, file)
'''

# Example 6: Reading JSON from a File
'''
with open('data/data.json', 'r') as file:
    data = json.load(file)
    print(data)
'''
# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Example 7: Processing JSON Data from a File
# Suppose we have a JSON file containing multiple user records.
'''
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bob@example.com"}
]
with open('data/users.json', 'w') as file:
    json.dump(users, file)

with open('data/users.json', 'r') as file:
    users = json.load(file)
    for user in users:
        print(f"{user['name']} ({user['age']}): {user['email']}")
'''

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
import csv
import json

# Reading data from CSV file
products = []
with open(r'E:\Field Work\1st Assignment\products.csv', 'r') as csv_file:  # Use raw string
    csv_reader = csv.DictReader(csv_file)  # Read CSV as dictionaries
    products = [row for row in csv_reader]  # Store rows as a list of dictionaries

# Writing data to JSON file
with open(r'E:\Field Work\1st Assignment\data_products.json', 'w') as json_file:  # Use raw string
    json.dump(products, json_file, indent=4)

print("CSV data successfully converted to JSON.")
# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.
import os
from datetime import datetime

def write_log(message):
    """
    Appends a log message with a timestamp to the log file.
    """
    # Ensure the directory exists
    log_dir = 'data'
    os.makedirs(log_dir, exist_ok=True)  # Create the 'data' directory if it doesn't exist
    
    # Construct the log file path
    log_file_path = os.path.join(log_dir, 'logs.txt')
    
    # Append the log entry
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - {message}\n"
    
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_entry)
    print(f"Log added: {log_entry.strip()}")

# Example usage
write_log("Server started.")
write_log("User login: sigmakhanam456@gmail.com.")
write_log("Error: Database connection failed.")
# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.

