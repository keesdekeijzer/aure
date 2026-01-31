import os

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content 

if __name__ == "__main__":
    file_path = 'example.txt'  # Replace with your file path
    try:
        content = read_file(file_path)
        print("File Content:")
        print(content)
    except FileNotFoundError as e:
        print(e)

