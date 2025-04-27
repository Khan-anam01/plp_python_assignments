def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {filename}")
    except IOError as e:
        print(f"Error: Could not write to the file '{filename}'. Details: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except IOError as e:
        return f"Error: The file '{filename}' could not be read. Details: {e}"
    
def modify_file(input_file, output_file, new_content):
    try:
        # Open the input file to read
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Add the new content (this does not modify the existing content)
        modified_content = content + "\n" + new_content  # Append the new content
        
        # Open the output file in append mode to add new data
        with open(output_file, 'a') as file:
            file.write(modified_content)
        
        print(f"New data added to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError as e:
        print(f"Error: An IOError occurred. Details: {e}")


def main():
    input_file = input("Enter the filename to read: ")
    output_file = input("Enter the filename to write: ")
    new_content = input("Enter the new content to add: ")
    modify_file(input_file, output_file, new_content)
    
    
main()



# # File Read & Write Challenge 🖋️: Reads a file and writes a modified version to a new file.
# def modify_file(input_file, output_file):
#     try:
#         # Open the input file to read
#         with open(input_file, 'r') as file:
#             content = file.read()
        
#         # Modify the content (example: convert to uppercase)
#         modified_content = content.upper()  # Modify as needed
        
#         # Write the modified content to the output file
#         with open(output_file, 'w') as file:
#             file.write(modified_content)
        
#         print(f"File modified and saved as {output_file}")
    
#     except FileNotFoundError:
#         print(f"Error: The file {input_file} was not found.")
#     except IOError as e:
#         print(f"Error: An IOError occurred. Details: {e}")

# # Error Handling Lab 🧪: Ask for a filename and handle errors if it doesn't exist or can't be read.
# def handle_file_error():
#     input_file = input("Enter the filename to read: ")
    
#     try:
#         # Try to open and read the file
#         with open(input_file, 'r') as file:
#             content = file.read()
#             print("File content successfully read!")
#             print(content)
    
#     except FileNotFoundError:
#         print(f"Error: The file {input_file} does not exist.")
#     except IOError as e:
#         print(f"Error: The file {input_file} cannot be read. Details: {e}")

# # Example Usage:
# handle_file_error()
# modify_file("example.txt", "modified_example.txt")
