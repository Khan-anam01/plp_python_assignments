# Function to write content to a file
def write_to_file(filename, content):
    try:
        # Open the file in write mode ('w') and write the content
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {filename}")  # Confirm successful write
    except IOError as e:
        # Catch IO errors like file permission issues
        print(f"Error: Could not write to the file '{filename}'. Details: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error: {e}")


# Function to read content from a file
def read_from_file(filename):
    try:
        # Open the file in read mode ('r') and read the content
        with open(filename, 'r') as file:
            content = file.read()
        return content  # Return the content of the file
    except FileNotFoundError:
        # If the file doesn't exist, return an error message
        return f"Error: The file '{filename}' does not exist."
    except IOError as e:
        # Catch IO errors if the file cannot be read
        return f"Error: The file '{filename}' could not be read. Details: {e}"


# Function to modify a file by appending new content to it
def modify_file(input_file, output_file, new_content):
    try:
        # Open the input file in read mode to get its content
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Add the new content to the existing content (appending with a newline)
        modified_content = content + "\n" + new_content
        
        # Open the output file in append mode ('a') to add new content without overwriting
        with open(output_file, 'a') as file:
            file.write(modified_content)
        
        print(f"New data added to {output_file}")  # Confirm new data was added

    except FileNotFoundError:
        # If the input file doesn't exist, print an error message
        print(f"Error: The file {input_file} was not found.")
    except IOError as e:
        # Catch IO errors while reading or writing to files
        print(f"Error: An IOError occurred. Details: {e}")


# Main function that drives the program
def main():
    # Prompt the user to enter the filename to read from
    input_file = input("Enter the filename to read: ")
    
    # Prompt the user to enter the filename to write to
    output_file = input("Enter the filename to write: ")
    
    # Prompt the user for new content to append to the output file
    new_content = input("Enter the new content to add: ")
    
    # Call the modify_file function to add new content to the output file
    modify_file(input_file, output_file, new_content)


# Run the main function to execute the program
main()
