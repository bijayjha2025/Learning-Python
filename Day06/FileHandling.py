# File Handling - file operations like creating, writing to, reading from, and appending to a file is possible. It also includes error handling to manage potential exceptions that may arise during file operations.

# 1. Creating and writing to a file
def file1():
    try:
        with open('file1.text', 'w') as file: #here, 'w' mode is used to write to the file. If the file already exists, it will be overwritten., with statement ensures proper resource management, and the file is automatically closed after the block is executed, as file means file object.
            file.write("Hello, I am learning Python.\n")
            file.write("This file is created for demonstrating file handling in Python.\n")

    except IOError:
        print("An error occurred while writing to the file.")

file1()

# 2. Reading from a file
def file2():
    try:
        with open('file1.text', 'r') as file: #here, 'r' mode is used to read from the file.
            content = file.read()
            print("File Content:")
            print(content)

    except IOError:
        print("An error occurred while reading the file.")

file2()

# 3. Appending to a file, means adding new content to the end of an existing file without overwriting the existing content.
def file3():
    try:
        with open('file1.text', 'a') as file: #here, 'a' mode is used to append to the file.
            file.write("Appending a new line to the existing file. It shows we can append without overwriting.\n")

    except IOError:
        print("An error occurred while appending to the file.")

file3()

# 4. Reading the updated file to see the appended content
def file4():
    try:
        with open('file1.text', 'r') as file:
            content = file.read()
            print("Updated File Content:")
            print(content)

    except IOError:
        print("An error occurred while reading the file.")

file4()

# 5. Handling file not found error
def file5():
    try:
        with open('haha.txt', 'r') as file: #trying to read a file that does not exist
            content = file.read()
            print(content)

    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist.")

file5()

# # 6. Handling permission error
# def file6():
#     try:
#         with open('/root/abc.txt', 'r') as file: #trying to read a file without proper permissions
#             content = file.read()
#             print(content)

#     except PermissionError:
#         print("Error: You do not have permission to access this file.")

# file6()

# 7. Using finally block to ensure file closure
def file7():
    file = None
    try:
        file = open('file1.text', 'r')
        content = file.read()
        print("File Content using finally block:")
        print(content)

    except IOError:
        print("An error occurred while reading the file.")

    finally:
        if file:
            file.close()
            print("File has been closed.")

file7()

# finally is used here to ensure that the file is closed properly, regardless of whether an exception occurred or not during the file operations. It is compulsory to close the file to free up system resources and avoid potential data corruption.

# 8. Using with statement for automatic file closure
def file8():
    try:
        with open('file1.text', 'r') as file:
            content = file.read()
            print("File Content using with statement:")
            print(content)

    except IOError:
        print("An error occurred while reading the file.")
file8()

# The with statement automatically handles file closure, ensuring that the file is properly closed after the block of code is executed, even if an exception occurs. This makes the code cleaner and less error-prone compared to manually opening and closing files. 