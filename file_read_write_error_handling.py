def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., convert text to uppercase)
        modified_content = content.upper()  # Example modification
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File modified successfully. The new content has been saved in {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
def main():
    input_filename = input("Enter the filename to read: ")
    output_filename = input("Enter the filename to save the modified content: ")
    
    read_and_modify_file(input_filename, output_filename)

# Run the program
if __name__ == "__main__":
    main()
